---
type: research
title: Architecture multi-agents et mémoire pour la boutique agentique
status: validé
related: ["[[_conventions]]", "[[RCH - API Shopify pour la boutique agentique (22-10-2026)]]", "[[RCH - Méthodes statistiques pour garder ou retirer un produit (25-10-2026)]]"]
decisions: []
date: 2026-10-25
sources:
  - https://www.anthropic.com/research/project-vend-2
  - https://simonwillison.net/2025/Jun/27/project-vend/
  - https://temporal.io/blog/announcing-openai-agents-sdk-integration
  - https://temporal.io/blog/temporal-langgraph-plugin-durable-execution
  - https://docs.langchain.com/oss/python/langgraph/interrupts
  - https://pydantic.dev/articles/pydantic-ai-v1
  - https://github.com/pydantic/pydantic-ai/releases
  - https://openai.github.io/openai-agents-python/human_in_the_loop/
  - https://platform.claude.com/docs/en/agent-sdk/hooks
  - https://docs.n8n.io/build/integrate-ai/ai-examples/human-in-the-loop-for-tools
  - https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-version-1-0/
  - https://adk.dev/2.0/
  - https://docs.crewai.com/en/enterprise/introduction
  - https://docs.n8n.io/privacy-and-security/sustainable-use-license
  - https://automem.ai/blog/agent-memory-in-2026-an-honest-comparison-of-mem0-zep-letta-and-the-rest
  - https://effloow.com/articles/mem0-zep-letta-agent-memory-latency-benchmark-2026
  - https://www.morphllm.com/obsidian-mcp-server
  - https://veraexmachina.com/tech/opentelemetry-genai-agent-observability-production/
  - https://clickhouse.com/blog/clickhouse-acquires-langfuse-open-source-llm-observability
  - https://shopify.dev/docs/api/admin-rest/latest/resources/product
  - https://www.risingtrends.co/blog/google-trends-api
  - https://developers.pinterest.com/docs/analytics-and-reports/trends/
  - https://developers.etsy.com/documentation/
  - https://getsquirrel.co/blog/post/7-registering-for-the-amazon-product-advertising-api
  - https://support.reddithelp.com/hc/en-us/articles/42728983564564-Responsible-Builder-Policy
  - https://www.techrepublic.com/article/news-reddit-rss-public-api-shutdown/
  - https://automatonagency.com/insights/autonomous-agent-revenue-experiment-teardown
  - https://www.trendlytic.io/blog/can-you-sell-ai-art-on-redbubble
  - https://www.french-business-law.com/services/protecting-database-rights-in-france
  - https://www.privacyworld.blog/2026/07/regulating-the-irreversible-the-edpbs-web-scraping-guidelines-and-the-limits-of-gdpr-orthodoxy/
  - https://www.shopify.com/news/winter-26-edition-merchant
last-verified: 2026-10-25
tags: [dropshipping, systeme, architecture, agents, memoire]
---
# RCH - Architecture multi-agents et mémoire (25-10-2026)

## Contexte posé
Question : quelles sont les bonnes pratiques en 2026 pour un système multi-agents qui gère une boutique Shopify de produits personnalisés, avec une mémoire Obsidian ?

Prompt de départ, recopié tel quel :

> Contexte : je suis développeur, déjà expérimenté en RAG et en systèmes agentiques. Je construis un système qui gère une boutique Shopify de produits personnalisés avec plusieurs agents : un agent de veille (tendances, saisonnalité, produits qui se vendent), un agent de création de produits, un script de publication, et un agent d'analyse des ventes. Je veux une couche mémoire, probablement Obsidian, pour que le système s'améliore et pour lui fournir de la documentation.
>
> Mission : fais une recherche sur les meilleures pratiques en 2026 pour ce type de système.
> Je veux savoir :
> - les frameworks d'orchestration multi-agents pertinents et leurs compromis ;
> - comment concevoir une mémoire à long terme qui sépare les données factuelles (ventes en base de données) des apprentissages rédigés (notes Markdown dans Obsidian) ;
> - comment intégrer une validation humaine au début, puis la réduire ;
> - comment évaluer et superviser les agents (logs, coûts, qualité, dérives) ;
> - les sources de données de tendances accessibles légalement (Google Trends, calendriers d'événements, données Shopify, etc.) ;
> - des retours d'expérience de systèmes e-commerce automatisés par IA.
>
> Format de sortie : 1) un résumé en 5 lignes, 2) une architecture recommandée décrite composant par composant, 3) un tableau comparatif des outils, 4) les risques et modes de défaillance, 5) les questions ouvertes.

## Conclusion en une phrase
Un flux durable et déterministe qui appelle des agents étroits, avec les faits en SQL, les leçons dans Obsidian reliées à leur preuve, et une autonomie gagnée par paliers mesurés, vaut mieux qu'un essaim d'agents autonomes.

## Résultats

### Orchestration
- La colonne vertébrale doit être une exécution durable : l'état est sauvegardé à chaque étape, et le flux reprend après un crash ou une longue attente humaine.
- Option principale : Temporal, avec des agents écrits en Pydantic AI ou avec l'OpenAI Agents SDK. Les attentes durables de Temporal ne consomment rien pendant l'attente.
- Option légère : LangGraph avec un checkpointer Postgres. `interrupt()` met le graphe en pause sans limite de durée.
- Piège LangGraph : à la reprise, les nœuds après le dernier checkpoint sont rejoués. Toute action externe doit donc être idempotente.
- Le script de publication reste du code testé, pas un agent.
- Project Vend : l'agent « PDG » basé sur le même modèle n'a rien apporté, car il partageait les angles morts de l'agent principal. Un rôle étroit et séparé a mieux fonctionné.
- CrewAI et n8n conviennent au prototypage ou aux notifications, pas au cœur du système.

| Outil | Durabilité | Validation humaine | Maturité (oct. 2026) | Enfermement |
|---|---|---|---|---|
| LangGraph | Checkpointer intégré | `interrupt()` natif | 1.0 depuis le 22/10/2025 | Open source, LangSmith payant |
| Temporal | Référence du marché | Signaux et minuteries | OpenAI Agents SDK en GA le 23/03/2026, plugin LangGraph en préversion | Open source, coût d'exploitation |
| Pydantic AI | Via Temporal, DBOS, Prefect, Restate | Approbation d'outils | v1 le 04/09/2025, v2 annoncée le 23/06/2026 | Open source, multi-fournisseurs |
| OpenAI Agents SDK | Sessions, durable via Temporal | Pause sur outil sensible | Stable | Tracing orienté OpenAI |
| Claude Agent SDK | Sessions | Hooks allow, deny, ask | Renommé le 29/09/2025 | Lié à Claude |
| Microsoft Agent Framework | Checkpointing | Approbations natives | 1.0 GA le 03/04/2026 | MIT, orienté Azure |
| Google ADK | Selon déploiement | Oui | 2.x, Java 1.0 le 30/03/2026 | Orienté Vertex AI |
| CrewAI | Flows avec état | Dans AMP | Stable | Plateforme payante |
| n8n | Exécutions persistées | Approbation d'outils | Mûr | Licence Sustainable Use, non OSI |

### Mémoire
- Les faits chiffrés vivent dans Postgres : commandes, sessions, coûts, expériences.
- Les leçons vivent dans Obsidian, avec un statut, une date de revue et un lien vers la requête SQL qui les prouve.
- Les agents écrivent seulement dans une boîte de réception. Une consolidation périodique relance la preuve avant de promouvoir une note.
- Un agent ne cite jamais un chiffre lu dans une note sans le recalculer en SQL.
- Le modèle des fenêtres de validité de Graphiti (moteur de Zep) inspire la gestion des faits qui changent.
- Mem0, Letta et Zep visent surtout la mémoire conversationnelle d'utilisateurs. Ils ne sont pas nécessaires au départ.
- Accès au coffre : plusieurs serveurs MCP Obsidian existent, dont certains lisent les fichiers sans qu'Obsidian tourne. Le Markdown reste la source de vérité, avec un index reconstructible et un versionnement git.

| Type de mémoire | Où | Qui écrit |
|---|---|---|
| Faits chiffrés | Postgres | Ingestion automatique |
| Épisodique | Table `runs` et notes journal | Agents |
| Sémantique | Notes de leçons | Consolidation seulement |
| Procédurale | Règles, listes de contrôle, prompts versionnés | Humain, ou agent via proposition |

### Validation humaine
- Commencer en mode fantôme : l'agent propose sans exécuter, et on compare ses choix à ceux de l'humain.
- Faire monter l'autonomie par type d'action et par paliers : fantôme, approbation unitaire, approbation par lot, exécution avec revue après coup.
- Le score de confiance du LLM seul n'est pas un critère fiable. Il doit être calibré contre les décisions humaines.
- Restent toujours bloqués : budget publicitaire, prix sous le plancher de marge et remises, designs signalés pour propriété intellectuelle, nouvelle catégorie de produit, textes juridiques et promesses de délai, remboursements.
- Project Vend : imposer des procédures de vérification (coûts, délais) a été le levier le plus efficace. Même en phase 2, l'agent n'avait pas d'accès direct au paiement.

### Supervision et évaluation
- Tracer avec les conventions sémantiques OpenTelemetry GenAI, vers Langfuse auto-hébergé ou Arize Phoenix.
- Suivre le coût par span, avec un budget par exécution et un coupe-circuit.
- Trois niveaux d'évaluation : jeu de cas rejoué à chaque changement de prompt ou de modèle ; juge LLM recalibré chaque mois contre les étiquettes d'Antoine ; métriques business par design.
- Métriques business : conversion par fiche, délai jusqu'à la première vente, part de designs sans vente, revenu par design publié, taux de remboursement, taux de retrait pour propriété intellectuelle.
- Dérive : comparer chaque semaine à une fenêtre de référence, y compris l'accord du juge et la diversité des styles générés.

### Sources de tendances
| Source | Statut | Usage |
|---|---|---|
| Shopify Admin GraphQL et ShopifyQL | Officiel, `shopifyqlQuery` depuis 2026-01 | Source de vérité des ventes |
| Google Trends API | Alpha sur candidature depuis le 24/07/2025 | Candidater |
| pytrends | Non officiel, erreurs 429 fréquentes | À éviter en production |
| Pinterest Trends API | Officiel | Très adapté au POD ⚠️ à vérifier : accès possiblement réservé |
| TikTok Creative Center | Pas d'API commerciale | Consultation manuelle |
| Etsy Open API v3 | Limitée à sa propre boutique | Ses propres données seulement |
| Amazon | PA-API retirée le 15/05/2026, Creators API sous condition | Peu utile |
| Reddit | Usage commercial sur contrat, API publique fermée en mars 2027 | Ne pas en dépendre |
| Calendriers d'événements | Données publiques | Table SQL de saisonnalité |

Cadre UE et France : exception de fouille de textes et de données commerciale (directive 2019/790 art. 4, CPI L122-5-3) sauf opposition lisible par machine ; droit sui generis des bases (directive 96/9 art. 7, CPI L342-3) ; conditions d'utilisation opposables comme contrat ; RGPD dès qu'une donnée personnelle est collectée. Collecter des agrégats, jamais de profils.

### Retours d'expérience
- Project Vend (Anthropic) : agent complaisant, poussé à multiplier les remises ; les procédures imposées ont été le meilleur levier ; un agent superviseur du même modèle n'a pas aidé.
- Automaton : un agent autonome avec budget et produit pendant un mois a rapporté 0 dollar. Les agents réduisent le coût d'exécution, pas le coût d'avoir raison sur la demande.
- POD : les suspensions viennent presque toujours des marques, personnages et droits à l'image, pas de l'usage de l'IA.
- Commerce agentique Shopify (Winter '26, Agentic Storefronts) : canal à activer, mais conversion dans le chat encore faible selon Walmart.

## Chiffres

### Sourcés
- LangGraph 1.0 : 22/10/2025. Source : changelog LangChain.
- Intégration OpenAI Agents SDK et Temporal en GA : 23/03/2026. Plugin LangGraph de Temporal en préversion depuis le 16/07/2026. Source : blog Temporal.
- Microsoft Agent Framework 1.0 GA : 03/04/2026. Source : devblogs Microsoft.
- Pydantic AI v1 : 04/09/2025 ; v2 annoncée le 23/06/2026. Source : pydantic.dev, GitHub.
- Langfuse racheté par ClickHouse le 16/01/2026, cœur sous licence MIT. Source : clickhouse.com.
- Conventions OpenTelemetry GenAI 1.42.0 : 12/06/2026, statut « Development ». Source : veraexmachina.com.
- Mem0 : 92,5 % sur LoCoMo et 94,4 % sur LongMemEval. Source : fournisseur.
- Zep : 90,2 % sur LongMemEval. Source : fournisseur.
- Test indépendant sur 419 tours : Letta 52,2 %, Mem0 50,0 %, Zep/Graphiti 37,0 %. Source : Effloow.
- API REST Admin Shopify « legacy » depuis le 01/10/2024 ; nouvelles apps publiques en GraphQL seul depuis le 01/04/2025. Source : shopify.dev.
- Amazon PA-API 5 retirée le 15/05/2026 ; Creators API soumise à 10 ventes affiliées sur 30 jours. Source : getsquirrel.co.
- Reddit : plus de nouvelles demandes d'accès après le 31/10/2026, API publique fermée en mars 2027. Source : Reddit Help, TechRepublic.
- Google Trends API alpha : depuis le 24/07/2025, fenêtre de 1 800 jours. Source : risingtrends.co.
- Project Vend : le « PDG » a refusé plus de cent demandes indulgentes mais en a autorisé environ huit fois plus. Source : Anthropic, 18/12/2025.
- SunFrog : 19,2 millions de dollars de dommages-intérêts le 12/04/2018. Source : World IP Review.
- Hells Angels contre Redbubble : 78 250 dollars australiens en 2022, réduits à 100 dollars en appel le 23/02/2024. Source : décisions de la Cour fédérale d'Australie.
- Shopify Winter '26 : 10/12/2025, plus de 150 mises à jour. Source : shopify.com.
- Walmart : conversion dans le chat trois fois plus faible que sur Walmart.com, environ 200 000 produits proposés. Source : WIRED, 18/03/2026.
- Gambit Security : coût moyen de 25,46 dollars par cible, au moins 27 entreprises compromises du 10 au 15/09/2026. ⚠️ à vérifier : source primaire non relue.

### Estimés
- Critère de passage de palier : au moins 50 décisions, au moins 95 % approuvées sans modification, zéro incident de propriété intellectuelle. Estimé : proposition de conception, pas une norme publiée.
- Seuil « sans vente » à 30 jours pour juger un design. Estimé.
- Consolidation de la mémoire chaque semaine, recalibrage du juge LLM chaque mois. Estimé.

## Caveats
- Les benchmarks de mémoire se contredisent entre chiffres fournisseurs et test indépendant. La contradiction est listée, pas tranchée.
- L'accès à l'API Pinterest Trends pour un compte standard n'est pas confirmé. ⚠️ à vérifier
- La réduction du paiement intégré d'OpenAI (Instant Checkout) en mars 2026 vient de sources secondaires. ⚠️ à vérifier
- Pydantic AI : une v2 annoncée coexiste avec des versions 1.107 publiées en octobre 2026. La branche maintenue reste à confirmer. ⚠️ à vérifier
- Les conventions OpenTelemetry GenAI peuvent encore renommer des attributs avant leur 1.0.
- Le cadre juridique est un résumé, pas un avis de juriste. La responsabilité en cas de contrefaçon publiée automatiquement reste à faire valider.
- Questions ouvertes du rapport : accès à l'alpha Google Trends ; choix du fournisseur POD, qui fixe la marge plancher ; taille d'échantillon minimale pour valider une leçon dans une petite boutique ; part du travail à déléguer à Sidekick.

## Retenu / écarté

