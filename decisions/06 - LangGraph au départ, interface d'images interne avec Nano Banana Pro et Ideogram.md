---
type: decision
title: 06 - LangGraph au départ, interface d'images interne avec Nano Banana Pro et Ideogram
status: validé
date: 2026-10-25
implemented: non
related: ["[[OVR - Drop shipping agentique]]", "[[SYN - Système]]", "[[SYN - Fournisseurs]]", "[[03 - Approbation unitaire au lancement, paliers d'autonomie, actions toujours bloquées]]", "[[05 - Printify en principal avec partenaire UE figé, Gelato en second, franchise de TVA au départ]]"]
decisions: ["[[03 - Approbation unitaire au lancement, paliers d'autonomie, actions toujours bloquées]]", "[[04 - Noël 2026 en test manuel réduit, Fête des grands-mères 2027 pour le système]]", "[[05 - Printify en principal avec partenaire UE figé, Gelato en second, franchise de TVA au départ]]"]
last-verified: 2026-10-25
tags: [dropshipping, systeme, decision]
---
# 06 - LangGraph au départ, interface d'images interne avec Nano Banana Pro et Ideogram

## Contexte
Sixième décision attendue par [[OVR - Drop shipping agentique]]. La recherche architecture retient une
exécution durable qui sauvegarde l'état à chaque étape et reprend après un crash ou une attente humaine,
avec deux options : Temporal et des agents Pydantic AI, ou LangGraph avec checkpointer Postgres et
`interrupt()` ([[RCH - Architecture multi-agents et mémoire (25-10-2026)]]). Pour les images, les modèles
à API et licence commerciale sont FLUX, GPT Image, Nano Banana, Ideogram et Recraft ; pour le texte dans
l'image, Nano Banana Pro, GPT Image et Ideogram ; OpenAI retire des modèles en octobre et décembre 2026,
d'où une interface interne qui cache le fournisseur. Coût estimé 0,12 $ par design publié
([[RCH - Génération d'images pour l'impression (22-10-2026)]], [[SYN - Système]]).
Le premier test du système est la Fête des grands-mères 2027, une boutique, un développeur ([[04 - Noël 2026 en test manuel réduit, Fête des grands-mères 2027 pour le système]]).

## Décision
**Orchestration : LangGraph au départ**, checkpointer Postgres, `interrupt()` pour chaque attente de
validation humaine (décision 03). Pas de serveur d'orchestration à exploiter en mars 2027.

Conditions pour garder Temporal possible :
- chaque étape du pipeline est une fonction idempotente, avec son état en Postgres ;
- le graphe enchaîne les étapes et ne porte aucune logique métier ;
- le script de publication (Shopify, Printify) reste du code testé, hors du graphe ;
- une passerelle unique détient les jetons Shopify et Printify et expose des opérations fermées.
Passage à Temporal quand le volume ou le nombre de boutiques le justifie, sans réécriture des étapes.

**Images : une interface interne** (génération, agrandissement, détourage, nettoyage des bords, sortie PNG
sRGB 300 DPI à la taille de la zone Printify), derrière laquelle deux fournisseurs sont branchés dès le départ :
- **Nano Banana Pro** par défaut, pour les prénoms et textes dans l'image ;
- **Ideogram** en second.
Le choix final se fait par test A/B sur les designs de Noël 2026 (coût par design vendu), puis à chaque
revue mensuelle. Tout fournisseur est remplaçable sans toucher aux agents.

## Alternatives écartées
- **Temporal dès le départ** : plus solide sur les retries, les délais longs et les gros volumes, mais
  un serveur, des workers et un modèle à apprendre, pour un volume de quelques dizaines de workflows par
  semaine en mars. Temps pris sur Noël.
- **Un seul modèle d'images** : les retraits et changements de licence de 2026 rendent la dépendance
  à un fournisseur trop risquée.
- **GPT Image par défaut** : qualité sur le texte reconnue, mais retraits de modèles annoncés chez OpenAI.
- **Midjourney** : pas d'API officielle. **Recraft** : utile en SVG, pas prioritaire pour le mug.
- **Mem0, Letta, Zep** pour la mémoire : mémoire conversationnelle, inutile ici ; le modèle Markdown
  plus Postgres de [[_conventions]] est conservé.

## Conséquences
- Stack du système : Python, LangGraph, Postgres, passerelles Shopify et Printify, interface d'images.
  Pydantic AI possible pour les agents ⚠️ branche maintenue à vérifier.
- Le schéma de données porte, par design : modèle utilisé, prompt haché, version de l'interface d'images,
  statut de revue (metafields `ai.*` sur Shopify, décision 03).
- Contrôle avant publication dans l'interface d'images : vérifications déterministes, OCR du texte,
  liste noire et détection de logos, déduplication par hachage perceptuel.
- Observabilité dès le départ : traces vers Langfuse ou Phoenix, coût par exécution avec coupe-circuit.
- Les notes MOD, CMP et FLOW de `3-systeme/` se fondent sur cette décision.
- À inscrire dans A VERIFIER : branche Pydantic AI ; conditions commerciales de Nano Banana Pro et
  Ideogram au moment du test ; taux d'erreur du juge sur les personnages protégés.

## Concerne
[[SYN - Système]] · [[SYN - Fournisseurs]] · notes MOD, CMP, FLOW à venir.
