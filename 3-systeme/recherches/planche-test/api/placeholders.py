"""Étape 1, lecture seule : placeholders Printify des trois produits, comparés aux planches du 02/11.

Usage : python3 placeholders.py
Le jeton est lu dans la variable d'environnement PRINTIFY_TOKEN. Il n'est jamais affiché ni écrit.
Aucune écriture chez Printify : trois GET sur le catalogue.
"""
import json
import math
import os
import sys
import urllib.error
import urllib.request

API = "https://api.printify.com/v1"

# Produits retenus (décision 02) et dimensions en mm
# (source : RCH - Contraintes d'impression Printify des trois produits (01-11-2026), parties 1 à 3).
PRODUITS = [
    {"nom": "mug", "blueprint": 1016, "provider": 26},
    {"nom": "boule", "blueprint": 2769, "provider": 86},
    {"nom": "bois", "blueprint": 697, "provider": 23},
]
MM = {
    79703: (math.pi * 80, 95.0),   # mug : circonférence × hauteur
    149574: (76.2, 76.2),          # boule Circle
    72964: (86, 105),              # Bell
    72960: (86, 162),              # Christmas Stocking
    72963: (92, 132),              # Tree
    72965: (85, 97),               # Star
    72962: (85, 125),              # Oval
    72961: (87, 115),              # Heart
}
# Planches produites le 02/11 (README de planche-test), comparées à la variante ciblée.
PLANCHES = [
    ("mug-test / mire-mug", 79703, 2475, 1155),
    ("boule-A / boule-B / mire-boule", 149574, 900, 900),
    ("bois-ovale / mire-bois-ovale", 72962, 1004, 1476),
]


def get(path, token):
    req = urllib.request.Request(
        API + path,
        headers={
            "Authorization": f"Bearer {token}",
            "User-Agent": "NolaPrint-planche-test/1.0",
            "Accept": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, json.load(r)
    except urllib.error.HTTPError as e:
        corps = e.read().decode("utf-8", "replace")[:300]
        return e.code, {"erreur": corps}


def main():
    token = os.environ.get("PRINTIFY_TOKEN")
    if not token:
        sys.exit("PRINTIFY_TOKEN absent de l'environnement.")

    zones = {}  # variant_id -> (largeur px, hauteur px) de la position front
    for p in PRODUITS:
        chemin = f"/catalog/blueprints/{p['blueprint']}/print_providers/{p['provider']}/variants.json"
        status, data = get(chemin, token)
        print(f"\n=== {p['nom']} : blueprint {p['blueprint']}, provider {p['provider']} : HTTP {status}")
        if status != 200:
            print(data)
            continue
        for v in data.get("variants", []):
            print(f"variante {v['id']} : {v['title']}")
            for ph in v.get("placeholders", []):
                w, h = ph["width"], ph["height"]
                ligne = f"  {ph['position']:<6} {w} × {h} px, ratio {w / h:.3f}"
                if ph.get("decoration_method"):
                    ligne += f", méthode {ph['decoration_method']}"
                if v["id"] in MM:
                    lmm, hmm = MM[v["id"]]
                    ligne += (f" ; DPI implicite {w / lmm * 25.4:.1f} en largeur, "
                              f"{h / hmm * 25.4:.1f} en hauteur ; ratio mm {lmm / hmm:.3f}")
                print(ligne)
                if ph["position"] == "front":
                    zones[v["id"]] = (w, h)

    print("\n=== Comparaison avec les planches du 02/11")
    print("Hypothèse : Printify place l'image centrée, largeur ajustée à la zone (scale 1).")
    for nom, vid, pw, ph_ in PLANCHES:
        if vid not in zones:
            print(f"{nom} : zone de la variante {vid} non lue")
            continue
        zw, zh = zones[vid]
        if (pw, ph_) == (zw, zh):
            print(f"{nom} : {pw} × {ph_} = zone {zw} × {zh}. Rien à régénérer.")
            continue
        h_ajustee = ph_ * zw / pw
        ecart = h_ajustee - zh
        sens = "rognés" if ecart > 0 else "laissés vides"
        print(f"{nom} : planche {pw} × {ph_} (ratio {pw / ph_:.3f}), "
              f"zone {zw} × {zh} (ratio {zw / zh:.3f}). À RÉGÉNÉRER.")
        print(f"  largeur ajustée : hauteur {h_ajustee:.0f} px, soit {abs(ecart) / 2:.0f} px "
              f"{sens} en haut et en bas.")


if __name__ == "__main__":
    main()
