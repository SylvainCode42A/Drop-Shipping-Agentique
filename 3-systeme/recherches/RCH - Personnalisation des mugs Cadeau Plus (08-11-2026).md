---
type: research
title: RCH - Personnalisation des mugs Cadeau Plus (08-11-2026)
status: validé
date: 2026-11-08
sources:
  - "Configurateur Customily des fiches Cadeau Plus, lu dans Chrome le 08/11/2026 (jeu d'options et gabarit de l'aperçu) : 3746M9I5A, 3943M5T0A, 3402M5E5A, 1969M9G7A, 2449M845O, 4322M8T7B, 13678M81WC, 17134M6BEI, 13185M6TTA"
  - "Mug Papasaurus : https://cadeauplus.com/products/effet-dimpression-3d-mug-personnalise-papasaurus-design-cartoon-4322m8t7b"
  - "Variantes Shopify des fiches (fichier .js du produit), lues le 08/11/2026"
  - "Aide Customily, Understand Functions in Option Sets : https://help.customily.com/hc/en-us/articles/39734732732059"
  - "Aide Customily, How to create an option set manually : https://help.customily.com/hc/en-us/articles/38942903765403"
  - "Aide Customily, How to Create an Option Set Automatically : https://help.customily.com/hc/en-us/articles/39182724178459"
  - "Aide Customily, Swatch Option : https://help.customily.com/articles/6716411794-swatch-option"
  - "Aide Customily, Image placeholder : https://help.customily.com/hc/en-us/articles/19530396621595"
  - "Aide Customily, AI filters for image placeholders : https://help.customily.com/hc/en-us/articles/42103759321627"
  - "Customily, annonce des Image Effects (15/10/2025) : https://customily.userjot.com/updates/p/new-image-effects-for-image-placeholders"
related: ["[[RCH - Designs des meilleures ventes de Cadeau Plus (01-11-2026)]]", "[[RCH - Audit des prix Cadeau Plus et coûts Printify (30-10-2026)]]", "[[A VERIFIER - Points à valider, vérifier, tester]]"]
decisions: []
last-verified: 2026-11-08
tags: [dropshipping, systeme, personnalisation, generation-images, concurrence, research]
---
# RCH - Personnalisation des mugs Cadeau Plus (08-11-2026)

## Contexte posé
Question d'Antoine, 08/11/2026 : quels moyens de personnalisation Cadeau Plus donne-t-il au client
sur ses mugs, comment chaque choix modifie l'image, et quelles parties de l'image ne bougent jamais.
Précision d'Antoine sur l'exemple du mug Papasaurus : voir toutes les manières simples d'éditer un mug
(nombre de dinosaures, nom, nombre d'enfants), et savoir si ce principe est documenté.
But : savoir ce que notre chaîne doit produire à l'avance et ce qu'elle doit calculer à la commande.

Méthode : lecture dans Chrome des données du configurateur, sans commande ni envoi de photo.
Pour chaque fiche, deux sources : le jeu d'options (ce que le client voit et à quel calque chaque
option est reliée) et le gabarit de l'aperçu (les calques image et texte, et leurs effets).
9 mugs lus : 5 meilleures ventes du relevé du 01/11 (lignes 01, 03, 05, 08, 09), le mug Papasaurus
et 3 mugs « photo IA ». Puis lecture de l'aide Customily.

## Conclusion en une phrase
Sur les mugs classiques, rien n'est généré à la commande : le client choisit dans des listes, des
vignettes et des champs de texte, et l'aperçu assemble des images dessinées d'avance selon un
principe documenté par Customily ; seuls les mugs « photo IA » génèrent une image, en passant la
photo du client dans gpt-image-1.5 avec un prompt fixe, puis en retirant le fond.

## Résultats

### 1. L'outil et son principe
- Le configurateur est Customily, une application Shopify de personnalisation.
- Un produit est un gabarit fait de calques : une image de fond fixe, des emplacements d'image et des
  champs de texte.
- Le client remplit un « jeu d'options ». Chaque option est reliée à un calque par une « fonction ».
- Fonctions observées : texte, image (choix dans une bibliothèque), couleur, bascule de gabarit
  (« product »), visibilité de calques (« layoutVisibility »), mots croisés (« crossword »), envoi de photo.
- Des conditions affichent une option seulement si une autre a une valeur donnée.

### 2. Exemple complet : le mug Papasaurus (4322M8T7B)
41 options, dont 5 visibles au départ. Parcours du client :

| Étape | Ce que le client fait | Effet dans l'image |
|---|---|---|
| 1. Version | « Pour Maman / Mamie » ou « Pour Papa / Papy » | Aucun effet direct ; affiche la bonne liste de titres |
| 2. Titre | Maman, Mamie, Papa, Papy… ou titre libre (15 caractères) | Titre en liste : lettrage dessiné ; titre libre : texte simple |
| 3. Grand dinosaure | 1 vignette parmi 5 | Calque du parent remplacé par une image de la bibliothèque |
| 4. Nom | Nom du parent (15 caractères) | Texte à position fixe |
| 5. Nombre d'enfants | De 1 à 15 | Bascule vers un autre gabarit complet, avec N places |
| 6. Chaque enfant | 1 dinosaure parmi 15 vignettes, puis un prénom | Un calque image et un calque texte par enfant |

Fixe : le décor, le cadrage, les polices, l'effet « faux 3D ». Des options cachées gèrent les titres
anglais (Daddy, Mummy, Grandma…).

### 3. Les moyens de personnalisation et leur effet sur l'image
| Choix du client | Effet dans l'image | Vu sur |
|---|---|---|
| Prénom | Calque texte à position, police et couleur fixes ; la taille s'ajuste ; 12 à 15 caractères | tous |
| Titre libre | Calque texte simple posé à plat ; 10 à 30 caractères | 01, 03, 05, 08, 4322 |
| Titre dans une liste (Mamie, Mémé, Papy…) | Image de lettrage dessinée d'avance (texture craie sur 08) ; plus travaillée que le titre libre | 03, 05, 08, 4322 |
| Version (pour maman ou pour papa) | Aucun effet direct ; change les listes proposées ensuite | 4322 |
| Phrase dans une liste fermée | Image dessinée d'avance, une par accord de genre et de nombre (4 à 18 phrases) | 09, 17134 |
| Nombre d'enfants, petits-enfants ou collègues | Bascule vers un autre gabarit complet, ou affichage d'autres calques | 01 (6), 05 (10), 08 (15), 09 (8), 4322 (15) |
| Personnage ou animal par personne | Vignette ; le calque est remplacé par une image de la bibliothèque | 4322 (5 parents, 15 enfants) |
| Avatar | Chaque partie est un calque image : peau, coiffure, yeux, sourcils, expression, haut | 08 |
| Couleur (tuiles, titre, texte) | Bascule de gabarit ou changement de couleur d'un texte, plus des images dessinées par couleur | 03, 05, 13678 |
| Mots croisés | Grille calculée par un algorithme de Customily à partir des prénoms | 03 |
| Photo (mug classique) | Détourage automatique du visage, posé dans un cadre fixe ; le client peut déplacer et redimensionner | 09 |
| Photo (mug IA) | Photo transformée par gpt-image-1.5 avec un prompt fixe, puis fond retiré | 13678, 17134, 13185 |
| Fond, décor ou police | Image de fond choisie dans une liste de 3 à 5, ou autre police | mugs IA |
| Tasse blanche ou bicolore, couleur de tasse | Variante Shopify, sans effet sur le design ; 18,45 € ou 21,45 € | 05, 17134 |

### 4. Les leviers d'édition simples
Le client n'utilise que cinq gestes :
- taper un texte (prénom, nom, titre libre) ;
- choisir dans une liste (titre, phrase, version) ;
- choisir une vignette (personnage, animal, partie d'avatar, fond, couleur) ;
- choisir un nombre, qui change tout le gabarit et fait apparaître autant de champs ;
- envoyer une photo, détourée ou transformée par IA.
Il ne dessine jamais et ne place rien à la main, sauf sa photo.

### 5. Ce que dit la documentation Customily
- Les fonctions relient chaque option au design ; une option sans fonction n'a aucun effet sur
  l'aperçu ni sur le fichier d'impression (Understand Functions).
- Une option peut porter plusieurs fonctions, quand un seul choix doit modifier plusieurs éléments
  (Understand Functions).
- La fonction « Change Product » fait passer l'aperçu sur un autre gabarit ; c'est le mécanisme du
  nombre d'enfants (Swatch Option).
- La logique conditionnelle permet des parcours adaptés au produit ; un jeu d'options peut servir à
  plusieurs produits (Create an option set manually).
- À la création d'un design, Customily génère le jeu d'options et relie les fonctions aux calques
  (Create an Option Set Automatically).
- Les effets IA s'appliquent automatiquement à l'envoi d'une photo ; OpenAI, Gemini et OpenRouter
  demandent la clé du marchand et sont payés à l'usage (AI filters for image placeholders).

### 6. Les options cachées
- Beaucoup d'options sont cachées au client. Elles choisissent l'image dessinée qui correspond à une
  combinaison : couleur × titre × langue (19 valeurs par couleur sur 03), couleur × nombre (05).
- Leurs libellés internes sont en vietnamien (« đen », « đỏ », « xanh », « chọn sẵn ») et des valeurs
  existent pour l'allemand et l'anglais : les mêmes designs servent plusieurs pays.
- Le mug 08 compte 610 options pour 15 enfants au plus.

### 7. Les mugs « photo IA »
- 3 fiches lues ; toutes au même prix que les autres mugs, 18,45 €.
- Le client ne tape aucun prompt : il envoie une photo, choisit un fond ou un décor, une couleur ou
  une police, et tape un prénom.
- Le prompt est fixe par produit, en anglais, d'environ 2 200 caractères. Il est découpé en blocs :
  style visé, fidélité des couleurs, sujet, cadrage, ambiance. Il exige de garder les couleurs, le
  nombre de sujets, la ressemblance et le cadrage de la photo, et interdit d'ajouter du texte ou des objets.
- Chaîne d'effets : gpt-image-1.5 en qualité moyenne, puis retrait du fond par Customily.

### 8. Ce qui ne bouge pas
- L'illustration principale : fleurs, mains, décor. Elle est dessinée une fois par nombre de personnes.
- La composition, les positions des textes, les polices et la palette de chaque gabarit.
- L'image de fond, sauf quand le client choisit parmi quelques fonds proposés.
- Sur les mugs IA : le style, imposé par le prompt.

### 9. Ce que le relevé suggère (non décidé)
- Le travail lourd est fait en amont : un graphiste dessine toutes les variantes (personnages,
  titres, un gabarit par nombre de personnes), puis le client les assemble. Notre chaîne pourrait
  générer ces bibliothèques à l'avance et laisser un outil du marché faire l'assemblage.
- Les titres en liste sont dessinés et les titres libres sont du texte simple : une liste courte de
  titres permet de soigner le lettrage là où il compte.
- La génération à la commande est réservée à la photo du client, avec un prompt fixe et un style fixe.

## Chiffres

### Sourcés
- Options par fiche : 01 : 8 ; 03 : 41 ; 05 : 81 ; 08 : 610 ; 09 : 19 ; 4322 : 41 ; mugs IA : 5 à 6 (mesuré le 08/11).
- Gabarits par nombre de personnes : 01 : 6 ; 05 : 10 ; 08 : 15 ; 09 : 8 ; 4322 : 15 (mesuré le 08/11).
- Mug Papasaurus : 5 grands dinosaures, 15 petits dinosaures, jusqu'à 15 enfants (mesuré le 08/11).
- Tasse bicolore : 21,45 € contre 18,45 € (mesuré le 08/11).
- Couleurs de tasse : 6 ou 7 selon la fiche (mesuré le 08/11).
- Mugs IA : modèle gpt-image-1.5, qualité moyenne, prompt d'environ 2 200 caractères (mesuré le 08/11).

### Estimés
- Aucun.

## Caveats
- 9 mugs lus sur un catalogue bien plus grand.
- La configuration lue est celle de l'aperçu ; le fichier d'impression n'est pas vu ⚠️ à vérifier.
- Aucune photo envoyée : le moment exact de l'appel à OpenAI vient de l'aide Customily, pas d'une
  observation ⚠️ à vérifier.
- Le coût d'une image gpt-image-1.5 en qualité moyenne n'est pas relevé ⚠️ à vérifier.
- Le prix de Customily n'est pas relevé ⚠️ à vérifier.
- Les options cachées sont interprétées par leur libellé et leurs conditions ; leur rôle exact n'est pas testé.

## Retenu / écarté

