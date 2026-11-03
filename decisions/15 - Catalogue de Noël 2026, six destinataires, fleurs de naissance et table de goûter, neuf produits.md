---
type: decision
title: 15 - Catalogue de Noël 2026, six destinataires, fleurs de naissance et table de goûter, neuf produits
status: validé
date: 2026-11-02
implemented: non
related: ["[[OVR - Drop shipping agentique]]", "[[SYN - Choix de la niche]]", "[[SYN - Système]]", "[[CMP - Personnalisation par produit]]", "[[RCH - Designs des meilleures ventes de Cadeau Plus (01-11-2026)]]", "[[RCH - Publicités Meta et designs Monsieur TShirt et Etsy (02-11-2026)]]", "[[RCH - Capacités des modèles d'images pour les calques (02-11-2026)]]", "[[RCH - Rendu des trois procédés d'impression et planche de test (02-11-2026)]]", "[[MOD - Catalogue et fiche produit]]", "[[A VERIFIER - Points à valider, vérifier, tester]]"]
decisions: ["[[01 - Audience visée et nouvelle offre, parents et grands-parents d'abord, nos designs ou la page blanche]]", "[[02 - Lancement avec le mug, la boule en cristal et la décoration en bois, trois imprimeurs UE]]", "[[04 - Noël 2026 en test manuel réduit, Fête des grands-mères 2027 pour le système]]", "[[13 - Texte en trois champs facultatifs, couleur du texte en palette, police fixée, page blanche recadrée par la cliente]]", "[[14 - Brief visuel, deux gabarits de design déclinés par titre et par occasion, rendu peint aux formes franches]]"]
last-verified: 2026-11-02
tags: [dropshipping, boutique, niches, brief, decision]
---
# 15 - Catalogue de Noël 2026, six destinataires, fleurs de naissance et table de goûter, neuf produits

## Contexte
La décision 14 fixe deux gabarits de design (un symbole au choix par prénom, scène fixe à zone de
texte), un sujet non saisonnier décliné par titre et par occasion, et un rendu gouache aux formes
franches. Elle ne dit pas quels symboles, quelle scène, quels destinataires ni combien de produits.
Le menu de la boutique Shopify a huit catégories : Maman, Papa, Mamie, Papy, Couple, Famille, Noël,
Amies et fratrie. Il reste treize jours avant la mise en ligne de 8 à 12 produits (15/11).

Ce que les relevés disent ([[RCH - Designs des meilleures ventes de Cadeau Plus (01-11-2026)]],
[[RCH - Publicités Meta et designs Monsieur TShirt et Etsy (02-11-2026)]]) :
- Mamie représente 12 des 30 meilleures ventes de Cadeau Plus, le couple 5, puis papa et papy ;
  « famille » une fois ; « amies et fratrie » zéro fois sur 60 designs.
- Noël n'apparaît que dans 1 design sur 30 : le cadeau de Noël est un objet pour Mamie, pas un design
  de Noël. La saison se joue sur le support (ornement, boule) et sur la publicité.
- Le symbole identique par prénom (cœur, fleur, animal) est vendu par au moins huit concurrents de
  12,90 à 25,41 €. Le choix du symbole pour chaque prénom (fleur de naissance, couleur) est rare :
  deux vendeurs Etsy sur quinze, dont un à 75 000 ventes de boutique.
- Les titres sont le levier de déclinaison : jusqu'à 8 surnoms par rôle chez Cadeau Plus, et 16
  designs sur 30 déclinables par simple changement de titre.

## Décision

### 1. Six destinataires, avec leurs titres
Un destinataire est une déclinaison : même composition, titre et palette propres (décision 14).
Titres en liste fermée, plus une saisie libre (décision 13).

| Destinataire | Titres proposés |
|---|---|
| Mamie | Mamie, Mémé, Mamou, Mamina, Grand-mère, Nana, Mamita, Bonne-maman |
| Papy | Papy, Papi, Pépé, Papou, Grand-père, Papet, Papito, Bon-papa |
| Maman | Maman, Mam, Mamoune, Môman, Mère |
| Papa | Papa, Pap, Papounet, Pôpa, Père |
| Couple | Papy et Mamie, Pépé et Mémé, Papa et Maman, ou deux surnoms choisis séparément |
| Famille | Famille, Famille + nom saisi, Chez nous, Notre tribu |

*Précision du 02/11/2026* : le titre affiché est une phrase formée avec le surnom : « Le jardin de
Mamie », « Le sapin de Papou », « Le goûter chez Pépé et Mémé », « Le jardin de la famille Dupont ». La
cliente choisit le surnom, le gabarit fournit la phrase. Des **phrases proposées** par destinataire
(trois ou quatre, tendres et courtes, plus la saisie libre) sont à écrire dans la fiche produit, à
partir du registre relevé chez les concurrents.

**Noël** est une collection croisée, pas un destinataire : elle regroupe par tag les déclinaisons de
Noël (boule, bois, mug avec ornements), qui restent aussi dans leur catégorie de destinataire.
**Amies et fratrie** reste masquée pour Noël 2026 : aucun signal dans les relevés, public hors de la
décision 01, et une catégorie vide nuit plus qu'une absence. À ouvrir quand un gabarit existera.

### 2. Gabarit A : un symbole au choix par prénom
- **Base, toute l'année : les douze fleurs de naissance**, une par mois. Liste fixée et affichée sur la
  fiche : janvier œillet, février violette, mars jonquille, avril marguerite, mai muguet, juin rose,
  juillet pied-d'alouette, août glaïeul, septembre aster, octobre souci, novembre chrysanthème,
  décembre houx. La cliente choisit la fleur dans le champ de chaque prénom.
- *Production du 02/11/2026* : douze fleurs validées en gouache (journal `production.json`). Août est le
  **tournesol**, le glaïeul n'ayant pas passé en sept essais ; mars garde la jonquille, la tulipe reste
  en réserve. La liste affichée sur la fiche dit « août : tournesol ». Les six ornements, la scène de
  goûter en six palettes et son calque d'hiver sont validés le même jour ; les 18 éléments détourés
  sont dans `production/valides/` ([[RCH - Production des illustrations de Noël 2026, ce que les prompts ont appris (02-11-2026)]]).
- **Noël : six ornements** au choix de la même façon : boule, étoile, sapin, flocon, bonhomme de pain
  d'épice, cœur de Noël.
- Chaque symbole est un élément isolé, généré une fois en gouache, détouré, placé par le code selon le
  nombre de prénoms (1 à 6). Les fleurs et les ornements gardent leurs couleurs propres.
- *Précision du 02/11/2026, après comparaison des maquettes aux meilleures ventes* : les fleurs sont
  **plantées**, pas posées. Une bande de sol en gouache (herbe et terre, bouts arrondis), générée une
  fois et recomposée à toute largeur par le code (bout gauche, milieu répété, bout droit), passe sous
  les tiges ; à Noël, une branche de sapin horizontale remplace le sol et les ornements y pendent par
  une ficelle tracée par le code. Le gabarit s'appelle **« Le jardin de … »** en base et
  **« Le sapin de … »** à Noël, avec le surnom choisi. Le **mois** s'écrit en petit sous chaque prénom
  (« Léa · juin ») : c'est ce qui explique le cadeau, et qu'aucun concurrent ne fait. Sur le mug, le
  fond est le crème de la palette, pas le blanc. Le souci et le chrysanthème sont régénérés avec une
  tige courte. Raison : le n°1 du marché s'appelle « Jardin d'amour de Mamie » et montre un lien
  visible entre les éléments ; nos fleurs isolées sur blanc ne le montraient pas.
- Police pressentie : Caveat Brush ⚠️ à confirmer à l'œil sur le gabarit.

### 3. Gabarit B : scène fixe, la table de goûter
Une table de goûter sans personnage : nappe, théière, tasses, gâteau, quelques jouets au sol, la zone
de texte sur le mur du fond. Elle convient à tous les destinataires. Calque d'hiver pour la boule et
le bois : fenêtre enneigée, sapin dans l'angle. Police pressentie : Nunito ⚠️ à confirmer.
*Précision du 02/11/2026* : le titre est une phrase qui nomme le lieu, **« Le goûter chez … »**, sinon
la scène ne dit pas pourquoi elle est là (le plus proche sur le marché est « le garage de Papa »). Le
sol est prolongé par code sous la zone de texte. Gabarit non prouvé par le marché : si Noël ne le vend
pas, le jardin devient la seule base.

### 4. Six palettes
Le fond, les accents et les 4 couleurs de texte (décision 13) changent par destinataire ; couleurs
moyennes à soutenues, aucun pastel en fond ([[RCH - Rendu des trois procédés d'impression et planche de test (02-11-2026)]]).

| Destinataire | Dominante | Accents | Texte au choix |
|---|---|---|---|
| Mamie | crème chaud | corail, vert sauge, ocre | brun, corail, vert sauge, bleu nuit |
| Papy | bleu gris clair | ocre, vert bouteille, brique | bleu nuit, brique, vert bouteille, brun |
| Maman | rose poudré | prune, moutarde, vert | prune, brun, vert, bleu nuit |
| Papa | gris chaud | bleu roi, brun, moutarde | bleu nuit, brun, bleu roi, noir |
| Couple | ivoire | bordeaux, or vieilli, vert | bordeaux, brun, vert, bleu nuit |
| Famille | ivoire | vert, terracotta, ocre | vert, brun, terracotta, bleu nuit |

Les codes sRGB exacts sont fixés dans le brief de génération, à partir du nuancier de la planche de test.

### 5. Neuf produits Shopify
Par support, un produit par gabarit, le destinataire en variante (six), plus la page blanche :

| Support | Gabarit A | Gabarit B | Page blanche | Déclinaison portée |
|---|---|---|---|---|
| Mug | 1 produit × 6 | 1 produit × 6 | 1 produit | base (fleurs) ; ornements de Noël disponibles |
| Boule en verre | 1 × 6 | 1 × 6 | 1 | Noël (ornements, calque d'hiver) |
| Bois, six formes | 1 × 6 formes × 6 | 1 × 6 × 6 | 1 | Noël |

Neuf produits, dans la fourchette de 8 à 12 de la décision 04. Tag `noel` sur la boule, le bois et
le mug aux ornements, pour la collection Noël.

### 6. Ce qu'il y a à produire
- 18 éléments isolés (12 fleurs, 6 ornements), générés une fois.
- 1 scène de goûter en 6 palettes, plus 1 calque d'hiver : 7 générations.
- 6 fonds de symboles (un par palette) et 6 variantes de composition (1 à 6 prénoms) par le code.
- Environ 36 générations à valider à la main, une raison courte par refus, journal des prompts
  conservé ([[SYN - Juridique]]).
- Recomposition par support : panneau du mug, disque, six formes.

## Alternatives écartées
- **Cœurs colorés par prénom** : vendus par cinq boutiques Etsy à 13 €, concurrence par le prix.
  Gardés en réserve si les fleurs ne passent pas la validation (douze fleurs reconnaissables en gouache
  à 85 mm est plus dur que douze cœurs).
- **Animaux par prénom** (« Mamie poule ») : registre humour, déjà occupé par Monsieur TShirt.
- **Deux palettes** (chaude, froide) au lieu de six : moins de générations, mais un couple et une
  famille en palette « Mamie » ; six fonds restent faisables avant le 15/11.
- **Un design de Noël en base** : mort le 26 décembre, et le marché ne l'achète pas en meilleure vente.
- **Amies et fratrie dès Noël** : aucun signal, public hors cible.
- **Un produit par destinataire** (36 produits) : trop de fiches pour apprendre quoi que ce soit des ventes.

## Conséquences
- **Brief de génération** à écrire : un prompt par élément et par scène, le style commun de la décision 14,
  les codes de palette, les contraintes de rendu de la CMP. Note dans `3-systeme/3-donnees/`, lue par la
  conversation de production.
- **Gabarits** : positions des symboles pour 1 à 6 prénoms, zone de texte de la scène, par support.
- **Fiches Shopify** ([[MOD - Catalogue et fiche produit]]) : champ titre en liste plus saisie, un champ
  prénom avec sélecteur de symbole (fleur ou ornement), phrase, couleur en palette ; variante
  destinataire ; tag `noel`. La liste des fleurs de naissance affichée sur la fiche.
- **Catégorie Amies et fratrie** masquée dans le menu jusqu'à nouvel ordre.
- **Page blanche** : les trois produits restent prévus (décision 01), gabarit sans illustration.
- À inscrire dans A VERIFIER : lisibilité des douze fleurs à 85 mm après validation ; choix des polices à
  l'œil ; plafond de variantes Shopify sur le bois (36 par produit).
- Validée par Antoine le 02/11/2026.

## Concerne
[[14 - Brief visuel, deux gabarits de design déclinés par titre et par occasion, rendu peint aux formes franches]] ·
[[CMP - Personnalisation par produit]] · [[MOD - Catalogue et fiche produit]] · [[SYN - Choix de la niche]] · brief de génération à venir.
