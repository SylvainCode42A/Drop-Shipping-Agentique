---
type: decision
title: 08 - Personnalisation à la commande en génération interne, test Printify avant le 5 novembre
status: validé
date: 2026-10-29
implemented: non
related: ["[[OVR - Drop shipping agentique]]", "[[SYN - Système]]", "[[SYN - Fournisseurs]]", "[[SYN - Choix de la niche]]", "[[RCH - Applications de personnalisation Shopify pour Printify et Gelato (29-10-2026)]]", "[[A VERIFIER - Points à valider, vérifier, tester]]"]
decisions: ["[[02 - Mug famille illustrée à 24,90 €, panier cible 45 €]]", "[[03 - Approbation unitaire au lancement, paliers d'autonomie, actions toujours bloquées]]", "[[04 - Noël 2026 en test manuel réduit, Fête des grands-mères 2027 pour le système]]", "[[05 - Printify en principal avec partenaire UE figé, Gelato en second, franchise de TVA au départ]]", "[[06 - LangGraph au départ, interface d'images interne avec Nano Banana Pro et Ideogram]]"]
last-verified: 2026-10-29
tags: [dropshipping, systeme, decision]
---
# 08 - Personnalisation à la commande en génération interne, test Printify avant le 5 novembre

## Contexte
Neuvième décision attendue par [[OVR - Drop shipping agentique]] (numérotée 9 dans la liste du 29/10,
prise en premier parce qu'elle ne dépend d'aucune vérification et conditionne le workflow du créateur).
Le produit est une illustration fixe choisie dans un catalogue ; la cliente saisit de 1 à 8 prénoms
de petits-enfants à la commande ; quelqu'un doit produire le fichier d'impression final et l'envoyer
au fournisseur ([[02 - Mug famille illustrée à 24,90 €, panier cible 45 €]]).
Le marché attend un aperçu avant paiement, un rappel sur les accents et un texte lisible ; l'erreur de
prénom est la première cause de mécontentement ([[SYN - Choix de la niche]]).
Deux voies documentées ([[RCH - Applications de personnalisation Shopify pour Printify et Gelato (29-10-2026)]], [[SYN - Système]]) :
- une application tierce (Teeinblue ou Customily, 49 $ par mois plus 0,25 à 1 $ par article) qui donne
  l'aperçu en direct et envoie le fichier à Printify, mais sans API de gabarits : chaque design passe à
  la main dans leur éditeur, et le changement de mise en page selon le nombre de prénoms n'est pas documenté ;
- la génération interne : illustration en calques, texte rendu par code, fichier poussé par l'API Printify,
  saisie par champs simples sur Shopify ; tout sous contrôle des agents, aperçu client à construire.
Deux développeurs travaillent sur le projet. Noël 2026 est un test manuel réduit, 8 à 12 mugs avant le
15/11/2026 ([[04 - Noël 2026 en test manuel réduit, Fête des grands-mères 2027 pour le système]]).

## Décision
**Personnalisation à la commande en génération interne**, dès Noël 2026.

Flux retenu :
1. Fiche produit Shopify avec des champs de prénoms obligatoires (sélecteur du nombre de personnes,
   un champ par prénom, 15 caractères par prénom, rappel d'orthographe et d'accents). Les prénoms
   arrivent dans la commande comme propriétés de ligne.
2. Le produit Shopify n'est **pas** relié à Printify en envoi automatique : seul notre script commande,
   sinon Printify importe la commande avec l'image de base, sans prénoms, et il y a deux commandes.
3. À la commande (webhook `orders/create`), le système choisit le gabarit selon le nombre de prénoms
   (1-2, 3-4, 5-6, 7-8), rend le texte sur l'illustration en calques avec une police testée sur les
   accents, et exporte un PNG sRGB 300 DPI à la taille de la zone d'impression de l'imprimeur.
4. Contrôle : vérifications déterministes, OCR du texte rendu, puis validation humaine de chaque fichier
   avant envoi au lancement, comme pour les designs ([[03 - Approbation unitaire au lancement, paliers d'autonomie, actions toujours bloquées]]).
5. Commande chez Printify par l'API, avec le PNG final dans la zone d'impression et le partenaire UE
   figé ([[05 - Printify en principal avec partenaire UE figé, Gelato en second, franchise de TVA au départ]]).

Aperçu client : pour Noël, un mockup statique et le rappel d'orthographe ; un aperçu rendu côté serveur
(même gabarit, même police que le fichier final) est construit après Noël. Un aperçu JavaScript dans le
navigateur n'est pas retenu, parce qu'il ne reproduit jamais exactement le rendu serveur.

Pour Noël, l'étape 3 peut être faite à la main sur chaque commande (fusion, puis commande dans Printify),
avec la même fiche produit ; l'automatisation complète vise mars 2027.

**Préalable : test, avant le 5 novembre 2026, d'une commande Printify avec un fichier d'impression propre
à la commande** (commande externe avec `blueprint_id`, `print_provider_id`, `variant_id` et `print_areas`
portant l'image, sans produit créé au préalable), en bac à sable ou sur une commande réelle d'échantillon.
**Repli si le test échoue : Printful**, qui accepte un fichier par ligne de commande ; le flux reste le même,
seule la passerelle fournisseur change. Une application tierce n'est pas le repli.

## Alternatives écartées
- **Application tierce (Teeinblue, Customily)** : aperçu client immédiat et flux éprouvé, mais aucune API
  de gabarits, donc les agents ne peuvent pas mettre un design en vente seuls ; 49 $ par mois pour un
  éditeur qu'il faudrait contourner en mars ; risque de s'y installer par confort.
- **Personnalisation native Printify** : gratuite, mais sans aperçu rendu sur Shopify, avec une
  validation manuelle contradictoire dans la documentation, et sans gabarits par nombre de prénoms.
- **Un seul champ « prénom » facultatif** : la niche vend 1 à 8 prénoms avec un élément graphique par
  enfant ; un mug famille sans prénom n'a pas de sens commercial.
- **Aperçu JavaScript côté navigateur** : lissage, interlettrage et retours à la ligne diffèrent du rendu
  serveur ; la cliente validerait une chose et en recevrait une autre.

## Conséquences
- Le créateur produit chaque illustration en calques (fond, famille, zone réservée aux prénoms) et
  déclare pour chaque support la zone de texte et les gabarits ([[SYN - Système]], formats par support).
- Un module de rendu de texte (Pillow ou rendu SVG), une passerelle Printify avec commandes externes,
  un webhook `orders/create` idempotent, et une étape de validation humaine du fichier rendu entrent
  dans la stack de la décision 06.
- Les échantillons de Noël sont commandés avec un fichier rendu par le système, pour tester la chaîne
  entière avant la mise en ligne.
- Le journal porte, par commande : prénoms saisis, gabarit choisi, police, hachage du fichier, résultat
  de l'OCR, validateur et date.
- À inscrire dans A VERIFIER : commande externe Printify (P1, avant le 05/11) ; police et OCR sur
  é, è, ê, ë, ï, ç, œ et prénoms composés ; zone d'impression exacte de l'imprimeur retenu ; absence
  de double commande après découplage de la synchro Printify.
- Une note FLOW dans `3-systeme/4-flux/` décrit ce flux.

## Concerne
[[SYN - Système]] · [[SYN - Fournisseurs]] · [[SYN - Choix de la niche]] · note FLOW à venir.
