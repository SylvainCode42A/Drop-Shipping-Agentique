---
type: decision
title: 14 - Brief visuel, deux gabarits de design déclinés par titre et par occasion, rendu peint aux formes franches
status: validé
date: 2026-11-01
implemented: non
related: ["[[OVR - Drop shipping agentique]]", "[[SYN - Choix de la niche]]", "[[SYN - Système]]", "[[RCH - Designs des meilleures ventes de Cadeau Plus (01-11-2026)]]", "[[RCH - Publicités Meta et designs Monsieur TShirt et Etsy (02-11-2026)]]", "[[RCH - Capacités des modèles d'images pour les calques (02-11-2026)]]", "[[RCH - Rendu des trois procédés d'impression et planche de test (02-11-2026)]]", "[[RCH - Contraintes d'impression Printify des trois produits (01-11-2026)]]", "[[RCH - Génération d'images pour l'impression (22-10-2026)]]", "[[CMP - Personnalisation par produit]]", "[[A VERIFIER - Points à valider, vérifier, tester]]"]
decisions: ["[[01 - Audience visée et nouvelle offre, parents et grands-parents d'abord, nos designs ou la page blanche]]", "[[02 - Lancement avec le mug, la boule en cristal et la décoration en bois, trois imprimeurs UE]]", "[[04 - Noël 2026 en test manuel réduit, Fête des grands-mères 2027 pour le système]]", "[[06 - LangGraph au départ, interface d'images interne avec Nano Banana Pro et Ideogram]]", "[[10 - Notre serveur produit l'image finale, Printify la reçoit par l'API]]", "[[13 - Texte en trois champs facultatifs, couleur du texte en palette, police fixée, page blanche recadrée par la cliente]]"]
last-verified: 2026-11-02
tags: [dropshipping, systeme, niches, brief, decision]
---
# 14 - Brief visuel, deux gabarits de design déclinés par titre et par occasion, rendu peint aux formes franches

## Contexte
Décision attendue par [[OVR - Drop shipping agentique]] (brief de la « famille illustrée »). Elle fixe
ce que le créateur, humain pour Noël 2026 puis agent, doit produire : la structure des designs, leur
sujet et leur rendu. Les choix de personnalisation sont dans la décision 13 et dans
[[CMP - Personnalisation par produit]].

Ce que le marché fait ([[RCH - Designs des meilleures ventes de Cadeau Plus (01-11-2026)]], 30
meilleures ventes, mesuré le 01/11/2026) : cinq gabarits font 20 ventes sur 30 ; 16 designs sur 30
se déclinent par changement de titre ; le texte est posé à plat sur 19 designs ; les rendus dominants
sont le peint (fleurs, mains tenues) et les aplats avec trait (« La bande à ») ; Noël n'apparaît que
dans 1 design sur 30 alors que la collection Noël compte 5 287 produits ; la mécanique « un symbole par
prénom » (une fleur par petit-enfant) existe et vend.

Ce que notre chaîne impose ([[10 - Notre serveur produit l'image finale, Printify la reçoit par l'API]],
[[13 - Texte en trois champs facultatifs, couleur du texte en palette, police fixée, page blanche recadrée par la cliente]]) :
illustration fixe en calques, texte posé à plat par le code après coup, même collection sur le mug,
la boule et six formes en bois.

Ce que les supports imposent ou laissent incertain ([[RCH - Contraintes d'impression Printify des trois produits (01-11-2026)]]) :
sur bois, l'encre posée à plat ne couvre pas tout le grain (fiche Printify) et le rendu des couleurs
claires est inconnu ⚠️ ; sur verre UV à dos blanc, le rendu des couleurs claires est inconnu ⚠️ ; le mug
est en sublimation. « Pas de traits fins sur bois » et « tout passe sur le mug » sont des déductions,
pas des faits relevés ⚠️.

## Décision

### 1. Deux gabarits de design, comparés à Noël 2026
Peu de gabarits, beaucoup de déclinaisons (décision 02, mise à jour du 01/11/2026). Pour Noël, un
gabarit de chaque famille, et les ventes départagent :
- **Un symbole par prénom** : un symbole par petit-enfant, le prénom sous chaque symbole, le titre
  au-dessus, la phrase en dessous. Une variante de composition par nombre de prénoms, de 1 à 6, donc
  six calques « symboles » par déclinaison. Éprouvé par le marché, texte plat.
  *Précision du 02/11/2026* ([[RCH - Publicités Meta et designs Monsieur TShirt et Etsy (02-11-2026)]]) :
  le symbole identique par prénom est vendu par au moins huit concurrents ; ce qui est rare, c'est le
  **choix du symbole pour chaque prénom**. Le gabarit devient donc « un symbole au choix par prénom » :
  une liste fermée de symboles par déclinaison (par exemple douze fleurs de naissance en base, six
  ornements à Noël), choisie par la cliente dans le champ de chaque prénom (décision 13). Le modèle
  produit la liste une fois ; le code place le symbole choisi.
- **Scène fixe à zone de texte** : une scène de vie familiale riche en couleur, une seule image par
  déclinaison, les prénoms en liste dans une zone réservée. C'est le vide repéré le 28/10 (scène fixe,
  avec aperçu, sur plusieurs supports). Moins de lien entre chaque prénom et le dessin.

### 2. Sujet non saisonnier, déclinaison par occasion
Le gabarit est pensé pour l'année ; la déclinaison porte l'occasion.
- Symbole par prénom : symbole de base non saisonnier (fleur, cœur, oiseau), et une déclinaison de
  Noël qui remplace le calque du symbole (boule, étoile) sans changer la composition. La boule en
  verre et la décoration en bois portent la déclinaison de Noël, le mug la version de base.
- Scène fixe : scène neutre (table, jardin, salon), déclinaison hivernale par un calque de décor
  (fenêtre enneigée, sapin dans un coin).
- Déclinaison par destinataire (maman, papa, mamie, papy, couple) par le titre et la palette, jamais
  par la composition.
Ce qui reste commun à toutes les déclinaisons d'un gabarit : la composition, les zones de texte, la
police, la palette de base.

### 3. Rendu : peint aux formes franches
Un seul rendu pour les deux gabarits, signature de la boutique : **gouache** (pigment opaque, pas de
lavis), contours fermés, couleurs moyennes à soutenues, aucun détail sous 1 mm à l'échelle de la
forme en bois (85 mm de large). C'est le peint du marché, contraint par le bois.
Ce rendu est **un pari prudent à confirmer sur l'échantillon** : les hypothèses sur le bois, le verre et
le mug sont inscrites au registre et testées sur la commande du 5 novembre.

### 4. Ce que le créateur produit, par gabarit et par déclinaison
- Les calques : fond, sujet (scène, ou les six variantes de symboles), décor saisonnier, et les
  zones de texte déclarées (titre, prénoms, phrase) avec police et palette ([[CMP - Personnalisation par produit]]).
- Une recomposition par gabarit de support : tour du mug, disque de la boule, chacune des six formes
  en bois ([[SYN - Système]], un visuel se recompose, il ne se redimensionne pas).
- Pour Noël 2026 : 2 gabarits × 5 destinataires au plus, soit 10 déclinaisons au plus, chacune en
  version de base et en version de Noël selon le support.

## Alternatives gardées en réserve
À reprendre si l'échantillon ou les ventes de Noël contredisent les choix ci-dessus.
| Option | Quand y revenir |
|---|---|
| **Rendu peint en aquarelle** (lavis, bords diffus) | si l'échantillon montre que les pastels et les bords doux passent bien sur bois et sur verre ; plus proche des mains tenues et des fleurs de Cadeau Plus |
| **Rendu aplats avec trait souple** (contours fermés, couleurs franches, sans matière peinte) | si le peint se dégrade sur bois ou sur verre ; lisible partout, mais proche de « La bande à » |
| **Un seul gabarit** au lieu de deux | si l'un des deux ne vend pas à Noël ; l'autre devient la base, et on ajoute un gabarit par trimestre |
| **Texte généré dans l'image** (prénoms rendus par le modèle, avec effet) | si le texte plat se vend moins que le texte intégré ; demande un appel par commande et l'OCR obligatoire (décision 13, alternative notée) |
| **Symbole de Noël en gabarit de base** sur la boule et le bois | si les ventes de Noël montrent que la cliente attend un objet de Noël et non un cadeau pour Mamie |

## Alternatives écartées
- **Mains tenues en faux relief 3D** : gabarit le plus vendu, mais le texte est intégré au relief, hors
  de notre chaîne ; copier le gabarit n°1 du concurrent n°1 est aussi un risque de parasitisme.
- **Personnages réglables (« La bande à », avatars)** : personnalisation visuelle par la cliente, que
  notre chaîne ne fait pas et que la 02 refuse (illustration fixe).
- **Mots croisés et jeux de lettres** : grille générée par un configurateur, texte intégré.
- **Un gabarit saisonnier** : mort le 26 décembre ; Noël est une occasion, pas un public (décision 01).
- **Dix illustrations différentes** (ancienne rédaction de la 02) : trop de compositions à tester, trop
  peu de ventes par design pour apprendre.
- **Un rendu par gabarit** : deux signatures pour une boutique ; la comparaison de Noël ne dirait plus
  si c'est le gabarit ou le rendu qui vend.

## Conséquences
- Antoine produit pour Noël 2026 les deux gabarits et leurs déclinaisons, avec l'interface d'images
  de la décision 06 ou à la main ; le journal des prompts et retouches sert de preuve d'apport humain
  ([[SYN - Juridique]]).
- Le fichier de la commande test du 5 novembre porte sur chaque support une pastille de pastels, un
  trait fin et un texte à 3 mm, pour trancher les hypothèses de rendu d'un coup.
- Le symbole par prénom demande au module de rendu de choisir le calque de symboles selon le nombre
  de prénoms saisis ; la scène fixe ne demande que la zone de texte.
- Shopify : une variante par déclinaison sur le mug et la boule ; 6 formes × déclinaisons sur le bois
  (décision 02).
- Les règles du créateur (`4-memoire-agents/regles/`) reprendront les sections 1 à 3 : à écrire en
  `propositions/` d'abord.
- À inscrire dans A VERIFIER : traits fins, pastels et texte à 3 mm sur bois, verre et mug (commande
  test) ; ventes comparées des deux gabarits à Noël.
- Aperçu de Noël 2026 (ajout du 02/11/2026, revue de
  [[RCH - Mockups réalistes par code des trois produits (02-11-2026)]]) : un mockup de face par rendu
  simple non calibré (cylindre analytique pour le mug, homographie pour le bois, disque pour la boule),
  ou photos des échantillons réels retouchées à la main. Le rendu calibré par mire est prévu pour le
  système de mars 2027 ; les échantillons de la commande test servent déjà à photographier la mire.
- Validée par Antoine le 01/11/2026 ; les options en réserve sont là pour adapter sans nouvelle décision.

## Concerne
[[02 - Lancement avec le mug, la boule en cristal et la décoration en bois, trois imprimeurs UE]] ·
[[13 - Texte en trois champs facultatifs, couleur du texte en palette, police fixée, page blanche recadrée par la cliente]] ·
[[CMP - Personnalisation par produit]] · [[SYN - Choix de la niche]] · [[SYN - Système]] · règles du créateur à venir.
