---
type: decision
title: 07 - Le site est un thème Shopify, modifié en local et poussé par la CLI
status: draft
date: 2026-11-09
implemented: oui
related: ["[[OVR - Boutique NolaPrint]]", "[[MOD - Thème Shopify]]", "[[FLOW - Déployer la maquette dans Shopify]]"]
decisions: ["[[01 - Cible, maman, papa, mamie, papy, nos designs ou sa photo]]", "[[02 - Le mug seul, Standard Mug 11 oz chez Textildruck Europa]]"]
last-verified: 2026-11-09
tags: [dropshipping, boutique, decision]
---
# 07 - Le site est un thème Shopify, modifié en local et poussé par la CLI

## Contexte
La boutique NolaPrint vend un seul produit, le mug (décision 02), en deux modes : nos designs ou
la photo de la cliente (décision 01). Shopify gère le panier, le paiement et les commandes.

## Décision

### Comment le site marche
| Partie | Qui la fait | Où |
|---|---|---|
| Pages, fiche produit, menu, textes | le thème NolaPrint | dépôt git du thème |
| Aperçu de personnalisation (texte, mug 3D) | le navigateur de la cliente | `assets/np-rendu.js`, `assets/np-mug3d.js` |
| Gabarits du mug (zones, polices, couleurs) | fichier de gabarits | `gabarits.json` |
| Panier, paiement, commandes | Shopify | admin Shopify |
| Produits, prix, variantes | Shopify, import CSV | `_imports-shopify/` |
| Fichier d'impression et commande Printify | notre serveur | décision Personnalisation |

### Comment on le modifie
1. Partir de la dernière version du dépôt git du thème.
2. Modifier dans `~/Documents/nolaprint-theme`.
3. Vérifier en local (`shopify theme dev`).
4. Pousser sur la boutique quand c'est bon :
   `shopify theme push --store 04qh0j-2k.myshopify.com --theme 209933369689`
5. Commit et push dans le dépôt git.

Il n'y a pas de maquette : le thème est la seule source du site.

## Alternatives écartées
- **Maquette HTML d'abord, thème ensuite** : deux versions à tenir à jour pour le même site.
- **Shopify en headless** : il faudrait recoder le panier, le paiement et les commandes.
- **Aperçu rendu par le serveur** : pas encore de serveur ; l'aperçu reste dans le navigateur.

## Conséquences
- L'aperçu du navigateur peut différer un peu du fichier imprimé (lissage, coupure des lignes) :
  le serveur doit rendre avec les mêmes gabarits et les mêmes polices ⚠️ écart à mesurer sur l'échantillon.
- Le dépôt git remplace les sauvegardes en `.zip`.
- Bannière cookies, bouton de rétractation et mentions légales : dans le thème (décision Juridique).

## Concerne
[[OVR - Boutique NolaPrint]] · [[MOD - Thème Shopify]] · décisions 01, 02, Personnalisation, Juridique
