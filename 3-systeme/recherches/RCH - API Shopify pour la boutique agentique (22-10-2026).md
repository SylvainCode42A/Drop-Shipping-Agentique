---
type: research
title: API Shopify pour la boutique agentique
status: validé
related: ["[[_conventions]]"]
decisions: []
date: 2026-10-22
sources:
  - https://shopify.dev/changelog/release-notes/2026-10
  - https://shopify.dev/docs/api/usage/versioning
  - https://shopify.dev/docs/apps/build/apis/graphql-admin/rate-limits
  - https://shopify.dev/docs/api/admin-graphql/latest/mutations/productSet
  - https://shopify.dev/docs/apps/build/product-merchandising/products-and-collections/sync-data
  - https://shopify.dev/docs/api/admin-graphql/latest/mutations/productcreatemedia
  - https://shopify.dev/docs/apps/build/online-store/product-media
  - https://shopify.dev/docs/api/admin-graphql/latest/queries/shopifyqlQuery
  - https://shopify.dev/docs/api/shopifyql/latest/schemas/sessions_and_behavior/sessions
  - https://shopify.dev/changelog/apps-now-need-shopify-approval-to-read-orders-older-than-60-days
  - https://shopify.dev/docs/apps/build/webhooks/troubleshooting-webhooks
  - https://changelog.shopify.com/posts/legacy-custom-apps-can-t-be-created-after-january-1-2026
  - https://www.shopify.com/legal/api-terms
  - https://www.shopify.com/legal/terms
  - https://support.google.com/merchants/answer/14743464
  - https://help.printify.com/hc/en-us/articles/4483630521105
  - https://help.printful.com/hc/en-us/articles/21033550791708
last-verified: 2026-10-22
tags: [dropshipping, systeme, shopify, api]
---
# RCH - API Shopify pour la boutique agentique (22-10-2026)

## Contexte posé
Question : que permet Shopify, à jour en 2026, pour une boutique de produits personnalisés gérée par des agents IA ?

Prompt de départ, recopié tel quel :

> Contexte : je suis développeur et je construis un système d'agents IA qui gère une boutique Shopify de produits personnalisés : création automatique de produits, publication, puis analyse des ventes pour retirer ou remplacer les produits.
>
> Mission : fais une recherche technique sur ce que permet Shopify pour ce cas d'usage, à jour en 2026.
> Je veux savoir :
> - comment créer, modifier, publier et archiver des produits via l'API Admin (GraphQL de préférence), avec variantes, images et métadonnées (metafields) ;
> - comment récupérer les données de ventes, de trafic et de conversion par produit ;
> - les limites d'appels (rate limits) et les bonnes pratiques ;
> - le type d'application à créer (custom app, app privée, etc.) et les autorisations nécessaires ;
> - ce que disent les conditions d'utilisation de Shopify sur l'automatisation et le contenu généré par IA ;
> - le plan Shopify minimum nécessaire pour accéder à ces fonctions.
>
> Format de sortie : un document technique avec 1) un résumé en 5 lignes, 2) les endpoints ou mutations clés avec des liens vers la documentation officielle, 3) les limites et pièges, 4) une architecture d'intégration recommandée, 5) les questions ouvertes.

## Conclusion en une phrase
Tout le cycle produit est automatisable avec la GraphQL Admin API 2026-10, à condition de créer l'app dans le Dev Dashboard, et la conversion par produit doit être complétée par un Web Pixel ou GA4.

## Résultats

### Version d'API
- La version stable la plus récente est 2026-10. La REST Admin API est « legacy », donc tout se fait en GraphQL.
- Une nouvelle version sort chaque trimestre. Il faut prévoir une mise à jour par trimestre.
- `productCreateMedia` est déprécié. Il faut passer par `productUpdate` ou `productSet`.
- Depuis 2026-10, un filtre de metafield invalide dans `products` renvoie une erreur au lieu d'être ignoré.

### Cycle de vie des produits
| Besoin | Mutation ou requête | Scope |
|---|---|---|
| Créer ou mettre à jour un produit complet sans doublon | `productSet` | `write_products` |
| Créer un produit simple | `productCreate` | `write_products` |
| Changer le statut (`ACTIVE`, `DRAFT`, `ARCHIVED`) | `productUpdate` | `write_products` |
| Variantes en lot | `productVariantsBulkCreate`, `productVariantsBulkUpdate` | `write_products` |
| Supprimer définitivement | `productDelete` | `write_products` |
| Images | `stagedUploadsCreate` puis `fileCreate`, puis association par `productUpdate` ou `productSet` | `write_files` |
| Métadonnées | `metafieldsSet`, `metafieldDefinitionCreate` | `write_products` |
| Publication sur les canaux | `publications`, `publishablePublish`, `publishableUnpublish` | `write_publications` |
| Traitements en masse | `bulkOperationRunQuery`, `bulkOperationRunMutation` | selon la ressource |

- `productSet` est un upsert : il crée l'objet s'il n'existe pas et le met à jour sinon. Les variantes absentes de l'entrée sont supprimées, donc il faut toujours envoyer la liste complète.
- Le traitement des images est asynchrone. Il faut attendre `fileStatus: READY` avant de publier.
- Un produit `ACTIVE` mais non publié n'est visible nulle part. Il faut le statut et la publication.
- Le rapport recommande d'archiver plutôt que supprimer, car `productDelete` est irréversible.
- Le rapport propose des metafields de traçabilité : `ai.design_id`, `ai.prompt_hash`, `ai.generation_date`, `ai.model`, `ai.review_status`, `ai.pod_provider`.

### Ventes, trafic et conversion
- Les ventes par produit sont fiables via `orders` avec `lineItems`, et via `shopifyqlQuery` sur la table `sales`.
- ShopifyQL est le langage analytique de Shopify, proche de SQL. Il est revenu dans l'Admin API en 2025-10 sous la forme de `shopifyqlQuery`.
- La table `sessions` donne surtout des métriques de boutique : sessions, pages vues, ajouts au panier, taux de conversion.
- Aucune métrique officielle « vues par produit » ou « conversion par produit » n'a été trouvée dans la documentation 2026. ⚠️ à vérifier
- Approximation possible : sessions par `landing_page_path` des pages produit.
- Les vues produit brutes ne sont pas lisibles par l'Admin API. Il faut les capter avec un Web Pixel (événements `product_viewed`, `product_added_to_cart`) ou GA4.
- Sans `read_all_orders`, les commandes de plus de 60 jours sont invisibles, sans message d'erreur. Ce scope demande une approbation de Shopify.
- `shopifyqlQuery` exige `read_reports` et un accès de niveau 2 aux données clients protégées, même pour un simple agrégat.

### Limites d'appels et bonnes pratiques
- Le modèle est un « leaky bucket » : un seau de points se remplit en continu pour chaque couple app et boutique.
- Une requête coûte des points : 1 par objet, 10 par mutation, et la taille des connexions compte.
- La réponse contient `extensions.cost.throttleStatus`. Le dépassement renvoie l'erreur `THROTTLED`, à traiter par backoff exponentiel.
- Les bulk operations ne sont pas soumises aux rate limits des requêtes simples.
- Webhooks : vérifier la signature `X-Shopify-Hmac-SHA256`, répondre en moins de 5 secondes, dédupliquer avec `X-Shopify-Webhook-Id`.
- Les webhooks ne sont pas garantis. Le rapport recommande une réconciliation nocturne avec `orders` sur `updated_at`.
- La pagination se fait par curseur (`first`, `after`, `pageInfo`).

### Type d'application et authentification
| Type | Statut en 2026 | Adapté au projet |
|---|---|---|
| App privée | Dépréciée | Non |
| Custom app créée dans l'admin | Création impossible depuis le 1er janvier 2026 | Seulement si elle existe déjà |
| App Dev Dashboard pour sa propre boutique | Méthode recommandée | Oui |
| Custom app d'un partenaire pour un client | Active, OAuth | Oui si la boutique appartient à un client |
| App publique | Active, GraphQL obligatoire | Non |

- Client credentials grant : le token expire après 24 heures. Il ne marche que si l'app et la boutique sont dans la même organisation Shopify.
- Authorization code grant : OAuth classique, token offline qui n'expire pas tant que l'app reste installée (source : forum Shopify).
- Les tokens offline expirants deviendront obligatoires pour les apps publiques au 1er janvier 2027. Les custom apps et les apps Dev Dashboard du marchand sont exclues.
- L'app connecteur de la Shopify CLI ne peut pas demander `read_all_orders` (source : forum Shopify, avril 2026).

Scopes listés par le rapport : `read_products`, `write_products`, `read_files`, `write_files`, `read_publications`, `write_publications`, `read_inventory`, `write_inventory`, `read_orders`, `read_all_orders`, `read_reports`, `read_metaobjects`, `write_metaobjects`, `write_metaobject_definitions`, `write_pixels`, `read_customer_events`.

### Outils agentiques Shopify (MCP)
- Dev MCP et Shopify AI Toolkit : donnent à un assistant de code l'accès à la documentation et aux schémas. Ils n'accèdent pas aux données de la boutique.
- Storefront MCP : permet aux agents d'achat externes de chercher dans le catalogue et de gérer un panier.
- Agentic Storefronts : diffusion du catalogue dans des assistants comme ChatGPT, pour les marchands américains éligibles. ⚠️ à vérifier (sources secondaires seulement)
- Aucun serveur MCP officiel d'administration ne remplace la couche Admin API.

### Conditions d'utilisation et IA
- Les conditions de l'API (version du 7 octobre 2026) interdisent le scraping et la collecte systématique de données.
- Elles interdisent d'entraîner ou d'améliorer un modèle d'IA avec des données issues de l'API, sauf consentement écrit de Shopify ou consentement du marchand pour ses propres données.
- L'inférence seule (envoyer des données à un modèle pour obtenir une réponse) n'est pas restreinte, selon un employé Shopify sur le forum.
- Les sous-traitants, dont le fournisseur de LLM, doivent protéger les données au moins autant que Shopify l'exige.
- Le marchand est responsable de ses contenus. Une contrefaçon (droit d'auteur, marque) peut entraîner le retrait du contenu ou la fermeture de la boutique.
- Aucune règle Shopify imposant une mention « généré par IA » sur les fiches n'a été trouvée.
- Google Merchant Center exige une métadonnée IPTC `DigitalSourceType: TrainedAlgorithmicMedia` sur les images générées par IA, et les attributs `structured_title` et `structured_description` pour les textes générés.
- L'article 50 de l'AI Act s'applique depuis le 2 août 2026. Les mockups photoréalistes pourraient être concernés. ⚠️ à vérifier par un juriste

### Fournisseurs print-on-demand
- Printify : une republication complète peut écraser les modifications faites dans Shopify. La publication sélective protège certains champs.
- Printful : le produit peut être créé dans Shopify puis synchronisé. Une variante désynchronisée n'importe plus ses commandes.
- Le rapport recommande un seul système maître par champ : variantes, SKU et fichiers d'impression chez le fournisseur ; titre, description, metafields et statut chez l'agent.

### Plan Shopify
- Boutique de développement : gratuite, pour tester, sans vraies commandes.
- Starter : non disponible pour les nouvelles boutiques selon des sources secondaires. À éviter.
- Basic est le minimum recommandé par le rapport. Grow ajoute des comptes collaborateurs, utiles pour la validation humaine.
- Aucune restriction de plan n'a été trouvée sur l'Admin API, les apps Dev Dashboard ou `shopifyqlQuery`.

### Architecture proposée par le rapport
1. Les agents ne parlent jamais directement à Shopify. Ils proposent des actions.
2. Une passerelle Shopify unique détient le token, expose des opérations métier fermées, fixe la version d'API, vérifie `userErrors` et journalise chaque action.
3. Une file d'attente par boutique respecte le budget de points, applique le backoff et porte une clé d'idempotence par tâche.
4. Un récepteur de webhooks vérifie le HMAC, stocke le corps brut, répond vite, puis traite en asynchrone.
5. Une base locale stocke produits, variantes, commandes, lignes, métriques quotidiennes et décisions.
6. Une boucle d'analyse attend une fenêtre d'observation minimale avant de proposer garder, modifier, archiver ou remplacer.
7. Garde-fous : création en `DRAFT`, validation humaine avant publication, contrôle propriété intellectuelle, quotas journaliers, `productDelete` interdit aux agents, disjoncteur, vérification des commandes en production avant archivage.

## Chiffres

### Sourcés
| Chiffre | Source |
|---|---|
| Version 2026-10 publiée le 1er octobre 2026, accessible jusqu'au 16 octobre 2027 | source : shopify.dev, release notes 2026-10 |
| Version stable supportée au moins 12 mois | source : shopify.dev, versioning |
| Version 2025-10 non supportée depuis le 16 octobre 2026 | source : shopify.dev, versioning |
| 2 048 variantes maximum par produit | source : shopify.dev, objet `Product` et `productSet` |
| 100 points par seconde (Basic, Grow), 200 (Advanced), 1 000 (Plus), 2 000 (enterprise) | source : shopify.dev, rate limits |
| 1 000 points maximum par requête, quel que soit le plan | source : shopify.dev, rate limits |
| 250 éléments maximum par argument de type tableau | source : shopify.dev, rate limits |
| Coût par défaut : 1 par objet, 10 par mutation, 0 par scalaire | source : shopify.dev, rate limits |
| Au-delà de 500 000 variantes, 10 000 nouvelles variantes par jour maximum, hors Plus | source : shopify.dev, rate limits |
| 25 metafields maximum par appel `metafieldsSet` | source : shopify.dev, `metafieldsSet` |
| Coût de `metafieldsSet` depuis le 15 septembre 2026 : 10 plus un poids par propriétaire (Product = 4, ProductVariant = 2), 260 points maximum | source : changelog shopify.dev |
| Commandes lisibles par défaut : 60 derniers jours | source : changelog shopify.dev |
| Webhooks : délai de 5 secondes, 8 nouvelles tentatives sur 4 heures | source : shopify.dev, troubleshoot webhooks |
| Token client credentials valable 24 heures | source : forum Shopify (employé) |
| Seau REST : 40 requêtes, vidé à 2 par seconde ; Plus : 400 et 20 par seconde | source : forum Shopify |
| Tokens offline expirants (60 minutes) obligatoires pour les apps publiques au 1er janvier 2027 | source : changelog shopify.dev |
| Article 50 de l'AI Act applicable au 2 août 2026, transition du marquage technique jusqu'au 2 décembre 2026 | source : Commission européenne ; Morgan Lewis pour la transition |
| Prix US : Basic 39 ou 29 dollars, Grow 105 ou 79, Advanced 399 ou 299, Plus à partir de 2 300 | source : sources secondaires concordantes ⚠️ à vérifier |
| Basic à 32 euros | source : une source secondaire ⚠️ à vérifier |

### Estimés
| Chiffre | Provenance |
|---|---|
| 500 designs, 3 couleurs et 6 tailles donnent 9 000 variantes | estimé (exemple de calcul du rapport) |
| Renouveler le token client credentials toutes les 20 heures environ | estimé (marge choisie par le rapport) |
| Fenêtre d'observation de 14 jours avant de juger un produit | estimé (exemple du rapport, à calibrer) |
| Plan de mise en route en 4 semaines | estimé (proposition du rapport) |

### Contradictions entre sources (non tranchées)
- Plafond de variantes : la documentation actuelle dit 500 000 variantes puis 10 000 par jour, avec une erreur 429. Des sources de 2025 (forum, Matrixify) disent 50 000 variantes puis 1 000 par jour, avec l'erreur `VARIANT_THROTTLE_EXCEEDED`.
- Retries des webhooks : la page « Troubleshoot webhooks » dit 8 tentatives sur 4 heures. Une ancienne page officielle dit 19 tentatives sur 48 heures.

## Caveats
- Le schéma ShopifyQL `sales` permet un regroupement par `product_title`. Le regroupement par identifiant produit n'est pas confirmé. ⚠️ à vérifier
- L'ancien dataset `products` de ShopifyQL avait des vues par produit. Sa présence en 2026-10 n'est pas confirmée. ⚠️ à vérifier
- La disponibilité de ShopifyQL sur tous les plans vient d'un développeur sur le forum, sans confirmation officielle. ⚠️ à vérifier
- L'existence d'un scope `read_analytics` utile n'a pas été vérifiée.
- L'indisponibilité du plan Starter et les dates du Shopify AI Toolkit viennent de sources secondaires. ⚠️ à vérifier
- La transmission de `structured_title`, `structured_description` et de la métadonnée IPTC par l'app Google et YouTube de Shopify n'est pas vérifiée. ⚠️ à vérifier
- Les conditions de Shopify Magic et les API de Printify et Printful n'ont pas été étudiées.
- La limite d'une seule bulk operation de chaque type par boutique est à confirmer. ⚠️ à vérifier
- Ce rapport n'est pas un avis juridique. La contrefaçon et l'AI Act demandent un juriste.

Questions ouvertes du rapport :
1. La boutique appartient-elle à ton organisation Shopify ? Sinon, le client credentials grant est impossible.
2. Quel fournisseur print-on-demand, et qui est le système maître des variantes et des SKU ?
3. `sales` permet-il de regrouper par identifiant produit ?
4. Une métrique de vues par produit existe-t-elle dans ShopifyQL 2026-10, ou faut-il un Web Pixel ?
5. Shopify accordera-t-il `read_all_orders` et l'accès de niveau 2, et dans quel délai ?
6. L'app Google et YouTube transmet-elle les attributs IA à Merchant Center ?
7. La boutique vend-elle dans l'Union européenne, et les mockups tombent-ils sous l'AI Act ?
8. Le fournisseur de LLM garantit-il par contrat l'absence d'entraînement ?
9. Quel volume de variantes à 12 mois, et quand approchera-t-on du seuil ?
10. Quels seuils statistiques avant de proposer un retrait ?

## Retenu / écarté

