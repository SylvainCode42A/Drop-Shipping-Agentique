---
type: decision
title: 08 - Personnalisation, un champ texte libre, l'image faite sur le site, envoyée à Printify par Shopify
status: draft
date: 2026-11-09
implemented: non
related: ["[[RCH - Contraintes d'impression Printify des trois produits (01-11-2026)]]", "[[CMP - Personnalisation par produit]]"]
decisions: ["[[01 - Cible, maman, papa, mamie, papy, nos designs ou sa photo]]", "[[02 - Le mug seul, Standard Mug 11 oz chez Textildruck Europa]]", "[[03 - Ce que font les agents, ce qu'ils ne font jamais]]", "[[07 - Le site est un thème Shopify, modifié en local et poussé par la CLI]]"]
last-verified: 2026-11-09
tags: [dropshipping, systeme, personnalisation, decision]
---
# 08 - Personnalisation, un champ texte libre, l'image faite sur le site, envoyée à Printify par Shopify

## Contexte
Printify n'écrit pas de texte et ne fait pas d'aperçu : il imprime l'image qu'il reçoit
([[RCH - Contraintes d'impression Printify des trois produits (01-11-2026)]]).

## Décision

### Ce que choisit la cliente
| Mode        | Elle choisit           | Elle peut ajouter                                 |
| ----------- | ---------------------- | ------------------------------------------------- |
| Nos designs | un design              | un texte libre, facultatif, 15 caractères au plus |
| Sa photo    | son image (JPG ou PNG) | le même texte libre                               |

- **Police, couleur et position du texte : fixées par le design.** La cliente ne choisit que les mots.
- **Photo** : recadrée automatiquement au centre. Tour complet dès 2 000 px de large, un seul côté
  en dessous, refusée sous 1 000 px ⚠️ seuils à confirmer sur l'échantillon.
- **Zone d'impression de nos designs** : tour complet du mug, sauf sous l'anse ⚠️ à confirmer sur l'échantillon.

### Comment l'image est faite
1. Sur la fiche produit, le site compose l'image en direct : le design (ou la photo) et le texte.
2. À la commande, cette image finale part chez Printify par la connexion Printify de Shopify
   ⚠️ à tester sur une vraie commande : Printify doit recevoir l'image du site, pas l'image fixe du produit.

### Qui fait les gabarits
Un gabarit dit, pour un design, où va le texte, sa police, sa couleur et sa taille maximale.
- **Première gamme** : faits par nous.
- **Ensuite** : faits par notre agent, pour chaque design qu'il crée (décision 03).

## Conséquences
- Le mug 3D du thème passe en tour complet pour nos designs ; pour une photo, il suit le choix
  tour complet ou un côté.
- Prix du texte et de la photo : décision des prix.
- Photo de la cliente : clause CGV et mention RGPD (décision Juridique).

## Concerne
[[CMP - Personnalisation par produit]] · décisions 01, 02, 03, 07
