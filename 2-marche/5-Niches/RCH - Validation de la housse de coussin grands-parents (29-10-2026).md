---
type: research
title: RCH - Validation de la housse de coussin grands-parents (29-10-2026)
status: validé
date: 2026-10-29
related: ["[[RCH - Coussin grands-parents (28-10-2026)]]", "[[RCH - Relevé connecté du catalogue Printify UE (29-10-2026)]]", "[[RCH - Synthèse comparative des produits d'élargissement (29-10-2026)]]", "[[SYN - Fournisseurs]]", "[[NICHE - Grands-parents]]", "[[A VERIFIER - Points à valider, vérifier, tester]]"]
decisions: ["[[08 - Personnalisation à la commande en génération interne, test Printify avant le 5 novembre]]", "[[05 - Printify en principal avec partenaire UE figé, Gelato en second, franchise de TVA au départ]]"]
sources:
  - Catalogue Printify connecté (compte d'Antoine), API interne product-catalog-service et designer-api, éditeur 229/10, 29/10/2026
  - api.printful.com/products (catalogue public v1), 29/10/2026
  - ecb.europa.eu (taux de référence du 28/10/2026)
  - oursoncalin.com, monsieurtshirt.eu, cadeauplus.com, cherchons.com (Cadeaux.com), bettinakdo.fr, 29/10/2026
last-verified: 2026-10-29
tags: [dropshipping, niches, grands-parents, coussin, printify]
---
# RCH - Validation de la housse de coussin grands-parents (29-10-2026)

## Contexte posé
Il s'agit de valider la housse de coussin personnalisée grands-parents comme produit d'élargissement,
pour Noël 2026 ou pour la Fête des grands-mères du 07/03/2027. Le marché est déjà étudié dans
[[RCH - Coussin grands-parents (28-10-2026)]] et n'est pas refait ici.

Le contexte est le suivant. La boutique est sur Shopify, avec Printify en principal. Le mug est chez
OPT OnDemand ou Textildruck Europa. La housse vient d'un troisième imprimeur, MWW On Demand, donc il
n'y a pas de colis commun avec le mug. Les illustrations sont fixes et les prénoms sont rendus à la
commande ([[08 - Personnalisation à la commande en génération interne, test Printify avant le 5 novembre]]).
Rien n'est décidé ici.

## Conclusion en une phrase
La housse 229 de MWW part très probablement d'Allemagne et tient la marge à 29,90 € comme à 34,90 €,
mais son fichier d'impression est un panneau double à 150 DPI qui impose un gabarit propre, et le
concurrent le plus proche vend déjà la housse seule à 24,95 €.

## Résultats

### 1. Résumé
1. MWW (provider 10) déclare deux sites dans l'API, aux États-Unis et en Allemagne. Le port vers
   l'Allemagne est domestique, en 2 à 3 jours. La France est livrée en 5 à 8 jours ouvrés.
2. La housse 40 × 40 coûte 18,47 $ livrée en standard et 15,29 $ en Premium. La 45 × 45 coûte
   19,88 $ et 16,37 $.
3. Le fichier mesure 4650 × 2325 px pour 14 pouces. Il contient le recto et le verso côte à côte,
   à 150 DPI.
4. Le garni 220 coûte 32,10 $ livré en 40 × 40. Il est à perte à 29,90 € et proche de zéro à 34,90 €.
5. Cadeau Plus affiche la housse seule à 24,95 € et le garni à 33,95 €. Ourson Câlin vend un coussin
   garni à 22,90 €.

### 2. Relevé connecté Printify, MWW On Demand (mesuré le 29/10, en dollars, destination France)

| Produit | Taille | Variante (API interne) | Standard | Premium | Port FR, 1re puis suivante | Livraison |
|---|---|---|---|---|---|---|
| Housse 229 | 14" (35,6 cm) | 41629 | 11,71 | 8,75 | 5,89 puis 1,39 | 5 à 8 j ouvrés |
| Housse 229 | 16" (40,6 cm) | 41632 | 12,58 | 9,40 | 5,89 puis 1,39 | 5 à 8 j |
| Housse 229 | 18" (45,7 cm) | 41635 | 13,89 | 10,38 | 5,99 puis 1,39 | 5 à 8 j |
| Housse 229 | 20" | 41638 | 17,04 | 12,74 | 5,99 puis 1,39 | 5 à 8 j |
| Housse 229 | 24", 26", 28" | 252309, 252310, 252311 | 19,70 ; 22,25 ; 24,60 | 14,72 ; 16,63 ; 18,38 | 5,99 puis 1,39 | 5 à 8 j |
| Garni 220 | 14" | 41521 | 16,67 | 12,08 | 12,79 puis 5,69 | 5 à 8 j |
| Garni 220 | 16" | 41524 | 18,21 | 13,20 | 13,89 puis 5,69 | 5 à 8 j |
| Garni 220 | 18" | 41527 | 20,38 | 14,77 | 13,89 puis 5,69 | 5 à 8 j |
| Garni 220 | 20" à 28" | 41530, 244992 à 244994 | 24,43 à 44,37 | 17,71 à 32,17 | 14,59 puis 6,99 | 5 à 8 j |

Autres mesures du 29/10 :
- Production moyenne de 1,5 jour pour la housse et de 1,4 jour pour le garni. Note de MWW : 8,5.
  La date limite de Noël 2026 n'a pas été relevée. ⚠️ à vérifier
- Sites : l'API liste deux sites, n° 118 aux États-Unis et n° 275 en Allemagne. Le tarif vers
  l'Allemagne est de 5,89 $ en 2 à 3 jours, celui vers la France de 5,89 à 5,99 $ en 5 à 8 jours.
  L'origine allemande est donc probable mais pas prouvée. Dans ce cas, il n'y a ni droit de 3 € ni
  TVA à l'import. ⚠️ à vérifier par échantillon
- Les deux produits sont aussi proposés par « Printify Choice », situé aux États-Unis. Il faut
  choisir MWW explicitement.
- Zone d'impression : une seule position « front » en sublimation. Le 14" mesure 4650 × 2325 px à
  150 DPI, lu dans l'éditeur. Les dimensions de l'API en mm donnent 5250 × 2625 px pour le 16" et
  5850 × 2925 px pour le 18" (calcul). ⚠️ à relire dans l'éditeur
- Fond perdu : le panneau d'une face fait 15,5 pouces pour une housse de 14 pouces. Cela donne
  environ 1,9 cm par côté (calcul). L'éditeur affiche une ligne de sécurité en pointillés.
- Le format de fichier n'a pas été relevé pour ce produit. ⚠️ à vérifier
- Matière : 100 % polyester filé et fermeture à glissière beige à tête métal, cachée. Son
  emplacement n'est pas indiqué. ⚠️ à vérifier. La taille peut varier de plus ou moins 0,5 pouce.
- La housse 229 est livrée sans coussin.
- Le garni 220 a une garniture en polyester recyclé, plus grande de 2 à 3 pouces que la housse.
  Il est expédié non assemblé, garniture sous vide.
- Lavage de la housse 229 : 40 °C maximum, sans sèche-linge.
- Lavage du garni 220 : 40 °C maximum, sèche-linge basse température.
- L'étiquette de composition n'est pas indiquée. ⚠️ à vérifier

### 3. Housse Printful Lettonie, en comparaison (catalogue public, 29/10)

| Produit | 16" | 18" | Disponibilité UE | Fichiers |
|---|---|---|---|---|
| Premium Pillow Case 215 (polyester effet lin 275 g/m²) | 14,95 $ | 18,25 $ | EU et EU_LV en stock | recto et verso séparés |
| Basic Pillow Case 89 | 12,75 $ | 15,75 $ | EU et EU_LV en stock | recto et verso séparés |
| Cotton Pillow Case 1583 (nouveau) | 16,63 $ | 18,67 $ | aucune ligne UE | recto et verso séparés |

Ces prix sont en dollars, hors TVA et hors port. Le prix en euros, le port vers la France et les
pixels exigent un compte Printful. Ils n'ont pas été relevés. ⚠️ à vérifier. La RCH du 28/10 donnait
17,11 € TTC pour la Premium, sur un devis Pays-Bas dont la taille n'était pas précisée.

### 4. Marché, relevé le 29/10/2026

| Acteur | Produit | Prix TTC | Housse seule ou garni | Format, matière | Délai, port |
|---|---|---|---|---|---|
| Ourson Câlin | « Mamie et ses petits enfants » | 22,90 € | garni (« housse et son intérieur ») | 38 × 38, coton ivoire, garniture polyester, 30 °C | 3 à 4 j ouvrés, port offert dès 60 € |
| Ourson Câlin | « Family Portrait » (deux versions, dont une en coton) | 24,90 € | non vérifié | — | — |
| Monsieur TShirt | « Mamie et ses petits cœurs » | 37,90 € | non précisé (doublure polyester) | 40 × 40, coton bio, Bordeaux | J+1 en Europe, −40 % sur le 2e article et −70 % sur le 3e le jour du relevé |
| Cadeau Plus | « Le Jardin de Mamie » | 24,95 € la housse ; 33,95 € avec garniture | les deux, option au choix | 40 × 40 | 2 à 3 j de production puis 5 à 8 j de livraison, port offert dès 70 € |
| Cadeaux.com | « Mamie et ses petits cœurs » (cœur) | 29,95 € + 6,92 € de port | non précisé | coussin cœur | vu sur cherchons.com, site non lu |
| Bettina Kdo | « Coussin avec photos Mamie » | 20,00 € | non dit, « déhoussable » | 40 × 40, polyester, sublimation | retrait sur place ou livraison |

Dates limites de Noël 2026 : aucune n'est affichée par ces cinq acteurs à la date du relevé.
Cadeau Plus annonce qu'elles seront publiées sur son site.

Comment ils annoncent la housse seule :
- Cadeau Plus est le seul à séparer deux options nommées, « Housse de Coussin » et « Rembourrage
  Inclus ». L'écart est de 9 €.
- Ourson Câlin écrit « Housse de coussin et son intérieur ».
- Les trois autres ne précisent rien.

### 5. Coût livré et marges (estimé)
Hypothèses :
- Taux BCE du 28/10/2026, le dernier publié au moment du relevé : 1 € = 1,1133 $, soit 0,8982 €
  pour un dollar.
- TVA facturée par Printify : 20 %. ⚠️ taux réel à vérifier. Elle n'est pas déductible en franchise
  et elle est déductible avec TVA collectée.
- Port offert à la cliente.
- Commission de 0,70 € à 29,90 € et de 0,77 € à 34,90 €.
- Abonnement Premium (39 $ par mois) non réparti sur les ventes.

| Produit | Coût HT | Coût TTC | Franchise 29,90 € | Franchise 34,90 € | TVA collectée 29,90 € | TVA collectée 34,90 € |
|---|---|---|---|---|---|---|
| Housse 40 × 40, standard | 16,59 € | 19,91 € | 9,3 € | 14,2 € | 7,6 € | 11,7 € |
| Housse 40 × 40, Premium | 13,73 € | 16,48 € | 12,7 € | 17,7 € | 10,5 € | 14,6 € |
| Housse 45 × 45, standard | 17,86 € | 21,43 € | 7,8 € | 12,7 € | 6,4 € | 10,5 € |
| Housse 45 × 45, Premium | 14,70 € | 17,64 € | 11,6 € | 16,5 € | 9,5 € | 13,6 € |
| Garni 40 × 40, standard | 28,83 € | 34,60 € | −5,4 € | −0,5 € | −5,6 € | −0,5 € |
| Garni 40 × 40, Premium | 24,33 € | 29,20 € | 0,0 € | 4,9 € | −0,9 € | 4,0 € |
| Garni 45 × 45, standard | 30,78 € | 36,94 € | −7,7 € | −2,8 € | −7,6 € | −2,5 € |
| Garni 45 × 45, Premium | 25,74 € | 30,89 € | −1,7 € | 3,2 € | −1,4 € | 2,6 € |

Lecture :
- Premium fait gagner environ 3,4 € TTC par housse 40 × 40 en franchise. L'abonnement (environ
  35 €) devient rentable vers 10 housses par mois, tous produits Printify confondus (estimé).
- Le garni coûte plus cher surtout à cause du port, qui passe de 5,89 à 13,89 $.

### 6. Contraintes de composition pour le créateur
- Le fichier est un panneau double. Une face fait 2325 × 2325 px en 14", 2625 px en 16" et 2925 px
  en 18". Les deux faces sont posées côte à côte.
- Le verso uni correspond donc à la moitié du fichier, peinte d'une couleur pleine. ⚠️ Le côté
  gauche ou droit du recto est à confirmer dans l'éditeur.
- Le fond perdu est d'environ 1,9 cm par côté (calcul). Les prénoms et les visages restent à 3 cm
  du bord fini, soit environ 5 cm du bord du fichier (estimé).
- Le garnissage est plus grand que la housse, donc le tissu se tend et les coins s'arrondissent.
  Rien d'important ne va dans les coins (RCH du 28/10).
- Lisibilité à 2 mètres : une hauteur de capitale de 10 mm ou plus, soit environ 60 px à 150 DPI
  (calcul).
- Les gabarits restent 1-2, 3-4, 5-6 et 7-8 prénoms, comme dans la décision 08.
- Le visuel du mug se recompose en carré. On ne l'étire pas.

### 7. Implications pour le rendu des prénoms (décision 08)
- La décision 08 prévoit un PNG à 300 DPI. Ici, la zone est définie à 150 DPI. Un fichier à 300 DPI
  fait 9300 × 4650 px en 14" et 11 700 × 5850 px en 18". ⚠️ L'acceptation de ce fichier est à vérifier.
- L'appel API porte une seule image dans `print_areas.front`, qui couvre les deux faces.
- Printful demande au contraire deux fichiers séparés, recto et verso. Si le repli Printful de la
  décision 08 s'applique, l'export change.
- La commande externe de test du 05/11 peut porter une housse 229 en 16" plutôt qu'un mug. Ce serait
  un fait à tester, pas une décision.

### 8. Risques
- **Housse seule mal comprise.** Un avis Cadeau Plus dit « il manque le rembourrage » (RCH du 28/10).
  Seul Cadeau Plus nomme l'option clairement.
- **Étiquetage textile, règlement UE 1007/2011.** La composition « 100 % polyester » doit être en
  français. Rien n'indique que la housse MWW porte une étiquette, ni en quelle langue.
- **GPSR, règlement 2023/988.** Il faut une personne responsable dans l'UE. MWW a un site en
  Allemagne, mais son adresse et son rôle de fabricant UE ne sont pas documentés.
- **Inflammabilité.** Aucune exigence française spécifique n'a été trouvée pour un coussin décoratif
  (RCH du 28/10). Le Royaume-Uni en a une, hors périmètre.
- **Lavage.** Les consignes de la housse 229 et du garni 220 se contredisent sur le sèche-linge.
- **Prix de marché.** À 29,90 €, la housse seule est 5 € au-dessus de celle de Cadeau Plus et 7 €
  au-dessus du garni d'Ourson Câlin.

### 9. Faisabilité au 15/11 contre report à mars 2027
- Pour le 15/11, il faut quatre choses : l'échantillon reçu, le gabarit en panneau double, le test
  de la décision 08, et la fiche Shopify qui annonce la housse seule.
- Délai de l'échantillon : 1,5 jour de production et 5 à 8 jours ouvrés de livraison. Une commande
  passée le 30/10 arriverait entre le 6 et le 11/11 (estimé).
- Pour mars 2027 : la Fête des grands-mères tombe le 07/03/2027. Le report laisse le temps de
  comparer avec Printful (fichiers séparés) et de construire l'aperçu côté serveur prévu après Noël.

### 10. Échantillon à commander (fait, pas décision)
Housse 229, 16", MWW On Demand, destination France. Coût estimé : 18,47 $ HT, soit environ 19,90 € TTC.

Le fichier doit être rendu par le système :
- 8 prénoms avec accents ;
- une illustration de test ;
- un verso uni.

À observer à la réception :
- pays d'expédition sur le colis ;
- étiquette de composition et sa langue ;
- emplacement de la fermeture ;
- rendu des petits textes ;
- tenue des bords.

### 11. Questions ouvertes
- La housse part-elle réellement d'Allemagne ? La TVA facturée est-elle allemande ou française ?
- Le recto est-il la moitié gauche ou droite du panneau ? Un fichier à 300 DPI est-il accepté ?
- Où est la fermeture, et la housse porte-t-elle une étiquette de composition en français ?
- Quelle est la date limite de Noël 2026 de MWW pour la France ?
- Faut-il annoncer la housse seule à 29,90 €, face à 24,95 € chez Cadeau Plus ? À trancher en
  décision, pas ici.

## Chiffres

### Sourcés
| Chiffre | Source | Date |
|---|---|---|
| Prix, ports, délais et variantes de la housse 229 et du garni 220 (§2) | catalogue Printify connecté, API interne | mesuré le 29/10 |
| Panneau de 4650 × 2325 px à 150 DPI (14") | éditeur Printify 229/10 | mesuré le 29/10 |
| Sites MWW aux États-Unis (118) et en Allemagne (275), port Allemagne de 2 à 3 j | API interne Printify | mesuré le 29/10 |
| Printful 215 : 14,95 $ et 18,25 $ ; 89 : 12,75 $ et 15,75 $ | api.printful.com/products | mesuré le 29/10 |
| 1 € = 1,1133 $ | BCE (ecb.europa.eu) | 28/10/2026 |
| Ourson Câlin 22,90 €, garni, 38 × 38 | oursoncalin.com | 29/10/2026 |
| Monsieur TShirt 37,90 €, 40 × 40 coton bio, Bordeaux | monsieurtshirt.eu | 29/10/2026 |
| Cadeau Plus 24,95 € housse, 33,95 € garni ; délais coussin 2-3 j + 5-8 j | cadeauplus.com | 29/10/2026 |
| Cadeaux.com 29,95 € + 6,92 € de port | cherchons.com | 29/10/2026 |
| Bettina Kdo 20,00 €, 40 × 40 polyester | bettinakdo.fr | 29/10/2026 |

### Estimés
- Les zones de 16" et 18" en pixels, et le fond perdu de 1,9 cm, viennent d'un calcul sur les
  dimensions de l'API.
- Les coûts en euros et les marges du §5 sont estimés. La TVA à 20 % est une hypothèse.
- Le seuil Premium vers 10 housses par mois est estimé.
- La marge de 5 cm depuis le bord du fichier et la hauteur de 60 px sont estimées.
- La date de réception de l'échantillon est estimée.

## Caveats
- Le taux BCE du 29/10 n'était pas encore publié au moment du relevé.
- Les identifiants viennent de l'API interne, pas de l'API publique.
- Le port Printful vers la France n'a pas été relevé.
- Le site de Cadeaux.com n'a pas été lu directement, seulement un comparateur.
- Le coussin Bettina Kdo « la plus chouette des mamies » de la RCH du 28/10 n'apparaît plus dans la
  liste du site.

Contradictions non tranchées :
- Cadeau Plus : la RCH du 28/10 indiquait un même prix pour la housse et le garni. Le 29/10, on
  relève 24,95 € et 33,95 €.
- MWW est décrit comme « Made-in-USA » dans sa fiche, mais l'API déclare un site en Allemagne.
- Le sèche-linge est interdit pour la housse 229 et autorisé à basse température pour le garni 220.
- Le port de la housse 14" et 16" est de 5,89 $ le 29/10, contre 5,99 $ dans le relevé du matin.
- La décision 08 prévoit 300 DPI, alors que la zone Printify est définie à 150 DPI.

## Retenu / écarté
(à remplir à la revue)
