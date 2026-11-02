"""Capacité 2 : image de référence pour tenir un style sur une série d'appels.

Prérequis : test_1_transparence.py (le maître est 1_transparence_ideo45.png).
Sorties : 2_ref_<symbole>_nbpro.png et 2_ref_<symbole>_ideo45.png, pour 4 symboles.
À regarder : même palette, même trait, même épaisseur de contour que le maître.
"""
from commun import IDEO_GENERATE, SORTIES, STYLE, gemini, ideogram

SCRIPT = "test_2_reference"
MAITRE = SORTIES / "1_transparence_ideo45.png"
SYMBOLES = {"coeur": "a heart", "oiseau": "a small bird",
            "boule": "a Christmas bauble", "etoile": "a Christmas star"}

if not MAITRE.exists():
    raise SystemExit("Lance d'abord test_1_transparence.py : le maître est absent.")

for nom, sujet in SYMBOLES.items():
    prompt = (f"Same painting style, palette and contour thickness as the reference image. "
              f"Replace the flower with {sujet}, centered, isolated. {STYLE}.")

    # Nano Banana Pro : le maître passe en référence, fond blanc uni (pas de transparence).
    gemini(SCRIPT, prompt + " Plain white background.", f"2_ref_{nom}_nbpro.png",
           images=[MAITRE], aspect="1:1", taille="1K")

    # Ideogram 4.5 : le maître passe dans images. La combinaison avec
    # background=transparent n'est pas documentée : on essaie, puis on retombe sur auto.
    champs = {"prompt": prompt, "magic_prompt": "off", "background": "transparent",
              "quality": "high", "size": "1024x1024", "num_images": "1"}
    sortie = ideogram(SCRIPT, IDEO_GENERATE, champs, f"2_ref_{nom}_ideo45.png",
                      fichiers_joints=[("images", MAITRE)])
    if sortie is None:
        champs["background"] = "auto"
        ideogram(SCRIPT, IDEO_GENERATE, champs, f"2_ref_{nom}_ideo45.png",
                 fichiers_joints=[("images", MAITRE)])
