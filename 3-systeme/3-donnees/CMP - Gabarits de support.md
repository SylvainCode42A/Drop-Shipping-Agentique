---
type: component
title: CMP - Gabarits de support
status: validé
related: ["[[CMP - Personnalisation par produit]]", "[[CMP - Brief de génération des illustrations de Noël 2026]]", "[[RCH - Contraintes d'impression Printify des trois produits (01-11-2026)]]", "[[RCH - Rendu des trois procédés d'impression et planche de test (02-11-2026)]]", "[[RCH - Rendu du texte, polices et OCR des accents (02-11-2026)]]", "[[A VERIFIER - Points à valider, vérifier, tester]]"]
decisions: ["[[02 - Lancement avec le mug, la boule en cristal et la décoration en bois, trois imprimeurs UE]]", "[[13 - Texte en trois champs facultatifs, couleur du texte en palette, police fixée, page blanche recadrée par la cliente]]", "[[14 - Brief visuel, deux gabarits de design déclinés par titre et par occasion, rendu peint aux formes franches]]", "[[15 - Catalogue de Noël 2026, six destinataires, fleurs de naissance et table de goûter, neuf produits]]"]
last-verified: 2026-11-02
tags: [dropshipping, systeme, rendu, gabarit, component]
---
# CMP - Gabarits de support

## Rôle
Où chaque élément se place sur chaque support, en millimètres : titre, symboles, prénoms, phrase, et
le recadrage de la scène. C'est la donnée que lit le module de rendu pour composer le fichier
d'impression et l'aperçu (décision 10), pour les deux gabarits de design de la décision 14
(A : un symbole au choix par prénom ; B : scène fixe à zone de texte). Les mêmes valeurs sont dans
`3-systeme/recherches/tests-images/production/gabarits.json`. Schémas du 02/11/2026 :
`3-systeme/recherches/planche-test/gabarits-support.png`.

## Intention
- **Un gabarit par support et par gabarit de design**, jamais une image redimensionnée d'un support à
  l'autre ([[SYN - Système]]).
- **Tout en millimètres** ; la conversion en pixels se fait à l'export, à partir des placeholders
  Printify ([[CMP - Personnalisation par produit]]).
- **Le nombre de prénoms N dicte la taille des symboles**, pas la cliente. Les symboles d'un même
  rendu ont tous la même taille, centrés dans leur zone, un prénom sous chacun.

## Règles communes
| Règle | Valeur |
|---|---|
| Marges de sécurité | mug : 10 mm latérales, 5 mm haut et bas ; boule : cercle utile de 66 mm ; bois : 5 mm dans le contour |
| Titre | capitale 8 mm sur le mug, 6 mm sur le bois, 5 mm en arc sur la boule ; police du gabarit (Caveat Brush pour A, Nunito pour B, décision 15 ⚠️ à confirmer à l'œil) |
| Prénoms | capitale 4 mm sur le mug, 3,5 mm sur le bois, 3 mm sur la boule ; réduction automatique jusqu'à 3 mm (3,5 sur bois) si le prénom dépasse sa case, puis tâche humaine ([[FLOW - Personnalisation à la commande]]) |
| Phrase | capitale 3 mm sur le mug, 2,5 mm ailleurs ; une ligne (deux sur le mug B) ; omise sur la boule si N > 3 et sur les formes basses si N > 4 |
| Couleur du texte | une des quatre couleurs de la palette du destinataire (décision 13) ; blanc jamais seul sur le mug ([[RCH - Rendu des trois procédés d'impression et planche de test (02-11-2026)]]) |
| Espace entre symboles | 2,5 mm sur le mug, 2 mm sur le bois, 2,5 mm sur la boule |
| Fichier | PNG sRGB 300 DPI à la taille exacte du placeholder ; fond blanc sur le mug, transparent (alpha 0) hors objet sur la boule et le bois ⚠️ selon l'échantillon |

## Mug, panneau 210 × 98 mm
Origine en haut à gauche du panneau. Zone sûre : x 10 à 200, y 5 à 93.

### Gabarit A
| Zone | x | y | largeur | hauteur |
|---|---|---|---|---|
| Titre | 20 | 8 | 170 | 14 |
| Rangée de symboles | centrée | 26 | selon N | taille du symbole |
| Prénoms | sous chaque symbole | symbole + 2 | taille du symbole | 7 |
| Phrase | 20 | 78 | 170 | 8 |

Taille du symbole selon N : 1 à 3 → 40 mm ; 4 → 36 ; 5 → 30 ; 6 → 26. La rangée est centrée sur x = 105.

### Gabarit B
| Zone | x | y | largeur | hauteur |
|---|---|---|---|---|
| Scène | 10 | 5 | 130 | 88 |
| Titre | 145 | 10 | 55 | 12 |
| Prénoms, colonne | 145 | 26 + 8 par prénom | 55 | 7 |
| Phrase | 145 | 78 | 55 | 10 |

Recadrage de la scène : la bande centrale du 4:3, rapport 130:88 (1,48), 90 % de la hauteur, centrée.
La colonne de texte est sur le mur droit de la scène, à droite de l'anse pour une droitière.

## Boule, disque de 76,2 mm
Origine au centre du disque. Cercle utile : rayon 33 mm.

### Gabarit A
| Zone | Position | Taille |
|---|---|---|
| Titre | arc supérieur, rayon 30 mm, de 200° à 340° | capitale 5 mm |
| Symboles, N ≤ 3 | une rangée centrée en y = 0 | 19 mm, espace 2,5 |
| Symboles, N = 4 à 6 | deux rangées de 3, centres en y = −10 et y + 12 | 16 mm, espace 2,5 |
| Prénoms | sous chaque symbole, +1 mm | capitale 3 mm |
| Phrase, N ≤ 3 seulement | arc inférieur, rayon 30 mm, de 30° à 150° | capitale 2,5 mm |

### Gabarit B
| Zone | Position | Taille |
|---|---|---|
| Scène | tout le disque, recadrage carré centré sur 60 % de la largeur de la scène (table à gauche, mur à droite) | pleine hauteur de la scène |
| Titre | x 10 à 33, y −26 à −16 | capitale 6 mm |
| Prénoms, colonne | x 10 à 33, y −13 + 6 par prénom | capitale 3 mm |
| Phrase | x 10 à 33, y 24 à 30 | capitale 2,5 mm |

## Décoration en bois, six formes
Origine en haut à gauche du fichier de la forme. Rectangles utiles estimés sur les dimensions de la
RCH Printify ⚠️ à confirmer sur le gabarit de découpe réel et sur l'échantillon.

| Forme | Fichier (mm) | Rectangle utile (x, y, l, h) | A : N max | A : disposition des symboles | B |
|---|---|---|---|---|---|
| Ovale | 85 × 125 | 5, 5, 75, 115 | 6 | 1 : 40 ; 2 : 2 × 28 en ligne ; 3 à 4 : 2 × 2 de 24 ; 5 à 6 : 3 rangées × 2 de 22 | oui |
| Chaussette | 86 × 162 | jambe : 42, 8, 36, 95 ; pied : 8, 108, 70, 46 | 6 | colonne de N × 22 dans la jambe (N ≤ 4), puis 2 colonnes de 16 ; phrase dans le pied | oui : scène dans le pied, titre et prénoms dans la jambe |
| Sapin | 92 × 132 | 24, 40, 44, 80 (élargi vers le bas) | 6 | 1 à 2 : 28 ; 3 à 4 : 2 × 2 de 20 ; 5 à 6 : 2 × 3 de 18 ; titre dans la pointe à 5 mm | oui : scène dans le tiers bas |
| Cloche | 86 × 105 | 15, 25, 56, 70 | 4 | 1 : 36 ; 2 : 2 × 26 ; 3 à 4 : 2 × 2 de 22 | non |
| Cœur | 87 × 115 | 13, 20, 60, 55 ; pointe : phrase | 4 | 1 : 40 ; 2 : 2 × 28 ; 3 à 4 : 2 × 2 de 24 | non |
| Étoile | 85 × 97 | 22, 30, 40, 40 | 4 | 1 : 30 ; 2 : 2 × 18 ; 3 à 4 : 2 × 2 de 16, prénoms 3 mm | non |

### Ovale, gabarit A
| Zone | x | y | largeur | hauteur |
|---|---|---|---|---|
| Titre | 22 | 12 | 41 | 10 |
| Grille de symboles | centrée sur x = 42,5 | 27 | selon N | selon N |
| Prénoms | sous chaque symbole, +0,5 | | taille du symbole | 4 |
| Phrase | 20 | 108 | 45 | 6 |

### Ovale, gabarit B
| Zone | x | y | largeur | hauteur |
|---|---|---|---|---|
| Titre | 25 | 8 | 35 | 8 |
| Prénoms, une ou deux lignes | 18 | 18 | 49 | 10 |
| Scène | 12 | 30 | 61 | 88 |

Recadrage de la scène : portrait, rapport 61:88 (0,69), pleine hauteur, centré sur 42 % de la largeur
(la table et la chaise). Phrase omise si N > 4. Les gabarits B de la chaussette et du sapin suivent le
même principe dans leur rectangle utile ; dessinés quand le gabarit de découpe sera confirmé.

## Entrées et sorties
- Entrées : support et forme, gabarit de design, N, les éléments de `production/valides/`, la scène
  recolorée du destinataire (base ou hiver), les champs de la cliente et sa couleur de texte.
- Sorties : le PNG d'impression à la taille du placeholder, et l'aperçu basse définition du même rendu.
- Données : `production/gabarits.json`, même contenu que cette note.

## Cas limites
- N > N max de la forme : la fiche produit n'offre pas ces champs (limite par forme, décision 13).
- Prénom qui dépasse après réduction au minimum : tâche humaine, jamais de coupure.
- Titre libre long (« Famille Dupont-Lefebvre ») : réduction jusqu'à 5 mm sur le mug, 4 mm ailleurs,
  puis tâche humaine.
- Phrase vide : la zone reste vide, rien ne remonte.
- Gabarit de découpe réel différent des rectangles estimés : les valeurs de ce tableau changent, le
  module lit `gabarits.json`, rien d'autre ne bouge.

## Notes liées
[[CMP - Personnalisation par produit]] · [[CMP - Brief de génération des illustrations de Noël 2026]] ·
[[FLOW - Personnalisation à la commande]] · [[RCH - Rendu du texte, polices et OCR des accents (02-11-2026)]]
