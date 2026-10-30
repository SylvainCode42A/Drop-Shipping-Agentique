---
type: decision
title: 03 - Approbation unitaire au lancement, paliers d'autonomie, actions toujours bloquées
status: validé
date: 2026-10-25
implemented: non
related: ["[[OVR - Drop shipping agentique]]", "[[SYN - Système]]", "[[SYN - Juridique]]", "[[02 - Mug famille illustrée à 24,90 €, panier cible 45 €]]"]
decisions: ["[[02 - Mug famille illustrée à 24,90 €, panier cible 45 €]]", "[[04 - Noël 2026 en test manuel réduit, Fête des grands-mères 2027 pour le système]]", "[[06 - LangGraph au départ, interface d'images interne avec Nano Banana Pro et Ideogram]]"]
last-verified: 2026-10-25
tags: [dropshipping, systeme, juridique, decision]
---
# 03 - Approbation unitaire au lancement, paliers d'autonomie, actions toujours bloquées

## Contexte
Troisième décision attendue par [[OVR - Drop shipping agentique]]. Le vendeur est responsable de la
contrefaçon même si le design vient d'une IA et si un tiers imprime ; les suspensions POD viennent des
marques et des personnages, pas de l'usage de l'IA ; Printify impose une relecture humaine de tout contenu
IA ([[SYN - Juridique]], [[SYN - Système]]). La recherche architecture propose de démarrer en mode
fantôme puis de monter l'autonomie par paliers et par type d'action, et constate qu'un agent superviseur
n'apporte rien, contrairement aux procédures imposées ([[RCH - Architecture multi-agents et mémoire (25-10-2026)]]).

## Décision
**Au lancement : approbation unitaire.** L'humain valide nominativement chaque design et chaque fiche
produit avant publication. L'analyste écrit seulement dans `propositions/` ; aucun produit n'est retiré
ni mis en pause sans ok humain. Le script de publication ne publie que ce qui porte un statut validé.

**Service client : humain au lancement, pas d'agent.** Chaque question et chaque réponse sont
documentées (type de demande, réponse donnée, résultat). Un agent de service client sera construit
ensuite sur ce corpus, en commençant au palier « agent rédige, humain valide ».

**Paliers d'autonomie, par type d'action, dans cet ordre :**
1. approbation unitaire ;
2. approbation par lot ;
3. revue après coup.
Passage au palier suivant quand, pour ce type d'action : 50 décisions, 95 % approuvées sans
modification, zéro incident PI (critère estimé, à réviser).

**Actions toujours bloquées, à tout palier, sans exception par un agent :**
- engager ou modifier un budget publicitaire ;
- fixer un prix sous le plancher de marge ;
- publier un design signalé par le contrôle PI (OCR, liste noire, détection de logos, TMview) ;
- ouvrir une nouvelle catégorie de produit ou un nouvel angle ;
- rédiger ou modifier un texte juridique (CGV, mentions, politique de retour) ou une promesse de délai ;
- accorder un remboursement, une réimpression ou un geste commercial ;
- supprimer un produit sur Shopify (`productDelete`) : archiver seulement ;
- écrire hors de `propositions/` dans `4-memoire-agents/`.

## Alternatives écartées
- **Mode fantôme pur** (les agents tournent, rien n'est publié) : utile pour calibrer, mais le test
  de Noël a besoin de produits en ligne. L'approbation unitaire joue le même rôle avec de vraies ventes.
- **Agent superviseur** qui valide à la place de l'humain : Project Vend montre qu'un superviseur du
  même modèle n'apporte rien ; la responsabilité juridique reste au vendeur.
- **Agent de service client dès le lancement** : aucun corpus de réponses, risque qu'il promette un
  remboursement non couvert ou refuse une rétractation légale ([[SYN - Modèle économique]]).

## Conséquences
- Le schéma de données porte un statut de revue par design et par produit, et le nom du valideur.
  Metafields de traçabilité sur Shopify : `ai.design_id`, `ai.prompt_hash`, `ai.model`, `ai.review_status`.
- La passerelle Shopify n'expose pas `productDelete` ; création en `DRAFT`.
- Les garde-fous juridiques deviennent des notes REGLE : termes interdits, thèmes âgistes exclus,
  marques connues (Disney, Obut, logos de clubs), journal de chaque design conservé 5 ans.
- Les réponses du service client sont documentées dans une note dédiée du vault, source du futur agent.
- La charge humaine au lancement est connue : chaque design, chaque fiche, chaque message client.
  Elle borne le nombre de produits du test de Noël (décision 4).

## Concerne
[[SYN - Système]] · [[SYN - Juridique]] · [[SYN - Modèle économique]] · notes MOD et REGLE à venir · décision 4.
