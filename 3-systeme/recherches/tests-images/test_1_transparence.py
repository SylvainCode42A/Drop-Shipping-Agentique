"""Capacité 1 : fond transparent natif, ou fond uni à détourer.

À lancer en premier. Sorties : 1_transparence_nbpro.png, 1_transparence_ideo45.png.
À regarder : canal alpha réel (mode RGBA, pixels de fond à alpha 0) ou damier dessiné.
"""
import numpy as np
from PIL import Image

from commun import IDEO_GENERATE, SORTIES, STYLE, gemini, ideogram, journal

SCRIPT = "test_1_transparence"
PROMPT = (f"A single stylized flower, centered, isolated, on a transparent background. {STYLE}.")

gemini(SCRIPT, PROMPT, "1_transparence_nbpro.png", aspect="1:1", taille="1K")

ideogram(SCRIPT, IDEO_GENERATE,
         {"prompt": PROMPT, "magic_prompt": "off", "background": "transparent",
          "quality": "medium", "size": "1024x1024", "num_images": "1"},
         "1_transparence_ideo45.png")

# Lecture automatique : la sortie a-t-elle vraiment de la transparence ?
for nom in ("1_transparence_nbpro.png", "1_transparence_ideo45.png"):
    chemin = SORTIES / nom
    if not chemin.exists():
        continue
    image = Image.open(chemin)
    resultat = {"fichier": nom, "mode": image.mode, "taille": image.size}
    if image.mode in ("RGBA", "LA"):
        alpha = np.array(image.getchannel("A"))
        resultat["part_pixels_transparents"] = round(float((alpha == 0).mean()), 3)
        resultat["part_pixels_semi_transparents"] = round(float(((alpha > 0) & (alpha < 255)).mean()), 4)
    else:
        resultat["part_pixels_transparents"] = 0
    journal(SCRIPT, {"lecture": resultat})
    print(resultat)
