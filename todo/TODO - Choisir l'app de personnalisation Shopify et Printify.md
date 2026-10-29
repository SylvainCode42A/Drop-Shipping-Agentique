---
type: todo
title: TODO - Choisir l'app de personnalisation Shopify et Printify
status: à faire
priority: haute
decision: "[[07 - La maquette est le cahier des charges du thème Shopify]]"
created: 2026-10-29
related: ["[[OVR - Boutique NolaPrint]]", "[[MOD - Catalogue et fiche produit]]", "[[CMP - Illustrations]]", "[[CMP - Panier]]", "[[SYN - Fournisseurs]]"]
decisions: ["[[05 - Printify en principal avec partenaire UE figé, Gelato en second, franchise de TVA au départ]]", "[[07 - La maquette est le cahier des charges du thème Shopify]]"]
last-verified: 2026-10-29
tags: [dropshipping, boutique, fournisseurs, todo]
---
# TODO - Choisir l'app de personnalisation Shopify et Printify

## Pourquoi
Toute la boutique repose sur un texte saisi par le client et imprimé sans erreur. Dans la maquette,
l'aperçu SVG et la case d'orthographe font ce travail ([[MOD - Catalogue et fiche produit]]) ; dans
Shopify, il faut une app qui fasse la même chose et transmette les prénoms à Printify
([[07 - La maquette est le cahier des charges du thème Shopify]]). C'est le point technique le plus risqué
du test de Noël, avec des produits en ligne au plus tard le 15/11/2026
([[04 - Noël 2026 en test manuel réduit, Fête des grands-mères 2027 pour le système]]).

## Ce qu'il faut faire
1. Lister les apps compatibles Shopify + Printify avec personnalisation par le client ⚠️ à rechercher
   (note RCH dans `2-marche/2-Fournisseurs/`).
2. Critères : aperçu en direct sur le vrai visuel ; champs texte avec limite de caractères ; liste de
   prénoms de 1 à 4 ; accents et traits d'union ; case de confirmation obligatoire ; propriétés de ligne
   transmises à Printify ; fichier d'impression généré à la taille de la zone ; prix ; avis.
3. Installer la meilleure sur la boutique de développement, configurer le mug famille illustrée.
4. Décider (note NN) et mettre à jour [[MOD - Catalogue et fiche produit]] et [[CMP - Illustrations]].

## Comment prouver
- Commande de test « Mamounette · Léa, Hugo, Élio-Noé · Noël 2026 » sur la boutique de développement.
- Le fichier reçu par Printify contient exactement ces textes, accents et trait d'union compris.
- L'échantillon imprimé correspond à l'aperçu affiché au client.
- L'ajout au panier est impossible sans la case cochée.

## État
- 2026-10-29 : créée à la fin du niveau `5-boutique/`.
