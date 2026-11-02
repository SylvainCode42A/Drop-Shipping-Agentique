"""Capacité 5 : élément isolé en gouache aux formes franches, sur fond uni.

Sorties : 5_boule_nbpro.png, 5_boule_ideo45_opaque.png, 5_boule_ideo45_transp.png.
À regarder : ombre portée, texture ajoutée au fond, bords nets, aucun détail
sous 12 px à 1 004 px de large (1 mm sur la forme en bois de 85 mm).
"""
import numpy as np
from PIL import Image

from commun import IDEO_GENERATE, SORTIES, STYLE, gemini, ideogram, journal

SCRIPT = "test_5_element_isole"
PROMPT = (f"A single Christmas bauble, centered, isolated, on a plain flat white background. "
          f"{STYLE}.")

gemini(SCRIPT, PROMPT, "5_boule_nbpro.png", aspect="1:1", taille="1K")

for fond, fichier in (("opaque", "5_boule_ideo45_opaque.png"),
                      ("transparent", "5_boule_ideo45_transp.png")):
    ideogram(SCRIPT, IDEO_GENERATE,
             {"prompt": PROMPT, "magic_prompt": "off", "background": fond,
              "quality": "high", "size": "1024x1024", "seed": "4242", "num_images": "1"},
             fichier)

# Lecture : le fond est-il vraiment uni ? On mesure une bande de 5 % sur chaque bord.
for nom in ("5_boule_nbpro.png", "5_boule_ideo45_opaque.png"):
    chemin = SORTIES / nom
    if not chemin.exists():
        continue
    image = np.asarray(Image.open(chemin).convert("RGB"), dtype=np.float32)
    h, w, _ = image.shape
    b = max(1, int(0.05 * min(h, w)))
    bords = np.concatenate([image[:b].reshape(-1, 3), image[-b:].reshape(-1, 3),
                            image[:, :b].reshape(-1, 3), image[:, -b:].reshape(-1, 3)])
    resultat = {"fichier": nom, "ecart_type_fond": round(float(bords.std(axis=0).mean()), 2),
                "couleur_moyenne_fond": [round(float(c)) for c in bords.mean(axis=0)]}
    journal(SCRIPT, {"lecture": resultat})
    print(resultat)
