---
type: research
title: RCH - Génération d'images pour l'impression (22-10-2026)
status: validé
related: []
decisions: []
date: 2026-10-22
sources:
  - https://www.developersdigest.tech/blog/image-video-generation-api-pricing-2026
  - https://docs.bfl.ml/release-notes
  - https://venturebeat.com/technology/black-forest-labs-opens-flux-3-image-klein-weights-with-free-commercial-use-limited-to-smaller-businesses
  - https://fal.ai/models/ideogram/v4.5
  - https://www.recraft.ai/docs/api-reference/pricing
  - https://business.adobe.com/products/firefly-business/firefly-ai-approach.html
  - https://www.printful.com/graphics-and-embroidery-guide
  - https://support.gelato.com/en/articles/8996354-what-are-the-guidelines-regarding-design-files-for-dtg-printing
  - https://developers.printful.com/docs/
  - https://dynamicmockups.com/pricing/
  - https://sudomock.com/pricing
  - https://vectorizer.ai/pricing
  - https://github.com/christophschuhmann/improved-aesthetic-predictor
  - https://github.com/PADDLEPADDLE/PADDLEOCR
  - https://printify.com/blog/print-on-demand-trends/
  - https://www.growtsy.com/etsy-ai-policy
last-verified: 2026-10-22
tags: [dropshipping, systeme, generation-images]
---
# RCH - Génération d'images pour l'impression (22-10-2026)

## Contexte posé
Prompt de départ, recopié tel quel :

> Contexte : je construis un système d'agents IA qui crée automatiquement des designs pour des produits personnalisés en impression à la demande (t-shirts, mugs, posters, etc.), vendus sur Shopify.
>
> Mission : fais une recherche technique sur la génération d'images adaptées à l'impression en 2026.
> Je veux savoir :
> - quels modèles de génération d'images sont les plus adaptés (qualité, rendu du texte, cohérence de style, coût par image, API disponible, licence commerciale) ;
> - comment obtenir la résolution et le format requis par l'impression (upscaling, vectorisation, fond transparent, profils couleur) ;
> - comment générer automatiquement des mockups réalistes ;
> - comment évaluer automatiquement la qualité d'un design avant publication ;
> - les styles et types de designs qui se vendent le mieux en print-on-demand.
>
> Format de sortie : 1) un résumé en 5 lignes, 2) un tableau comparatif des outils avec prix et licences, 3) un pipeline technique recommandé étape par étape, 4) les limites connues, 5) les questions ouvertes.

Recherche menée avec le mode recherche avancée de claude.ai, le 22/10/2026.

## Conclusion en une phrase
Un modèle par API à licence commerciale claire, suivi d'un post-traitement déterministe et d'un contrôle avant publication, suffit techniquement ; le vrai risque est juridique (marques, personnages protégés), pas technique.

## Résultats

### Modèles de génération
- Pour un usage commercial automatisé, il faut un modèle avec une API officielle : FLUX.2 ou FLUX 3 (Black Forest Labs), GPT Image 2.5 (OpenAI), Nano Banana Pro ou 2.1 (Google), Ideogram 4.5, Recraft V4.1.
- Midjourney n'a pas d'API officielle. Les wrappers non officiels violent ses conditions. Il est donc exclu.
- Texte dans l'image : Nano Banana Pro, GPT Image 2.5 et Ideogram 4.5 sont les plus fiables. Le classement général d'Ideogram 4.5 sur Artificial Analysis est bas, ce qui montre qu'un classement général ne mesure pas le rendu du texte.
- Vectoriel : Recraft V4 / V4.1 est le seul modèle majeur qui produit du vrai SVG.
- Cohérence de style : images de référence (FLUX.2, FLUX 3), styles de marque (Recraft), ou LoRA entraînée sur nos designs (FLUX 3 Image Klein). Une LoRA est un petit module ajouté au modèle pour lui apprendre un style.
- Licences des poids ouverts : la tendance 2026 est au durcissement. Qwen-Image 2.1, FLUX.2 dev et FLUX.2 Klein 9B sont non commerciaux. FLUX 3 Image Klein n'est gratuit que sous un plafond de chiffre d'affaires.
- Indemnisation propriété intellectuelle : seul Adobe Firefly l'offre, et seulement pour ses modèles natifs, hors bêta et hors modèles partenaires, avec un contrat entreprise.
- Cycle de vie : OpenAI retire plusieurs modèles en octobre et décembre 2026. Le fournisseur doit donc être caché derrière une interface interne.

### Format d'impression
- Cible : PNG transparent, en sRGB avec profil incorporé, à 150 DPI minimum et 300 DPI pour papier, stickers et coques.
- Les fournisseurs attendent du sRGB et font eux-mêmes la conversion CMJN.
- Aucun générateur ne sort la taille d'impression : l'agrandissement est obligatoire.
- Agrandissement : Real-ESRGAN pour les aplats et le trait, Topaz Precision pour le détaillé. Les agrandisseurs « créatifs » inventent des détails et abîment le texte.
- Transparence : native chez GPT Image (`background="transparent"`, PNG ou WebP). Sinon, fond uni puis détourage par BiRefNet (licence MIT).
- Bords en DTG : les pixels semi-transparents font des halos. Il faut seuiller l'alpha ou le tramer, nettoyer les franges et retirer les îlots isolés.

### Mockups
- API Printful : gratuite, asynchrone, limitée en débit. Les URL expirent, il faut stocker les images.
- API de rendu PSD (Dynamic Mockups, SudoMock) : rapides et peu chères. Elles placent le design dans un calque Photoshop avec ses déformations.
- Les modèles d'édition IA peuvent modifier le design. On les réserve aux images d'ambiance, pas aux vues du produit vendu.

### Contrôle avant publication
- Contrôles déterministes : dimensions, DPI, alpha, bords, profil sRGB, poids du fichier.
- Texte : OCR (PaddleOCR) puis comparaison au slogan attendu.
- Esthétique : prédicteur LAION v2 comme filtre grossier seulement, car il est biaisé. Q-Align a une licence ambiguë.
- Juge vision-langage avec une grille fixe et une sortie JSON, calibré sur des designs annotés à la main.
- Propriété intellectuelle : liste noire (marques, personnages, célébrités), recherche de marques par service tiers, détection de logos. Pas d'API officielle de recherche plein texte à l'USPTO.
- Déduplication : hachage perceptuel et embeddings CLIP.
- Printify impose de relire et approuver tout contenu IA avant publication. Le vendeur porte le risque de contrefaçon.

### Ce qui se vend
- Micro-niches identitaires : animaux et races, métiers, sport, jeux vidéo, fêtes, astrologie, fierté locale.
- La personnalisation (prénom, race, ville) est difficile à copier en masse.
- Le slogan seul est saturé.
- Etsy autorise les créations IA guidées par le vendeur, avec déclaration obligatoire.
- Ces tendances viennent surtout de blogs de fournisseurs et de vendeurs, pas de données indépendantes.

### Pipeline proposé par la recherche
Proposition de la recherche, rien n'est décidé.
1. Recherche de niche, avec filtre liste noire et marques dès le départ.
2. Rédaction d'un prompt structuré par un modèle de langage.
3. Génération de 4 à 8 variantes, avec le modèle choisi selon le type de design.
4. Préfiltre rapide : OCR, score esthétique, déduplication.
5. Juge vision-langage sur les variantes restantes.
6. Détourage et nettoyage des bords.
7. Agrandissement ou vectorisation.
8. Normalisation : sRGB, DPI, poids du fichier.
9. Contrôle final et revue humaine, au moins sur un échantillon.
10. Mockups, stockés chez nous.
11. Publication chez le fournisseur et sur Shopify, avec mention IA si la plateforme l'exige.
12. Boucle de retour : ventes par niche, style et modèle.

## Chiffres

### Sourcés
| Chiffre | Source |
|---|---|
| GPT Image 2.5 : 30 USD par million de jetons image en sortie, 15 USD en Batch | source : Developers Digest, 10/2026 |
| GPT Image 2 : 0,006 / 0,053 / 0,211 USD par image 1024 × 1024 | source : Developers Digest, 10/2026 |
| GPT Image 1.5 : 0,009 / 0,034 / 0,133 USD par image | source : costgoat.com, aifreeapi.com |
| Retrait gpt-image-1 le 23/10/2026 ; gpt-image-1.5, 1-mini et chatgpt-image-latest le 01/12/2026 | source : Developers Digest, 18/10/2026 |
| Nano Banana Pro : 0,134 USD (1K ou 2K), 0,24 USD (4K), moitié prix en Batch | source : glbgpt.com, aifreeapi.com |
| Nano Banana 2.1 : 0,0336 / 0,0504 / 0,113 USD (1K / 2K / 4K) | source : Developers Digest |
| FLUX.2 Pro : 0,03 USD le premier mégapixel puis 0,015 USD par mégapixel | source : flowith.io |
| FLUX.2 Flex : 0,05 à 0,06 USD ; FLUX.2 Max : 0,07 USD | source : OpenRouter |
| FLUX 3 Image sorti le 01/10/2026 ; FLUX 3 Image Klein (poids ouverts) le 15/10/2026 | source : docs.bfl.ml, GlobeNewswire |
| FLUX 3 Image Klein : 5,6 milliards de paramètres, jusqu'à 10 images de référence | source : VentureBeat, layer3labs.io |
| FLUX 3 Image Klein API : 0,009 USD (1K), 0,014 USD (2K) | source : Developers Digest |
| Licence FLUX Kommunity : usage commercial gratuit sous 5 millions USD de chiffre d'affaires annuel | source : VentureBeat |
| FLUX.2 Klein 4B : 0,014 USD, Apache 2.0 ; 9B : 0,015 USD, non commercial | source : flowith.io, scriptbyai.com |
| Ideogram 4.5 : 0,03 / 0,06 / 0,22 USD, sorti le 30/09/2026 | source : fal.ai |
| Recraft V4.1 : 0,035 USD ; V4.1 Pro : 0,21 USD ; V4 Vector : 0,08 USD ; V4 Pro Vector : 0,30 USD ; Vectorize : 0,01 USD | source : recraft.ai (doc API) |
| Grok Imagine Image 2.0 : 0,04 USD en qualité basse 1K | source : Developers Digest |
| Midjourney : 10 à 120 USD par mois, pas d'API officielle | source : tech-insider.org, unifically.com |
| Qwen-Image 2.1 : 7 milliards de paramètres, licence de recherche non commerciale, sorti le 20/09/2026 | source : eesel.ai, cellcog.ai, apidog.com |
| BiRefNet sur Replicate : environ 0,51 USD pour 1 000 images | source : aireiter.com |
| Real-ESRGAN sur Replicate : environ 0,002 USD par image | source : forasoft.com, aitoolsbakery.com |
| Topaz API : 50 USD par mois pour 500 crédits ; 240 USD pour 3 000 crédits ; 1 crédit par 24 mégapixels en Gigapixel | source : wireflow.ai |
| Clarity Upscaler : 0,03 USD par mégapixel | source : fal.ai |
| Vectorizer.ai : de 0,20 USD par image (50 par mois) à 0,05 USD (100 000 par mois) | source : vectorizer.ai |
| Printful : sRGB IEC61966-2.1, 150 DPI minimum, 300 DPI pour coques, stickers et papier, 200 Mo maximum | source : printful.com (guide graphique) |
| Printful : zone t-shirt 12 × 16 pouces, jusqu'à 15 × 18 sur certains produits DTG | source : printful.com |
| Gelato DTG : 150 DPI minimum, 300 recommandés, sRGB | source : support.gelato.com |
| API Printful : 120 appels par minute en général, limite plus basse pour les mockups | source : developers.printful.com |
| Dynamic Mockups : 50 crédits gratuits ; Pro 15 USD par mois en annuel pour 3 600 crédits par an, puis 0,051 USD par crédit ; 300 requêtes par minute | source : dynamicmockups.com |
| SudoMock : 25 USD par mois pour 5 000 rendus, à partir de 0,002 USD par rendu | source : sudomock.com |
| Mediamodifier : 499 USD par mois pour 5 000 rendus | source : sudomock.com (comparatif) |
| Placeit : 14,95 USD par mois, sans API | source : sudomock.com (comparatif) |
| Google Vision OCR et logos : 1,50 USD pour 1 000 images, 1 000 images OCR gratuites par mois | source : vantaige.io, softwarefinder.com |
| Clés USPTO non mises à jour désactivées le 08/10/2026 | source : developer.uspto.gov |
| Conditions Printify mises à jour le 17/09/2026 : relecture obligatoire du contenu IA | source : conditions Printify |
| Conditions Printful du 30/06/2026 | source : printful.com |
| Habillement : 39,5 % des revenus du marché POD en 2025 | source : Grand View Research, rapport 2026-2033 |
| Marché POD : 10,8 milliards USD en 2025, croissance de 23,6 % par an sur 2026-2033 ; décoration murale à 24,5 % par an | source : Grand View Research |
| Etsy Creativity Standards mis à jour le 10/06/2025 | source : growtsy.com, krafie.com |

### Estimés
| Chiffre | Statut |
|---|---|
| Coût par design publié d'environ 0,12 USD avec un modèle à 0,03 USD, 2 appels par design et 50 % de rejet | estimé (calcul illustratif) |
| T-shirt 12 × 16 pouces : 1 800 × 2 400 px à 150 DPI, 3 600 × 4 800 px à 300 DPI | estimé (calcul : pouces × DPI) |
| Agrandissement nécessaire de 2 à 4 fois | estimé (sorties de 1 à 4 mégapixels) |
| Cible 4 500 × 5 400 px pour un t-shirt | estimé, convention courante ⚠️ à vérifier |
| Écarter au moins la moitié des variantes au préfiltre | estimé |
| Printify : 300 DPI recommandés, 120 à 150 DPI acceptables en grand format | source secondaire (Let's Enhance) ⚠️ à vérifier |

## Caveats
- La plupart des prix viennent d'agrégateurs et de revendeurs (août à octobre 2026), pas des pages officielles. Ils changent souvent.
- GPT Image 2.5 n'a pas de prix par image publié. Seul le tarif au jeton est connu.
- Non vérifiés : Leonardo, Stability AI, HiDream, Together AI, et les API de mockups Printify et Gelato. ⚠️ à vérifier
- Licence de potrace (GPL) non revérifiée. ⚠️ à vérifier
- Désactivation de la transparence sur gpt-image-2 au 30/09/2026 : rapportée par un intermédiaire (APIYI), non confirmée par OpenAI. ⚠️ à vérifier
- Shopify : aucune règle propre à l'IA trouvée, et le texte exact de la politique d'usage acceptable n'a pas été lu. ⚠️ à vérifier
- Les données de tendances viennent de blogs commerciaux, pas de sources indépendantes.
- Aucun outil automatique ne donne une garantie juridique. Il signale seulement un risque.

Contradictions entre sources, non tranchées :
- BRIA RMBG-2.0 par API : 0,018 USD ou 0,08 USD par image selon la source.
- Jetons d'une image 4K de Nano Banana 2.1 : 3 780 ou 2 520 selon deux pages de Google.
- Débit des mockups Printful : « 2 à 10 par minute » dans la doc Printful, « 2 pour une boutique nouvelle, 10 pour une boutique établie » selon Jentic.
- Filigrane des rendus API du plan gratuit Dynamic Mockups : oui sur la page des prix, non sur la page API.
- Licence de Q-Align / OneAlign : MIT sur la fiche du modèle, licence S-Lab dans le dépôt.
- Retraits Etsy au premier trimestre 2026 : environ 12 000 annonces et 8 500 avertissements selon iscompliant.app ; chiffres réfutés par Growtsy (13/10/2026), qui n'en trouve aucune trace chez Etsy.
- Part de l'habillement : 39,5 % (Grand View Research) ou 39,45 % (Market.us).

Questions ouvertes :
- Quelle part de contribution humaine Etsy, Printify ou Shopify jugeront-ils suffisante pour un pipeline automatisé ?
- Les designs purement IA seront-ils protégeables par le droit d'auteur ?
- Prix et licence de FLUX 3 Dev ; poids ouverts annoncés pour Ideogram.
- Quel modèle donne le meilleur coût par design vendu (test A/B à faire) ?
- Taux réel d'erreur d'un juge vision-langage sur les personnages protégés.
- Midjourney lancera-t-il une API entreprise ?
- Les contraintes de saturation et de trame varient-elles selon l'imprimante de chaque site de production ?

## Retenu / écarté

