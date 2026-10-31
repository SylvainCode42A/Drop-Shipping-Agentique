---
type: todo
title: TODO - Inscrire les frais de retour et le texte à 1 € dans les CGV
status: en cours
priority: haute
decision: "[[11 - Texte facultatif à 1 €, frais de retour à la charge du client, retours chez Sylvain]]"
created: 2026-10-30
related: ["[[MOD - Pages légales et rétractation]]", "[[RCH - Retours, rétractation et abus (30-10-2026)]]", "[[RCH - Défauts produit, casse et réclamations Printify (31-10-2026)]]", "[[12 - Lots de 3 à environ moins 10 %, lot un de chaque sans remise]]", "[[SYN - Juridique]]", "[[TODO - Choisir les apps de rétractation et de consentement]]"]
decisions: ["[[11 - Texte facultatif à 1 €, frais de retour à la charge du client, retours chez Sylvain]]"]
last-verified: 2026-10-31
tags: [dropshipping, boutique, juridique, todo]
---
# TODO - Inscrire les frais de retour et le texte à 1 € dans les CGV

## Pourquoi
Sans information du client, les frais de renvoi restent à la charge de la boutique (art. L221-23)
([[RCH - Retours, rétractation et abus (30-10-2026)]]). Et le client doit savoir avant de commander
qu'un article avec texte n'ouvre pas de rétractation.

## Ce qu'il faut faire
1. **CGV, article rétractation** : frais directs de renvoi à la charge du client ; adresse de retour
   (chez Sylvain) ; délai de 14 jours pour renvoyer ; remboursement de la livraison standard de l'aller seulement.
2. **CGV, exclusion** : articles avec texte ou image du client exclus de la rétractation (art. L221-28 3°) ;
   articles de nos designs sans texte rétractables.
3. **Formulaire type** en annexe des CGV : reprendre la version en vigueur depuis le 19/06/2026
   (annexe à l'art. R221-3, décret n° 2026-3).
4. **Option texte à 1 €** : la décrire dans les CGV (prix) et sur la fiche produit.
5. **Commandes anormales** : clause sur les quantités réservées à un usage personnel et le refus des
   commandes anormales ⚠️ à rédiger avec un avocat.
6. **Fiche produit et panier** : mention visible « avec texte : pas de rétractation » avant validation.
7. **Défaut ou casse (articles 6 et 8)** : signalement avec photo et n° de commande, de préférence
   dans les 30 jours après réception (délai Printify) ; réimpression ou remboursement sans renvoi
   du produit ; rappel de la garantie légale de conformité de 2 ans, qui ne peut pas être raccourcie
   ([[RCH - Défauts produit, casse et réclamations Printify (31-10-2026)]]).
8. **Lots (prix)** : 3 mugs 49,95 €, 3 boules 53,95 €, 3 bois 48,45 €, un de chaque 56,35 € ;
   options texte et page blanche par article, non remisées ([[12 - Lots de 3 à environ moins 10 %, lot un de chaque sans remise]]).
9. **Rétractation d'un article d'un lot** : montant remboursé quand un seul article sans texte
   d'un lot remisé est renvoyé ⚠️ à rédiger avec un avocat.
10. **Identité du vendeur** (nom, SIREN, adresse de retour, e-mail, domaine, médiateur) : après la
    création de la micro-entreprise par Sylvain.
11. Mettre à jour `LEGAL.cgv()` et `LEGAL.livraison()` dans [[MOD - Pages légales et rétractation]],
    puis faire relire par un avocat ; formulaire de contact : envoyer réellement la photo.

## Comment prouver
- Les CGV publiées contiennent la phrase sur les frais de renvoi et l'adresse de retour.
- Une commande test avec texte affiche la mention d'exclusion avant le paiement ; sans texte, elle ne l'affiche pas.
- Le prix du mug passe de 18,45 € à 19,45 € quand un texte est saisi (décision 09).

## État
- 2026-10-30 : créée avec la décision 11.
- 2026-10-31 : ajout des points 7 à 10 (défauts et casse, lots, rétractation dans un lot, identité en attente de la micro-entreprise).
- 2026-10-31 : maquette mise à jour (`LEGAL.cgv()` articles 2, 3, 4, 6, 7, 8, 12 et `LEGAL.livraison()`) : points 1, 2, 4, 5,
  7, 8, 9 rédigés ; copie d'avant dans `Claude outputs/nolaprint-sans-apercu-en-direct.avant-cgv-31-10.html`.
  Restent : point 3 (formulaire type, texte en vigueur à copier depuis Légifrance), encadré de
  l'annexe D211-2 à copier mot pour mot, point 6 (fiche et panier, avec la TODO prix), point 10
  (identité, après la micro-entreprise), envoi réel de la photo du formulaire de contact,
  relecture par un avocat. Les zones `todo` jaunes de la maquette marquent chaque manque.
