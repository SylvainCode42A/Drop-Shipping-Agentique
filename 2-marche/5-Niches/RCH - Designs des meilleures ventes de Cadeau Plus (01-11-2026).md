---
type: research
title: RCH - Designs des meilleures ventes de Cadeau Plus (01-11-2026)
status: draft
date: 2026-11-01
sources:
  - "Cadeau Plus, meilleures ventes : https://cadeauplus.com/collections/meilleures-ventes"
  - "Cadeau Plus, collections Maman, Papa, Mamie, Papy, Couple (tri meilleures ventes) : https://cadeauplus.com/collections/cadeau-personnalise-maman, …-papa, …-mamie, …-grand-pere, …-couple"
  - "Cadeau Plus, collections d'occasion : Noël, fêtes des mères, des pères, des grands-mères, des grands-pères, Saint-Valentin, anniversaire"
  - "30 fiches produit Cadeau Plus, relevées à la main dans Chrome le 01/11/2026"
  - "Données : 2-marche/5-Niches/donnees/designs-concurrents.csv"
related: ["[[SYN - Choix de la niche]]", "[[RCH - Audit des cibles adultes chez les concurrents (30-10-2026)]]", "[[RCH - Concurrents du mug famille à prénoms (29-10-2026)]]", "[[A VERIFIER - Points à valider, vérifier, tester]]"]
decisions: ["[[01 - Audience visée et nouvelle offre, parents et grands-parents d'abord, nos designs ou la page blanche]]"]
last-verified: 2026-11-01
tags: [dropshipping, niches, concurrence, designs, research]
---
# RCH - Designs des meilleures ventes de Cadeau Plus (01-11-2026)

## Contexte posé
Question d'Antoine, 01/11/2026 : construire la connaissance de « ce qui se vend » en cadeaux
personnalisés, pour écrire le brief des illustrations de NolaPrint. Phase 1 : annotation à la main
des designs des concurrents, en commençant par Cadeau Plus, concurrent direct n°1
([[RCH - Concurrents du mug famille à prénoms (29-10-2026)]]).

Méthode : relevé dans Chrome, une ligne par design, dans une grille fixe.
- Designs 1 à 10 : les 10 premiers mugs de la collection Meilleures ventes, dans l'ordre affiché.
- Designs 11 à 30 : les premiers produits des collections Maman, Papa, Mamie, Papy et Couple
  (tri meilleures ventes), tous supports, sans doublon avec les lignes déjà relevées.
- Occasion : relevée en cherchant chaque design dans les 7 collections d'occasion du site, pas devinée.
- Aucun CAPTCHA, aucune bannière cookies, aucun compte créé, aucun fichier téléchargé.

Données : `2-marche/5-Niches/donnees/designs-concurrents.csv`, séparateur point-virgule,
30 lignes plus l'en-tête.

## Conclusion en une phrase
Chez Cadeau Plus, cinq gabarits font 20 des 30 meilleures ventes relevées (mains tenues, la bande à,
fleurs à prénoms, mots croisés, lieu de papa), presque tout se personnalise par un titre et des
prénoms, et le texte est posé à plat dans 19 designs sur 30, donc la plupart des gabarits qui se
vendent sont à la portée de notre chaîne.

## Résultats

### 1. La grille de relevé (validée le 01/11/2026)
| Bloc | Champ | Valeurs |
|---|---|---|
| Identification | id, concurrent, url, support, date_releve, url_visuel, url_mockup | support : mug, boule, bois, autre ; url_visuel vide si rien n'est publié |
| Regroupement | gabarit | nom court qui regroupe les variantes (mains-tenues, bande-a…) |
| Cible | destinataire_principal | maman, papa, mamie, papy, couple, amie, fratrie, animal, travail, autre |
| | declinable_par_titre | oui, non : le même design se vend pour papa, papi, maman, mamie par simple changement de titre |
| | occasion | relevée depuis les collections d'occasion où le design apparaît |
| | titre, phrase, nb_variantes_phrase | texte libre ; titre et phrase séparés |
| | registre | tendre, humour, fierté, souvenir |
| Image | composition | texte seul, texte dominant, illustration dominante, équilibré |
| | rendu | une valeur dominante, une secondaire facultative : trait, aplats, peint, photo, typographique |
| | figuration | plusieurs valeurs : personnages stylisés, personnages réalistes, parties du corps, objets et symboles, décor, jeu graphique |
| | effet | aucun, faux relief 3D, texture, ombre portée |
| | texte_integre | oui, non : le texte fait partie de l'illustration (relief, courbure, texture partagée) ou il est posé à plat |
| | nb_couleurs, fond | monochrome, 2-3, multicolore ; blanc, coloré |
| | typographie | manuscrite, bâton, serif, mixte, fantaisie |
| Personnalisation | mecanique | cases : titre, prénoms, personnages réglables, photo, couleur |
| | nb_max_prenoms, apercu | nombre ou « non affiché » ; oui, non |
| Signal de vente | prix, rang, nb_avis, achats_24h, date_dernier_avis, pub | pub reste « inconnu » : passe séparée sur la Meta Ad Library, par concurrent |
| Notes | ce_qui_frappe, risque_pi | texte libre |

### 2. Gabarits
| Gabarit | Designs | Ce que c'est |
|---|---|---|
| mains-tenues | 6 | mains de l'adulte et des enfants, un prénom par main, fond floral en faux relief 3D ; version couple au trait seul |
| bande-a | 5 | « La bande à Mamie / Papy », avatars d'enfants réglables, prénom sous chaque enfant |
| fleurs-prenoms | 4 | une fleur peinte par prénom, prénom le long de la tige ; « Le jardin de Mamie », « D'abord Maman, maintenant Mamie » |
| mots-croises | 3 | prénoms en tuiles de jeu de lettres, grille générée par le configurateur |
| lieu-de-papa | 2 | « Le garage de Papa », plaque vintage, avatars |
| Un exemplaire chacun | 10 | cœur à prénoms, avatars amies, visages de collègues, photo commémorative, assiette de papa, câlin de poche, couple de Noël, pellicule photos, papillons à prénoms, phrase et cœurs |

### 3. Texte intégré ou posé à plat
| texte_integre | Designs | Lesquels |
|---|---|---|
| oui | 7 | les 5 mains tenues en faux 3D, 2 mots croisés |
| partiel | 4 | titre intégré et prénoms à plat (2 garages), ou l'inverse (2 toiles mots croisés) |
| non | 19 | fleurs, papillons, bande-a, couple, photo… |

### 4. Cible et personnalisation
- Destinataire principal : mamie 12, couple 5, papa 4, papy 4, maman 2, travail 1, amie 1, famille 1.
- 16 designs sur 30 sont déclinables par simple changement de titre.
- Registre : tendre 23, humour 6, souvenir 1.
- Mécanique : prénoms 28, titre 21, couleur 13, personnages réglables 9, photo 3.
- Occasion (un design peut en avoir plusieurs) : fête des grands-pères 9, fête des grands-mères 8,
  fête des mères 6, Saint-Valentin 4, fête des pères 3, Noël 1, anniversaire 1, aucune 5.
- Le titre est très travaillé : jusqu'à 8 surnoms proposés pour une grand-mère (Mamie, Mère, Môman,
  Mamou, Maminou, Nana, Maman, Mémé) plus un titre libre.

### 5. Cas qui ne rentrent pas dans la grille
- Mécanique : symbole choisi par prénom (une fleur par enfant), icône choisie, citation en liste
  fermée ou libre.
- Gabarit hybride : bande-a et mots-croises sur la même toile (ligne 29).
- Rendu 3D numérique, aspect pâte à modeler (ligne 26).
- Fond transparent (acrylique, cristal) ou matière (bois, métal) : 7 lignes.
- Effet de gravure laser dans le cristal (ligne 14).
- texte_integre partiel : 4 lignes ; texture enfermée dans les lettres du titre, à juger (ligne 20).
- Destinataire « famille » (ligne 18) et objet commémoratif pour un défunt (ligne 14, meilleure
  vente de la collection Papa).
- Famille représentée par des animaux (ligne 22, des oursons).
- Support : 16 lignes sur 30 valent « autre » (t-shirt, toile, plaque, vase), donc le champ distingue peu.
- Couple toujours composé d'un homme et d'une femme (lignes 24, 26, 30).

### 6. Ce que le relevé suggère (non décidé)
- Les gabarits fleurs-prenoms, papillons-prenoms et bande-a se vendent et ont le texte à plat :
  ce sont les plus proches de notre chaîne.
- Le faux relief 3D (mains tenues) est le gabarit le plus vendu sur les mugs, mais son texte est
  intégré au relief.
- Un même design se décline par titre et se vend sur plusieurs supports (mug, vase, toile, t-shirt) :
  peu de designs couvrent beaucoup de fiches.

## Chiffres

### Sourcés
- 30 designs relevés, 30 lignes dans le CSV (mesuré le 01/11).
- Prix : tous les mugs à 18,45 € (barré 30,95 €) ; les autres supports de 12,95 € à 38,95 € ;
  vente flash affichée du 1er au 15 novembre sur toutes les fiches (mesuré le 01/11).
- Avis par fiche : de 5 à 464 ; notes de 4,78 à 4,97 (mesuré le 01/11).
- Achats affichés sur 24 h : de 21 à 115 par fiche (mesuré le 01/11).
- Collections d'occasion lues : Noël 5 287 produits, fête des grands-pères 4 598, fête des mères
  3 409, Saint-Valentin 1 719, fête des pères 1 092, anniversaire 918, fête des grands-mères 903
  (mesuré le 01/11).
- Deuxième meilleure vente du site, tous produits : la toile « La famille, c'est l'amour » en mots
  croisés, 464 avis (mesuré le 01/11).

### Estimés
- Achats affichés sur 24 h, moyenne : 56 pour les designs à texte intégré, 68 pour les designs à
  texte posé à plat (calculé sur la colonne achats_24h ; compteur peu fiable, voir Caveats).

## Caveats
- Un seul concurrent relevé ; 30 designs seulement.
- L'ordre « meilleures ventes » est celui de Cadeau Plus ; sa règle de tri n'est pas connue.
- Le compteur « achats des dernières 24 heures » semble peu fiable : la ligne 30 affiche 61 achats
  avec 5 avis, dont le dernier date du 19/03/2026 ⚠️ à vérifier.
- Les réglages des personnages n'ont pas été ouverts sur 3 fiches (lignes 20, 21, 29) ; le choix
  d'une fleur par prénom n'est pas confirmé sur les lignes 12 et 19 ⚠️ à vérifier.
- La date du dernier avis est la plus récente de la première page d'avis ; un avis épinglé peut
  apparaître en tête.
- texte_integre est un jugement visuel sur le mockup, pas sur le fichier source.
- La publicité (pub) n'est pas relevée : passe Meta Ad Library à faire ⚠️ à vérifier.
- Les collections Maman et Mamie de Cadeau Plus se recoupent : les 5 premières meilleures ventes
  Maman sont des produits Mamie.

## Retenu / écarté

