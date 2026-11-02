"""Capacité 6 : régénérer une scène avec une variante contrôlée (fenêtre enneigée).

À lancer avant test_3 : la scène de base sert aussi au test 3.
Sorties : 6_scene_base_<modele>.png, 6_hiver_<modele>.png, 6_masque.png, 6_diff_<modele>.png.
À regarder : écart hors masque (idéalement nul) et dérive de couleur de toute la scène.
"""
from commun import (IDEO_EDIT, IDEO_GENERATE, SORTIES, STYLE, difference, gemini_chat,
                    ideogram, journal, masque_ideogram)

SCRIPT = "test_6_variante"
SCENE = (f"A warm family living room scene: grandparents and grandchildren around a table, "
         f"a vase of flowers on the table, a plain wall in the upper right corner. {STYLE}.")
HIVER = ("Add a window with snow falling outside in the upper right corner. "
         "Keep everything else exactly identical.")
ZONE_HIVER = (0.62, 0.05, 0.95, 0.42)  # gauche, haut, droite, bas (fractions)

# Nano Banana Pro : deux tours de conversation, sans masque.
gemini_chat(SCRIPT, [SCENE, HIVER], ["6_scene_base_nbpro.png", "6_hiver_nbpro.png"],
            aspect="4:3", taille="2K")

# Ideogram 4.5 : scène de base, puis Precise Edit avec masque sur le coin.
base = ideogram(SCRIPT, IDEO_GENERATE,
                {"prompt": SCENE, "magic_prompt": "off", "background": "opaque",
                 "quality": "high", "size": "1024x1024", "seed": "4242", "num_images": "1"},
                "6_scene_base_ideo45.png")
if base:
    masque = masque_ideogram(base, ZONE_HIVER, "6_masque.png")
    ideogram(SCRIPT, IDEO_EDIT,
             {"prompt": HIVER, "context_window": "auto", "quality": "high",
              "seed": "4242", "num_images": "1"},
             "6_hiver_ideo45.png",
             fichiers_joints=[("image", base), ("mask", masque)])

# Mesure : écart hors masque, avec le même masque pour les deux modèles.
for modele in ("nbpro", "ideo45"):
    avant = SORTIES / f"6_scene_base_{modele}.png"
    apres = SORTIES / f"6_hiver_{modele}.png"
    if not (avant.exists() and apres.exists()):
        continue
    masque = masque_ideogram(avant, ZONE_HIVER, f"6_masque_{modele}.png")
    mesure = difference(avant, apres, masque, f"6_diff_{modele}.png")
    journal(SCRIPT, {"lecture": {"modele": modele, **mesure}})
    print(modele, mesure)
