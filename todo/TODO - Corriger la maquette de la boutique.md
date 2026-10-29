---
type: todo
title: TODO - Corriger la maquette de la boutique
status: à faire
priority: moyenne
decision: "[[07 - La maquette est le cahier des charges du thème Shopify]]"
created: 2026-10-29
related: ["[[OVR - Boutique NolaPrint]]", "[[MOD - Accueil]]", "[[MOD - Habillage]]", "[[MOD - Panier et commande]]", "[[MOD - Pages légales et rétractation]]", "[[CMP - Panier]]"]
decisions: ["[[07 - La maquette est le cahier des charges du thème Shopify]]"]
last-verified: 2026-10-29
tags: [dropshipping, boutique, todo]
---
# TODO - Corriger la maquette de la boutique

## Pourquoi
La maquette est le cahier des charges du thème Shopify ([[07 - La maquette est le cahier des charges du thème Shopify]]) :
ses défauts seraient recopiés dans le thème. Ils ont été relevés à la lecture du code le 29/10/2026,
en documentant `5-boutique/`.

## Ce qu'il faut faire
Dans `Claude outputs/nolaprint-sans-apercu-en-direct.html`, sans toucher au rendu ordinateur :
1. **Nom** : remplacer « Mésange & Cie » par « NolaPrint » dans le `<title>`, l'`aria-label` du logo,
   le logo et le © du pied de page, les mentions légales ; préfixe `MC-` → `NP-` (commande et exemple de
   rétractation) ; clés `mc_cart` et `mc_consent` → `np_cart` et `np_consent` ([[MOD - Habillage]], [[CMP - Panier]]).
2. **FAQ de l'accueil** : supprimer le lien vide `<a href="#faq"></a>` l.976 ; « Foire au questions » →
   « Foire aux questions » ([[MOD - Accueil]]).
3. **Dates et prix en dur** : tirer « 10 décembre » du bandeau de `NOEL_DEADLINE`, et « 44,90 € » du prix
   du Duo dans `PRODUCTS` ; dans `coDone`, une date limite par pays (France 10/12, BE-LU-DE 04/12)
   ([[MOD - Habillage]], [[MOD - Panier et commande]]).
4. **CSS inutile** : retirer `.live-label`, `.live-dot`, `.tag-perso`, `.news*`, `.perso*`, `.steps*`, `.cover-sprig`.
5. **Panier et commande** : plafond de 20 sur le « + » du tiroir ; fusionner deux lignes identiques
   (même produit, même personnalisation) ; garder la case « cadeau » dans `coData` ; ne pas remettre
   `coData` à zéro quand on change une quantité pendant la commande ([[MOD - Panier et commande]]).

## Comment prouver
- Recherche dans le fichier : 0 occurrence de « Mésange », `MC-`, `mc_`, `#faq"></a>`.
- Captures ordinateur (1366 px) avant et après : identiques, au pixel près hors textes corrigés.
- Captures téléphone (390 px) : identiques hors textes corrigés.
- Test manuel : mug + mug identique → une ligne en quantité 2 ; « + » bloqué à 20 ; changer une quantité
  à l'étape Livraison garde l'adresse ; la case « cadeau » apparaît dans le récapitulatif.
- Bandeau : changer `NOEL_DEADLINE` au 12/12 → le bandeau affiche « 12 décembre ».
- Mise à jour des notes `5-boutique/` touchées (numéros de ligne, cas limites retirés, `last-verified`).

## État
- 2026-10-29 : créée à la fin du niveau `5-boutique/`.
