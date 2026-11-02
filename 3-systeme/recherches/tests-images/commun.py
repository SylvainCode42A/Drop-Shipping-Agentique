"""Outils communs aux tests d'images NolaPrint (RCH du 02-11-2026).

Les clés sont lues dans GEMINI_API_KEY et IDEOGRAM_API_KEY. Elles ne sont jamais
écrites, ni dans les fichiers ni dans les journaux.
Dépendances : pip install google-genai requests pillow numpy
"""
import json
import os
import time
from pathlib import Path

import numpy as np
import requests
from PIL import Image

DOSSIER = Path(__file__).resolve().parent
SORTIES = DOSSIER / "sorties"
SORTIES.mkdir(exist_ok=True)

STYLE = ("gouache illustration, opaque pigment, no wash, closed contours, "
         "medium to saturated colors, bold simple shapes, no fine detail, "
         "no drop shadow, no paper texture")

MODELE_GEMINI = "gemini-3-pro-image"
IDEO_GENERATE = "https://api.ideogram.ai/v2/image/generate/ideogram-4-5"
IDEO_EDIT = "https://api.ideogram.ai/v2/image/precise-edit/ideogram-4-5"


def cle(nom):
    """Renvoie la clé, ou None si elle manque (le modèle est alors sauté)."""
    valeur = os.environ.get(nom)
    if not valeur:
        print(f"{nom} absente : modèle sauté.")
    return valeur


def journal(script, entree):
    """Ajoute une entrée au journal JSON du script, dans sorties/."""
    chemin = SORTIES / f"{script}.json"
    donnees = json.loads(chemin.read_text()) if chemin.exists() else []
    entree["horodatage"] = time.strftime("%Y-%m-%d %H:%M:%S")
    donnees.append(entree)
    chemin.write_text(json.dumps(donnees, ensure_ascii=False, indent=2))


# ---------- Gemini (Nano Banana Pro) ----------

def _config_gemini(aspect, taille):
    from google.genai import types
    return types.GenerateContentConfig(
        response_modalities=["TEXT", "IMAGE"],
        image_config=types.ImageConfig(aspect_ratio=aspect, image_size=taille),
    )


def _enregistrer_gemini(reponse, fichier):
    """Écrit la première image de la réponse. Renvoie (chemin, type MIME) ou (None, None).
    Sans image, lève une erreur qui donne le motif d'arrêt du modèle."""
    candidat = reponse.candidates[0] if reponse.candidates else None
    parts = candidat.content.parts if candidat and candidat.content else None
    if not parts:
        motif = getattr(candidat, "finish_reason", None) if candidat else None
        blocage = getattr(reponse, "prompt_feedback", None)
        raise RuntimeError(f"aucune image ; finish_reason={motif} ; prompt_feedback={blocage}")
    for part in parts:
        if getattr(part, "inline_data", None) and part.inline_data.data:
            chemin = SORTIES / fichier
            chemin.write_bytes(part.inline_data.data)
            return chemin, part.inline_data.mime_type
    return None, None


def gemini(script, prompt, fichier, images=(), aspect="1:1", taille="1K"):
    """Un appel Nano Banana Pro. images : chemins d'images de référence."""
    key = cle("GEMINI_API_KEY")
    if not key:
        return None
    from google import genai
    client = genai.Client(api_key=key)
    contenus = [prompt] + [Image.open(p) for p in images]
    debut = time.time()
    try:
        reponse = client.models.generate_content(
            model=MODELE_GEMINI, contents=contenus,
            config=_config_gemini(aspect, taille))
        chemin, mime = _enregistrer_gemini(reponse, fichier)
        erreur = None if chemin else "aucune image dans la réponse"
    except Exception as e:  # on journalise l'échec, sans arrêter le script
        chemin, mime, erreur = None, None, str(e)
    journal(script, {"modele": MODELE_GEMINI, "prompt": prompt, "fichier": fichier,
                     "references": [str(p) for p in images], "aspect": aspect,
                     "taille": taille, "mime": mime, "duree_s": round(time.time() - debut, 1),
                     "erreur": erreur})
    print(f"{fichier} : {'ok' if chemin else erreur}")
    return chemin


def gemini_chat(script, tours, fichiers, aspect="1:1", taille="1K"):
    """Édition en plusieurs tours : un fichier écrit par tour."""
    key = cle("GEMINI_API_KEY")
    if not key:
        return []
    from google import genai
    client = genai.Client(api_key=key)
    chat = client.chats.create(model=MODELE_GEMINI, config=_config_gemini(aspect, taille))
    chemins = []
    for prompt, fichier in zip(tours, fichiers):
        debut = time.time()
        try:
            chemin, mime = _enregistrer_gemini(chat.send_message(prompt), fichier)
            erreur = None if chemin else "aucune image dans la réponse"
        except Exception as e:
            chemin, mime, erreur = None, None, str(e)
        journal(script, {"modele": MODELE_GEMINI, "mode": "chat", "prompt": prompt,
                         "fichier": fichier, "mime": mime,
                         "duree_s": round(time.time() - debut, 1), "erreur": erreur})
        print(f"{fichier} : {'ok' if chemin else erreur}")
        chemins.append(chemin)
        if not chemin:
            break
    return chemins


# ---------- Ideogram ----------

def _premiere_url(objet):
    """Cherche la première URL d'image dans la réponse (format non vérifié)."""
    if isinstance(objet, dict):
        for k, v in objet.items():
            if k == "url" and isinstance(v, str):
                return v
            trouve = _premiere_url(v)
            if trouve:
                return trouve
    elif isinstance(objet, list):
        for v in objet:
            trouve = _premiere_url(v)
            if trouve:
                return trouve
    return None


def _sans_urls(objet):
    """Copie de la réponse pour le journal, sans les URL signées."""
    if isinstance(objet, dict):
        return {k: ("<url>" if k == "url" else _sans_urls(v)) for k, v in objet.items()}
    if isinstance(objet, list):
        return [_sans_urls(v) for v in objet]
    return objet


def ideogram(script, url, champs, fichier, fichiers_joints=()):
    """Un appel Ideogram en multipart. fichiers_joints : liste de (champ, chemin)."""
    key = cle("IDEOGRAM_API_KEY")
    if not key:
        return None
    ouverts = [(nom, (Path(p).name, open(p, "rb"), "image/png")) for nom, p in fichiers_joints]
    # Ideogram exige multipart/form-data, même sans fichier joint :
    # chaque champ texte passe donc en partie multipart (nom de fichier None).
    parties = [(k, (None, str(v))) for k, v in champs.items()] + ouverts
    debut = time.time()
    chemin, erreur, brut = None, None, None
    try:
        r = requests.post(url, headers={"Api-Key": key}, files=parties, timeout=300)
        brut = r.json() if r.headers.get("content-type", "").startswith("application/json") else r.text
        if r.ok:
            lien = _premiere_url(brut)
            if lien:
                chemin = SORTIES / fichier
                chemin.write_bytes(requests.get(lien, timeout=120).content)
            else:
                erreur = "aucune URL dans la réponse"
        else:
            erreur = f"HTTP {r.status_code}"
    except Exception as e:
        erreur = str(e)
    finally:
        for _, (_, f, _) in ouverts:
            f.close()
    journal(script, {"modele": url.rsplit("/", 2)[-2] + "/" + url.rsplit("/", 1)[-1],
                     "champs": champs, "joints": [[n, str(p)] for n, p in fichiers_joints],
                     "fichier": fichier, "duree_s": round(time.time() - debut, 1),
                     "erreur": erreur, "reponse": _sans_urls(brut)})
    print(f"{fichier} : {'ok' if chemin else erreur}")
    return chemin


# ---------- Masques et différences ----------

def masque_ideogram(source, boite, fichier):
    """Masque Ideogram : noir = zone à modifier, blanc = zone gardée.
    boite = (gauche, haut, droite, bas) en fractions de 0 à 1."""
    largeur, hauteur = Image.open(source).size
    masque = Image.new("L", (largeur, hauteur), 255)
    g, h, d, b = boite
    masque.paste(0, (int(g * largeur), int(h * hauteur), int(d * largeur), int(b * hauteur)))
    chemin = SORTIES / fichier
    masque.save(chemin)
    return chemin


def difference(avant, apres, masque, fichier):
    """Mesure l'écart hors masque entre deux images. Écrit une carte de différence."""
    a = Image.open(avant).convert("RGB")
    b = Image.open(apres).convert("RGB")
    redim = a.size != b.size
    if redim:
        b = b.resize(a.size)
    m = np.array(Image.open(masque).convert("L").resize(a.size)) > 127  # vrai = hors zone
    ecart = np.abs(np.asarray(a, dtype=np.int16) - np.asarray(b, dtype=np.int16)).max(axis=2)
    Image.fromarray(np.clip(ecart * 4, 0, 255).astype(np.uint8)).save(SORTIES / fichier)
    hors = ecart[m]
    return {"ecart_moyen_hors_masque": round(float(hors.mean()), 2),
            "part_pixels_changes_hors_masque": round(float((hors > 8).mean()), 4),
            "tailles_differentes": redim}
