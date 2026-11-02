"""Capacité 7 : résolution, formats de sortie, durée et coût par appel.

Aucun appel d'API : lit les images et les journaux des tests 1 à 6.
Sortie : 7_rapport.json.
Les limites de débit ne se mesurent pas ici : relever celles de Gemini dans
AI Studio, et noter tout code HTTP 429 vu dans les journaux.
"""
import json

from PIL import Image

from commun import SORTIES

images = []
for chemin in sorted(SORTIES.glob("[1-6]_*.png")):
    try:
        image = Image.open(chemin)
        images.append({"fichier": chemin.name, "format_reel": image.format,
                       "mode": image.mode, "largeur": image.size[0], "hauteur": image.size[1],
                       "profil_icc": bool(image.info.get("icc_profile")),
                       "dpi": image.info.get("dpi"), "octets": chemin.stat().st_size})
    except Exception as e:
        images.append({"fichier": chemin.name, "erreur": str(e)})

appels, erreurs = [], []
for journal in sorted(SORTIES.glob("test_*.json")):
    for entree in json.loads(journal.read_text()):
        if "lecture" in entree:
            continue
        ligne = {"script": journal.stem, "modele": entree.get("modele"),
                 "fichier": entree.get("fichier"), "duree_s": entree.get("duree_s"),
                 "mime": entree.get("mime"), "erreur": entree.get("erreur")}
        reponse = entree.get("reponse")
        if isinstance(reponse, dict):
            ligne["cout_annonce"] = reponse.get("cost") or reponse.get("price")
        appels.append(ligne)
        if entree.get("erreur"):
            erreurs.append(ligne)

rapport = {"images": images, "appels": appels, "erreurs": erreurs,
           "nombre_appels": len(appels), "nombre_erreurs": len(erreurs)}
(SORTIES / "7_rapport.json").write_text(json.dumps(rapport, ensure_ascii=False, indent=2))
print(f"{len(images)} images, {len(appels)} appels, {len(erreurs)} erreurs : 7_rapport.json")
