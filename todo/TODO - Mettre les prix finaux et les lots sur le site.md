---
type: todo
title: TODO - Mettre les prix finaux et les lots sur le site
status: à faire
priority: haute
decision: "[[09 - Établissement des nouveaux prix, alignés sur Cadeau Plus sans faux prix barrés]]"
created: 2026-10-31
related: ["[[12 - Lots de 3 à environ moins 10 %, lot un de chaque sans remise]]", "[[MOD - Thème Shopify]]", "[[FLOW - Importer les produits par CSV]]", "[[MOD - Pages légales et rétractation]]"]
decisions: ["[[09 - Établissement des nouveaux prix, alignés sur Cadeau Plus sans faux prix barrés]]", "[[12 - Lots de 3 à environ moins 10 %, lot un de chaque sans remise]]", "[[11 - Texte facultatif à 1 €, frais de retour à la charge du client, retours chez Sylvain]]"]
last-verified: 2026-10-31
tags: [dropshipping, boutique, prix, todo]
---
# TODO - Mettre les prix finaux et les lots sur le site

## Pourquoi
Les prix de la décision 09 sont validés par Sylvain le 31/10/2026 ; les lots de la décision 12 sont
choisis le même jour. Le site doit les afficher avant le lancement de Noël.

## Ce qu'il faut faire
1. **Prix à l'unité** (décision 09) :
   | | Mug | Boule | Bois |
   |---|---|---|---|
   | Notre illustration, sans texte | 18,45 € | 19,95 € | 17,95 € |
   | + texte | + 1 € | + 1 € | + 1 € |
   | Page blanche | + 2 € | + 2 € | + 2 € |
2. **Lots** (décision 12) : 3 mugs 49,95 € · 3 boules 53,95 € · 3 bois 48,45 € · un de chaque
   56,35 € ; illustration, forme et texte au choix par article ; options non remisées.
3. **Livraison** : 4,90 € par commande, offerte dès 60 € de marchandises.
4. **Aucun prix barré** ; sur les lots : « au lieu de X € à l'unité ».
5. **Mentions** sur fiche et panier : « sans texte : rétractation 14 jours » ; « avec texte ou page
   blanche : pas de rétractation » ; « TVA non applicable, art. 293 B du CGI ».
6. **Maquette** (`LEGAL.livraison()`, constantes `FREE_SHIP`, `SHIP_FR`) puis **Shopify** : option
   « Façon de vendre » (+ 0 / 1 / 2 €), « Forme » pour le bois ; lots en produits ou app de bundles ⚠️ à choisir.
7. Prérequis : Printify facturé en euros (Wallet → Payment details), décision 09.

## Comment prouver
- Panier test : 1 mug sans texte = 18,45 + 4,90 = 23,35 € ; avec texte = 24,35 €.
- Panier test : lot de 3 mugs, 2 textes = 49,95 + 2 + 4,90 = 56,85 €.
- Panier test à 60 € de marchandises : livraison 0 €.

## État
- 2026-10-31 : créée ; prix de la décision 09 validés par Sylvain, lots de la décision 12 en draft.
