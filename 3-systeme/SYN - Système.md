---
type: synthese
title: SYN - Système
status: validé
related: ["[[_conventions]]", "[[SYN - Fournisseurs]]", "[[SYN - Acquisition]]", "[[SYN - Juridique]]", "[[SYN - Choix de la niche]]", "[[A VERIFIER - Points à valider, vérifier, tester]]"]
decisions: ["[[03 - Approbation unitaire au lancement, paliers d'autonomie, actions toujours bloquées]]", "[[06 - LangGraph au départ, interface d'images interne avec Nano Banana Pro et Ideogram]]"]
last-verified: 2026-10-25
tags: [dropshipping, systeme, synthese]
---
# SYN - Système

État des connaissances techniques sur le système d'agents : Shopify, génération d'images, décision statistique, architecture et mémoire. Quatre recherches. Les notes MOD, CMP et FLOW de ce dossier s'appuieront sur cette synthèse. Rien n'est décidé ici.

## Ce qu'on sait

### Shopify
- Version stable 2026-10, tout en GraphQL, une mise à jour par trimestre. Cycle produit complet : `productSet` (upsert, envoyer toutes les variantes), `productUpdate` pour le statut, `stagedUploadsCreate` puis `fileCreate` pour les images (attendre `READY`), `metafieldsSet`, `publishablePublish`. Un produit `ACTIVE` non publié n'est visible nulle part ([[RCH - API Shopify pour la boutique agentique (22-10-2026)]]).
- Type d'app : créée dans le Dev Dashboard pour sa propre boutique. Les custom apps de l'admin ne se créent plus depuis le 01/01/2026. Token client credentials valable 24 h si app et boutique sont dans la même organisation ([[RCH - API Shopify pour la boutique agentique (22-10-2026)]]).
- Ventes par produit fiables via `orders` et `shopifyqlQuery` (table `sales`). Aucune métrique officielle de vues ou de conversion par produit : il faut un Web Pixel (`product_viewed`, `product_added_to_cart`) ou GA4 ([[RCH - API Shopify pour la boutique agentique (22-10-2026)]]).
- Sans `read_all_orders`, les commandes de plus de 60 jours sont invisibles sans erreur ; ce scope et `shopifyqlQuery` demandent une approbation de Shopify ([[RCH - API Shopify pour la boutique agentique (22-10-2026)]]).
- Limites : 100 points par seconde en Basic, erreur `THROTTLED` à traiter par backoff, bulk operations hors limite. Webhooks non garantis : vérifier le HMAC, répondre en moins de 5 s, dédupliquer, réconcilier chaque nuit ([[RCH - API Shopify pour la boutique agentique (22-10-2026)]]).
- Conditions API : interdiction d'entraîner un modèle avec les données ; l'inférence seule n'est pas restreinte. Google Merchant Center exige une métadonnée IPTC sur les images IA ([[RCH - API Shopify pour la boutique agentique (22-10-2026)]]).
- Plan Basic suffisant ; boutique de développement gratuite pour tester ([[RCH - API Shopify pour la boutique agentique (22-10-2026)]]).
- Garde-fous proposés : création en `DRAFT`, `productDelete` interdit aux agents, archiver plutôt que supprimer, metafields de traçabilité (`ai.design_id`, `ai.prompt_hash`, `ai.model`, `ai.review_status`), un seul système maître par champ ([[RCH - API Shopify pour la boutique agentique (22-10-2026)]]).

### Génération d'images
- Modèles à API et licence commerciale : FLUX.2 ou FLUX 3, GPT Image, Nano Banana, Ideogram 4.5, Recraft (seul vrai SVG). Midjourney exclu, pas d'API officielle. Pour le texte dans l'image : Nano Banana Pro, GPT Image, Ideogram ([[RCH - Génération d'images pour l'impression (22-10-2026)]]).
- Les licences des poids ouverts se durcissent en 2026. Seul Adobe Firefly offre une indemnisation PI, en contrat entreprise. OpenAI retire des modèles en octobre et décembre 2026 : cacher le fournisseur derrière une interface interne ([[RCH - Génération d'images pour l'impression (22-10-2026)]]).
- Format cible : PNG transparent, sRGB, 150 DPI minimum, 300 pour papier et coques. Aucun générateur ne sort la taille d'impression : agrandissement obligatoire (Real-ESRGAN pour les aplats), détourage (BiRefNet), nettoyage des bords pour éviter les halos ([[RCH - Génération d'images pour l'impression (22-10-2026)]], [[SYN - Fournisseurs]]).
- Mockups : API Printful gratuite mais lente, ou rendu PSD (Dynamic Mockups, SudoMock). Jamais d'édition IA sur la vue du produit vendu ([[RCH - Génération d'images pour l'impression (22-10-2026)]]).
- Contrôle avant publication : vérifications déterministes, OCR du texte, score esthétique en filtre grossier, juge vision-langage calibré, liste noire et détection de logos, déduplication par hachage perceptuel. Printify impose une relecture humaine de tout contenu IA ([[RCH - Génération d'images pour l'impression (22-10-2026)]]).
- Coût estimé : environ 0,12 $ par design publié ([[RCH - Génération d'images pour l'impression (22-10-2026)]]).

### Décision statistique
- Les petits nombres trompent : un produit à 1,4 % fait zéro vente sur 100 visites une fois sur quatre. Une règle « zéro vente après 100 visites » éliminerait un bon produit sur quatre ([[RCH - Méthodes statistiques pour garder ou retirer un produit (25-10-2026)]]).
- Méthode centrale : Beta-Binomial avec prior tiré du catalogue (force bornée entre 50 et 500 visites fictives), décision sur la probabilité que la marge par visite passe sous un seuil, et perte attendue ([[RCH - Méthodes statistiques pour garder ou retirer un produit (25-10-2026)]]).
- Règles de départ : exposition minimale de 300 visites, 14 jours et 4 ventes attendues ; retrait si probabilité sous le seuil d'au moins 90 % deux revues de suite ; garder si au-dessus à 80 % ; revue hebdomadaire à jour fixe ; au plus 10 % de retraits par semaine ; fenêtre de 90 jours ou escompte gamma 0,98 à 0,99 ; pause saisonnière au lieu de retrait ([[RCH - Méthodes statistiques pour garder ou retirer un produit (25-10-2026)]]).
- Visibilité par échantillonnage de Thompson, récompense = taux tiré multiplié par la marge unitaire. Priors par catégorie pour les nouveaux produits ([[RCH - Méthodes statistiques pour garder ou retirer un produit (25-10-2026)]]).
- Pièges : biais de position, sources de trafic, budgets pub inégaux, peeking, comparaisons multiples, biais du survivant, suivi cassé. Décider sur les ventes Shopify, pas sur les conversions des plateformes ([[RCH - Méthodes statistiques pour garder ou retirer un produit (25-10-2026)]], [[SYN - Acquisition]]).
- Les calculs du rapport ont été faits à la main et le pseudo-code n'a pas été exécuté ⚠️ à recalculer avec scipy et à calibrer par simulation ([[RCH - Méthodes statistiques pour garder ou retirer un produit (25-10-2026)]]).

### Architecture
- Colonne vertébrale : une exécution durable qui sauvegarde l'état à chaque étape et reprend après un crash ou une attente humaine. Option principale Temporal avec des agents Pydantic AI ; option légère LangGraph avec checkpointer Postgres et `interrupt()`. Toute action externe doit être idempotente ([[RCH - Architecture multi-agents et mémoire (25-10-2026)]]).
- Agents étroits à rôle séparé ; le script de publication reste du code testé. Project Vend : un agent superviseur du même modèle n'a rien apporté, les procédures imposées ont été le meilleur levier ([[RCH - Architecture multi-agents et mémoire (25-10-2026)]]).
- Les agents ne parlent jamais directement à Shopify : une passerelle unique détient le token, expose des opérations fermées, journalise ; une file d'attente par boutique applique le budget de points et l'idempotence ([[RCH - API Shopify pour la boutique agentique (22-10-2026)]]).
- Fournisseur : file d'attente par endpoint, créations idempotentes, visuels stockés chez soi ([[SYN - Fournisseurs]]).

### Mémoire
- Faits chiffrés en Postgres ; leçons dans Obsidian avec statut, date de revue et lien vers la requête SQL qui les prouve ; agents limités à une boîte de réception ; consolidation périodique qui relance la preuve avant promotion. Un agent ne cite jamais un chiffre lu dans une note sans le recalculer ([[RCH - Architecture multi-agents et mémoire (25-10-2026)]]). C'est le modèle retenu dans [[_conventions]], section 6.
- Mem0, Letta et Zep visent la mémoire conversationnelle : inutiles au départ. Markdown source de vérité, index reconstructible, versionnement git ([[RCH - Architecture multi-agents et mémoire (25-10-2026)]]).

### Validation humaine et supervision
- Démarrer en mode fantôme, puis monter l'autonomie par type d'action et par paliers : approbation unitaire, par lot, revue après coup. Critère estimé de passage : 50 décisions, 95 % approuvées sans modification, zéro incident PI ([[RCH - Architecture multi-agents et mémoire (25-10-2026)]]).
- Toujours bloqués : budget publicitaire, prix sous le plancher de marge, designs signalés PI, nouvelle catégorie, textes juridiques et promesses de délai, remboursements ([[RCH - Architecture multi-agents et mémoire (25-10-2026)]]).
- Traces OpenTelemetry GenAI vers Langfuse ou Phoenix, coût par exécution avec coupe-circuit, jeu de cas rejoué à chaque changement de prompt, juge LLM recalibré chaque mois, métriques business par design ([[RCH - Architecture multi-agents et mémoire (25-10-2026)]]).

### Sources de tendances
- Shopify est la source de vérité des ventes. Google Trends API en alpha sur candidature, pytrends à éviter, Pinterest Trends API officielle ⚠️ accès à vérifier, Amazon et Reddit peu utiles, calendriers d'événements en table SQL ([[RCH - Architecture multi-agents et mémoire (25-10-2026)]]).
- Cadre UE : exception de fouille sauf opposition lisible par machine, droit des bases de données, conditions d'utilisation opposables, RGPD. Collecter des agrégats, jamais de profils ([[RCH - Architecture multi-agents et mémoire (25-10-2026)]]).

### Retours d'expérience
- Project Vend : agent complaisant poussé aux remises. Automaton : un agent autonome a rapporté 0 $ en un mois. Les agents réduisent le coût d'exécution, pas le coût d'avoir raison sur la demande. Les suspensions POD viennent des marques et personnages, pas de l'usage de l'IA ([[RCH - Architecture multi-agents et mémoire (25-10-2026)]]).

### Contradictions non tranchées
- Plafond de variantes Shopify : 500 000 puis 10 000 par jour (doc actuelle) contre 50 000 puis 1 000 (sources 2025). Retries des webhooks : 8 sur 4 h ou 19 sur 48 h.
- Benchmarks de mémoire : chiffres fournisseurs (Mem0 92,5 %) contre test indépendant (Letta 52 %, Mem0 50 %).
- Fenêtre d'observation : 14 jours (Shopify et statistiques), 30 jours « sans vente » (architecture).
- Débit des mockups Printful : 2 à 10 par minute selon la doc, selon l'ancienneté de la boutique selon un tiers.

## Ce qui est décidé
- Approbation unitaire de chaque design et fiche au lancement, analyste en proposition seulement, service client humain et documenté, paliers d'autonomie par type d'action (unitaire, lot, après coup ; 50 décisions, 95 %, zéro incident PI), liste des actions toujours bloquées dont `productDelete` ([[03 - Approbation unitaire au lancement, paliers d'autonomie, actions toujours bloquées]]).
- Deux choix de structure sont fixés dans [[_conventions]] : faits en base, leçons dans Obsidian, agents limités à `propositions/`, l'humain tranche.
- Orchestration LangGraph au départ (checkpointer Postgres, `interrupt()`), étapes idempotentes pour garder Temporal possible ; interface d'images interne avec Nano Banana Pro par défaut et Ideogram en second, choix par A/B sur Noël ([[06 - LangGraph au départ, interface d'images interne avec Nano Banana Pro et Ideogram]]).

Décisions attendues :
- le suivi des vues produit (Web Pixel ou GA4) ;
- les seuils de décision de l'analyste, après simulation.

## Questions ouvertes
- La boutique appartient-elle à l'organisation Shopify d'Antoine ? Sinon le client credentials grant est impossible.
- `sales` permet-il de regrouper par identifiant produit ? Une métrique de vues par produit existe-t-elle en 2026-10 ?
- Délai d'obtention de `read_all_orders` et de l'accès de niveau 2.
- Quel modèle d'images donne le meilleur coût par design vendu (test A/B à faire) ? Taux d'erreur réel du juge sur les personnages protégés.
- Accès à l'alpha Google Trends et à Pinterest Trends.
- Taille d'échantillon minimale pour valider une leçon dans une petite boutique.
- Branche maintenue de Pydantic AI (v1 ou v2) ⚠️ à vérifier.
- Le fournisseur de LLM garantit-il par contrat l'absence d'entraînement ?

## Recherches
- [[RCH - API Shopify pour la boutique agentique (22-10-2026)]]
- [[RCH - Génération d'images pour l'impression (22-10-2026)]]
- [[RCH - Méthodes statistiques pour garder ou retirer un produit (25-10-2026)]]
- [[RCH - Architecture multi-agents et mémoire (25-10-2026)]]
