---
type: research
title: Fournisseurs print-on-demand et API (France et UE)
status: validé
related: ["[[SYN - Fournisseurs]]"]
decisions: []
date: 2026-10-25
sources:
  - https://developers.printify.com/
  - https://help.printify.com/hc/en-us/articles/16132946730769-How-can-I-publish-the-Printify-shipping-rates-to-Shopify
  - https://help.printify.com/hc/en-us/articles/4483628807185-Why-can-t-I-publish-my-products-to-Shopify
  - https://help.printify.com/hc/en-us/articles/4483617936657-What-type-of-print-files-does-Printify-require
  - https://printify.com/network-fulfillment-status/
  - https://printify.com/print-on-demand/france/
  - https://dashboard.gelato.com/docs/ecommerce/products/create-from-template/
  - https://dashboard.gelato.com/docs/guides/create-product-from-template/
  - https://support.gelato.com/en/articles/8996064-creating-products-via-api-from-template
  - https://www.gelato.com/legal/api-terms
  - https://www.gelato.com/fr/exp%C3%A9dition-et-livraison
  - https://www.gelato.com/plus
  - https://support.gelato.com/en/articles/8996313-how-much-does-gelato-subscription-cost
  - https://developers.printful.com/docs/
  - https://developers.printful.com/docs/v2-beta/
  - https://www.printful.com/print-on-demand-europe
  - https://www.printful.com/print-on-demand-spain
  - https://www.printful.com/graphics-and-embroidery-guide
  - https://www.printful.com/creating-dtg-file
  - https://www.tpop.com/en/shipping
  - https://www.tpop.com/en/pricing
  - https://help.tpop.com/en/roadmap
  - https://help.tpop.com/en/impression-a-la-demande/integration-of-external-platforms/shopify-etsy-woocommerce
  - https://www.prodigi.com/faq/print-api/
  - https://github.com/api-evangelist/spod
  - https://community.shopify.com/t/printful-not-syncing-orders-or-live-rates/298982
  - https://community.shopify.com/t/are-you-facing-a-maximum-shipping-template-limit-error-while-publishing/293477
  - https://podvector.ai/articles/printify/costs-and-charges/printify-premium-price-full-breakdown-for-pod-sellers
  - https://merchtitans.com/blog/gelato-vs-printful
last-verified: 2026-10-25
tags: [dropshipping, fournisseurs, research]
---
# RCH - Fournisseurs print-on-demand et API (25-10-2026)

## Contexte posé
Prompt de départ, recopié tel quel :

> Contexte : je prépare une boutique Shopify de produits personnalisés en impression à la demande, gérée en grande partie par des agents IA qui créeront et publieront les produits automatiquement. Le marché visé est la France et l'Union européenne.
>
> Mission : compare les principaux fournisseurs de print-on-demand (au minimum Printful, Printify, Gelato, et d'autres pertinents pour l'Europe).
> Pour chacun, je veux :
> - la qualité de leur API (création de produits, upload de designs, génération de mockups, suivi des commandes) et sa documentation ;
> - l'intégration avec Shopify ;
> - les lieux de production en Europe et les délais de livraison vers la France ;
> - les prix de base sur quelques produits courants ;
> - les exigences techniques des fichiers d'impression (résolution, DPI, formats, zones d'impression) ;
> - les retours d'expérience sur la qualité et le service client.
>
> Format de sortie : un tableau comparatif, puis 1) un résumé en 5 lignes, 2) une recommandation argumentée pour un système automatisé par API, 3) les risques, 4) les questions ouvertes. Cite tes sources.

## Conclusion en une phrase
Printify est le seul fournisseur dont l'API couvre toute la chaîne jusqu'à la publication Shopify ; Gelato le complète pour les affiches et les mugs produits en France ; Printful a la meilleure qualité mais ne crée pas de produit Shopify par API ; T-Pop n'a pas d'API publique.

## Résultats

### Tableau comparatif
| Critère | Printify | Gelato | Printful | T-Pop | Prodigi | Spreadconnect (ex-SPOD) |
|---|---|---|---|---|---|---|
| Modèle | Place de marché de partenaires | Réseau de partenaires locaux, routage automatique | Ateliers en propre | Atelier en propre en France | Réseau de laboratoires | Ateliers du groupe Spreadshirt |
| Création de produit par API | Oui, complète | Oui, depuis un modèle créé dans le tableau de bord | Seulement pour une boutique « Manual orders / API » | Non, pas d'API publique | Non, API de commandes | Oui (« articles ») |
| Publication Shopify par API | Oui (endpoint publish) | Oui, réservé aux boutiques Shopify | Non : créer le produit via l'API Shopify puis le lier | Non | Non | ⚠️ à vérifier |
| Mockups par API | Oui, avec le produit | Oui, en arrière-plan | Oui, tâches asynchrones | Non | Non | ⚠️ à vérifier |
| Webhooks | Oui | Oui | Oui | Non | Oui (callbacks) | Oui |
| Sandbox | ⚠️ à vérifier | Commandes « draft » | Simulateur de webhooks | Non | Oui, environnement séparé | ⚠️ à vérifier |
| Production en Europe | Allemagne, France, Espagne, Royaume-Uni, etc. | 32 pays dont la France | Espagne, Lettonie, Royaume-Uni | France (Barjac) | Pays-Bas (Venlo) et partenaires | Allemagne, Tchéquie, Pologne |

### Printify
- API REST avec spécification OpenAPI et collection Postman. Couvre catalogue, produits, commandes, uploads, webhooks.
- Authentification par jeton personnel valable un an. OAuth demande une validation par Printify.
- Le catalogue donne les dimensions en pixels de chaque zone d'impression. Un agent peut donc adapter le visuel seul.
- Publication vers Shopify par `POST /v1/shops/{shop_id}/products/{product_id}/publish.json`. Pour une boutique Shopify connectée, Printify pousse le produit et gère les profils d'expédition.
- La qualité dépend du partenaire choisi. Il faut figer des partenaires européens.
- Printify et Printful appartiennent au même groupe (FYUL).

### Gelato
- Endpoint clé : `POST /v1/stores/{storeId}/products:create-from-template`, réservé aux boutiques Shopify.
- Un humain prépare un modèle par type de produit. L'agent envoie l'identifiant du modèle et les URL des visuels.
- Webhooks sur les statuts de commande et les modèles. Commandes de test en mode « draft ».
- Limite : l'agent ne peut pas créer un nouveau type de produit sans modèle.

### Printful
- Documentation la plus complète : v1 et v2 (v2 en open beta), OpenAPI, Postman, simulateur de webhooks, réponses en `fr_FR`.
- L'API Products ne crée des produits que dans une boutique « Manual orders / API ».
- Pour Shopify : créer le produit avec l'API Admin Shopify, puis le lier via l'Ecommerce Platform Sync API.
- Les bijoux ne sont pas disponibles par API. Les jetons privés expirent et se remplacent à la main.

### T-Pop
- Atelier en France, tarifs publics en euros HT.
- Pas d'API publique. La feuille de route annonce une API de commandes « en cours ».
- L'app Shopify transmet les commandes, mais la création de produits reste manuelle.

### Prodigi et Spreadconnect
- Prodigi : API v4 avec sandbox séparé, commandes, devis et callbacks. Pas de création de produit Shopify. Fort sur l'art mural.
- Spreadconnect : API REST pour créer des articles, commander et suivre. Plus de 250 types de produits.

### Fournisseurs écartés sans vérification détaillée
- Gooten et CustomCat : orientés États-Unis.
- Teemill et Inkthreadable : production au Royaume-Uni, donc douane vers la France.
- Peecho : racheté par Prodigi en décembre 2023.

### Fichiers d'impression
| Critère | Printful | Printify | Gelato |
|---|---|---|---|
| Formats | PNG, JPG ; PNG obligatoire en DTG | PNG, JPEG, SVG | PDF, PNG, JPG, HEIC ; PNG pour le textile |
| Profil couleur | sRGB | ⚠️ à vérifier | sRGB ; CMYK PDF/X-4 conseillé pour les affiches |

### Retours d'expérience
- Forums Shopify : chez Printful, des commandes ou tarifs ne se synchronisent plus après réinstallation de l'app.
- Forums Shopify : chez Printify, la limite de 100 profils d'expédition bloque la publication.
- Comparatifs : Printful plus régulier en qualité ; Gelato rapide en Europe mais variable selon le partenaire.
- Notes Trustpilot actuelles et retours français sur Reddit : ⚠️ à vérifier.

### Recommandation du rapport
- Principal : Printify pour le textile, avec partenaires UE figés.
- Complément : Gelato pour affiches et mugs.
- Alternative qualité : Printful avec création du produit via l'API Shopify.
- Règles d'implémentation proposées : file d'attente par endpoint, créations idempotentes, validation des visuels avant upload, variantes limitées, validation humaine avant publication, échantillons avant vente, visuels stockés chez soi.

## Chiffres

### Sourcés
| Chiffre | Valeur | Provenance |
|---|---|---|
| Limite globale Printify | 600 requêtes par minute | source : developers.printify.com |
| Limite catalogue Printify | 100 requêtes par minute | source : developers.printify.com |
| Limite publication Printify | 200 par 30 minutes | source : developers.printify.com |
| Taux d'erreur toléré Printify | 5 % des requêtes | source : developers.printify.com |
| Durée du jeton Printify | 1 an | source : developers.printify.com |
| Zone « front » DTF Printify (exemple) | 3153 x 3995 px | source : developers.printify.com |
| Profils d'expédition Shopify | 100 maximum par boutique | source : aide Printify |
| Plafond variantes Shopify | 1 000 par jour au-delà de 50 000 variantes, hors Plus | source : aide Printify |
| Limite de taux Gelato | 100 requêtes par seconde | source : documentation Gelato |
| Plafond Gelato | 5 000 appels par jour sauf accord | source : conditions API Gelato |
| Livraison Gelato | 90 % en 5 jours (marketing, non audité) | source : gelato.com/fr |
| Pays de production Gelato | 32 | source : gelato.com |
| Limite générale Printful | 120 requêtes par minute | source : developers.printful.com |
| Requêtes non authentifiées Printful | 30 par minute | source : developers.printful.com |
| Tâches de mockups Printful | 2 à 10 par minute | source : developers.printful.com |
| Sync produits Printful | 10 par minute | source : developers.printful.com |
| Production T-Pop | 2 à 4 jours | source : tpop.com/en/shipping |
| Livraison France T-Pop | 2 à 3 jours ouvrés | source : tpop.com/en/shipping |
| Expédition T-Pop t-shirt, affiche, tote | 3,95 € HT, plus 1,20 € par article | source : tpop.com/en/shipping |
| Expédition T-Pop sweat | 5,20 € HT, plus 1,50 € | source : tpop.com/en/shipping |
| Expédition T-Pop mug | 4,90 € HT, plus 1,70 € | source : tpop.com/en/shipping |
| Production partenaires Printify UE | 2 à 5 jours ouvrés | source : printify.com/network-fulfillment-status |
| T-shirt Bella+Canvas 3001 Printify | 10,98 $ ; 8,77 $ en Premium | source : podvector.ai (tiers) |
| T-shirt Bella+Canvas 3001 Printful | 11,69 $ | source : tiers, ⚠️ à vérifier |
| T-shirt Gildan 5000 Printful | 9,25 $ | source : tiers, ⚠️ à vérifier |
| T-shirt Stanley/Stella Printful | 21,10 $ | source : tiers, ⚠️ à vérifier |
| T-shirt T-Pop Kariban | 11,00 € HT | source : tpop.com |
| T-shirt T-Pop bio Native Spirit | 12,20 € HT | source : tpop.com |
| Sweat T-Pop | 22,80 € à 31,00 € HT | source : tpop.com |
| Mug T-Pop 330 ml | dès 5,95 € HT | source : tpop.com |
| Affiche A3 T-Pop | 8,00 € mat ; 9,00 € lustré HT | source : tpop.com |
| Tote bag T-Pop | 9,00 € à 10,70 € HT | source : tpop.com |
| Sweat Gelato Premium Unisex | dès 26 € | source : gelato.com, pays et TVA non précisés |
| T-shirt ringer Gelato | dès 12,43 € | source : gelato.com, pays et TVA non précisés |
| Mug « magic » Gelato | dès 9,57 € | source : gelato.com |
| Printify Premium | 39 $/mois ou 299 $/an, jusqu'à 20 % | source : podvector.ai (tiers) |
| Gelato+ | 27,99 €/mois ou 19,99 €/mois en annuel | source : gelato.com/plus |
| Printful Growth | 24,99 $/mois | source : fiche Printful sur le Shopify App Store |
| T-Pop Unlimited | 19,99 €/mois ; Business 249,99 €/mois | source : tpop.com/en/pricing |
| Résolution Printful | 150 DPI ; 300 DPI pour papier, coques, stickers | source : printful.com |
| Taille max fichier Printful | 200 Mo | source : printful.com |
| Résolution Printify | 300 DPI ; 120 à 150 DPI grands formats | source : aide Printify |
| Taille max fichier Printify | 100 Mo PNG/JPEG ; 20 Mo SVG | source : aide Printify |
| Résolution Gelato | 150 à 300 DPI à taille réelle | source : aide Gelato |
| Zone mug 11 oz Gelato | 200 x 96 mm | source : aide Gelato |
| Expédition t-shirt Printful vers l'UE | 4,79 $, plus 1,45 $ par article | source : tiers, ⚠️ à vérifier (tarifs modifiés en 2026) |

### Estimés
| Chiffre | Valeur | Provenance |
|---|---|---|
| Publications Printify par jour | jusqu'à 9 600 | estimé : 200 par 30 min sur 24 h |

### Contradictions entre sources (non tranchées)
- Site Printful en Espagne : Barcelone selon Printful, Madrid selon des sources tierces.
- Partenaires Gelato : 250, 140 ou 130 selon les pages et les dates.
- Remise Gelato+ : 33 % selon la page officielle, 25 % ou 35 % selon d'autres sources.
- Délai Printify vers l'Europe : 2 à 5 jours de production selon Printify, 10 à 15 jours ouvrés selon un ancien comparatif.

## Caveats
- Plusieurs prix viennent de sources tierces et sont en dollars.
- Les prix Gelato ne précisent ni le pays ni la TVA. Les promotions faussent les prix affichés.
- Printful a changé ses tarifs d'expédition en février et en juin 2026.
- Printful v2 est en beta. Printify peut modifier ou retirer ses API avec préavis.
- Les règles IOSS et TVA décrites sont générales, pas vérifiées par fournisseur.
- Les politiques des fournisseurs et de Shopify sur les designs générés par IA n'ont pas été vérifiées.
- Limites de taux de Prodigi et Spreadconnect non trouvées.
- Questions ouvertes du rapport :
  - Notes Trustpilot et retours français actuels.
  - Meilleurs partenaires Printify en France et en Allemagne pour Bella+Canvas 3001 et Stanley/Stella.
  - Prix Gelato exacts pour la France.
  - Gelato accepte-t-il de relever les 5 000 appels par jour ?
  - Printify a-t-il un environnement de test ?
  - Date et périmètre de l'API T-Pop.
  - Remise réelle du plan Printful Growth sur les produits UE.

## Retenu / écarté
