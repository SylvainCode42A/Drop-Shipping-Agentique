---
type: decision
title: 13 - Texte en trois champs facultatifs, couleur du texte en palette, police fixée, page blanche recadrée par la cliente
status: validé
date: 2026-11-01
implemented: non
related: ["[[OVR - Drop shipping agentique]]", "[[SYN - Système]]", "[[SYN - Fournisseurs]]", "[[FLOW - Personnalisation à la commande]]", "[[FLOW - De la personnalisation à la commande]]", "[[RCH - Contraintes d'impression Printify des trois produits (01-11-2026)]]", "[[RCH - Designs des meilleures ventes de Cadeau Plus (01-11-2026)]]", "[[TODO - Personnalisation au choix sur toute la surface du mug, de la boule et de la déco en bois]]", "[[A VERIFIER - Points à valider, vérifier, tester]]"]
decisions: ["[[01 - Audience visée et nouvelle offre, parents et grands-parents d'abord, nos designs ou la page blanche]]", "[[02 - Lancement avec le mug, la boule en cristal et la décoration en bois, trois imprimeurs UE]]", "[[10 - Notre serveur produit l'image finale, Printify la reçoit par l'API]]", "[[11 - Texte facultatif à 1 €, frais de retour à la charge du client, retours chez Sylvain]]"]
last-verified: 2026-11-02
tags: [dropshipping, systeme, boutique, personnalisation, decision]
---
# 13 - Texte en trois champs facultatifs, couleur du texte en palette, police fixée, page blanche recadrée par la cliente

## Contexte
Les décisions 01, 02 et 10 fixent les deux modes de personnalisation (nos designs, page blanche),
les trois produits et la production du fichier par notre serveur. Quatre points restaient sans
réponse : la couleur du texte, la police, la forme du champ texte, et le traitement de l'image
envoyée par la cliente.

Ce que le marché fait ([[RCH - Designs des meilleures ventes de Cadeau Plus (01-11-2026)]], 30 meilleures
ventes, mesuré le 01/11/2026) : prénoms sur 28 designs, titre sur 21,
couleur au choix sur 13 ; texte posé à plat sur 19 designs, sans vente inférieure aux textes
intégrés (compteur d'achats non fiable, à lire avec prudence) ; mécanique « un symbole par
prénom » présente.

Ce que Printify permet ([[RCH - Contraintes d'impression Printify des trois produits (01-11-2026)]]) :
une image propre à chaque commande, pas de texte rendu par Printify, pas d'aperçu par l'API ;
mug sur tout le tour (95 × 80 mm), boule en rond de 76,2 mm à dos blanc, six formes en bois de
85 à 92 mm de large découpées au contour. Dimensions en pixels en attente du jeton API ⚠️.

## Décision

### 1. Texte en trois champs facultatifs
Sur les trois produits, dans les deux modes :
- **titre** (« Mamie », « Papa », liste proposée ou saisie libre) ;
- **prénoms**, de 0 à 6, un champ par prénom, 15 caractères au plus par prénom ;
- **phrase**, une ligne, libre.
Tous facultatifs. Dès qu'un champ est rempli, l'option texte s'applique, à +1 € (décision 11).
Le gabarit de chaque illustration et de chaque support fixe la position, la taille maximale et la
réduction automatique de chaque élément. Le nombre de lignes découle du gabarit, pas de la cliente.
La limite de 6 prénoms est à confirmer par support ⚠️ (bois et boule).

### 2. Couleur du texte en palette
La cliente choisit la couleur du texte dans une liste fermée de 4 à 6 couleurs, définie par le
gabarit de chaque illustration pour aller avec le dessin. La couleur ne s'applique qu'au texte,
jamais au fond ni à l'illustration.

### 3. Police fixée par le gabarit
Une police par illustration, choisie avec elle et testée sur é, è, ê, ë, ï, ç, œ et les prénoms
composés. La cliente ne choisit pas la police. Une liste de polices pourra s'ouvrir plus tard sans
changer la fiche produit.
*Précision du 02/11/2026* : quatre polices OFL couvrent tous les accents français et passent le contrôle
OCR (Caveat Brush, Kalam, Patrick Hand, Nunito) ; aucune police « gouache » n'existe sous licence POD
([[RCH - Rendu du texte, polices et OCR des accents (02-11-2026)]]).

### 4. Page blanche : formats, seuil et recadrage
- Formats acceptés : JPG, PNG, HEIC ; le HEIC est converti par le serveur.
- Seuil : 1 200 px sur le petit côté, refus en dessous avec un message clair ; avertissement
  entre 1 200 et 2 000 px.
- Recadrage par la cliente dans la forme choisie (tout, sapin, étoile, rond ; fond blanc autour,
  TODO du 31/10) : déplacer et zoomer seulement. Les coordonnées de recadrage sont envoyées avec
  la commande et appliquées par le serveur, qui produit le fichier final.
- L'image est contrôlée avant impression comme le prévoit la décision 01.

## Alternatives écartées
- **Un seul champ texte libre** (décision 10) : la cliente compose elle-même « Mamie Léa Hugo » ;
  le rendu ne distingue pas le titre des prénoms ; impossible de placer un symbole par prénom.
- **Prénoms obligatoires** (décision 08) : déjà écarté par la 11, le texte est une option.
- **Couleur du fond ou de l'illustration au choix** : change le dessin entier et casse l'idée
  d'illustration fixe ; multiplie les aperçus.
- **Police au choix dans une liste** : chaque police multiplie les tests d'accents, les gabarits de
  taille et les cas d'OCR ; une illustration a un style, la police en fait partie.
- **Recadrage automatique par le serveur** : coupe les visages ; la cliente est la seule à savoir
  ce qui compte dans sa photo.
- **Éditeur complet dans le navigateur** (rotation, filtres, texte libre positionné) : l'aperçu
  JavaScript ne reproduit pas le rendu serveur (décision 08) ; déplacer et zoomer suffit.

## Conséquences
- **Précise la décision 10** : le champ texte unique devient trois champs facultatifs ; les trois cas
  du tableau de la 10 restent valables.
- **Fiche produit Shopify** : champs titre, prénom 1 à 6, phrase, couleur (liste), et pour la page
  blanche : image, forme, coordonnées de recadrage. Tous en propriétés de ligne. Mettre à jour
  [[FLOW - De la personnalisation à la commande]] et [[MOD - Thème Shopify]].
- **Gabarit** : pour chaque illustration et chaque support, il déclare la police, la palette, la
  zone et la taille de chaque élément de texte, et la forme de découpe. Une note
  `CMP - Personnalisation par produit` dans `3-systeme/3-donnees/` décrit l'ensemble.
- **Module de rendu** : conversion HEIC, recadrage par coordonnées, rendu des trois éléments de
  texte, réduction automatique.
- **Brief visuel (décision 11 attendue)** : les trois champs permettent la mécanique « un symbole par
  prénom » comme la scène fixe ; le brief choisira.
- À inscrire dans A VERIFIER : limite de prénoms par support, palette lisible sur verre et sur bois,
  conversion HEIC, seuil de 1 200 px suffisant sur le tour complet du mug (environ 3 000 px
  attendus à 300 DPI, estimé).
- Validée par Antoine le 01/11/2026.

## Concerne
[[10 - Notre serveur produit l'image finale, Printify la reçoit par l'API]] · [[SYN - Système]] ·
[[FLOW - Personnalisation à la commande]] · [[FLOW - De la personnalisation à la commande]] ·
[[MOD - Thème Shopify]] · note CMP à venir.
