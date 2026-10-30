---
type: decision
title: 08 - Notre serveur fusionne l'illustration et le prénom, Printify reçoit une image finale
status: draft
date: 2026-10-29
implemented: non
related: ["[[FLOW - De la commande personnalisée à Printify]]", "[[SYN - Fournisseurs]]", "[[SYN - Système]]"]
decisions: ["[[02 - Mug famille illustrée à 24,90 €, duo à 44,90 €, panier cible 45 €]]", "[[03 - Approbation unitaire au lancement, paliers d'autonomie, actions toujours bloquées]]", "[[04 - Noël 2026 en test manuel réduit, Fête des grands-mères 2027 pour le système]]", "[[05 - Printify en principal avec partenaire UE figé, Gelato en second, franchise de TVA au départ]]", "[[07 - La maquette est le cahier des charges du thème Shopify]]"]
last-verified: 2026-10-29
tags: [dropshipping, systeme, fournisseurs, decision]
---
# 08 - Notre serveur fusionne l'illustration et le prénom, Printify reçoit une image finale

## Contexte
Le client ne choisit pas l'image : nous publions une sélection d'illustrations, une par produit.
Il peut ajouter un prénom, ou non. Trois façons de produire le fichier d'impression ont été comparées
le 29/10/2026 :
- personnalisation automatique Printify : calques personnalisables dans Product Creator, bloc
  « Printify Personalize Button » dans le thème Shopify ; mais la personnalisation devient obligatoire
  pour le produit, et Shopify n'offre ni choix de police ni choix de couleur (source : help.printify.com,
  articles 28903711308177 et 41063013169297) ;
- app tierce (Customily, Teeinblue) : aperçu riche, abonnement mensuel, dépendance de plus ;
- fusion par notre propre code.

L'API Printify accepte une commande sans produit créé chez Printify : ligne `lineItemWithBlueprint`
avec `print_provider_id`, `blueprint_id`, `variant_id`, `quantity` et `print_areas` (URL d'image), puis
`send_to_production` (source : developers.printify.com/openapi.json, lu le 29/10/2026).

## Décision
**Notre serveur fusionne l'illustration et le prénom en un PNG final, et crée la commande Printify par
l'API.** Le prénom est facultatif : sans prénom, l'illustration part telle quelle.
- La fiche Shopify porte un champ texte facultatif et un aperçu sur le mockup, avec le même gabarit
  que le rendu final.
- Les produits Shopify ne sont **pas** reliés à la synchronisation Printify.
- Pour Noël 2026, la fusion et la commande Printify sont faites à la main
  ([[04 - Noël 2026 en test manuel réduit, Fête des grands-mères 2027 pour le système]]).

## Alternatives écartées
- **Personnalisation automatique Printify** : prénom obligatoire, pas de maîtrise du rendu, aperçu
  imposé par Printify.
- **App tierce** : coût mensuel et rendu hors de notre contrôle, pour un besoin limité à un texte.
- **Personnalisation assistée par IA de Printify** : réservée au mode manuel, rendu interprété par
  une IA, risque d'erreur sur le prénom (source : help.printify.com, article 45728947477521).

## Conséquences
- Remplace, dans [[07 - La maquette est le cahier des charges du thème Shopify]], le point « aperçu
  de personnalisation (app reliée à Printify ⚠️ à choisir) » : l'aperçu est dans notre thème.
- Le suivi d'expédition ne remonte pas seul dans Shopify : il faut le relayer depuis Printify
  ⚠️ à vérifier (webhooks Printify).
- Un gabarit par illustration : zone du prénom, police avec accents, taille maximale, réduction
  automatique.
- À inscrire dans A VERIFIER : webhooks d'expédition Printify, accents de la police, rendu d'un
  prénom de 15 caractères sur l'échantillon.

## Concerne
[[FLOW - De la commande personnalisée à Printify]] · [[SYN - Fournisseurs]] · [[SYN - Système]] ·
[[07 - La maquette est le cahier des charges du thème Shopify]]
