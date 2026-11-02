---
type: research
title: RCH - Publicités Meta et designs Monsieur TShirt et Etsy (02-11-2026)
status: validé
date: 2026-11-02
sources:
  - "Meta Ad Library, France, publicités actives : https://www.facebook.com/ads/library/ (lue le 02/11/2026)"
  - "Monsieur TShirt, mugs triés par meilleures ventes : https://www.monsieurtshirt.com/mugs?order_by=SALES&order_way=DESC"
  - "Etsy France, recherche « mug mamie prénoms », tri le plus pertinent : https://www.etsy.com/fr/search?q=mug%20mamie%20pr%C3%A9noms"
  - "30 fiches produit (15 Monsieur TShirt, 15 Etsy), relevées dans Chrome le 02/11/2026"
  - "Données : 2-marche/5-Niches/donnees/designs-concurrents.csv"
related: ["[[RCH - Designs des meilleures ventes de Cadeau Plus (01-11-2026)]]", "[[SYN - Choix de la niche]]", "[[RCH - Concurrents du mug famille à prénoms (29-10-2026)]]", "[[A VERIFIER - Points à valider, vérifier, tester]]"]
decisions: ["[[01 - Audience visée et nouvelle offre, parents et grands-parents d'abord, nos designs ou la page blanche]]"]
last-verified: 2026-11-02
tags: [dropshipping, niches, concurrence, designs, publicite, research]
---
# RCH - Publicités Meta et designs Monsieur TShirt et Etsy (02-11-2026)

## Contexte posé
Question d'Antoine, 02/11/2026 : suite du relevé des designs concurrents
([[RCH - Designs des meilleures ventes de Cadeau Plus (01-11-2026)]]).
1. Meta Ad Library, France, publicités actives, pour Cadeau Plus, Monsieur TShirt, Ourson Câlin,
   Henriette and Co, Cadeaux.com et CadoMaestro : nombre de publicités actives, gabarits visibles dans
   les 10 plus anciennes encore actives (une publicité qui dure est supposée rentable), date de début,
   produit, accroche. Remplir la colonne `pub` du CSV pour les designs déjà relevés.
2. Relever 15 mugs Monsieur TShirt (meilleures ventes) et 15 annonces Etsy FR (« mug mamie prénoms »)
   avec la grille existante. Chercher qui vend déjà « un symbole par prénom », et à quel prix.

Méthode : Chrome, lecture seule, cookies non essentiels refusés sur Etsy, aucun compte, aucun
téléchargement. Sur la Ad Library, le filtre de période sert à isoler les publicités actives les plus
anciennes, car la page n'offre pas de tri « plus anciennes ». Chez Cadeau Plus, le code produit commence
par un numéro de design (`1969` dans `1969m9g7a`) : la recherche `cadeauplus.com/<numéro>` retrouve un
design sur tous ses supports et toutes les pages de la marque.

## Conclusion en une phrase
Le gabarit « un symbole par prénom » est déjà vendu partout, de 12,90 € à 25,41 €, mais un seul vendeur
relevé laisse choisir un symbole différent pour chaque prénom (fleur de naissance ou couleur du cœur),
et chez Cadeau Plus un design rentable se reconnaît moins à l'âge de sa publicité qu'à son portage sur
de nouveaux supports.

## Résultats

### 1. Publicités actives par annonceur (Meta Ad Library, France)
| Annonceur | Actives | Plus ancienne active | Ce qui domine |
|---|---|---|---|
| Cadeau Plus (au moins 7 pages) | environ 1 600 | 20/08/2026 | ornements de Noël, mini-poupées photo, câlins de poche |
| Monsieur TShirt | 160 | 14/04/2026 | t-shirts à slogan, codes promo, devis entreprise |
| CadoMaestro | 25 | 24/03/2026 | catalogue de revendeur, peu de designs propres |
| Cadeaux.com | 21 | 20/05/2026 | prénoms d'enfants, collages photo |
| Henriette and Co | 12 | 26/10/2026 | objets de Noël au prénom de l'enfant |
| Ourson Câlin | 1 | 09/10/2026 | « Un prénom, mille câlins » |

### 2. Gabarits des publicités les plus anciennes
- **Cadeau Plus**, 10 plus anciennes toutes pages : plaque métal jardin (20/08), mug humour pour papa
  (21/08), short hawaïen (29/08), ornement rentrée (29/08), t-shirt jardinier (04/09), toile
  « La famille, l'amour » en mots croisés (11/09, ligne 18 du CSV), ornement voiture (11/09), lampe
  commémorative photo (15/09, ligne 14), ornement « Notre premier Noël ensemble » (17/09 et 19/09).
- **Monsieur TShirt** : slogans typographiques (« Tel père tel fils » depuis le 14/04, « Papa l'homme
  le mythe la légende » depuis le 17/06) ; le reste vend la marque (codes, avis, devis).
- **Cadeaux.com**, 5 publicités du 20/05 : t-shirt « MAMAN » avec l'année et les prénoms brodés sur la
  manche, vase gravé au prénom, disque d'or « Chacun son talent », cadre collage où le mot PAPA ou
  MAMAN couvre les photos.
- **Henriette and Co** : lutin farceur, hotte et étoile de sapin en velours, au prénom de l'enfant.
- **CadoMaestro** : bols « Humeur du matin » d'une autre marque, multi-outils, chaussettes.
- **Ourson Câlin** : une seule publicité en carrousel.

### 3. Les designs Cadeau Plus du CSV en publicité
8 des 30 designs ont au moins une publicité active (colonne `pub`). Cinq sont portés sur un support de
Noël plutôt que sur leur support d'origine : le cœur Maman Mamie (1969) en sac et ornement LED, les mots
croisés (3402) en ornement LED, « D'abord Maman, maintenant Mamie » (5040) en veilleuse, l'objet
commémoratif (6116) en boule de Noël, et le numéro 0065 en chaussette ⚠️ design non vérifié.

### 4. Monsieur TShirt, 15 meilleures ventes mugs
- Tous les mugs à 25,41 € (barré 29,90 €), 4 finitions (céramique, métal, anse cœur, magique).
- La 1re meilleure vente est l'éditeur page blanche, avec un bouton de création par IA.
- Gabarits : photo et texte 3, avatar seul 2, famille d'avatars 2, cœurs par prénom 1, animal par
  prénom 1, bande-a 1, visages et cœurs 1, rôles et années 1, portrait IA 1, texte et motif 1, page
  blanche 1.
- Le mug le plus noté est la famille cartoon sur un canapé (1 755 avis), loin devant les autres.

### 5. Etsy, 15 annonces « mug mamie prénoms »
- Prix de 8,94 € à 22,90 €, la plupart entre 13 € et 19 €.
- Gabarits : cœurs par prénom 5, fleurs par prénom 4, mains tenues 2, visage détouré 1, fleur de
  naissance seule 1, couronne de fleurs 1, tasse aux fleurs séchées 1.
- Deux boutiques reprennent des gabarits vus ailleurs : le mug « Mamie et ses petits cœurs » de
  Monsieur TShirt (AtelierPetiteChose, 14,90 €) et les mains tenues en faux 3D de Cadeau Plus
  (PortraitArtStudioFR, 22,90 €).

### 6. Qui vend « un symbole par prénom »
| Variante | Vendeur | Prix | Choix du symbole par prénom |
|---|---|---|---|
| un cœur identique par prénom | Monsieur TShirt (max 9) | 25,41 € | non |
| | Etsy AtelierPetiteChose, LovaPrint, CWADHESIF | 12,90 € à 14,90 € | non |
| un cœur coloré par prénom | Etsy MelleCreativeDesign | 19,60 € | oui, la couleur |
| un animal par prénom | Monsieur TShirt, Mamie poule (max 8) | 25,41 € | non |
| une fleur par prénom | Etsy MegaGraphicTees | 18,78 € | oui, fleur du mois de naissance |
| | Etsy CMAMARC, Jassimino, Mimilleet1creation | 15,00 € à 18,99 € | non confirmé ⚠️ |
| | Cadeau Plus, toile et vase (lignes 13 et 19) | 23,95 € à 24,95 € | oui sur la toile ; à vérifier sur le vase ⚠️ |
| une fleur de naissance seule | Etsy Demarkco | 10,11 € | oui, mais un seul prénom |

### 7. Cas qui ne rentrent pas dans la grille
- Pas de colonne pour le compteur de ventes Etsy : il est noté dans `rang` (ventes de la boutique,
  « dans N paniers », badge Best-seller ou Populaire).
- Le prénom vendu en option payante (MonCadeauPerso : 13,00 € sans, 15,00 € avec).
- L'éditeur page blanche n'a ni gabarit, ni registre, ni composition.
- La photo transformée en avatar ou en scène 3D par IA (Monsieur TShirt 12 et 14).
- Tasse en verre aux fleurs séchées et mug en grès gravé : faits main, hors de portée du POD.

### 8. Ce que le relevé suggère (non décidé)
- Le symbole par prénom ne différencie plus à lui seul. Le choix du symbole pour chaque prénom (fleur de
  naissance, couleur) est rare et se vend dans la même gamme de prix.
- Cadeau Plus renouvelle ses publicités en moins de trois mois. Un design rentable y apparaît plutôt
  quand il est porté sur un nouveau support pour la saison.
- Monsieur TShirt vend tous ses mugs au même prix et met en tête un éditeur libre : le prix ne
  distingue pas les designs chez lui.

## Chiffres

### Sourcés
- Publicités actives en France : Cadeau Plus environ 1 600 (recherche `cadeauplus.com`), Monsieur
  TShirt 160, CadoMaestro 25, Cadeaux.com 21, Henriette and Co 12, Ourson Câlin 1 (mesuré le 02/11).
- Cadeau Plus : 43 publicités actives diffusées avant le 30/09 ; aucune avant le 20/08 (mesuré le 02/11).
- Design commémoratif 6116 de Cadeau Plus : 11 publicités actives, la plus ancienne du 15/09 (mesuré le 02/11).
- Monsieur TShirt : 550 mugs au catalogue, tous à 25,41 € barré 29,90 € (mesuré le 02/11).
- Monsieur TShirt, avis : famille cartoon 1 755, Mamie poule 354, page blanche 247, famille figurine
  238, Mamie et ses petits cœurs 137 (mesuré le 02/11).
- Etsy, ventes des boutiques : MegaGraphicTees 75,2 k, CMAMARC 20 k, LovaPrint 10,9 k, MonCadeauPerso
  10,3 k, Demarkco 5,7 k, AtelierMiamor 3 k, AtelierPetiteChose 2,3 k, FestibabyCreation 2,1 k,
  AtelierIsaB 1,8 k, MelleCreativeDesign 737, CWADHESIF 593, Mimilleet1creation 336, Jassimino 183,
  PortraitArtStudioFR 78, balmau 0 (mesuré le 02/11).

### Estimés
- Aucun.

## Caveats
- Etsy n'offre pas de tri « meilleures ventes » : le relevé suit le tri par pertinence, et le compteur
  de ventes est celui de la boutique, pas de l'annonce.
- Le choix des 15 annonces Etsy privilégie les mugs non sponsorisés liés aux prénoms ; MegaGraphicTees
  est une annonce sponsorisée, Mimilleet1creation a été ouverte depuis sa boutique.
- Le nombre de publicités de Cadeau Plus vient d'une recherche par mot-clé : il peut inclure des
  annonces d'autres marques qui citent ce lien ⚠️ à vérifier.
- La colonne `pub` des lignes Monsieur TShirt reste « inconnu » : seule la page de la marque a été lue,
  pas chaque design.
- Ourson Câlin n'a qu'une publicité active : la passe ne dit rien de ses designs.
- Le numéro 0065 de Cadeau Plus (toile « Le jardin de Mamie ») revient en chaussette de Noël ; rien ne
  prouve que ce soit le même design ⚠️ à vérifier.
- Le CSV existant contient des « ; » dans des textes : ses 30 premières lignes comptent 35 à 38 colonnes
  au lieu de 34 ⚠️ à corriger. Les 30 nouvelles lignes n'en contiennent pas.
- Les URL des mockups des 30 nouveaux designs ne sont pas relevées.

## Retenu / écarté
Revue du 02/11/2026 avec Antoine.

**Retenu**
- « Un symbole par prénom » est un gabarit banal : vendu de 12,90 à 25,41 € par au moins huit
  vendeurs. Ce qui est rare, et vendu dans la même gamme : le choix du symbole pour chaque prénom
  (fleur de naissance, couleur). C'est la mécanique retenue pour notre gabarit ; elle tient dans la
  décision 13, un champ par prénom pouvant porter un choix de symbole.
- Chez Cadeau Plus, le signal d'un design rentable est son portage sur un nouveau support pour la
  saison, plus que l'âge de sa publicité. Critère à reprendre dans la veille.
- Monsieur TShirt met en tête un éditeur page blanche avec création par IA : confirme la décision 01
  et signale un concurrent sur la génération.
- Le CSV de 60 lignes comme base de la veille, après réparation des 30 premières lignes.

**Écarté**
- Le prix comme différenciateur : Monsieur TShirt vend tout au même prix, Etsy se tient entre 13 et 19 €.
- L'âge des publicités comme mesure de rentabilité chez Cadeau Plus (renouvellement en moins de
  trois mois).
- Les objets faits main (grès gravé, fleurs séchées) : hors POD.

**Conséquence**
- Précise [[14 - Brief visuel, deux gabarits de design déclinés par titre et par occasion, rendu peint aux formes franches]] :
  le gabarit devient « un symbole au choix par prénom », liste fermée de symboles par déclinaison.
- [[SYN - Choix de la niche]] à mettre à jour.
- Au registre A VERIFIER : réparer le CSV ; vérifier le design 0065 ; nombre de publicités Cadeau Plus
  gonflé par la recherche par mot-clé.
