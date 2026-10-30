---
type: todo
title: TODO - Brancher le suivi des visiteurs
status: à faire
priority: haute
decision: ""
created: 2026-10-30
related: ["[[MOD - Cookies et consentement]]", "[[TODO - Choisir les apps de rétractation et de consentement]]", "[[RCH - Canaux d'acquisition (22-10-2026)]]", "[[SYN - Acquisition]]", "[[MOD - Thème Shopify]]"]
decisions: ["[[04 - Noël 2026 en test manuel réduit, Fête des grands-mères 2027 pour le système]]"]
last-verified: 2026-10-30
tags: [dropshipping, boutique, acquisition, todo]
---
# TODO - Brancher le suivi des visiteurs

## Pourquoi
Sans mesure, ni la publicité ni l'agent analyste ne peuvent juger un produit. Le rapport d'acquisition
place la bannière de consentement, le Consent Mode v2, le pixel Meta et l'API Conversions dans les
semaines 1 et 2 de la préparation. Il dit aussi que l'agent doit juger sur les ventes Shopify, car
les conversions des plateformes sont partielles à cause du refus des cookies
([[RCH - Canaux d'acquisition (22-10-2026)]]).
Au 30/10/2026, rien n'est installé : ce point se remplit au branchement de Meta Ads.

## Ce qu'il faut faire
Pour chaque outil, noter : voie d'installation (app Shopify, Customer Events, code du thème),
identifiant (jamais de clé ni de jeton), date, qui l'a fait, test passé ou non.

| Outil | Rôle | État |
|---|---|---|
| Pixel Meta + API Conversions | mesure des publicités Meta | à faire, au branchement de Meta Ads |
| Pixel TikTok | mesure des publicités TikTok | à faire ⚠️ canal de deuxième phase selon la RCH |
| Google (GA4, Ads, Consent Mode v2) | audience et Google Shopping | à faire |
| Shopify Analytics | ventes de référence pour l'agent | à vérifier : actif par défaut ? |
| Microsoft Clarity | cartes de chaleur, enregistrements de sessions | à faire ⚠️ soumis au consentement ? |
| Événements personnalisés | étapes propres à NolaPrint | à définir |
| Consentement CNIL | bloque tout ce qui précède sans accord | voir [[TODO - Choisir les apps de rétractation et de consentement]] |

Événements à définir au branchement :
- standards : PageView, ViewContent, AddToCart, InitiateCheckout, Purchase ;
- propres à NolaPrint : ⚠️ à décider (par exemple personnalisation commencée, case orthographe cochée).

Décider (note NN) si un choix est tranché, puis mettre à jour [[MOD - Cookies et consentement]].

## Comment prouver
- « Tout refuser » : aucun appel vers Meta, TikTok, Google ni Clarity dans l'onglet réseau.
- « Tout accepter » : chaque pixel se déclenche ; les événements apparaissent dans le gestionnaire
  d'événements de Meta (outil de test) et dans les vues temps réel de Google.
- Un achat test remonte une seule fois Purchase, avec le bon montant.

## État
- 2026-10-30 : créée. Rien n'est installé ; à remplir au branchement de Meta Ads.
