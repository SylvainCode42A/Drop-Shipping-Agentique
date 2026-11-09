---
type: decision
title: 03 - Ce que font les agents, ce qu'ils ne font jamais
status: draft
date: 2026-11-09
implemented: non
related: ["[[RCH - Architecture multi-agents et mémoire (25-10-2026)]]", "[[SYN - Système]]", "[[SYN - Juridique]]"]
decisions: ["[[01 - Cible, maman, papa, mamie, papy, nos designs ou sa photo]]", "[[02 - Le mug seul, Standard Mug 11 oz chez Textildruck Europa]]"]
last-verified: 2026-11-09
tags: [dropshipping, systeme, decision]
---
# 03 - Ce que font les agents, ce qu'ils ne font jamais

## Contexte
La boutique est gérée par des agents. Le vendeur reste responsable de ce qui est imprimé, même
si le design vient d'une IA et si Printify l'imprime ([[SYN - Juridique]]).

## Décision

### Ce que font les agents
1. **Chercher ou créer un design** : ils partent de nos motifs ou en génèrent de nouveaux.
2. **Se l'approprier** : un design inspiré d'ailleurs est retravaillé pour devenir le nôtre.
3. **L'intégrer à la boutique** : fiche, variantes, mise en ligne.
4. **Garder, changer ou retirer un motif** selon les statistiques de Shopify (ventes, visites).
Retirer veut dire archiver, jamais supprimer.

### Ce que valide un humain
| Quoi | Validation |
|---|---|
| Designs de la première gamme | un par un, par nous |
| Designs suivants (existants ou générés) | aucune, automatique |
| Commandes, dont celles avec la photo de la cliente | aucune, envoi automatique à Printify |
| Service client | fait par nous ; chaque question et chaque réponse sont notées |

### Ce que les agents ne font jamais
- Engager ou modifier un budget publicitaire.
- Fixer ou changer un prix.
- Modifier un texte juridique (CGV, mentions, politique de retour) ou un délai promis.
- Rembourser, réimprimer ou faire un geste commercial.
- Publier un design qui reprend un dessin, un personnage ou une marque existants : l'agent
  s'inspire d'une idée (une fleur par prénom), jamais d'un dessin. Un contrôle automatique
  (logos, texte, ressemblance) bloque avant publication.
- Tout ce qui n'est pas dans « Ce que font les agents ».

## Alternatives écartées
- **Validation humaine de chaque design, toujours** : freine la boucle, contraire au projet agentique.
- **Paliers d'autonomie (50 décisions, 95 % approuvées)** : inutiles, l'autonomie est totale
  après la première gamme.
- **Agent de service client dès le départ** : aucune réponse notée pour l'entraîner.
- **Journal de traçabilité par design (modèle, prompt, valideur, 5 ans)** : non retenu.

## Conséquences
- Les notes de service client vont dans une note dédiée du vault : base du futur agent.
- Commandes avec photo cliente : un contrôle automatique minimal (résolution) avant envoi ⚠️ à confirmer.
- Stock maison (article déjà chez nous) : la commande ne part pas chez Printify
  ([[TODO - Stock maison, bloquer Printify quand le produit est déjà chez nous]]) ⚠️ à confirmer.

## Concerne
[[SYN - Système]] · [[SYN - Juridique]] · décisions Designs, Prix, Juridique
