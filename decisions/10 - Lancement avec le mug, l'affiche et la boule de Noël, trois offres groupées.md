---
type: decision
title: 10 - Lancement avec le mug, l'affiche et la boule de Noël, trois offres groupées
status: draft
date: 2026-10-29
implemented: non
related: ["[[RCH - Synthèse comparative des produits d'élargissement (29-10-2026)]]", "[[RCH - Décoration de sapin personnalisée grands-parents (29-10-2026)]]", "[[RCH - Chaussette de Noël personnalisée grands-parents (29-10-2026)]]", "[[RCH - Sous-verres personnalisés pour grands-parents (28-10-2026)]]", "[[RCH - Carte de vœux et étiquette cadeau grands-parents (29-10-2026)]]", "[[RCH - Concurrents du mug famille à prénoms (29-10-2026)]]", "[[FLOW - Personnalisation à la commande]]", "[[MOD - Thème Shopify]]", "[[A VERIFIER - Points à valider, vérifier, tester]]"]
decisions: ["[[02 - Mug famille illustrée à 24,90 €, duo à 44,90 €, panier cible 45 €]]", "[[04 - Noël 2026 en test manuel réduit, Fête des grands-mères 2027 pour le système]]", "[[08 - Personnalisation à la commande en génération interne, test Printify avant le 5 novembre]]", "[[09 - Noël 2026 avec le mug et l'affiche chez OPT OnDemand, housse et décoration reportées]]"]
last-verified: 2026-10-29
tags: [dropshipping, niches, fournisseurs, boutique, decision, noel]
---
# 10 - Lancement avec le mug, l'affiche et la boule de Noël, trois offres groupées

## Contexte
La décision 09 retient le mug et l'affiche chez OPT OnDemand pour Noël 2026, reporte la décoration
de sapin à Noël 2027 et écarte la chaussette et les sous-verres
([[09 - Noël 2026 avec le mug et l'affiche chez OPT OnDemand, housse et décoration reportées]]).
Le 29/10, Sylvain demande trois ou quatre produits pour commencer, dont une boule de Noël, une
chaussette de Noël et un cadeau offert pour deux mugs achetés, dans une boutique qui reste centrée
sur la niche grands-parents ([[01 - Grands-parents en principal, retraite par métier en secondaire]]).
Les études disent, au prix de marché, port offert, en franchise de TVA (estimé) :
- boule céramique 1676 chez Harrier : environ 5 € de marge à 19,90 €, 10 € à 24,90 €, imprimeur
  distinct du mug, marché français à 9,90 € pour le bois gravé et 19,90 à 26 € pour l'illustré
  ([[RCH - Décoration de sapin personnalisée grands-parents (29-10-2026)]]) ;
- chaussette de Noël : aucun imprimeur dans l'UE, coût rendu en France de 18 à 39 € pour un prix
  de marché de 7,50 à 16 € ([[RCH - Chaussette de Noël personnalisée grands-parents (29-10-2026)]]) ;
- sous-verre offert : seule la céramique à l'unité 1523 chez WOYC (Italie) existe en UE, 8,37 $
  plus 5,99 $ de port, soit environ 13 € par offre, dans un colis séparé
  ([[RCH - Sous-verres personnalisés pour grands-parents (28-10-2026)]]) ;
- sticker carré 476 chez OPT : 3,89 $, 0,10 $ de port s'il suit le mug dans le même colis, port à
  confirmer ([[RCH - Carte de vœux et étiquette cadeau grands-parents (29-10-2026)]]).

## Décision
**Trois produits, un seul univers : la famille de Mamie et Papi, dessinée, avec les prénoms des
petits-enfants, sur trois supports.**
- **Mug famille illustrée**, blueprint 441, OPT OnDemand : 24,90 €.
- **Affiche de la famille**, blueprint 443, OPT OnDemand : A4 24,90 €, A3 29,90 €.
- **Boule de Noël de la famille**, céramique 1676, Harrier : 19,90 € à l'unité, 34,90 € le lot de
  deux boules identiques. Le design peut montrer une chaussette par petit-enfant avec son prénom :
  le motif de la chaussette reste dans la boutique sans le produit déficitaire.

**Trois offres.**
- Duo Mamie & Papi, deux mugs : 44,90 € au lieu de 49,80 € (décision 02).
- Lot mug + affiche A4 : 44,90 € au lieu de 49,80 € (décision 09).
- Étiquette cadeau (sticker OPT) offerte dès 45 € d'achat, une fois son port mesuré. Elle remplace
  le sous-verre offert.

**La boule est conditionnelle.** Harrier figure « United Kingdom » dans l'API Printify. Si la
commande de test montre une expédition hors UE (droit de 3 € et TVA à l'import), la boule est retirée
et la décision 09 s'applique telle quelle.

**Fiche produit.** Champs de personnalisation conformes à [[FLOW - Personnalisation à la commande]] :
`Appellation`, `Nombre de prénoms`, `Prénom 1` à `Prénom 8`, 15 caractères au plus, case
d'orthographe obligatoire. Boule limitée à 4 prénoms pour la lisibilité sur 7,5 cm. Duo : une
appellation par mug. Produits non synchronisés avec Printify (décision 08). Quand les designs
d'Antoine sont prêts, une fiche produit par design.

## Alternatives écartées
- **Chaussette de Noël** : perte sur chaque vente faute d'imprimeur UE.
- **Sous-verre offert pour deux mugs** : environ 13 € de coût par offre et un colis de plus ;
  remplacé par l'étiquette cadeau.
- **Quatrième produit, housse de coussin** (MWW, 29,90 €, 9 à 13 €) : troisième imprimeur, format
  panneau double, Cadeau Plus 5 € moins cher ; gardée pour la Fête des grands-mères 2027.
- **Mug et affiche seuls (décision 09 telle quelle)** : plus simple, mais sans produit saisonnier
  de Noël ni prix d'entrée sous 24,90 €.

## Conséquences
- Précise la décision 09 : la décoration de sapin passe de Noël 2027 à Noël 2026, sous condition.
  Harrier devient le deuxième imprimeur ; une commande mug + boule part en deux colis.
- La commande de test avant le 05/11/2026 ajoute la boule 1676 chez Harrier et le sticker 476 chez
  OPT : pays d'expédition, port, qualité de l'impression des prénoms sur céramique.
- Le créateur produit chaque design en trois compositions : bandeau 2,4:1 (mug), portrait série A
  (affiche), carré recto-verso 7,5 cm (boule), avec les gabarits 1-2 et 3-4 pour la boule.
- Thème Shopify (dossier `nolaprint-theme`) : fiche produit à appellation et nombre de prénoms,
  réglages par tags (`prenoms-max:4`, `appellation-2`), vrai panier Shopify. Fichier d'import
  `nolaprint-produits.csv` : mug, affiche, boule, duo, lot mug + affiche. [[MOD - Thème Shopify]]
  est à mettre à jour.
- À inscrire dans A VERIFIER : pays d'expédition de Harrier, port du lot mug + affiche, port du
  sticker avec le mug.
- Validation d'Antoine attendue avant de passer en `validé`.

## Concerne
[[09 - Noël 2026 avec le mug et l'affiche chez OPT OnDemand, housse et décoration reportées]] · [[SYN - Choix de la niche]] · [[SYN - Fournisseurs]] · [[FLOW - Personnalisation à la commande]] · [[MOD - Thème Shopify]]
