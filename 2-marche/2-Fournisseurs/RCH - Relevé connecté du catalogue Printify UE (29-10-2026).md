---
type: research
title: RCH - Relevé connecté du catalogue Printify UE (29-10-2026)
status: validé
related: ["[[SYN - Fournisseurs]]", "[[RCH - Vérification Printify UE du mug et vue d'ensemble des produits (28-10-2026)]]", "[[RCH - Fournisseurs print-on-demand et API (25-10-2026)]]", "[[05 - Printify seul fournisseur avec partenaire UE figé, franchise de TVA au départ]]", "[[A VERIFIER - Points à valider, vérifier, tester]]"]
decisions: []
date: 2026-10-29
sources:
  - Catalogue Printify connecté (compte d'Antoine), filtre « Ships from : Europe », API interne product-catalog-service lue par le navigateur, 29/10/2026 vers 10 h 45
  - https://developers.printify.com/ (section Catalog, profils d'expédition)
  - https://developers.printify.com/openapi.json (schémas submitOrderRequest et lineItemWithBlueprint)
  - https://help.printify.com/hc/en-us/articles/4483617307665 (Other orders)
  - https://help.printify.com/hc/en-us/articles/4483600546705-Can-I-claim-a-VAT-exemption-on-orders-from-Printify
  - https://help.printify.com/hc/en-us/articles/4483635869073-Does-Printify-charge-VAT-on-my-orders
  - https://printify.com/network-fulfillment-status/ (mise à jour du 22/10/2026)
  - https://printify.com/blog/holiday-guide/ (21/09/2026)
last-verified: 2026-10-29
tags: [dropshipping, fournisseurs, mug, printify, api]
---
# RCH - Relevé connecté du catalogue Printify UE (29-10-2026)

## Contexte posé
Relevé factuel du catalogue Printify, connecté au compte, pour une boutique française.
Destination France, filtre « Ships from : Europe ». Quatre parties : les mugs 11 oz, les
autres produits, les lots en un colis, l'API et les commandes. Consigne : pas de
recommandation, contradictions listées sans trancher. Complète la RCH du 28/10/2026, qui
n'avait que l'affichage public.

## Conclusion en une phrase
Le mug blanc 535 n'a aucun imprimeur UE, mais cinq autres mugs 11 oz en ont un (OPT OnDemand,
Textildruck Europa, Harrier), et l'API accepte une commande sans produit créé au préalable.

## Résultats

### Partie 1 : mugs
- Blueprint 535 « 11oz White Mug » : aucun imprimeur UE. Printify affiche « There are no
  local providers available for this product in your selected country or region ». Seul
  imprimeur : T Shirt and Sons (Royaume-Uni). Capture du 29/10 conservée hors vault.
- Blueprint 827 : l'API interne renvoie 404, aucun imprimeur. La mention « discontinued »
  n'a pas été relue. ⚠️ à vérifier
- Mugs 11 oz avec imprimeur UE : 441 Ceramic Mug (EU) chez OPT OnDemand (CZ) ; 1016 Standard
  Mug, 1018 Two-Tone, 1017 Color-Changing et 1117 Black Coffee Cup chez Textildruck Europa
  (DE) ; 1125 Ceramic Coffee Cups, 635 Accent et 479 Black Mug chez Harrier (sites CZ et GB).
- Lavage : lave-vaisselle pour 441, 1016, 1018, 635, 1125 ; lavage main pour 1017 et 1117.
- Imprimeurs hors UE vus : T Shirt and Sons (GB), Printify Choice, SwiftPOD, Monster Digital,
  District Photo, SPOKE (US), Colorway (US, AU, GB), Prima Printing (AU).

### Partie 2 : autres produits
- Imprimeur UE trouvé : sous-verre céramique 1523 (WOYC, site IT) ; coussin garni 220 et
  housse 229 (MWW On Demand, site DE) ; tablier AOP 418 (MWW) ; tote W801 731 (Textildruck
  Europa) ; tote 1930 et gobelet inox 20 oz 1927 (Printful, site LV) ; affiches 1033 et 1275
  (Posterflow, DE), 443 (OPT OnDemand), 492, 493, 494 (Print Pigeons, LV), 1220 et 1236
  (Jondo, site ES) ; Mason Jar 742 (Textildruck) ; plaids Sherpa 238 et 736 (MWW).
- Aucun imprimeur UE : Corkwood Coaster Set 510 (US, AU, GB), Cork Back Coaster 480 (US),
  torchons 677, 1003, 1169, 11032, tabliers 713, 830 (GB) et 858 (CN), travel mugs et autres
  gobelets testés, bougies, planches à découper, puzzles et boîtes métal testés.
- Le Mason Jar 742 (Textildruck, 12,81 $) est en verre givré, pas en inox.

### Partie 3 : lots en un colis
- OPT OnDemand fabrique le mug 441 et l'affiche 443.
- Textildruck Europa fabrique les mugs 1016 à 1018 et 1117, et le tote 731.
- Printful fabrique le mug 478 et le tote 1930.
- Harrier : aucun autre produit de la liste parmi les blueprints testés.
- La documentation API applique le tarif « article suivant » aux articles du même blueprint
  et du même imprimeur. L'envoi de deux blueprints dans un seul colis n'est pas documenté.
  ⚠️ à vérifier

### Partie 4 : API et commandes
- `POST /v1/shops/{shop_id}/orders.json` accepte une ligne `lineItemWithBlueprint` :
  `print_provider_id`, `blueprint_id`, `variant_id`, `quantity` obligatoires, `print_areas`
  simple (une URL par position) ou avancé (image, échelle, x, y, angle). Source : openapi.json.
- La documentation ajoute que la création de produit issue d'une commande n'est pas limitée.
- Exemple de corps : voir ci-dessous. Le `variant_id` 62327 (11 oz du 441 chez OPT) vient de
  l'API interne. ⚠️ à vérifier par l'API publique
- Désactiver la synchronisation Shopify pour un produit : aucun réglage par produit trouvé.
  Une commande sans produit Printify lié arrive dans l'onglet « Other orders » et s'importe
  à la main. Source : article 4483617307665.
- TVA : Printify facture la TVA sur les commandes vers l'UE, le Royaume-Uni et la Norvège.
  Elle est récupérable « si vous êtes assujetti ». Printify ne mentionne pas la franchise en base.
- Dates limites de Noël 2026 : non publiées au 22/10/2026. La page affiche encore 2025.

```json
{
  "external_id": "shopify-1001",
  "line_items": [{
    "blueprint_id": 441,
    "print_provider_id": 30,
    "variant_id": 62327,
    "print_areas": { "front": "https://exemple.fr/design-1001.png" },
    "quantity": 1
  }],
  "shipping_method": 1,
  "send_shipping_notification": false,
  "address_to": {
    "first_name": "Jeanne", "last_name": "Martin",
    "email": "jeanne@exemple.fr", "phone": "0600000000",
    "country": "FR", "region": "", "address1": "1 rue Exemple",
    "city": "Nice", "zip": "06000"
  }
}
```

## Chiffres
Tous mesurés le 29/10 dans le catalogue connecté, en dollars, sauf mention.

| Produit | Imprimeur | Prix std / Premium | Port FR, 1er puis suivant |
|---|---|---|---|
| Mug 441, 11 oz | OPT OnDemand | 5,88 / 4,39 $ | 6,89 puis 1,99 $ (5 à 8 j) |
| Mug 441, 15 oz | OPT OnDemand | 9,87 / 7,37 $ | 6,89 puis 1,99 $ |
| Mug 1016, 11 oz blanc | Textildruck Europa | 5,91 / 4,42 $ | 6,89 puis 1,99 $ (5 à 10 j) |
| Mug 1018, bicolore | Textildruck Europa | 6,90 / 5,15 $ | 6,89 puis 1,99 $ |
| Mug 1017, magique | Textildruck Europa | 8,19 / 6,12 $ | 6,89 puis 1,99 $ |
| Mug 1117, noir | Textildruck Europa | 9,31 / 6,96 $ | 6,89 puis 1,99 $ |
| Mug 1125, 11 oz blanc | Harrier | 5,47 / 4,08 $ | 6,89 puis 2,39 $ (5 à 15 j) |
| Mug 635, accent | Harrier | 7,91 / 5,70 $ | 6,89 puis 2,39 $ |
| Mug 535, 11 oz blanc | T Shirt and Sons (GB) | 5,34 / 3,99 $ | 15,49 puis 1,99 $ (5 à 10 j) |
| Mug 478, 11 oz | Printful | 5,02 / 3,75 $ | 22,09 puis 7,99 $, tarif « Rest of the World » |
| Sous-verre 1523 | WOYC | 8,37 / 6,06 $ | 5,99 puis 1,49 $ |
| Housse 229, 14 à 18 po | MWW On Demand | 11,71 à 13,89 $ | 5,99 puis 1,39 $ |
| Coussin 220, 14 à 18 po | MWW On Demand | 16,67 à 20,38 $ | 12,79 à 13,89 puis 5,69 $ |
| Tablier 418 | MWW On Demand | 22,54 / 16,85 $ | 6,69 puis 1,39 $ |
| Tote 731 (W801) | Textildruck Europa | 13,00 / 9,72 $ | 5,69 puis 1,19 $ |
| Tote 1930 | Printful | 18,68 / 15,94 $ | 4,99 puis 1,45 $ |
| Gobelet inox 1927, 20 oz | Printful | 21,79 / 19,32 $ | 7,79 puis 4,90 $ |
| Mason Jar 742 | Textildruck Europa | 12,81 / 9,29 $ | 6,89 puis 1,99 $ |
| Plaid Sherpa 238 | MWW On Demand | 24,81 à 49,26 $ | 10,39 à 24,49 $ |
| Affiche 1033, A4 / A3 / 30 × 40 / 50 × 70 | Posterflow | 9,26 / 11,15 / 11,15 / 15,86 $ | 16,29 puis 0,29 $ (5 à 15 j) |
| Affiche 1275 encadrée, mêmes formats | Posterflow | 22,66 / 29,28 / 29,28 / 41,54 $ | 16,79 à 18,89 puis 1,99 à 3,99 $ |
| Affiche 443, A4 / A3 | OPT OnDemand | 6,50 / 7,09 $ | 6,09 puis 0,29 $ (5 à 8 j) |

Notes des imprimeurs (mesuré le 29/10) : OPT OnDemand 9,27 ; Harrier 9,57 ; Textildruck
Europa 8,65 ; MWW On Demand 8,49 ; Posterflow 9,71 ; Print Pigeons 10.

Dates limites Noël 2025, livraison standard vers l'Europe (source : network-fulfillment-status) :
OPT OnDemand 5 déc. ; Posterflow 27 nov. ; Print Pigeons 28 nov. ; Textildruck Europa 9 déc.
(priority 11 déc.) ; Harrier 2 déc. ; Printful 5 déc.

## Caveats
- Prix affichés en dollars. Les euros n'ont pas été relevés.
- L'API interne du catalogue n'est pas l'API publique. Ses identifiants restent à confirmer.
- Harrier, WOYC, MWW, Printful et Jondo ont plusieurs sites. Le site qui expédie vers la
  France n'est pas affiché. ⚠️ à vérifier
- Printful déclare des sites en Lettonie et en Espagne, mais sa table pour le mug 478 n'a pas
  de ligne France et applique « Rest of the World ».
- Non trouvé : torchon Greenbomb, tablier Textildruck Europa, pixels et DPI par imprimeur,
  format de fichier, option de routage UE de la boutique, envoi à plat ou en tube Posterflow.

Contradictions avec les prix publics, sans trancher :
- Sous-verres Colorway : 14,27 $ en public, 14,55 $ en connecté.
- Affiche Posterflow : dès 9,08 $ et encadrée dès 22,22 $ en public, 9,26 $ et 22,66 $ en connecté.
- Tote W801 à 13,00 $ et mug 535 à 5,34 $ : identiques.

## Retenu / écarté
(rempli à la revue)
