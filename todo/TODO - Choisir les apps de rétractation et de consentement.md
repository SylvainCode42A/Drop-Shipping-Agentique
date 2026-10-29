---
type: todo
title: TODO - Choisir les apps de rétractation et de consentement
status: à faire
priority: haute
decision: "[[07 - La maquette est le cahier des charges du thème Shopify]]"
created: 2026-10-29
related: ["[[OVR - Boutique NolaPrint]]", "[[MOD - Pages légales et rétractation]]", "[[MOD - Cookies et consentement]]", "[[FLOW - Rétractation en ligne]]", "[[SYN - Juridique]]", "[[RCH - Retours et remboursements (28-10-2026)]]"]
decisions: ["[[04 - Noël 2026 en test manuel réduit, Fête des grands-mères 2027 pour le système]]", "[[07 - La maquette est le cahier des charges du thème Shopify]]"]
last-verified: 2026-10-29
tags: [dropshipping, boutique, juridique, todo]
---
# TODO - Choisir les apps de rétractation et de consentement

## Pourquoi
Deux obligations simulées dans la maquette doivent exister pour de vrai avant la première publicité :
la fonction de rétractation en ligne, obligatoire depuis le 19/06/2026 (amende jusqu'à 15 000 € pour une
personne physique) ([[RCH - Retours et remboursements (28-10-2026)]]), et le consentement préalable aux
cookies, sans lequel le pixel Meta ne peut pas être posé ([[SYN - Juridique]], [[SYN - Acquisition]]).

## Ce qu'il faut faire
1. **Rétractation** : comparer les apps Shopify (bouton nommé, identification, confirmation, accusé
   horodaté par e-mail) contre un développement dédié ⚠️ à rechercher ; reprendre le parcours de
   [[FLOW - Rétractation en ligne]].
2. **Consentement** : bannière Shopify (API Customer Privacy) ou app dédiée ; « Tout refuser » au premier
   niveau ; consentement transmis au pixel Meta, à l'API Conversions et au Consent Mode v2 de Google ;
   durée de validité du choix ⚠️ à vérifier (CNIL).
3. Décider (note NN) et mettre à jour [[MOD - Pages légales et rétractation]] et [[MOD - Cookies et consentement]].

## Comment prouver
- Rétractation : une demande test reçoit un e-mail horodaté immédiat ; le lien est présent en pied de
  page sur toutes les pages.
- Consentement : « Tout refuser » → aucun appel vers Meta ni Google dans l'onglet réseau du navigateur ;
  « Tout accepter » → le pixel se déclenche ; le choix se modifie depuis le pied de page.

## État
- 2026-10-29 : créée à la fin du niveau `5-boutique/`.
