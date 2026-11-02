---
type: research
title: RCH - Contraintes d'impression Printify des trois produits (01-11-2026)
status: validé
date: 2026-11-01
sources:
  - "Printify Public API, spécification : https://developers.printify.com/openapi.json (lu le 01/11/2026)"
  - "Printify Public API, référence : https://developers.printify.com/ (lu le 01/11/2026)"
  - "Catalogue Printify public, API interne product-catalog-service, lue sans connexion le 01/11/2026 : /api/v2/blueprints/{1016,2769,697} ; …/print-providers ; …/print-providers/{26,86,23}/variants ; …/size-guide"
  - "Printify, aide, fichiers d'impression : https://help.printify.com/hc/en-us/articles/4483617936657 (lu le 01/11/2026)"
  - "Printify Public API, GET /v1/catalog/blueprints/{1016,2769,697}/print_providers/{26,86,23}/variants.json, appel authentifié en lecture seule (01/11/2026)"
  - "Même appel, revérifié par 3-systeme/recherches/planche-test/api/placeholders.py (02/11/2026)"
  - "[[FLOW - Personnalisation à la commande]] (réglages d'approbation, lu le 29/10/2026)"
  - "[[RCH - Audit des coûts réels Printify des trois produits (31-10-2026)]]"
  - "[[RCH - Sélection du catalogue de lancement (30-10-2026)]]"
related: ["[[SYN - Fournisseurs]]", "[[FLOW - Personnalisation à la commande]]", "[[TODO - Personnalisation au choix sur toute la surface du mug, de la boule et de la déco en bois]]", "[[A VERIFIER - Points à valider, vérifier, tester]]"]
decisions: ["[[10 - Notre serveur produit l'image finale, Printify la reçoit par l'API]]", "[[02 - Lancement avec le mug, la boule en cristal et la décoration en bois, trois imprimeurs UE]]"]
last-verified: 2026-11-02
tags: [dropshipping, fournisseurs, printify, personnalisation, research]
---
# RCH - Contraintes d'impression Printify des trois produits (01-11-2026)

## Contexte posé
Demande d'Antoine, 01/11/2026. La décision 10 fait produire le fichier d'impression par notre serveur
et l'envoie à Printify par l'API. Avant de fixer ce qu'on offre à la cliente (texte, image, forme), il
faut savoir ce que Printify et chaque imprimeur acceptent, et où ils limitent.

Produits : Standard Mug 11oz (blueprint 1016) chez Textildruck Europa (26) ; Glass Ornament, Single
(2769), forme Circle, chez Chill (86) ; Wooden Ornaments (697), six formes, chez WOYC (23).

Méthode : spécification et référence de l'API publique ; catalogue public par son API interne, sans
connexion ; aide Printify. La lecture de l'éditeur de produit dans Chrome n'a pas abouti : le
navigateur a cessé de répondre à l'ouverture de l'éditeur. Rien n'a été créé, commandé ni modifié.

## Conclusion en une phrase
L'API accepte une image différente à chaque commande, plusieurs images positionnées sur une même zone
et un design différent par variante ; elle ne rend pas de texte et ne donne pas d'aperçu sans produit
créé chez Printify ; la boule n'existe qu'en rond chez Chill ; les dimensions en pixels sont connues
(partie 8), le bois a une position `back` en plus de `front` ; la zone de sécurité, l'anse et la
découpe du bois restent à relever.

## Résultats

### 1. Mug — Standard Mug 11oz (1016), Textildruck Europa (26)
| Point | Valeur | Limite | Source |
|---|---|---|---|
| Zones | API publique : une seule position, `front`, en sublimation. Le catalogue listait aussi `all` (« All areas »), absente de l'API | — | API variants.json et catalogue, 01/11/2026 |
| Dimensions | Mug de 95 mm de haut, 80 mm de diamètre ; zone `front` de 2244 × 945 px (partie 8) | DPI implicite incohérent entre hauteur et tour : la zone ne couvre ni toute la hauteur ni tout le tour ⚠️ ; zone de sécurité, zone de l'anse : non trouvées ⚠️ | Guide des tailles et API variants.json, 01/11/2026 |
| Variante | 79703 (11oz, White, Glossy), en stock | Une seule variante | Catalogue, 01/11/2026 |
| Fichier | Formats et tailles communs (partie 4) | Rendu d'une zone laissée vide : non trouvé ⚠️ | Aide, 01/11/2026 |
| Contraintes d'impression | Décor tout le tour, finition brillante | Hauteur minimale du texte, finesse des traits, couleurs claires : non trouvées ⚠️ | Fiche du blueprint, 01/11/2026 |

### 2. Boule — Glass Ornament, Single (2769), Chill (86)
| Point | Valeur | Limite | Source |
|---|---|---|---|
| Zones | Une zone, `front`, impression UV | Recto seul | Catalogue, 01/11/2026 |
| Dimensions | 76,2 × 76,2 mm ; verre cristal ; dos blanc (« White backing ») ; ruban rouge ; zone `front` de 900 × 900 px, soit 300 DPI (partie 8) | Zone de sécurité : non trouvée ⚠️ | Fiche du blueprint et API variants.json, 01/11/2026 |
| Variante | 149574 (One size, Circle) | Chez Chill, Circle seulement ; le cœur du guide des tailles n'est pas proposé par Chill | Catalogue, 01/11/2026 |
| Fichier | Effet d'un pixel transparent sur verre à dos blanc : non trouvé | ⚠️ commande test | — |
| Contraintes d'impression | Rendu des couleurs claires en UV sur verre : non trouvé | ⚠️ commande test | — |

### 3. Décoration en bois — Wooden Ornaments (697), WOYC (23)
| Point | Valeur | Limite | Source |
|---|---|---|---|
| Zones | API publique : deux positions, `front` et `back`, en sublimation, de mêmes dimensions. Le catalogue nommait la zone `aop` (« All over print ») ; la fiche indique un dos aimanté (« Magnetic back ») | Dos réellement imprimé malgré l'aimant : non confirmé ⚠️ commande test | API variants.json, catalogue et fiche, 01/11/2026 |
| Dimensions (largeur × hauteur, mm ; épaisseur 10 mm) | Bell 86 × 105 ; Christmas Stocking 86 × 162 ; Tree 92 × 132 ; Star 85 × 97 ; Oval 85 × 125 ; Heart 87 × 115 ; pixels par forme en partie 8 | Zone de sécurité, découpe au contour : non trouvées ⚠️ | Guide des tailles et API variants.json, 01/11/2026 |
| Variantes | 72964 Bell ; 72960 Christmas Stocking ; 72963 Tree ; 72965 Star ; 72962 Oval ; 72961 Heart ; option taille unique 2012 | Même prix pour les six | Catalogue, 01/11/2026 |
| Fichier | Sous-couche blanche : non trouvée | ⚠️ commande test | — |
| Contraintes d'impression | Encre posée à plat, qui peut ne pas couvrir tout le grain : zones plus claires ou plus foncées | Rendu des couleurs claires sur bois ⚠️ | Fiche du blueprint, 01/11/2026 |

Autres mentions de la fiche : bois massif, fabriqué en Corée du Sud, ruban rouge.

### 4. Commun aux trois produits
**Fichiers** (aide Printify, 01/11/2026) :
- formats JPEG, PNG et SVG ;
- 100 Mo au plus en JPEG ou PNG, 20 Mo en SVG ;
- 300 DPI recommandés, une résolution plus faible pouvant suffire selon le produit ;
- un fichier de basse résolution est « amélioré » automatiquement par Printify avant production ;
- les exigences propres à chaque zone s'affichent dans le Product Creator.

**Commande par l'API** (openapi.json, 01/11/2026) :
- `lineItemWithBlueprint` : `print_provider_id`, `blueprint_id`, `variant_id` et `quantity` obligatoires ;
  `print_areas`, `print_details`, `external_id` de ligne et `personalisation` facultatifs ;
- `print_areas` simple : une URL d'image par position ;
- `print_areas` avancé : une liste d'images par position, chacune avec `src` (URL), `x`, `y`, `scale`
  et `angle` ; l'exemple officiel place deux images sur `front` ;
- `print_details.print_on_side` : `regular` ou `mirror`, pour les toiles ; sans objet ici ;
- chaque ligne porte ses propres URL : une image différente à chaque commande, et un design différent
  par variante, sont donc possibles ;
- la ligne prend une URL, pas un identifiant d'upload ; le moment où Printify télécharge l'URL n'est
  pas documenté ⚠️.

**Uploads** (référence de l'API, 01/11/2026) : `POST /v1/uploads/images.json`, par URL ou en base64,
`file_name` obligatoire. Au-delà de 5 Mo, l'URL est recommandée ; Printify prévoit d'abandonner le
base64 au-delà de 5 Mo. La réponse donne `id`, `width`, `height`, `size`, `mime_type` et `preview_url`.

**Débit** (référence de l'API, 01/11/2026) : 600 requêtes par minute au total, 100 par minute sur le
catalogue ; au-delà, réponse 429.

**Placeholders** (référence de l'API, 01/11/2026) : chaque variante de `variants.json` donne ses
`placeholders` avec `position`, `decoration_method`, `width` et `height` en pixels. Choisir une
position revient à choisir la méthode d'impression.

### 5. Approbation et doublons
- Statut `on-hold` : la commande attend une action de la marchande et reste modifiable (référence de
  l'API, 01/11/2026).
- `send_to_production` existe ; sa description ne dit rien de plus (openapi.json, 01/11/2026).
- Commande créée par l'API sans `send_to_production` : comportement non documenté ⚠️ commande test.
- Réglages d'approbation : Manual, automatique en 1 heure, automatique en 24 heures (par défaut), ou à
  heure fixe (aide Printify, lu le 29/10/2026, repris de [[FLOW - Personnalisation à la commande]] ;
  non relu le 01/11).
- `external_id` en doublon : les réponses de `orders.json` ne sont pas documentées dans openapi.json ;
  seule une source communautaire rapporte une 409, code 8503 ⚠️ commande test.

### 6. Ce que Printify ne permet pas
- Texte rendu par Printify sur une ligne sans produit : la `personalisation` d'une ligne renvoie à une
  configuration créée sur un produit Printify.
- Aperçu ou mockup par l'API sans produit : `personalization_previews.json` exige un `product_id`.
- Boule en cœur chez Chill.
- Impression au dos de la boule (dos blanc, une seule position `front`). Pour le bois, l'API propose une
  position `back` ; un dos réellement imprimé malgré l'aimant reste à confirmer ⚠️ commande test.

À l'inverse, plusieurs images sur une même zone sont possibles par `print_areas` avancé.

### 7. Ce que ça autorise et interdit pour la cliente
Autorise :
- une image propre à chaque commande, sur les trois produits ;
- une illustration différente par forme en bois ;
- des calques séparés sur une zone (illustration, texte), même si un fichier fusionné par notre serveur
  reste le plus sûr (décision 10).

Interdit :
- la boule en cœur ;
- un dos imprimé sur la boule ; sur le bois, le dos est proposé par l'API mais reste à confirmer ⚠️ ;
- un texte ou un aperçu produit par Printify sans produit créé chez Printify : l'aperçu reste dans
  notre thème.

### 8. Placeholders en pixels (API, 01/11/2026)
Revérifié le 02/11/2026 par `3-systeme/recherches/planche-test/api/placeholders.py` : valeurs identiques pour les trois produits.

Source : `GET https://api.printify.com/v1/catalog/blueprints/{blueprint}/print_providers/{provider}/variants.json`,
appel authentifié en lecture seule, 01/11/2026, réponse HTTP 200 pour les trois produits.

Calculs : DPI implicite = pixels ÷ mm × 25,4, avec les dimensions en mm des parties 1 à 3 ; ratio =
largeur ÷ hauteur.

**Mug — 1016, Textildruck Europa (26)**

| Variante | Position | Méthode | Pixels (l × h) | DPI implicite | Ratio px | Ratio mm |
|---|---|---|---|---|---|---|
| 79703, « 11oz / White / Glossy » | `front` | dye-sublimation | 2244 × 945 | 252,7 en hauteur (95 mm) ; 226,8 en largeur sur la circonférence (π × 80 = 251,3 mm) | 2,375 | 2,65 (circonférence ÷ hauteur) |

**Boule — 2769, Chill (86)**

| Variante | Position | Méthode | Pixels (l × h) | DPI implicite | Ratio px | Ratio mm |
|---|---|---|---|---|---|---|
| 149574, « One size / Circle » | `front` | uv | 900 × 900 | 300,0 sur 76,2 mm | 1,00 | 1,00 |

**Bois — 697, WOYC (23)** ; `back` a les mêmes dimensions que `front` pour chaque forme.

| Variante | Positions | Méthode | Pixels (l × h) | DPI largeur | DPI hauteur | Ratio px | Ratio mm |
|---|---|---|---|---|---|---|---|
| 72960 Christmas Stocking | `front`, `back` | dye-sublimation | 1158 × 1874 | 342,0 | 293,8 | 0,618 | 0,531 |
| 72961 Heart | `front`, `back` | dye-sublimation | 1098 × 1430 | 320,6 | 315,8 | 0,768 | 0,757 |
| 72962 Oval | `front`, `back` | dye-sublimation | 1085 × 1545 | 324,2 | 313,9 | 0,702 | 0,680 |
| 72963 Tree | `front`, `back` | dye-sublimation | 1149 × 1606 | 317,2 | 309,0 | 0,715 | 0,697 |
| 72964 Bell | `front`, `back` | dye-sublimation | 1097 × 1299 | 324,0 | 314,2 | 0,845 | 0,819 |
| 72965 Star | `front`, `back` | dye-sublimation | 1097 × 1214 | 327,8 | 317,9 | 0,904 | 0,876 |

Écarts avec les parties 1 à 3 :
- identifiants de variantes : tous identiques ;
- mug : seule `front` existe dans l'API ; la position `all` du catalogue n'y figure pas ;
- mug : les deux DPI ne concordent pas, la zone ne couvre ni toute la hauteur ni tout le tour ; à
  300 DPI elle mesurerait 190 × 80 mm, soit environ 61 mm laissés autour de l'anse ; hypothèse, pas
  une mesure ⚠️ ;
- bois : positions `front` et `back`, et non `aop` ; méthode sublimation, que le catalogue n'indiquait pas ;
- bois : `back` contredit « recto seul, probablement » et le dos aimanté ; dos imprimé ⚠️ commande test ;
- bois : pour cinq formes, DPI un peu au-dessus de 300 et ratio en pixels un peu plus large que la
  pièce ; la zone dépasse peut-être légèrement la pièce, comme un fond perdu ⚠️ ;
- bois : la chaussette sort du lot (342 DPI en largeur, 294 en hauteur) ; soit ses dimensions en mm
  sont fausses, soit sa zone est cadrée autrement ⚠️.

## Chiffres
Sourcés :
- dimensions des placeholders en pixels : API variants.json, mesuré le 01/11 ; DPI et ratios calculés
  à partir de ces pixels et des dimensions en mm ;
- identifiants de variantes, positions, méthodes d'impression : catalogue, mesuré le 01/11 ;
- dimensions en mm : guide des tailles du catalogue, mesuré le 01/11 ; l'unité n'est pas affichée,
  les valeurs concordent avec 76,2 mm et 8,6 × 16,2 cm déjà relevés ;
- formats et tailles de fichier : aide Printify, 01/11 ;
- 5 Mo pour le base64, 600 et 100 requêtes par minute : référence de l'API, 01/11.

Estimés : aucun.

## Caveats
- Noms de positions et identifiants de variantes : confirmés par l'API publique le 01/11 (partie 8).
- Pixels et DPI implicite relevés par l'API (partie 8). Zone de sécurité, zone de l'anse et découpe au
  contour non relevées : l'éditeur n'a pas pu être lu ⚠️.
- Rendu du blanc, des couleurs claires, des petits textes et des pixels transparents sur bois et sur
  verre : seule une commande test le dira ⚠️.

Contradictions, sans trancher :
- Chill : « rond ou cœur » dans [[RCH - Sélection du catalogue de lancement (30-10-2026)]], Circle
  seulement dans le catalogue du 01/11.
- Bois : position `aop` dans le catalogue, zone de prix `front` dans le même blueprint. Tranché par
  l'API le 01/11 : positions `front` et `back`.
- Réimpression par l'API : le registre A VERIFIER dit qu'aucun endpoint n'existe (copie api-evangelist) ;
  openapi.json du 01/11 contient `support-requests/reprint` et `support-requests/refund`.
- Bois sur un seul recto : la TODO du 31/10 le suppose, la fiche dit « Magnetic back ». L'API du 01/11
  propose une position `back` ; un dos réellement imprimé reste à tester ⚠️.

## Retenu / écarté
(à remplir à la revue)
