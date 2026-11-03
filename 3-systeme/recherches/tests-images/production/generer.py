"""Génération des illustrations de Noël 2026 avec Nano Banana Pro.

Usage, depuis tests-images/production/ :
  python generer.py element rose 1 2            # la rose, graines 1 et 2
  python generer.py element oeillet violette 1  # plusieurs éléments, une graine
  python generer.py ornement boule etoile 1 2
  python generer.py support sol branche 1 2      # bande de sol et branche, en 16:9 (brief 4 bis)
  python generer.py scene mamie 1 2              # scène Mamie, graines 1 et 2
  python generer.py scene papy papa 7            # autres palettes, graine retenue
  python generer.py hiver mamie 7                # calque d'hiver sur la scène Mamie (second tour)

Référence de style : dès qu'un fichier production/reference.png existe, il est passé à chaque appel.
Images dans production/, journal dans production/production.json. Clé dans GEMINI_API_KEY.
"""
import sys
import time
from pathlib import Path

ICI = Path(__file__).resolve().parent
sys.path.insert(0, str(ICI.parent))          # pour importer commun.py
import commun                                 # noqa: E402
import brief                                  # noqa: E402

commun.SORTIES = ICI                          # les sorties vont dans production/
SCRIPT = "production"
REFERENCE = ICI / "reference.png"
TAILLE = "2K"


def _config(aspect, graine):
    from google.genai import types
    return types.GenerateContentConfig(
        response_modalities=["TEXT", "IMAGE"], seed=int(graine),
        image_config=types.ImageConfig(aspect_ratio=aspect, image_size=TAILLE),
    )


def appel(prompt, fichier, graine, aspect, images=()):
    """Un appel Nano Banana Pro avec graine, journalisé. Renvoie le chemin ou None."""
    key = commun.cle("GEMINI_API_KEY")
    if not key:
        return None
    from google import genai
    from PIL import Image
    client = genai.Client(api_key=key)
    contenus = [prompt] + [Image.open(p) for p in images]
    debut = time.time()
    try:
        reponse = client.models.generate_content(model=commun.MODELE_GEMINI, contents=contenus,
                                                 config=_config(aspect, graine))
        chemin, mime = commun._enregistrer_gemini(reponse, fichier)
        erreur = None if chemin else "aucune image dans la réponse"
    except Exception as e:
        chemin, mime, erreur = None, None, str(e)
    commun.journal(SCRIPT, {"modele": commun.MODELE_GEMINI, "prompt": prompt, "graine": int(graine),
                            "fichier": fichier, "references": [str(p) for p in images],
                            "aspect": aspect, "taille": TAILLE, "mime": mime,
                            "duree_s": round(time.time() - debut, 1), "erreur": erreur,
                            "verdict": None, "raison": None})
    print(f"{fichier} : {'ok' if chemin else erreur}")
    return chemin


def element(nom, graine):
    prompt, fond = brief.prompt_element(nom)
    refs = [REFERENCE] if REFERENCE.exists() else []
    if refs:
        prompt = brief.REFERENCE_STYLE + prompt
    aspect = brief.ASPECT_SUPPORTS if nom in brief.SUPPORTS else "1:1"
    return appel(prompt, f"{nom}-seed{graine}.png", graine, aspect, refs)


def scene(destinataire, graine):
    prompt, fond = brief.prompt_scene(destinataire)
    refs = [REFERENCE] if REFERENCE.exists() else []
    if refs:
        prompt = brief.REFERENCE_STYLE + prompt
    return appel(prompt, f"scene-{destinataire}-seed{graine}.png", graine, "4:3", refs)


def hiver(destinataire, graine):
    """Second tour sur la scène retenue : la scène de base passe en image, le prompt demande l'ajout."""
    base = ICI / f"scene-{destinataire}-seed{graine}.png"
    if not base.exists():
        raise SystemExit(f"{base.name} absent : génère d'abord la scène.")
    return appel(brief.HIVER, f"scene-{destinataire}-hiver-seed{graine}.png", graine, "4:3", [base])


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) < 3:
        raise SystemExit(__doc__)
    mode, noms, graines = args[0], [a for a in args[1:] if not a.isdigit()], [a for a in args[1:] if a.isdigit()]
    for nom in noms:
        for g in graines:
            if mode in ("element", "ornement", "support"):
                if nom not in brief.FLEURS and nom not in brief.ORNEMENTS and nom not in brief.SUPPORTS:
                    raise SystemExit(f"élément inconnu : {nom}")
                element(nom, g)
            elif mode == "scene":
                scene(nom, g)
            elif mode == "hiver":
                hiver(nom, g)
            else:
                raise SystemExit(__doc__)
