"""Capacité 4 : respect d'une zone laissée vide, par prompt ou par masque.

Sorties : 4_zone_nbpro.png, 4_zone_ideo45.png (prompt seul),
4_zone_ideo45_masque.png (zone repeinte en aplat par Precise Edit), 4_masque.png.
À regarder : uniformité du tiers inférieur (écart type faible = aplat propre),
et débordement de la scène dans la zone.
"""
import numpy as np
from PIL import Image

from commun import (IDEO_EDIT, IDEO_GENERATE, SORTIES, STYLE, gemini, ideogram, journal,
                    masque_ideogram)

SCRIPT = "test_4_zone_vide"
ZONE = (0.0, 0.67, 1.0, 1.0)  # tiers inférieur
PROMPT = (f"A warm family living room scene with grandparents and grandchildren, "
          f"placed in the upper two thirds of the image only. The lower third of the image "
          f"is left completely empty: a flat, uniform cream color, with no object, "
          f"no pattern and no text. {STYLE}.")

gemini(SCRIPT, PROMPT, "4_zone_nbpro.png", aspect="3:4", taille="2K")

base = ideogram(SCRIPT, IDEO_GENERATE,
                {"prompt": PROMPT, "magic_prompt": "off", "background": "opaque",
                 "quality": "high", "size": "1024x1024", "seed": "4242", "num_images": "1"},
                "4_zone_ideo45.png")
if base:
    masque = masque_ideogram(base, ZONE, "4_masque.png")
    ideogram(SCRIPT, IDEO_EDIT,
             {"prompt": "Paint this area as a flat, uniform cream color, with nothing in it.",
              "context_window": "auto", "quality": "high", "seed": "4242", "num_images": "1"},
             "4_zone_ideo45_masque.png",
             fichiers_joints=[("image", base), ("mask", masque)])

# Lecture : écart type des couleurs dans le tiers inférieur.
for nom in ("4_zone_nbpro.png", "4_zone_ideo45.png", "4_zone_ideo45_masque.png"):
    chemin = SORTIES / nom
    if not chemin.exists():
        continue
    image = np.asarray(Image.open(chemin).convert("RGB"), dtype=np.float32)
    zone = image[int(image.shape[0] * ZONE[1]):, :, :]
    resultat = {"fichier": nom, "ecart_type_zone": round(float(zone.std(axis=(0, 1)).mean()), 2),
                "couleur_moyenne_zone": [round(float(c)) for c in zone.mean(axis=(0, 1))]}
    journal(SCRIPT, {"lecture": resultat})
    print(resultat)
