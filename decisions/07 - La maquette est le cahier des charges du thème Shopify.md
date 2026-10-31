---
type: decision
title: 07 - La maquette est le cahier des charges du thème Shopify
status: draft
date: 2026-10-29
implemented: non
related: ["[[OVR - Boutique NolaPrint]]", "[[OVR - Drop shipping agentique]]", "[[SYN - Système]]", "[[SYN - Juridique]]"]
decisions: ["[[04 - Noël 2026 en test manuel réduit, Fête des grands-mères 2027 pour le système]]", "[[05 - Printify seul fournisseur avec partenaire UE figé, franchise de TVA au départ]]"]
last-verified: 2026-10-29
tags: [dropshipping, boutique, decision]
---
# 07 - La maquette est le cahier des charges du thème Shopify

## Contexte
La maquette HTML de la boutique (`Claude outputs/nolaprint-sans-apercu-en-direct.html`) est validée
visuellement le 29/10/2026 ([[OVR - Boutique NolaPrint]]). Elle simule tout dans le navigateur :
routeur par ancre, panier `localStorage`, commande sans paiement, bannière cookies maison, aperçu SVG.
La boutique réelle doit vendre via Shopify et transmettre les prénoms à Printify
([[04 - Noël 2026 en test manuel réduit, Fête des grands-mères 2027 pour le système]],
[[05 - Printify seul fournisseur avec partenaire UE figé, franchise de TVA au départ]]).

## Décision
La maquette est le **cahier des charges** de la boutique. La vraie boutique est un **thème Shopify**
reconstruit à partir d'elle.
- Reprises telles quelles : mise en page, couleurs, textes, ordre des sections, règles visibles par le
  client (case de vérification de l'orthographe, mentions légales, délais affichés).
- Remplacées par Shopify : routeur, panier, commande et paiement, bannière cookies (API Customer Privacy),
  aperçu de personnalisation (app reliée à Printify ⚠️ à choisir).
- Toute modification de design se fait d'abord dans la maquette, puis est reportée dans le thème.

## Alternatives écartées
- **Déployer la maquette telle quelle, Shopify en headless** : il faudrait recoder panier, paiement et
  synchronisation des commandes, hors de portée avant le 15/11/2026.
- **Démo de design sans suite** : le travail de mise en page et de textes serait perdu pour le thème.

## Conséquences
- Il faut choisir une app de personnalisation compatible Shopify et Printify, avec aperçu en direct et
  rappel sur les accents ⚠️ à choisir et à tester.
- Le bouton de rétractation, la bannière cookies et les mentions légales doivent être refaits dans
  Shopify (app ou développement) ([[SYN - Juridique]]).
- Les notes MOD, CMP et FLOW de `5-boutique/` décrivent la maquette ; chacune dira ce que devient son
  bloc dans le thème.
- À inscrire dans A VERIFIER : app de personnalisation, solution Shopify pour le bouton de rétractation.
- 29/10/2026 : vitrine intermédiaire déployée telle quelle via un layout alternatif ([[MOD - Thème Shopify]]) ; ce n'est pas l'alternative headless écartée, car Shopify sert la page et le futur thème reste à faire.

## Concerne
[[OVR - Boutique NolaPrint]] · [[SYN - Juridique]] · [[SYN - Système]] · notes MOD de `5-boutique/` à venir.
