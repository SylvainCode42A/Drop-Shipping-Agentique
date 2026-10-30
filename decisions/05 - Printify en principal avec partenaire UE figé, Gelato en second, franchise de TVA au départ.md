---
type: decision
title: 05 - Printify en principal avec partenaire UE figé, Gelato en second, franchise de TVA au départ
status: validé
date: 2026-10-25
implemented: non
related: ["[[OVR - Drop shipping agentique]]", "[[SYN - Fournisseurs]]", "[[SYN - Juridique]]", "[[SYN - Système]]", "[[04 - Noël 2026 en test manuel réduit, Fête des grands-mères 2027 pour le système]]"]
decisions: ["[[02 - Mug famille illustrée à 24,90 €, panier cible 45 €]]", "[[04 - Noël 2026 en test manuel réduit, Fête des grands-mères 2027 pour le système]]", "[[06 - LangGraph au départ, interface d'images interne avec Nano Banana Pro et Ideogram]]"]
last-verified: 2026-10-25
tags: [dropshipping, fournisseurs, juridique, decision]
---
# 05 - Printify en principal avec partenaire UE figé, Gelato en second, franchise de TVA au départ

## Contexte
Cinquième décision attendue par [[OVR - Drop shipping agentique]]. Printify est le seul fournisseur dont
l'API couvre toute la chaîne jusqu'à la publication Shopify, un agent pouvant créer un produit sans modèle ;
sa qualité dépend du partenaire, qu'il faut figer. Gelato produit en France avec routage automatique, mais
l'API crée un produit seulement à partir d'un modèle préparé à la main. Printful a la qualité la plus
régulière mais des ateliers en Espagne et en Lettonie et pas de création de produit Shopify par API.
T-Pop est en France sans API ([[SYN - Fournisseurs]], [[RCH - Fournisseurs print-on-demand et API (25-10-2026)]]).
Le pays d'expédition décide du schéma de TVA : depuis la France, le seuil de 10 000 € de ventes UE joue ;
depuis un autre pays de l'UE, la TVA du pays du client peut être due dès le premier euro ([[SYN - Juridique]]).
Aucun prix, délai ni taux de casse réel n'a été mesuré.

## Décision
- **Fournisseur principal : Printify**, avec un partenaire européen figé pour le mug, de préférence en
  France, sinon en Allemagne. Le partenaire est choisi après échantillons et inscrit dans la configuration
  de la passerelle ; un agent ne peut pas en changer.
- **Fournisseur second : Gelato**, pour comparer sur les échantillons de Noël et servir de repli si le
  partenaire Printify défaille en haute saison. Un modèle « mug famille illustrée » y est préparé.
- **Échantillons** chez les deux avant le 15/11/2026 : un mug avec prénoms accentués.
  Mesurés : rendu des prénoms, casse, délai réel, emballage.
- **TVA : franchise en base au départ**, micro-entreprise, comme le recommande le rapport juridique.
  Le cas d'un partenaire qui expédie depuis un autre pays de l'UE est soumis à un expert-comptable avant
  janvier 2027 ; pour Noël, le risque est borné par le volume.

## Alternatives écartées
- **Gelato en principal** : plus simple pour un test manuel, mais le routage automatique rend le pays
  d'expédition incertain pour la TVA et la qualité variable, et le système de mars a besoin d'un atelier
  maîtrisé et d'une création de produit par API sans modèle.
- **Printful** : qualité régulière, mais création de produit Shopify détournée par l'API Admin, chaque mug
  facturé comme un premier article, ateliers hors de France.
- **T-Pop** : atelier en France et livraison en 2-3 jours, mais pas d'API publique ; à revoir si l'API
  annoncée sort.

## Conséquences
- La passerelle fournisseur (décision 06, notes MOD) cible l'API Printify : file d'attente par endpoint,
  créations idempotentes, visuels stockés chez soi, jeton d'un an à renouveler.
- Le partenaire figé et son pays d'expédition sont une donnée de configuration, pas une décision d'agent.
- Les profils d'expédition Shopify sont limités à 100 : la passerelle ne crée pas de profil par produit.
- À inscrire dans A VERIFIER : meilleur partenaire Printify en France ou en Allemagne pour le mug ;
  environnement de test Printify ; politique Printify sur les designs IA (relecture humaine imposée) ;
  Gelato permet-il de forcer le pays de production ; schéma de TVA selon le pays d'expédition réel.
- À inscrire dans TODO : commander les échantillons, ouvrir le compte Printify et la boutique de développement.

## Concerne
[[SYN - Fournisseurs]] · [[SYN - Juridique]] · [[SYN - Système]] · décision 06 · notes MOD à venir.
