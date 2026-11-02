"""Mesures de validation et planche contact pour les sorties de generer.py.

Usage, depuis tests-images/production/ :
  python analyse.py rose-seed1.png rose-seed2.png      # mesures de chaque image
  python analyse.py --planche contact-fleurs.png *.png  # planche contact à 1 004 px de large par vignette
  python analyse.py --verdict rose-seed1.png ok "" ; python analyse.py --verdict rose-seed2.png refus "silhouette"

Mesures (critères 7 du brief) :
- fond : écart type des pixels de la bordure (uni si < 3) et couleur moyenne ;
- marges : distance de l'objet à chaque bord, en % (attendu > 10 %) ;
- zone de texte des scènes : écart type du tiers droit (uni si < 3).
"""
import json
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ICI = Path(__file__).resolve().parent
JOURNAL = ICI / "production.json"
CIBLE = 1004  # 85 mm à 300 DPI


def mesures(chemin):
    im = Image.open(chemin).convert("RGB")
    a = np.asarray(im, dtype=np.int16)
    h, w, _ = a.shape
    b = 8
    bordure = np.concatenate([a[:b].reshape(-1, 3), a[-b:].reshape(-1, 3),
                              a[:, :b].reshape(-1, 3), a[:, -b:].reshape(-1, 3)])
    fond = bordure.mean(axis=0)
    ecart_fond = float(bordure.std(axis=0).mean())
    # objet : pixels à plus de 40 du fond
    dist = np.abs(a - fond).max(axis=2)
    objet = dist > 40
    ys, xs = np.where(objet)
    if len(xs):
        marges = {"gauche": round(100 * xs.min() / w, 1), "droite": round(100 * (w - 1 - xs.max()) / w, 1),
                  "haut": round(100 * ys.min() / h, 1), "bas": round(100 * (h - 1 - ys.max()) / h, 1)}
    else:
        marges = None
    tiers_droit = a[:, int(w * 2 / 3):]
    res = {"fichier": Path(chemin).name, "taille": [w, h],
           "fond_moyen": "#%02X%02X%02X" % tuple(int(v) for v in fond),
           "ecart_type_fond": round(ecart_fond, 2), "fond_uni": ecart_fond < 3,
           "marges_pct": marges, "part_objet_pct": round(100 * objet.mean(), 1),
           "ecart_type_tiers_droit": round(float(tiers_droit.reshape(-1, 3).std(axis=0).mean()), 2)}
    return res


def planche(sortie, fichiers, colonnes=4):
    vign = []
    for f in fichiers:
        im = Image.open(f).convert("RGB")
        im.thumbnail((CIBLE, CIBLE))
        vign.append((Path(f).name, im))
    cw, ch = CIBLE + 20, CIBLE + 50
    lignes = (len(vign) + colonnes - 1) // colonnes
    out = Image.new("RGB", (cw * colonnes, ch * lignes), "white")
    d = ImageDraw.Draw(out)
    try:
        fnt = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 28)
    except Exception:
        fnt = ImageFont.load_default()
    for i, (nom, im) in enumerate(vign):
        x, y = (i % colonnes) * cw + 10, (i // colonnes) * ch + 10
        out.paste(im, (x, y))
        d.text((x, y + CIBLE + 8), nom, fill="black", font=fnt)
    out.save(ICI / sortie)
    print("planche :", ICI / sortie)


def verdict(fichier, ok, raison):
    donnees = json.loads(JOURNAL.read_text())
    # Les appels en erreur (429, etc.) portent le même nom de fichier sans l'avoir écrit : on les saute.
    for e in reversed(donnees):
        if e.get("fichier") == fichier and not e.get("erreur"):
            e["verdict"] = "ok" if ok == "ok" else "refus"
            e["raison"] = raison or None
            break
    else:
        raise SystemExit(f"{fichier} absent du journal")
    JOURNAL.write_text(json.dumps(donnees, ensure_ascii=False, indent=2))
    print(fichier, "→", ok, raison)


if __name__ == "__main__":
    args = sys.argv[1:]
    if args and args[0] == "--planche":
        planche(args[1], args[2:])
    elif args and args[0] == "--verdict":
        verdict(args[1], args[2], args[3] if len(args) > 3 else "")
    else:
        for f in args:
            print(json.dumps(mesures(f), ensure_ascii=False))
