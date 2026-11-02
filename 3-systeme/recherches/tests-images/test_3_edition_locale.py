"""Capacité 3 : édition locale, remplacer un élément sans redessiner le reste.

Prérequis : test_6_variante.py (scènes 6_scene_base_<modele>.png).
Sorties : 3_edit_<modele>.png, 3_masque.png, 3_diff_<modele>.png.
À regarder : écart hors masque. Si le vase n'est pas dans la zone du masque,
ajuster ZONE_VASE après avoir regardé la scène de base, puis relancer.
"""
from commun import IDEO_EDIT, SORTIES, difference, gemini, ideogram, journal, masque_ideogram

SCRIPT = "test_3_edition_locale"
INSTRUCTION = ("Replace the vase of flowers on the table with a teapot, same painting style. "
               "Change nothing else.")
ZONE_VASE = (0.38, 0.30, 0.62, 0.70)  # gauche, haut, droite, bas (fractions), à ajuster

# Nano Banana Pro : instruction seule, la scène passe en image d'entrée, sans masque.
base_nb = SORTIES / "6_scene_base_nbpro.png"
if base_nb.exists():
    gemini(SCRIPT, INSTRUCTION, "3_edit_nbpro.png", images=[base_nb], aspect="4:3", taille="2K")

# Ideogram 4.5 Precise Edit : masque noir sur la zone du vase.
base_ideo = SORTIES / "6_scene_base_ideo45.png"
if base_ideo.exists():
    masque = masque_ideogram(base_ideo, ZONE_VASE, "3_masque.png")
    ideogram(SCRIPT, IDEO_EDIT,
             {"prompt": INSTRUCTION, "context_window": "auto", "quality": "high",
              "seed": "4242", "num_images": "1"},
             "3_edit_ideo45.png",
             fichiers_joints=[("image", base_ideo), ("mask", masque)])

for modele in ("nbpro", "ideo45"):
    avant = SORTIES / f"6_scene_base_{modele}.png"
    apres = SORTIES / f"3_edit_{modele}.png"
    if not (avant.exists() and apres.exists()):
        continue
    masque = masque_ideogram(avant, ZONE_VASE, f"3_masque_{modele}.png")
    mesure = difference(avant, apres, masque, f"3_diff_{modele}.png")
    journal(SCRIPT, {"lecture": {"modele": modele, **mesure}})
    print(modele, mesure)
