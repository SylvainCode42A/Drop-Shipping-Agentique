---
type: todo
title: TODO - Stock maison, bloquer Printify quand le produit est déjà chez nous
status: à faire
priority: basse
decision: "[[12 - Établissement des nouveaux prix, alignés sur Cadeau Plus sans faux prix barrés]]"
created: 2026-10-30
related: ["[[TODO - Choisir les apps de rétractation et de consentement]]", "[[TODO - Choisir l'app de personnalisation Shopify et Printify]]", "[[SYN - Juridique]]", "[[RCH - Retours et remboursements (28-10-2026)]]"]
decisions: ["[[11 - Audience visée et nouvelle offre, parents et grands-parents d'abord, nos designs ou la page blanche]]", "[[12 - Établissement des nouveaux prix, alignés sur Cadeau Plus sans faux prix barrés]]", "[[13 - Offres de lancement, duo de mugs et deux lots mélangés]]"]
last-verified: 2026-10-30
tags: [dropshipping, boutique, printify, automatisation, todo]
---
# TODO - Stock maison, bloquer Printify quand le produit est déjà chez nous

## Pourquoi
Un produit retourné sans défaut (ou une erreur de commande) reste chez nous. Si un client commande
exactement le même article, l'expédier nous-mêmes évite de payer une nouvelle impression à Printify.
Idée de Sylvain le 30/10/2026.

Limite : la correspondance doit être exacte (produit, design, texte, forme), donc elle n'arrivera
presque jamais avec des prénoms ; utile surtout pour les textes génériques (« Maman », « Papy »,
« Joyeux Noël »). Si les CGV excluent la rétractation pour les produits personnalisés (art. L221-28 3°
du Code de la consommation, à faire relire par un juriste), les retours sans défaut seront rares.
Les défauts sont réimprimés gratuitement par Printify sur réclamation avec photos (délai ⚠️ à vérifier).

## Ce qu'il faut faire
1. **Tableau du stock maison** (Google Sheet) : produit, design (`_design`, ex. `d01`), texte (`Texte`),
   forme (variante bois), état, date d'entrée.
2. **Printify ne reçoit rien sans accord** : soit l'app Printify en approbation manuelle des commandes,
   soit le bot crée lui-même les commandes par l'API Printify (création puis envoi en production)
   ⚠️ réglages et endpoints à vérifier dans la doc Printify.
3. **Bot** (petit service Python, webhook Shopify `orders/create`) :
   - correspondance trouvée → ne transmet pas à Printify, envoie un e-mail (commande, contenu exact,
     adresse du client), retire l'objet du tableau ;
   - pas de correspondance → transmet la commande à Printify.
4. **Expédition** : on poste l'objet et on saisit le numéro de suivi dans Shopify (commande marquée
   expédiée, e-mail d'expédition au client).
5. Version simple en attendant le bot : approbation manuelle Printify + coup d'œil au tableau pour les
   commandes à texte générique.

## Comment prouver
- Commande test identique à une ligne du tableau → aucune commande chez Printify, e-mail reçu, ligne
  retirée du tableau.
- Commande test sans correspondance → commande créée chez Printify et envoyée en production.

## État
- 2026-10-30 : créée. À faire quand le volume de commandes le justifie (après le lien Printify).
