"""Étape 2 : commande test Printify des trois procédés (planches du 02/11, 300 DPI).

Usage :
  python3 commande_test.py            mug-test, boule-A, bois-ovale (3 lignes)
  python3 commande_test.py --mires    ajoute les trois mires (6 lignes)
  python3 commande_test.py --shop ID  si le compte a plusieurs boutiques

Ce que fait le script :
  1. lit le shop_id par GET /v1/shops.json ;
  2. téléverse les PNG en base64 par POST /v1/uploads/images.json et affiche les identifiants ;
  3. affiche le récapitulatif et demande « oui » avant toute commande ;
  4. crée UNE commande externe (lineItemWithBlueprint), SANS send_to_production ;
  5. relit la commande par GET et affiche statut et coûts.

Le jeton est lu dans PRINTIFY_TOKEN : jamais affiché, jamais écrit.
L'adresse est lue dans adresse.json, à côté du script, rempli par Antoine (à ne pas committer).
"""
import argparse
import base64
import json
import os
import sys
import urllib.error
import urllib.request

API = "https://api.printify.com/v1"
HERE = os.path.dirname(os.path.abspath(__file__))
PLANCHES = os.path.dirname(HERE)
EXTERNAL_ID = "nolaprint-test-2026-11-05"

# blueprint, print_provider, variant (API variants.json, 01/11 et 02/11/2026), position front
MUG = (1016, 26, 79703)
BOULE = (2769, 86, 149574)
BOIS_OVALE = (697, 23, 72962)

PIECES = [
    ("mug-test-2244x945.png", MUG),
    ("boule-A-900x900.png", BOULE),
    ("bois-ovale-1085x1545.png", BOIS_OVALE),
]
MIRES = [
    ("mire-mug-2244x945.png", MUG),
    ("mire-boule-900x900.png", BOULE),
    ("mire-bois-ovale-1085x1545.png", BOIS_OVALE),
]
CHAMPS_ADRESSE = ["first_name", "last_name", "email", "phone", "country", "region",
                  "address1", "address2", "city", "zip"]


def appel(methode, chemin, token, corps=None):
    data = json.dumps(corps).encode("utf-8") if corps is not None else None
    req = urllib.request.Request(
        API + chemin, data=data, method=methode,
        headers={
            "Authorization": f"Bearer {token}",
            "User-Agent": "NolaPrint-commande-test/1.0",
            "Content-Type": "application/json;charset=utf-8",
            "Accept": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            texte = r.read().decode("utf-8")
            return r.status, (json.loads(texte) if texte else {})
    except urllib.error.HTTPError as e:
        return e.code, {"erreur": e.read().decode("utf-8", "replace")[:800]}


def stop(msg):
    sys.exit(f"ARRÊT : {msg}")


def euros(centimes):
    return "—" if centimes is None else f"{centimes / 100:.2f}"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--mires", action="store_true", help="ajoute les trois mires")
    p.add_argument("--shop", type=int, help="shop_id si plusieurs boutiques")
    args = p.parse_args()

    token = os.environ.get("PRINTIFY_TOKEN")
    if not token:
        stop("PRINTIFY_TOKEN absent de l'environnement.")

    # Adresse : contrôlée avant tout appel
    chemin_adresse = os.path.join(HERE, "adresse.json")
    if not os.path.exists(chemin_adresse):
        stop(f"{chemin_adresse} introuvable.")
    with open(chemin_adresse, encoding="utf-8") as f:
        adresse = json.load(f)
    manquants = [c for c in CHAMPS_ADRESSE if c != "address2" and not str(adresse.get(c, "")).strip()]
    if manquants:
        stop(f"champs vides dans adresse.json : {', '.join(manquants)}")
    adresse = {c: adresse.get(c, "") for c in CHAMPS_ADRESSE}

    lignes = PIECES + (MIRES if args.mires else [])
    for nom, _ in lignes:
        if not os.path.exists(os.path.join(PLANCHES, nom)):
            stop(f"planche absente : {nom}")

    # 1. Boutique
    status, shops = appel("GET", "/shops.json", token)
    if status != 200:
        stop(f"GET /shops.json : HTTP {status} {shops}")
    print("Boutiques :")
    for s in shops:
        print(f"  {s['id']} : {s.get('title')} ({s.get('sales_channel')})")
    if args.shop:
        shop_id = args.shop
    elif len(shops) == 1:
        shop_id = shops[0]["id"]
    else:
        stop("aucune ou plusieurs boutiques : relance avec --shop ID.")
    print(f"shop_id retenu : {shop_id}\n")

    # 2. Téléversements
    images = {}
    for nom, _ in lignes:
        with open(os.path.join(PLANCHES, nom), "rb") as f:
            contenu = base64.b64encode(f.read()).decode("ascii")
        status, up = appel("POST", "/uploads/images.json", token,
                           {"file_name": nom, "contents": contenu})
        if status not in (200, 201):
            stop(f"upload {nom} : HTTP {status} {up}")
        images[nom] = up
        print(f"upload {nom} : id {up['id']}, {up.get('width')} × {up.get('height')} px, "
              f"{up.get('size')} octets")
        print(f"  preview_url {up.get('preview_url')}")

    # 3. Commande (la ligne prend une URL : on passe la preview_url de l'upload)
    line_items = []
    for nom, (bp, pp, var) in lignes:
        line_items.append({
            "blueprint_id": bp,
            "print_provider_id": pp,
            "variant_id": var,
            "quantity": 1,
            "print_areas": {"front": images[nom]["preview_url"]},
        })
    commande = {
        "external_id": EXTERNAL_ID,
        "label": "Planche de test des trois procédés",
        "line_items": line_items,
        "shipping_method": 1,
        "is_printify_express": False,
        "is_economy_shipping": False,
        "send_shipping_notification": False,
        "address_to": adresse,
    }

    print(f"\nCommande à créer : external_id {EXTERNAL_ID}, {len(line_items)} ligne(s), "
          f"livraison {adresse['city']} ({adresse['country']}).")
    for nom, (bp, pp, var) in lignes:
        print(f"  {nom} : blueprint {bp}, provider {pp}, variante {var}, front")
    print("Pas de send_to_production : la commande attendra ton approbation dans Printify.")
    if input("Créer la commande ? Tape oui : ").strip().lower() != "oui":
        stop("annulé, aucune commande créée (les uploads restent dans la médiathèque).")

    status, cree = appel("POST", f"/shops/{shop_id}/orders.json", token, commande)
    print(f"\nPOST orders.json : HTTP {status}")
    if status not in (200, 201):
        print(json.dumps(cree, ensure_ascii=False, indent=2))
        stop("commande non créée.")
    order_id = cree.get("id")
    print(f"identifiant de commande : {order_id}")

    # 4. Relecture
    status, o = appel("GET", f"/shops/{shop_id}/orders/{order_id}.json", token)
    print(f"\nGET relecture : HTTP {status}")
    if status != 200:
        print(o)
        return
    print(f"statut : {o.get('status')}")
    print(f"external_id : {o.get('metadata', {}).get('shop_order_label') or o.get('external_id')}")
    print(f"total articles : {euros(o.get('total_price'))}")
    print(f"total expédition : {euros(o.get('total_shipping'))}")
    print(f"total taxes : {euros(o.get('total_tax'))}")
    for li in o.get("line_items", []):
        print(f"  ligne {li.get('product_id') or ''} variante {li.get('variant_id')} : "
              f"coût {euros(li.get('cost'))}, expédition {euros(li.get('shipping_cost'))}, "
              f"statut {li.get('status')}, provider {li.get('print_provider_id')}")
    print("\nMontants dans la devise du compte Printify (renvoyés en centimes, divisés par 100).")


if __name__ == "__main__":
    main()
