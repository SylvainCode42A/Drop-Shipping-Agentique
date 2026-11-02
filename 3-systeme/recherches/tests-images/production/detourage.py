"""Détourage des éléments validés : PNG alpha sRGB 300 DPI dans production/valides/.

Chaîne de la RCH « Détourage, nettoyage des bords et agrandissement pour l'impression (02-11-2026) » :
1. un réseau (rembg, isnet-general-use par défaut, ou birefnet-general) donne la zone de l'objet
   et son cœur sûr ;
2. une clé de couleur Lab sur le fond (vert ou magenta, mesuré sur la bordure de chaque image)
   donne le bord exact : transparent sous 10, opaque au-dessus de 60 ;
3. fusion : clé dans la zone du réseau et dans les taches de peinture franche qui la touchent ;
   intérieur de la peinture franche forcé opaque (le réseau peut rater une couleur proche du fond,
   comme l'œillet rose sur magenta), ainsi que le cœur sûr du réseau (sauve un reflet) ;
4. îlots sous 8 px (à l'échelle 1 024 px) supprimés, ni érosion ni ouverture ;
   puis seules les parties d'au moins 1 % de la plus grande sont gardées (bout de tige fantôme) ;
5. démêlage du bord : alpha recalculé comme mélange de la peinture voisine et du fond, puis
   décontamination des couleurs du bord avec pymatting ;
6. recadrage sur l'objet avec une marge, PNG RGBA, profil sRGB, 300 DPI. Pas d'agrandissement :
   un élément 2K dépasse déjà 1 004 px (85 mm à 300 DPI).

Usage, depuis tests-images/production/ :
  python detourage.py                      # tous les éléments au verdict ok du journal
  python detourage.py rose-seed4.png ...   # seulement ces fichiers
  python detourage.py --modele birefnet-general
Une planche de contrôle (éléments posés sur blanc, bois clair et bleu) est écrite dans
production/controle-detourage.png.
Dépendances : pip install rembg onnxruntime opencv-python pymatting scipy pillow numpy
"""
import json
import sys
import time
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageCms

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI))
import brief  # noqa: E402

SORTIE = ICI / "valides"
JOURNAL = ICI / "production.json"
T0, T1 = 10, 60          # rampe de la clé Lab
ZONE_PX = 25             # la clé agit à moins de 25 px (à 1 024 px) du masque du réseau
LOIN_PX = 200            # au-delà de la zone, une tache de clé n'est gardée qu'à moins de 200 px
ILOT_PX = 8              # îlots et trous sous 8 px² (à 1 024 px)
PART_MIN = 0.01          # une partie détachée doit faire 1 % de la plus grande
MARGE_PX = 24            # marge autour de l'objet après recadrage


def lab(img_rgb):
    """RGB uint8 -> Lab (L 0..100)."""
    return cv2.cvtColor(np.ascontiguousarray(img_rgb), cv2.COLOR_RGB2LAB).astype(np.float32) \
        * [100 / 255, 1, 1] - [0, 128, 128]


def disque(r):
    r = max(1, int(r))
    return cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * r + 1,) * 2)


def couleur_fond(img):
    b = np.concatenate([img[:8].reshape(-1, 3), img[-8:].reshape(-1, 3),
                        img[:, :8].reshape(-1, 3), img[:, -8:].reshape(-1, 3)])
    return np.median(b, 0)


def masque_reseau(img, session):
    from rembg import remove
    m = remove(Image.fromarray(img), session=session, only_mask=True)
    return np.asarray(m.convert("L"), dtype=np.float32) / 255


def fusion(img, seg):
    k = img.shape[1] / 1024
    fond = couleur_fond(img)
    d = np.linalg.norm(lab(img) - lab(np.uint8(fond)[None, None]), axis=2)
    bord = np.concatenate([d[:8].ravel(), d[-8:].ravel(), d[:, :8].ravel(), d[:, -8:].ravel()])
    t_coeur = max(1.5, 1.7 * np.percentile(bord, 99))
    a = np.clip((d - T0) / (T1 - T0), 0, 1)
    s = (seg > 0.5).astype(np.uint8)
    zone = cv2.dilate(s, disque(ZONE_PX * k)) > 0
    loin = cv2.dilate(s, disque(LOIN_PX * k)) > 0
    # peinture franche : tout ce qui se détache du fond de plus de T0 + 5. Une couleur proche du fond
    # (œillet rose sur magenta, à 45 du fond en Lab) que le réseau ne voit pas y est comprise.
    peint = (d > T0 + 5).astype(np.uint8)
    n, l, st, _ = cv2.connectedComponentsWithStats(peint)
    garder = np.zeros_like(peint, bool)
    for i in range(1, n):
        if st[i, 4] >= ILOT_PX * k * k and (loin[l == i]).any():
            garder |= (l == i)
    objet = zone | (cv2.dilate(garder.astype(np.uint8), disque(3 * k)) > 0)
    out = np.where(objet, a, 0.0)
    # cœur opaque : intérieur de la peinture franche (gouache opaque, le brief interdit le lavis),
    # et cœur sûr du réseau (sauve un aplat plus proche encore du fond, comme un reflet)
    plein = cv2.erode(garder.astype(np.uint8), disque(2 * k)) > 0
    out = np.where(plein | ((seg > 0.9) & (d > t_coeur)), 1.0, out)
    return out.astype(np.float32), fond


def nettoyer(a, k):
    b = (a > 0.5).astype(np.uint8)
    n, l, st, _ = cv2.connectedComponentsWithStats(b)
    if n > 1:
        aires = st[1:, 4]
        grande = aires.max()
        for i in range(1, n):
            if st[i, 4] < ILOT_PX * k * k or st[i, 4] < PART_MIN * grande:
                a[cv2.dilate((l == i).astype(np.uint8), np.ones((5, 5))) > 0] = 0
    # restes semi-transparents qui ne touchent aucune partie gardée (halo, fantôme)
    garde = cv2.dilate((a > 0.5).astype(np.uint8), disque(3 * k)) > 0
    a[~garde] = 0
    n, l, st, _ = cv2.connectedComponentsWithStats(1 - (a > 0.5).astype(np.uint8))
    for i in range(1, n):
        if st[i, 4] < ILOT_PX * k * k:
            a[l == i] = 1
    return a


def demeler_bord(img, a, fond, k):
    """Bord mêlé de fond : un pixel du bord est vu comme un mélange alpha*F + (1-alpha)*fond, avec F
    la couleur de la peinture la plus proche à l'intérieur. La clé Lab juge opaque un pixel jaune et
    magenta à moitié (loin du fond en Lab) : sans ce démêlage, il reste un liseré rose."""
    from scipy import ndimage
    coeur = cv2.erode((a > 0.99).astype(np.uint8), disque(2 * k)) > 0
    if not coeur.any():
        return a
    bande = (a > 0) & ~coeur & (cv2.dilate(coeur.astype(np.uint8), disque(6 * k)) > 0)
    _, (iy, ix) = ndimage.distance_transform_edt(~coeur, return_indices=True)
    P = img.astype(np.float32)
    F = P[iy, ix]
    B = fond.astype(np.float32)
    FB = F - B
    alpha = np.einsum("ijk,ijk->ij", P - B, FB) / np.maximum(np.einsum("ijk,ijk->ij", FB, FB), 1)
    alpha = np.clip(alpha, 0, 1)
    # seulement là où la peinture est bien distincte du fond, sinon on garde la clé
    net = np.linalg.norm(FB, axis=-1) > 60
    a = a.copy()
    m = bande & net
    a[m] = np.minimum(a[m], alpha[m])
    return a


def decontaminer(img, a):
    from pymatting import estimate_foreground_ml
    fg = estimate_foreground_ml(img / 255.0, a.astype(np.float64))
    return np.clip(fg * 255, 0, 255).astype(np.uint8)


def recadrer(rgb, a):
    ys, xs = np.where(a > 0.01)
    h, w = a.shape
    y0, y1 = max(0, ys.min() - MARGE_PX), min(h, ys.max() + MARGE_PX + 1)
    x0, x1 = max(0, xs.min() - MARGE_PX), min(w, xs.max() + MARGE_PX + 1)
    return rgb[y0:y1, x0:x1], a[y0:y1, x0:x1]


def enregistrer(rgb, a, chemin):
    rgba = np.dstack([rgb, np.round(a * 255).astype(np.uint8)])
    srgb = ImageCms.ImageCmsProfile(ImageCms.createProfile("sRGB")).tobytes()
    Image.fromarray(rgba, "RGBA").save(chemin, dpi=(300, 300), icc_profile=srgb)


def elements_valides():
    """Fichiers au verdict ok du journal dont le nom est une fleur ou un ornement du brief."""
    noms = set(brief.FLEURS) | set(brief.ORNEMENTS)
    fichiers = []
    for e in json.loads(JOURNAL.read_text()):
        f = e.get("fichier", "")
        if e.get("verdict") == "ok" and not e.get("erreur") and f.split("-seed")[0] in noms:
            if f not in fichiers:
                fichiers.append(f)
    return fichiers


def planche(chemins, sortie):
    fonds = [(255, 255, 255), (222, 196, 160), (40, 70, 140)]   # blanc du mug, bois clair, bleu
    case = 300
    out = Image.new("RGB", (case * len(fonds), case * len(chemins)), "white")
    for r, c in enumerate(chemins):
        im = Image.open(c).convert("RGBA")
        im.thumbnail((case - 20, case - 20))
        for j, f in enumerate(fonds):
            tuile = Image.new("RGB", (case, case), f)
            tuile.paste(im, ((case - im.width) // 2, (case - im.height) // 2), im)
            out.paste(tuile, (j * case, r * case))
    out.save(sortie)
    print("planche :", sortie)


def main(args):
    modele = "isnet-general-use"
    if "--modele" in args:
        i = args.index("--modele")
        modele = args[i + 1]
        args = args[:i] + args[i + 2:]
    fichiers = args or elements_valides()
    from rembg import new_session
    session = new_session(modele)
    SORTIE.mkdir(exist_ok=True)
    faits = []
    for f in fichiers:
        t = time.time()
        img = np.asarray(Image.open(ICI / f).convert("RGB"))
        k = img.shape[1] / 1024
        a, fond = fusion(img, masque_reseau(img, session))
        a = nettoyer(a, k)
        a = demeler_bord(img, a, fond, k)
        rgb = decontaminer(img, a)
        rgb, a = recadrer(rgb, a)
        nom = f.split("-seed")[0] + ".png"
        enregistrer(rgb, a, SORTIE / nom)
        faits.append(SORTIE / nom)
        print(f"{f} -> valides/{nom} : {a.shape[1]} x {a.shape[0]} px, fond #%02X%02X%02X, %.1f s"
              % (*fond.astype(int), time.time() - t))
    if faits:
        planche(faits, ICI / "controle-detourage.png")


if __name__ == "__main__":
    main(sys.argv[1:])
