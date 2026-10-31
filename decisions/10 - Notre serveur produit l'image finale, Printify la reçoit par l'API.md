---
type: decision
title: 10 - Notre serveur produit l'image finale, Printify la reçoit par l'API
status: draft
date: 2026-10-29
implemented: non
related: ["[[FLOW - Personnalisation à la commande]]", "[[SYN - Fournisseurs]]", "[[SYN - Système]]"]
decisions: ["[[03 - Approbation unitaire au lancement, paliers d'autonomie, actions toujours bloquées]]", "[[04 - Noël 2026 en test manuel réduit, Fête des grands-mères 2027 pour le système]]", "[[05 - Printify seul fournisseur avec partenaire UE figé, franchise de TVA au départ]]", "[[07 - La maquette est le cahier des charges du thème Shopify]]", "[[08 - Personnalisation à la commande en génération interne, test Printify avant le 5 novembre]]", "[[02 - Lancement avec le mug, la boule en cristal et la décoration en bois, trois imprimeurs UE]]", "[[01 - Audience visée et nouvelle offre, parents et grands-parents d'abord, nos designs ou la page blanche]]", "[[11 - Texte facultatif à 1 €, frais de retour à la charge du client, retours chez Sylvain]]"]
last-verified: 2026-10-31
tags: [dropshipping, systeme, fournisseurs, decision]
---
# 10 - Notre serveur produit l'image finale, Printify la reçoit par l'API

> Numérotée 14 puis 13 jusqu'au 31/10/2026. Mise en cohérence le 31/10/2026 : c'est la seule décision
> sur la production du fichier d'impression. Elle remplace le flux à prénoms obligatoires de la
> décision 08 et la personnalisation automatisée Printify des décisions 01 et 02.

## Contexte
Trois mécanismes coexistaient : génération interne avec 1 à 8 prénoms obligatoires (08),
personnalisation automatisée Printify (01, 02), fusion par notre serveur avec texte facultatif (14).
La personnalisation automatisée Printify rend la personnalisation obligatoire et ne laisse ni police
ni couleur au choix sur Shopify (source : help.printify.com, articles 28903711308177 et 41063013169297).
L'API Printify accepte une commande sans produit créé chez Printify : ligne `lineItemWithBlueprint`
avec `print_provider_id`, `blueprint_id`, `variant_id`, `quantity` et `print_areas` (URL d'image),
puis `send_to_production` (source : developers.printify.com/openapi.json, lu le 29/10/2026).

## Décision
**Une image par commande est envoyée à Printify par notre API. Trois cas :**

| Cas | Ce que la cliente choisit | Ce que fait notre serveur | Prix |
|---|---|---|---|
| Nos designs, sans texte | une illustration (et la forme pour le bois) | envoie l'image associée à la variante, telle quelle | prix de base |
| Nos designs, avec texte | une illustration + son texte | fusionne l'illustration et le texte en un PNG final | +1 € |
| Page blanche | sa propre image, texte facultatif | contrôle l'image, la fusionne avec le texte éventuel | prix de base, +1 € si texte |

- Les produits Shopify ne sont **pas** reliés à la synchronisation Printify : seul notre script commande.
- La fiche Shopify porte un champ texte facultatif et un aperçu sur le mockup, avec le même gabarit
  que le rendu final.
- Déclencheur : webhook Shopify `orders/paid`.
- Au lancement, un humain valide chaque fichier avant l'envoi
  ([[03 - Approbation unitaire au lancement, paliers d'autonomie, actions toujours bloquées]]).
- Pour Noël 2026, la fusion et la commande Printify peuvent être faites à la main
  ([[04 - Noël 2026 en test manuel réduit, Fête des grands-mères 2027 pour le système]]) ;
  l'automatisation vient ensuite, sans changer la fiche produit.
- Fournisseur : Printify seulement. Si un imprimeur déçoit, le repli est un autre imprimeur Printify.

## Alternatives écartées
- **Personnalisation automatisée Printify** : texte obligatoire, rendu et aperçu imposés par Printify.
- **Prénoms obligatoires, gabarits 1-2 à 7-8 (décision 08)** : refusé, le texte est une option à 1 €
  ([[11 - Texte facultatif à 1 €, frais de retour à la charge du client, retours chez Sylvain]]).
- **App tierce (Customily, Teeinblue)** : coût mensuel, rendu hors de notre contrôle.
- **Personnalisation assistée par IA de Printify** : rendu interprété par une IA, risque d'erreur
  sur le texte (source : help.printify.com, article 45728947477521).
- **Gelato ou Printful en repli** : on garde un seul fournisseur.

## Conséquences
- Remplace, dans la 07, le point « aperçu de personnalisation (app reliée à Printify) » : l'aperçu est dans notre thème.
- Remplace le flux de la 08 et le paragraphe « Mise en œuvre de la personnalisation » de la 02.
- Un gabarit par illustration et par support (bandeau du mug, cercle de la boule, six formes en bois) :
  zone de texte, police avec accents, taille maximale, réduction automatique.
- Page blanche : contrôle de l'image cliente avant impression (résolution, cadrage, contenus
  interdits, marques et personnages), clause CGV, mention RGPD (décision 01).
- Le suivi d'expédition ne remonte pas seul dans Shopify : à relayer depuis Printify ⚠️ à vérifier (webhooks Printify).
- À inscrire dans A VERIFIER : commande `lineItemWithBlueprint` chez Textildruck, Chill et WOYC ;
  webhooks d'expédition Printify ; accents de la police ; rendu d'un texte long sur verre et sur bois.
- Validation d'Antoine attendue avant de passer en `validé`.

## Concerne
[[FLOW - Personnalisation à la commande]] · [[SYN - Fournisseurs]] · [[SYN - Système]] ·
[[07 - La maquette est le cahier des charges du thème Shopify]] · [[08 - Personnalisation à la commande en génération interne, test Printify avant le 5 novembre]] ·
[[02 - Lancement avec le mug, la boule en cristal et la décoration en bois, trois imprimeurs UE]]
