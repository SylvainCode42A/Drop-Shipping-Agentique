"""Aperçu basse définition d'une commande, pour le thème Shopify (le mug 3D plaque cette image).

Même code que le fichier d'impression : rendre(commande, echelle=0.25). Tout est en millimètres dans
rendu.py, seul le nombre de pixels par millimètre change ; les textes sont donc réduits, recoupés et
placés exactement comme sur le fichier d'impression, et une tâche humaine à l'impression en est une ici.

Usage, depuis production/rendu/ :
    python apercu.py                 # les douze exemples en aperçu, avec temps et écart à l'impression
    from apercu import apercu
    image, alertes = apercu(commande)
Sorties : apercus/<nom>.png (sRGB, 75 DPI, 25 % du placeholder ; mug 619 × 289 px).
"""
import time

import numpy as np
from PIL import Image

from rendu import DPI, ICI, SRGB, TacheHumaine, rendre

ECHELLE = 0.25
SORTIE = ICI / "apercus"


def apercu(commande: dict) -> tuple[Image.Image, list[str]]:
    return rendre(commande, echelle=ECHELLE)


def enregistrer_apercu(img: Image.Image, chemin) -> None:
    if img.getchannel("A").getextrema() == (255, 255):
        img = img.convert("RGB")
    img.save(chemin, dpi=(DPI * ECHELLE, DPI * ECHELLE), icc_profile=SRGB, optimize=True)


def ecart_avec_impression(petit: Image.Image, grand: Image.Image) -> float:
    """Écart moyen (sur 255) entre l'aperçu et l'impression réduite en Lanczos, sur fond blanc."""
    def plat(im):
        fond = Image.new("RGBA", im.size, (255, 255, 255, 255))
        fond.alpha_composite(im.convert("RGBA"))
        return np.asarray(fond.convert("RGB"), dtype=np.float32)
    reduit = grand.resize(petit.size, Image.LANCZOS)
    return float(np.abs(plat(petit) - plat(reduit)).mean())


if __name__ == "__main__":
    from exemples import EXEMPLES
    SORTIE.mkdir(exist_ok=True)
    for nom, cmd in EXEMPLES.items():
        try:
            debut = time.time()
            petit, _ = apercu(cmd)
            t_apercu = time.time() - debut
            debut = time.time()
            grand, _ = rendre(cmd)
            t_impression = time.time() - debut
        except TacheHumaine as e:
            print(f"{nom} : TÂCHE HUMAINE : {e}")
            continue
        enregistrer_apercu(petit, SORTIE / f"{nom}.png")
        print(f"{nom}.png : {petit.width} × {petit.height} px, {t_apercu:.2f} s "
              f"(impression {t_impression:.2f} s), écart à l'impression réduite {ecart_avec_impression(petit, grand):.1f}/255")
