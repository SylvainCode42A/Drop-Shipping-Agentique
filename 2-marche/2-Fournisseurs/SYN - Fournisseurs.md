---
type: synthese
title: SYN - Fournisseurs
status: draft
related:
  - "[[SYN - Modèle économique]]"
  - "[[SYN - Juridique]]"
  - "[[SYN - Système]]"
  - "[[A VERIFIER - Points à valider, vérifier, tester]]"
decisions:
  - "[[02 - Le mug seul, Standard Mug 11 oz chez Textildruck Europa]]"
last-verified: 2026-11-09
tags:
  - dropshipping
  - fournisseurs
  - synthese
---
# SYN - Fournisseurs

Ce qu'on sait sur le fournisseur du mug : Printify, imprimeur Textildruck Europa.
Les décisions sont dans `decisions/` ; cette note ne les recopie pas, elle les cite.

## Ce qu'on sait

### Printify et son API
- API REST complète (catalogue, produits, commandes, uploads, webhooks), publication vers Shopify
  par un endpoint dédié. Le catalogue donne les dimensions en pixels de chaque zone d'impression
  ([[RCH - Fournisseurs print-on-demand et API (25-10-2026)]]).
- Limites : 600 requêtes par minute, 100 sur le catalogue, 200 publications par 30 minutes,
  jeton valable un an ([[RCH - Fournisseurs print-on-demand et API (25-10-2026)]]).
- Shopify : 100 profils d'expédition maximum par boutique
  ([[RCH - Fournisseurs print-on-demand et API (25-10-2026)]]).
- Depuis le 1er juillet 2026, Printify route les commandes UE vers un imprimeur UE quand il existe
  ([[RCH - Vérification Printify UE du mug et vue d'ensemble des produits (28-10-2026)]]).
- Printify facture la TVA sur les commandes vers l'UE ; récupérable « si vous êtes assujetti »,
  rien sur la franchise en base ⚠️ expert-comptable
  ([[RCH - Relevé connecté du catalogue Printify UE (29-10-2026)]]).

### Le mug chez Textildruck Europa
- Textildruck Europa (Allemagne, note 8,65) : Standard Mug 11 oz, blueprint 1016, 5,91 $
  (4,42 $ avec Premium), port 6,89 $ puis 1,99 $ par mug suivant, 5 à 10 jours
  (source : relevé connecté du 29/10, [[RCH - Relevé connecté du catalogue Printify UE (29-10-2026)]]).
- Coût réel d'un mug livré en France (source : facture Printify du 03/11/2026) : 5,91 $ fabrication
  + 6,89 $ port + 2,55 $ TVA = 15,35 $, soit 13,68 € ; frais de change en plus ⚠️
  ([[02 - Le mug seul, Standard Mug 11 oz chez Textildruck Europa]]).
- Délai mesuré : produit en 2 jours, livré 8 à 10 jours après la commande ⚠️ à confirmer à la réception.
- Abonnement Printify Premium : 39 $ par mois en mensuel, 24,99 $ en annuel, jusqu'à 20 % de remise
  ([[RCH - Synthèse comparative des produits d'élargissement (29-10-2026)]]).

### Le fichier d'impression du mug
- PNG ou JPG, profil sRGB, 150 à 300 DPI à taille réelle
  ([[RCH - Fournisseurs print-on-demand et API (25-10-2026)]]).
- Taille de la zone 11 oz selon les sources : 2475 × 1155 px (guide Printify), 2480 × 1146,
  2700 × 1120, 2625 × 1050 ⚠️ contradictoire, à lire sur le gabarit Textildruck 1016
  ([[RCH - Marché des mugs grands-parents avec prénoms (28-10-2026)]]).

### La douane (règle hors UE de la décision 02)
- Du 1er juillet 2026 au 1er juillet 2028, tout colis de 150 € ou moins venant d'un pays tiers paie
  3 € par catégorie tarifaire, plus la TVA à l'import ⚠️
  ([[RCH - Synthèse comparative des produits d'élargissement (29-10-2026)]], [[SYN - Juridique]]).

## Ce qui est décidé
- Mug seul, Standard Mug 11 oz (1016) chez Textildruck Europa, Printify seul fournisseur :
  [[02 - Le mug seul, Standard Mug 11 oz chez Textildruck Europa]].

## Questions ouvertes
- Gabarit exact (pixels, DPI) du Standard Mug 1016 chez Textildruck.
- Rendu, emballage et casse à la réception de l'échantillon.
- Frais de change réels sur le relevé bancaire.
- TVA Printify en franchise de TVA : récupérable ou non ⚠️ expert-comptable.
- Documentation GPSR et contact alimentaire fournie par Textildruck.

## Recherches
- [[RCH - Fournisseurs print-on-demand et API (25-10-2026)]]
- [[RCH - Vérification Printify UE du mug et vue d'ensemble des produits (28-10-2026)]]
- [[RCH - Relevé connecté du catalogue Printify UE (29-10-2026)]]
- [[RCH - Marché des mugs grands-parents avec prénoms (28-10-2026)]]
- [[RCH - Synthèse comparative des produits d'élargissement (29-10-2026)]]
