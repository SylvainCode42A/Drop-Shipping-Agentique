---
type: decision
title: 09 - Noël 2026 avec le mug et l'affiche chez OPT OnDemand, housse et décoration reportées
status: validé
date: 2026-10-29
implemented: non
related: ["[[OVR - Drop shipping agentique]]", "[[SYN - Choix de la niche]]", "[[SYN - Fournisseurs]]", "[[SYN - Système]]", "[[RCH - Synthèse comparative des produits d'élargissement (29-10-2026)]]", "[[RCH - Validation de l'affiche grands-parents en produit compagnon du mug (29-10-2026)]]", "[[RCH - Validation du tote bag compagnon du mug (29-10-2026)]]", "[[RCH - Validation de la housse de coussin grands-parents (29-10-2026)]]", "[[RCH - Décoration de sapin personnalisée grands-parents (29-10-2026)]]", "[[RCH - Relevé connecté du catalogue Printify UE (29-10-2026)]]", "[[A VERIFIER - Points à valider, vérifier, tester]]"]
decisions: ["[[02 - Mug famille illustrée à 24,90 €, duo à 44,90 €, panier cible 45 €]]", "[[04 - Noël 2026 en test manuel réduit, Fête des grands-mères 2027 pour le système]]", "[[05 - Printify en principal avec partenaire UE figé, Gelato en second, franchise de TVA au départ]]", "[[08 - Personnalisation à la commande en génération interne, test Printify avant le 5 novembre]]"]
last-verified: 2026-10-29
tags: [dropshipping, niches, fournisseurs, decision, noel]
---
# 09 - Noël 2026 avec le mug et l'affiche chez OPT OnDemand, housse et décoration reportées

## Contexte
Neuvième décision attendue par [[OVR - Drop shipping agentique]] : les produits d'élargissement
après le mug, et leur ordre. Seize produits ont été étudiés les 28 et 29/10/2026, puis le catalogue
Printify a été relevé en connecté, puis trois candidats ont reçu une étude de validation avec prix
mesurés ([[RCH - Synthèse comparative des produits d'élargissement (29-10-2026)]]).

Ce que les chiffres disent, en franchise de TVA, port offert, prix Printify du 29/10 convertis à
0,897 € :
- l'affiche A4 ou A3 chez OPT OnDemand (Tchéquie, 6,50 et 7,09 $, port 6,09 $) laisse 12 à 14 €
  à 24,90 €, avec le même imprimeur que le mug 441 ; le lot mug + affiche à 44,90 € laisse 21 €
  si Printify facture deux ports pleins, 26 € si le tarif « article suivant » s'applique
  ([[RCH - Validation de l'affiche grands-parents en produit compagnon du mug (29-10-2026)]]) ;
- le tote W801 chez Textildruck Europa n'existe qu'en noir, rouge et marine, en portrait, au
  lavage main ; 4 € de marge sans Premium, 8 € avec, à 24,90 € ; il impose une version fond
  foncé de chaque illustration et le choix de Textildruck pour le mug
  ([[RCH - Validation du tote bag compagnon du mug (29-10-2026)]]) ;
- la housse de coussin chez MWW On Demand (site Allemagne probable) laisse 9 à 13 € à 29,90 €,
  mais vient d'un troisième imprimeur, demande un panneau double recto-verso à 150 DPI, et
  Cadeau Plus vend la housse seule à 24,95 €
  ([[RCH - Validation de la housse de coussin grands-parents (29-10-2026)]]) ;
- la décoration de sapin chez Harrier laisse 5 € à 19,90 € et 10 € à 24,90 €, vient d'un
  troisième imprimeur sans colis commun, sur un marché français à 9,90 €
  ([[RCH - Décoration de sapin personnalisée grands-parents (29-10-2026)]]) ;
- chaussette, carte seule, sous-verres en lot, tablier, torchon, gobelet, plaid, bougie, boîte,
  planche et puzzle sont sans imprimeur UE ou sans marge.
Noël 2026 est un test manuel de 8 à 12 designs, mise en ligne au 15/11/2026, à deux
développeurs ([[04 - Noël 2026 en test manuel réduit, Fête des grands-mères 2027 pour le système]]).

## Décision
**Catalogue de Noël 2026 : le mug 11 oz et l'affiche, tous deux chez OPT OnDemand.** Rien d'autre.

- Mug 11 oz, blueprint 441 « Ceramic Mug (EU) », OPT OnDemand, 24,90 €.
- Affiche A4 et A3 portrait, blueprint 443, OPT OnDemand, papier mat, 24,90 € en A4 et 29,90 € en A3.
- Offres groupées : duo de mugs à 44,90 € (décision 02) et lot mug + affiche A4 à 44,90 €.
  Un lot mug + affiche A3 à 49,90 € est possible dès que le port du lot est mesuré.
- Un même design sert les deux supports : bandeau pour le mug, fichier maître A3 portrait de
  3 510 × 4 950 px réduit pour l'A4.

**Partenaire mug figé : OPT OnDemand**, ce qui précise la décision 05 (« France sinon
Allemagne » devient « Tchéquie »). Textildruck Europa reste le repli, Gelato le second fournisseur.
Ce choix est confirmé ou renversé par les échantillons : si la qualité d'OPT déçoit, le repli est
Textildruck avec le mug 1016, et l'affiche part alors d'un imprimeur distinct.

**Reportés à la Fête des grands-mères 2027** : la housse de coussin (MWW) et la décoration de
sapin (Harrier, hors saison en mars, à reconsidérer pour Noël 2027). Un échantillon de chaque est
commandé dès maintenant, dans la commande de test, pour ne pas repartir de zéro.

**Écartés** : tote bag (sauf si un tote écru UE abordable apparaît), chaussette de Noël, carte
seule, sous-verres en lot, tablier, torchon, gobelet, plaid, bougie, boîte, planche, puzzle.
Le sticker carré d'OPT reste une piste de complément de panier, après mesure du port.

**Commande de test, avant le 05/11/2026**, par l'API, chez OPT, livrée en France, avec un
fichier rendu par le système : mug 441, affiche A4 mate, affiche A3 brillante. Elle sert de test
de commande externe (décision 08), mesure le port réel du lot et le nombre de colis, et montre
l'emballage et le papier.

## Alternatives écartées
- **Mug seul plus duo** : le plus simple, mais sans produit qui montre l'illustration en grand
  et sans lot au-dessus du duo ; l'affiche coûte une composition portrait, pas une chaîne de rendu.
- **Mug chez Textildruck plus tote** : marge faible sans Premium, trois coloris foncés, version
  fond foncé de chaque illustration, lavage main, et perte du colis commun avec l'affiche.
- **Trois produits ou plus pour Noël (housse, décoration)** : chaque ajout apporte un imprimeur,
  un format maître et une chaîne de rendu à construire avant le 15/11, pour un test manuel.
- **Affiche chez Posterflow** : meilleure note et formats 30 × 40 et 50 × 70, mais port à 16,29 $
  et imprimeur distinct du mug ; à reprendre pour les grands formats.

## Conséquences
- La boutique de Noël a deux fiches produit (mug, affiche avec variante A4 et A3), deux offres
  groupées, 8 à 12 designs.
- Le créateur produit chaque design en deux compositions : bandeau 2,4:1 et portrait série A,
  en calques, avec les gabarits de prénoms 1-2, 3-4, 5-6, 7-8 pour chaque composition.
- Le système de rendu (décision 08) couvre deux zones d'impression : 2475 × 1155 px (mug, à
  confirmer chez OPT) et 2 490 × 3 510 px ou 3 510 × 4 950 px (affiche).
- Les points P1 du registre se concentrent sur OPT : identifiants de variantes par l'API
  publique, emballage de l'affiche, pays d'origine, port du lot, TVA facturée.
- La décision 05 est précisée, pas modifiée : partenaire figé OPT OnDemand, sous réserve des
  échantillons.
- Pour mars 2027 : housse de coussin et sticker en candidats ; décoration de sapin pour Noël 2027.
- 30/10/2026 : précisée par [[10 - Lancement avec le mug, la boule en cristal et la décoration en bois, trois imprimeurs UE]] (mug Textildruck, boule en verre Chill, décoration en bois WOYC à forme libre parmi six, environ 10 illustrations communes aux trois produits et texte libre, affiche retirée), en attente de validation par Antoine. La « chaussette de Noël » écartée ci-dessus est la chaussette en tissu ; la décoration de sapin reportée passe à Noël 2026 en bois.

## Concerne
[[SYN - Choix de la niche]] · [[SYN - Fournisseurs]] · [[SYN - Système]] · [[05 - Printify en principal avec partenaire UE figé, Gelato en second, franchise de TVA au départ]] · [[08 - Personnalisation à la commande en génération interne, test Printify avant le 5 novembre]] · notes TODO Noël à venir.
