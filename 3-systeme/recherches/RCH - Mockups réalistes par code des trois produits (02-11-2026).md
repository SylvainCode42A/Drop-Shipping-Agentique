---
type: research
title: RCH - Mockups réalistes par code des trois produits (02-11-2026)
status: validé
date: 2026-11-02
sources:
  - "Dynamic Mockups, gabarits mug 11 oz : https://dynamicmockups.com/templates/c/mug-mockups/11oz/ (lu le 02/11/2026)"
  - "Dynamic Mockups, API : https://dynamicmockups.com/mockup-generator-api/ (lu le 02/11/2026)"
  - "Dynamic Mockups, CGU : https://dynamicmockups.com/terms-of-service/ (lu le 02/11/2026)"
  - "Dynamic Mockups, dépôt : https://github.com/dynamicmockups/mockup-generator-api (lu le 02/11/2026)"
  - "SudoMock, tarifs : https://sudomock.com/pricing (page « Verified July 2026 », lu le 02/11/2026)"
  - "SudoMock, SDK Python : https://github.com/sudomock/sudomock-python (lu le 02/11/2026)"
  - "SudoMock, comparatifs (concurrent direct) : https://sudomock.com/vs/placeit ; https://sudomock.com/blog/adobe-photoshop-api-pricing-2026 ; https://sudomock.com/blog/printful-mockup-api-pricing-2026 (lus le 02/11/2026)"
  - "Mediamodifier, API : https://mockup-api.mediamodifier.com/ et gabarit Christmas Ball https://mediamodifier.com/mockup/christmas-ball-ornament-online-mockup-template/1030 (lus le 02/11/2026)"
  - "Placeit, revue tierce : https://ecomm.design/placeit-pricing/ (lu le 02/11/2026)"
  - "Bannerbear et Templated, revues tierces : https://www.1capture.io/blog/bannerbear-review ; https://html2img.com/articles/bannerbear-alternatives/ ; https://www.imejis.io/blogs/comparisons/best-bannerbear-alternatives (lus le 02/11/2026)"
  - "Printify Public API, référence : https://developers.printify.com/ (lu le 02/11/2026)"
  - "Printify, CGU de l'API : https://printify.com/api-terms/ (lu le 02/11/2026)"
  - "Ultrathink, retour développeur Printify API (22/04/2026) : https://ultrathink.art/blog/printify-api-programmatic-products"
  - "Make Community, mockups Printify vides : https://community.make.com/t/printify-product-creation-images-not-showing-in-mock-ups/14074"
  - "Printful, ornements bois : https://www.printful.com/custom/decor/holiday/wooden-ornaments (lu le 02/11/2026)"
  - "Cloudinary, déformation par carte de déplacement : https://cloudinary.com/documentation/reshaping_and_distorting_images"
  - "Roy Shilkrot, cylindricalWarp (OpenCV) : https://gist.github.com/royshil/0b21e8e7c6c1f46a16db66c384742b2b"
  - "Snibgo, Cylinders (ImageMagick) : https://im.snibgo.com/cylinder.htm"
  - "[[RCH - Contraintes d'impression Printify des trois produits (01-11-2026)]]"
related: ["[[TODO - Personnalisation au choix sur toute la surface du mug, de la boule et de la déco en bois]]", "[[CMP - Illustrations]]", "[[RCH - Contraintes d'impression Printify des trois produits (01-11-2026)]]", "[[MOD - Catalogue et fiche produit]]", "[[A VERIFIER - Points à valider, vérifier, tester]]"]
decisions: ["[[10 - Notre serveur produit l'image finale, Printify la reçoit par l'API]]", "[[08 - Personnalisation à la commande en génération interne, test Printify avant le 5 novembre]]", "[[07 - La maquette est le cahier des charges du thème Shopify]]"]
last-verified: 2026-11-02
tags: [dropshipping, systeme, boutique, mockup, printify, research]
---
# RCH - Mockups réalistes par code des trois produits (02-11-2026)

## Contexte posé
Demande d'Antoine, 02/11/2026. L'aperçu produit est rendu par notre thème, pas par Printify.
Printify ne donne aucun mockup sans produit créé
([[RCH - Contraintes d'impression Printify des trois produits (01-11-2026)]]).
Notre serveur produit l'image finale ([[10 - Notre serveur produit l'image finale, Printify la reçoit par l'API]]).
La décision 08 interdit un aperçu JavaScript qui diverge du rendu.
La cliente peut personnaliser toute la surface
([[TODO - Personnalisation au choix sur toute la surface du mug, de la boule et de la déco en bois]]).

Supports : Standard Mug 11oz (blueprint 1016, Textildruck Europa 26), vue de face et tour complet ;
Glass Ornament Single (2769, Chill 86), rond 76,2 mm, dos blanc, ruban ;
Wooden Ornaments (697, WOYC 23), six formes : cloche, chaussette, sapin, étoile, ovale, cœur.

Questions :
1. API de rendu PSD : gabarit par objet, prix par rendu, délai, qualité, filigrane.
2. Rendu maison : déformation par code, photo d'échantillon avec calque de placement, protocole photo.
3. Aperçu en direct : rendu serveur ou canvas, et ce que la décision 08 interdit.
4. Printify : un produit « modèle » par support donne-t-il des mockups pour n'importe quelle image, à quel coût en appels.

Méthode : recherche web du 02/11/2026. Rien n'a été créé ni commandé chez Printify.

## Conclusion en une phrase
Un rendu maison côté serveur, calibré sur des photos d'échantillons imprimés d'une mire, couvre les
trois produits pour un coût par mockup quasi nul et respecte la décision 08 par construction ;
les API de mockups n'ont pas de gabarit pour la boule ni pour le bois et facturent chaque angle ;
Printify ne sert qu'à vérifier le placement, une fois par support.

## Résultats

### 1. API de rendu de mockups
| Service | Mug 11 oz | Boule 76 mm | Bois 6 formes | Import PSD | Prix | Délai | Résolution | Filigrane |
|---|---|---|---|---|---|---|---|---|
| Dynamic Mockups | Oui, plus de 500 gabarits annoncés | Non trouvé | Non trouvé | Oui | Pro 15 $/mois à l'année (19 $ au mois), 3 600 crédits/an, 1 crédit par rendu ; recharge 0,051 $/crédit | Moins de 1 s annoncé ; 30 images en 4 s | Jusqu'à 4096 px | En Free seulement |
| SudoMock | Pas de bibliothèque ; on apporte son PSD | Non | Non | Oui, gratuit | 0,05 $/rendu sans abonnement (5 $ minimum) ; Starter 25 $/mois ; jusqu'à 0,002 $ au volume max | Moins de 1 s annoncé | Jusqu'à 10 000 px | Tant que la carte n'est pas validée, avec largeur limitée à 1 024 px |
| Mediamodifier | Bibliothèque générale | Un gabarit « Christmas Ball » générique (2017) | Non | Sur devis (15 à 35 $ par gabarit) | 499 $/mois pour 5 000 rendus | Non publié | Selon gabarit | Non précisé |
| Placeit | Oui, à la main | Générique | Non | Non | 14,95 $/mois ; pas d'API | — | — | — |
| Smartmockups | Fermé le 27/09/2024 (racheté par Canva) | — | — | — | — | — | — | — |
| Bannerbear, Templated | Compositing 2D, sans déformation | Non | Non | Non | 49 $/mois pour 1 000 (Bannerbear) ; 29 $/mois pour 1 000 (Templated) | — | — | — |
| Printful Mockup Generator | Oui | Catalogue Printful | Les six formes, en Printful | Non | Gratuit | 10 à 30 s | — | — |

- **Aucune API n'a de gabarit pour la boule 76 mm ni pour les six formes en bois.** Il faudrait fabriquer
  nos propres PSD : le travail difficile (photographier, caler la déformation) reste à notre charge.
- **Le coût vient de l'aperçu en direct.** À 0,05 $ par rendu, 20 modifications coûtent 1 $ sur une vue.
  Un tour de mug en 24 angles coûte 1,20 $ par état du design (estimé).
- Dynamic Mockups n'héberge les images rendues que 24 h.
- Printful : ses CGU réservent les mockups aux produits Printful. Inutilisable chez nous.

### 2. Printify : un produit « modèle » par support
- **Pas d'endpoint « générer un mockup ».** Les mockups sont le tableau `images` du produit, en lecture
  seule, par variante et par position.
- **Piste non testée : la ressource Personalization.** Elle génère des aperçus d'un produit personnalisé,
  mais exige un `product_id` (`personalization_previews.json`, déjà noté dans la RCH du 01/11).
- **Appels par mockup : 3 au minimum.** Upload de l'image, `PUT` du produit, puis lectures du produit
  jusqu'à ce que `images` soit rempli. Avec publication : 5 ou plus.
- **Délai : 45 à 60 s**, quel que soit le produit (un seul retour développeur, avril 2026).
  Le tableau `images` est vide juste après la création.
- **Limites :** 600 requêtes/min au total ; 100/min sur le catalogue ; 200 publications par 30 min ;
  une limite par jour, non chiffrée, sur la création de produits et de mockups, relevable par ticket support.
- **Angles du mug :** `front`, `back`, `left`, `right`, `context-1`, `context-2`. La vue `front` montre
  le côté de l'anse, souvent vierge.
- **Réutilisation publique des URL `images.printify.com` :** aucune clause trouvée.
- Les produits créés par l'API sans le Mockup Generator ne passent pas le contrôle qualité standard de
  Printify (CGU de l'API).
- **Conséquence :** un produit modèle mis à jour en boucle ne convient pas à l'aperçu en direct.
  Il sert une fois par support, imprimé de la mire, pour vérifier orientation et placement.

### 3. Rendu maison : principe commun
On commande un échantillon imprimé d'une mire codée (damier et marqueurs ArUco). On le photographie.
On calcule, pour chaque pixel de la photo, sa position dans le fichier d'impression : c'est la **carte UV**.
Le rendu devient une suite d'opérations fixes :
1. déformer le fichier d'impression par la carte UV (`cv2.remap`) ;
2. multiplier par un calque d'ombrage (photo de l'objet vierge divisée par une plaque blanche) ;
3. ajouter les reflets en mode « écran » (photo de l'échantillon imprimé en noir) ;
4. poser le tout sur la photo de fond (anse, ruban, ombre portée) avec le masque de la surface imprimable.

La carte UV est un fichier versionné, partagé entre le serveur et un éventuel rendu navigateur.
Briques utiles : gist cylindricalWarp (numpy et OpenCV), pages Cylinders de Snibgo (ImageMagick),
`cv2.findHomography`, `pixelmatch` et SSIM pour les tests.

### 4. Rendu maison : par produit
**Mug 11 oz (95 mm de haut, 80 mm de diamètre).**
- Prototype analytique possible : l'angle d'un pixel vaut l'arc sinus de sa distance au centre divisée
  par le rayon apparent. La mire corrige ensuite la forme réelle.
- Tour complet : le corps est de révolution. On décale la carte UV pour fabriquer les autres angles.
  Seule l'anse demande une photo de fond par angle.
- Montrer aussi le fichier d'impression à plat : c'est l'image exacte envoyée à Printify.

**Boule en verre 76,2 mm, dos blanc.**
- Projection sphérique théorique, puis correction par la mire photographiée.
- Deux calques distincts : ombrage diffus (faible, car le dos est blanc) et reflets nets du verre.
- Calotte métallique et ruban : couche photo intacte, posée au-dessus.

**Bois, six formes.**
- Surface plane : une homographie par forme et par angle suffit.
- Masque de découpe par forme, tiré de la photo de l'objet vierge.
- Grain : multiplier le visuel par une texture de grain normalisée. La fiche Printify dit que l'encre
  ne couvre pas tout le grain.
- Chant de 10 mm visible de trois quarts : couche photo, non imprimée.

### 5. Aperçu en direct et décision 08
| Critère | Rendu serveur renvoyé en image | Canvas ou WebGL avec la même déformation |
|---|---|---|
| Fidélité au fichier d'impression | Identique par construction | Risque d'écart : interpolation, gamma, alpha, polices |
| Latence | Aller-retour réseau et rendu ; attente de 300 à 500 ms après la dernière saisie | Instantané |
| Coût serveur | CPU seulement, avec cache | Nul |
| Décision 08 | Conforme | Conforme seulement si des tests prouvent l'égalité |

- **Ce que la décision 08 interdit en pratique :** composer le fichier d'impression en JavaScript
  (texte, polices, recadrage). C'est la source d'écart la plus probable, avant la déformation.
- **Position recommandée :** le serveur compose le fichier d'impression, puis en tire les mockups.
  Basse définition pendant l'édition, pleine définition à l'ajout au panier, même code.
- **Tour du mug :** le serveur rend 8 ou 24 vues en une seule image (sprite). Le navigateur les fait
  défiler sans rien calculer.
- **Si un canvas est ajouté plus tard :** il reçoit le fichier d'impression du serveur et ne fait que
  la déformation, avec les mêmes cartes. Un test en CI compare serveur et canvas sur 20 à 50 designs
  de référence.

### 6. Ce qu'il faut photographier à la réception des échantillons
**À commander chez les mêmes imprimeurs que la production, pour chaque support :**
- un exemplaire imprimé de la mire, qui couvre toute la zone imprimable, avec repères « haut » et « anse » ;
- un exemplaire en gris moyen 50 % (couleur et ombrage) ;
- un exemplaire en noir (reflets) ;
- un exemplaire vierge ou au motif minimal.

**Matériel figé pendant toute la session :** trépied ; focale longue (85 à 105 mm équivalent) ;
mode manuel, f/8 à f/11, ISO de base, mise au point et balance des blancs fixes ; RAW et JPEG ;
deux LED haut IRC à 5 000 à 5 600 K en softbox ; fond neutre sans couture ; carte grise ;
plateau tournant gradué pour le mug.

**Prises, sans bouger caméra ni lumière entre elles :**
1. le fond seul, à chaque angle ;
2. une plaque blanche à la place de l'objet ;
3. l'objet vierge ;
4. l'objet imprimé de la mire ;
5. l'objet en gris 50 % ;
6. l'objet en noir.

**Nombre d'images (estimé) :**
- mug : 24 angles × 5 états, soit 120 ; minimum 8 angles × 5, soit 40 ;
- boule : 4 vues × 5 états, soit 20 ;
- bois : 6 formes × 3 vues × 5 états, soit 90.

### 7. Recommandation par produit
| Produit | Option | Coût par mockup | Effort | Repli |
|---|---|---|---|---|
| Mug 11 oz | Rendu maison : face, sprite 24 vues, fichier à plat | Moins de 0,001 € (estimé) | Environ 2 semaines | SudoMock avec notre PSD, 0,05 $ par angle |
| Boule 76 mm | Rendu maison : mire, reflets, ruban en couche photo | Moins de 0,001 € (estimé) | 2 à 3 jours après l'outil d'étalonnage | Aucun gabarit d'API fidèle |
| Bois, 6 formes | Rendu maison : homographie, masque, grain | Moins de 0,001 € (estimé) | 2 à 4 jours | Aucun gabarit d'API ; Printful interdit |
| Printify | Un produit mire par support, une fois, pour vérifier | 0 €, 3 appels ou plus et 45 à 60 s | 0,5 jour | — |

## Chiffres
Sourcés :
- Dynamic Mockups : Pro 15 $/mois à l'année, 3 600 crédits/an, 0,051 $ par crédit en recharge,
  moins de 1 s, 4096 px, hébergement 24 h (source : dynamicmockups.com, lu le 02/11/2026).
- SudoMock : 0,05 $/rendu sans abonnement, Starter 25 $/mois, 0,002 $ au volume max, 10 000 px
  (source : sudomock.com/pricing, lu le 02/11/2026).
- Mediamodifier : 499 $/mois pour 5 000 rendus (source : mediamodifier.com, lu le 02/11/2026).
- Placeit : 14,95 $/mois, sans API (source : ecomm.design, lu le 02/11/2026).
- Bannerbear : 49 $/mois pour 1 000 crédits (source : 1capture.io, vérifié le 14/10/2026).
- Templated : 29 $/mois à l'année pour 1 000 (source : html2img.com et imejis.io, juillet-août 2026).
- Smartmockups fermé le 27/09/2024 (source : centre d'aide Canva, cité par SudoMock).
- Printify : 600 requêtes/min, 100/min sur le catalogue, 200 publications par 30 min, limite par jour
  non chiffrée (source : developers.printify.com, lu le 02/11/2026).
- Printify : mockups en 45 à 60 s (source : ultrathink.art, 22/04/2026).
- Mug 95 × 80 mm ; boule 76,2 mm ; bois 10 mm d'épaisseur
  (source : [[RCH - Contraintes d'impression Printify des trois produits (01-11-2026)]]).

Estimés :
- coût par mockup maison inférieur à 0,001 € (CPU) ;
- 1,20 $ par état du design pour un tour de mug en 24 vues par API ;
- nombre d'angles et d'images du protocole photo ;
- effort total : 21 à 34 jours, soit 3 à 5 semaines-développeur, réparti ainsi :
  photos 1 à 2 j ; outil d'étalonnage 4 à 6 j ; mug 3 à 5 j ; boule 2 à 3 j ; bois 2 à 4 j ;
  API de rendu et cache 4 à 6 j ; intégration au thème 3 à 5 j ; tests en CI 2 à 3 j.

## Caveats
- Les prix, délais et comparatifs viennent surtout des pages commerciales des éditeurs. Plusieurs
  comparatifs sont publiés par SudoMock, concurrent direct. Les latences sont annoncées, non mesurées.
- CGU de Dynamic Mockups : une clause limite l'usage à un usage personnel ou interne ⚠️ à vérifier.
- Réutilisation publique des mockups Printify : aucune clause trouvée ⚠️ à vérifier.
- Régénération des mockups Printify après un simple `PUT`, et son délai : non confirmées ⚠️ à vérifier.
- Ressource Personalization de Printify : aperçus possibles avec un produit modèle, non testés ⚠️ à vérifier.
- Pixels exacts des zones imprimables : à lire dans les `placeholders` de chaque variante ⚠️ à vérifier.
- Photoroom et Renderforest : non évalués.
- Les ⚠️ de cette note sont à reporter dans [[A VERIFIER - Points à valider, vérifier, tester]] à la revue.

Contradictions, sans trancher :
- SudoMock : 0,05 $ par rendu sur la page tarifs, 0,10 $ dans le README du SDK Python.
- Ornement bois à six formes : le rapport web ne l'a trouvé que chez Printful ; la RCH du 01/11 le
  relève chez Printify (blueprint 697, WOYC). Épaisseur : 9 mm chez Printful, 10 mm chez Printify.
- Boule : le rapport web n'a trouvé qu'un ornement cristal gravé (blueprint 2671) ; la RCH du 01/11
  relève le Glass Ornament Single (2769, Chill).

## Retenu / écarté
Revue du 02/11/2026 avec Antoine.

**Retenu**
- La cible : rendu maison côté serveur par carte UV calibrée sur des échantillons imprimés d'une mire,
  même code pour l'aperçu basse définition et le mockup final. Conforme à la décision 08 par
  construction. Prévu pour le système de mars 2027, pas pour Noël.
- Le protocole photo à la réception des échantillons (mire, gris 50 %, noir, vierge ; caméra et lumière
  figées), à exécuter dès la commande test du 05/11 : un exemplaire « mire » par support est ajouté à
  [[TODO - Planche de test des trois procédés pour la commande du 05-11]].
- Printify : un produit mire par support, une fois, pour vérifier le placement.
- Pour Noël 2026, provisoire : un mockup de face par rendu simple non calibré (déformation cylindrique
  analytique pour le mug, homographie pour le bois, disque pour la boule), ou photos des échantillons
  réels retouchées à la main. Inscrit dans la décision 14.

**Écarté**
- Les API de mockups (Dynamic Mockups, SudoMock, Mediamodifier) : aucun gabarit pour la boule ni le
  bois, coût par angle, hébergement 24 h.
- Printful Mockup Generator : CGU réservées à Printful.
- Un produit Printify mis à jour en boucle pour l'aperçu : 45 à 60 s par rendu, limites journalières.
- Un canvas qui compose le fichier d'impression : interdit par la décision 08. Un canvas qui ne fait que
  déformer reste possible plus tard, avec test d'égalité en CI.

**Conséquence**
- Ligne ajoutée dans [[14 - Brief visuel, deux gabarits de design déclinés par titre et par occasion, rendu peint aux formes franches]] (aperçu de Noël).
- Au registre A VERIFIER : CGU Dynamic Mockups (usage interne) ; réutilisation publique des URL
  Printify ; ressource Personalization de Printify.
