---
type: research
title: Images IA — conditions des modèles et politiques des plateformes (2026)
status: validé
related: ["[[SYN - Juridique]]", "[[SYN - Fournisseurs]]", "[[SYN - Acquisition]]"]
decisions: []
last-verified: 2026-10-29
date: 2026-10-29
sources:
  - https://ai.google.dev/gemini-api/terms
  - https://ai.google.dev/gemini-api/terms_preview
  - https://benchlm.ai/md/media-pricing/nano-banana.md
  - https://ideogram.ai/pricing/?pricing_tab=api
  - https://ideogram.ai/legal/api-tos
  - https://usagepricing.com/blueprint/ideogram
  - https://costbench.com/software/ai-media-apis/black-forest-labs/
  - https://developers.openai.com/api/docs/models/gpt-image-1.5
  - https://stability.ai/membership
  - https://www.recraft.ai/pricing?tab=api
  - https://printify.com/third-party-ai-tool-terms-of-use/
  - https://printify.com/policies/updates/
  - https://support.gelato.com/en/articles/8996134-creating-with-gelato-content-guidelines
  - https://www.printful.com/policies/download/intellectual-property-policy
  - https://help.shopify.com/cs/manual/compliance/intellectual-property
  - https://www.etsy.com/legal/creativity
  - https://commonthreadco.com/blogs/coachs-corner/meta-ai-ad-labels-mandatory-disclosure-ecommerce-2026
  - https://support.google.com/merchants/answer/14743464
  - https://ppc.land/iptc-metadata/
  - https://digital-strategy.ec.europa.eu/en/faqs/signing-code-practice-transparency-ai-generated-content
  - https://www.twobirds.com/en/insights/2026/taking-the-eu-ai-act-to-practice-the-final-transparency-code-of-practice
  - https://www.aiacto.eu/en/blog/digital-omnibus-ai-act-report-2027
  - https://www.economie.gouv.fr/apie/quel-droit-dauteur-lere-de-lintelligence-artificielle-generative
  - https://kohenavocats.fr/?p=2080717
  - https://www.inpi.fr/base-marques
tags: [dropshipping, juridique]
---

# RCH - Images IA, modèles et plateformes (29-10-2026)

## Contexte posé
Boutique française d'impression à la demande. Des agents génèrent des illustrations fixes, un humain les valide, Shopify les vend, Printify (UE) ou Gelato les imprime. Modèle principal pressenti : Nano Banana Pro (Google Gemini). Second : Ideogram, derrière une interface interne. Une liste noire de styles et de marques est prévue. Vente en France et dans l'UE, publicité envisagée sur Meta et Google.

Question posée : documenter, sans rien décider, les conditions commerciales 2026 des modèles d'images (prix, licence, filigrane, données, historique, résolution) et les politiques des plateformes de vente, d'impression et de publicité sur les visuels IA, plus le droit de l'UE et les sources pour une liste noire. Prompt complet dans la conversation claude.ai du 29/10/2026.

## Conclusion en une phrase
Les deux modèles pressentis permettent la vente de produits imprimés et excluent l'entraînement sur les données de l'API payante ; le risque principal vient de la propriété intellectuelle des sorties, que tous les imprimeurs mettent à la charge du vendeur, et du maintien des marqueurs IA (IPTC, C2PA, SynthID) exigés ou utilisés par l'AI Act, Google et Meta.

## Résultats

### 1. Tableau comparatif des modèles

| Modèle | Prix API 2026 | Licence commerciale | Filigrane, métadonnées | Non-entraînement | Résolution |
|---|---|---|---|---|---|
| Nano Banana Pro (`gemini-3-pro-image-preview`) | 0,134 $ par image en 1K ou 2K, 0,24 $ en 4K ; batch à moitié prix (0,067 $ et 0,12 $). source : benchlm.ai, lu le 11/09/2026 | Usage commercial ⚠️ à vérifier dans les conditions Google sur la propriété des sorties | SynthID (invisible) sur toutes les images, plus métadonnées C2PA (source : techspot, 11/2025). Pas de filigrane visible via l'API selon un guide tiers de janvier 2026 ⚠️ | Service payant : Google n'utilise ni prompts ni réponses pour améliorer ses produits (conditions Gemini API du 25/09/2025) | 1K, 2K, 4K. Lancé le 20/11/2025, toujours en « preview » |
| Ideogram (3.0, 4.0, 4.5) | 4.0 : 0,03 $ Turbo, 0,06 $ Default, 0,10 $ Quality (source : usagepricing.com, capture du 15/06/2026). Prix 3.0 contradictoires (voir Caveats) | Ideogram ne revendique pas la propriété des images ; usage commercial libre (FAQ ideogram.ai/pricing, lu le 29/10/2026) | ⚠️ non documenté | Accord développeur : pas d'entraînement sur entrées et sorties de l'API, sauf contenu signalé comme violant les règles (révisé le 14/08/2024) | ⚠️ à vérifier ; 4.0 listé en 2K |
| Flux (Black Forest Labs) | FLUX.2 pro : 0,030 $ le premier mégapixel, 0,015 $ les suivants ; FLUX.2 Max : 0,07 $ par mégapixel (costbench avril 2026 ; OpenRouter) | Sorties de l'API officielle utilisables commercialement à tous les niveaux (blog invideo, août 2026) ⚠️ | ⚠️ non documenté | ⚠️ non documenté | Facturation au mégapixel ; maximum ⚠️ |
| Midjourney | Pas d'API officielle ; les « API Midjourney » sont des intermédiaires non officiels contraires aux conditions (pricepertoken) | Entreprise au-delà de 1 M$ de CA : plan Pro (60 $) ou Mega (120 $) obligatoire (CGU du 27/05/2026, citées par krea.ai) | Métadonnées EXIF et XMP (prompt, modèle, seed) | ⚠️ ; images visibles en galerie publique hors Pro et Mega | ⚠️ |
| OpenAI gpt-image-1.5 | Qualité haute : 0,133 $ en 1024×1024, 0,20 $ en 1536×1024 (developers.openai.com) | ⚠️ à vérifier | IPTC via C2PA annoncé en février 2024 (iptc.org) | ⚠️ à vérifier | 1024×1024, 1536×1024, 1024×1536 |
| Stability | Stable Image Ultra 0,08 $, Core 0,03 $ (1 crédit = 0,01 $) | Licence Community gratuite sous 1 M$ de revenus annuels, Enterprise au-delà (stability.ai/membership) | Filigrane invisible sur les déploiements locaux (outil tiers PyPI) ⚠️ | ⚠️ | ⚠️ |
| Recraft | V3 raster 0,04 $, V3 vecteur 0,08 $ ; V4.1 raster 0,035 $ depuis juin 2026 ; V4 Pro vecteur 0,30 $ | Plan gratuit : images publiques, non commerciales, propriété de Recraft. Plans payants : propriété et droits commerciaux | ⚠️ | ⚠️ ; offre Enterprise annoncée « alignée RGPD » | Sortie vectorielle SVG native |

Précisions Google (Nano Banana Pro) :
- Dans l'EEE, en Suisse et au Royaume-Uni, seules les offres payantes peuvent servir à une application proposée à des utilisateurs.
- Les prompts et réponses peuvent être stockés temporairement ou mis en cache dans tout pays où Google a des installations ; traitement selon l'avenant de Google en tant que sous-traitant (RGPD).
- Les conditions interdisent les applications destinées ou susceptibles d'être utilisées par des moins de 18 ans.
- Google publie un aperçu de nouvelles conditions de l'API Gemini (ai.google.dev/gemini-api/terms_preview), date d'effet inconnue.
- Dans l'application Gemini, seuls les abonnés Ultra n'ont pas de filigrane visible ; SynthID reste actif.

Précisions Ideogram :
- Limite de débit par défaut : 10 requêtes en cours. Préavis de 14 jours avant tout changement de prix important.
- L'accord développeur (14/08/2024, §2.3.1) demande d'indiquer dans l'application que les sorties viennent du modèle Ideogram, par exemple « Powered by Ideogram ». Application à notre cas : question ouverte.
- La page officielle liste aussi Ideogram 4.5, une version Vector, et des liens GitHub et Hugging Face pour Ideogram 4.
- Conditions grand public : les images laissées publiques peuvent servir à la promotion et à l'entraînement (analyse ConductAtlas des conditions du 05/05/2026).

Historique des changements 2025-2026 :
- 25/09/2025 : nouvelle version des conditions de l'API Gemini.
- 20/11/2025 : lancement de Nano Banana Pro.
- 26/02/2026 : lancement de Nano Banana 2 (`gemini-3.1-flash-image-preview`).
- Juin 2026 : Ideogram 4.0 ajouté à l'API, page de prix encore datée du 06/08/2025.
- Juillet 2026 : en abonnement, Ideogram 4.0 facturé par image et non par lot de quatre (même nombre de crédits pour quatre fois moins d'images).
- 23/10/2026 : retrait annoncé de gpt-image-1 (pricepertoken).

### 2. Tableau des politiques par plateforme

| Plateforme | Règle | Obligation de déclaration | Sanction | Source, date |
|---|---|---|---|---|
| Printify | Le vendeur vérifie que ses sorties IA n'enfreignent aucun droit de tiers ; une sortie IA ne doit pas être présentée comme entièrement humaine ; les sorties peuvent ne pas être uniques, donc pas d'exclusivité | Pas de déclaration IA dans la fiche | Retrait sur notification de type DMCA. Depuis le 08/07/2026, le vendeur répond aussi des contenus de personnalisation de ses clients | printify.com/third-party-ai-tool-terms-of-use ; printify.com/policies/updates |
| Gelato | Les règles de propriété intellectuelle couvrent explicitement les contenus IA ; le vendeur vérifie la conformité aux réglementations IA applicables | Aucune | Le vendeur garantit Gelato contre toute réclamation de tiers ; mesures sur le compte après des retraits répétés ⚠️ (contexte exact à relire) | support.gelato.com, article 8996134 |
| Printful | La politique de propriété intellectuelle du 03/02/2026 vise explicitement les contenus IA | Aucune | Un contenu interdit peut entraîner la résiliation du compte | printful.com, politique PI |
| Shopify | Interdiction de vendre des biens contrefaisants ou portant atteinte à des marques, droits d'auteur ou brevets | Aucune règle IA spécifique trouvée dans une source officielle (contradiction, voir Caveats) | Retrait du contenu à la discrétion de Shopify ; résiliation possible | help.shopify.com ; politique d'utilisation acceptable |
| Etsy | Les créations IA issues des prompts du vendeur relèvent de « Designed by a seller » | Mention de l'IA dans la description ; déclaration du partenaire de production et du lieu d'expédition | Retrait des fiches non conformes ; frais dus | etsy.com/legal/creativity, mis à jour le 10/06/2025, lu le 29/10/2026 |
| Amazon | Depuis juillet 2026, les images de personnes photoréalistes générées par IA portent le marqueur « contains-synthetic-performer » (listings et A+) | Visages synthétiques seulement | ⚠️ non documenté | Sources secondaires (canopymanagement, novadata 23/07/2026) ⚠️ à vérifier dans Seller Central |
| Meta Ads | Label « AI info » appliqué automatiquement, notamment si des métadonnées C2PA d'un outil tiers sont détectées ; label près de « Sponsorisé » pour les personnes photoréalistes | Sans C2PA et avec un contenu photoréaliste : déclaration par l'annonceur | Rejet surtout pour les publicités politiques ou avec personnes photoréalistes générées | commonthreadco.com, 13/07/2026 ; affiversemedia.com, 10/07/2026 |
| Google Merchant Center | Depuis le 19/02/2024, marqueur IPTC DigitalSourceType trainedAlgorithmicMedia obligatoire sur les images produit générées par IA ; retrait interdit (image_link, additional_image_link, lifestyle_image_link) | Métadonnée IPTC | Refus, et action sur le compte en cas de tromperie sur le produit (source secondaire) | support.google.com/merchants/answer/14743464 ; ppc.land |
| Google Ads | Pas de règle IA spécifique trouvée hors Merchant Center | ⚠️ | ⚠️ | à rechercher |

### 3. Droit de l'UE

AI Act, article 50 :
- L'article 50 s'applique depuis le 2 août 2026.
- Le marquage lisible par machine (article 50(2) : filigranes, métadonnées) a un délai de grâce jusqu'au 2 décembre 2026, seulement pour les systèmes mis sur le marché avant le 2 août 2026 (article 111(4)).
- Le Digital Omnibus est le règlement (UE) 2026/1744, en vigueur depuis le 27 juillet 2026 ; il ne modifie pas l'article 50.
- Les obligations d'étiquetage des déployeurs (article 50(4), hypertrucages) s'appliquent sans transition.
- Les images générées avant le 2 août 2026 n'ont pas à être marquées rétroactivement (date de génération retenue par les lignes directrices finales).
- Lignes directrices finales publiées le 20/07/2026 ; code de bonnes pratiques sur la transparence des contenus IA publié le 10/06/2026.
- Le code fixe un socle à deux couches pour les fournisseurs : métadonnées signées et filigrane imperceptible.
- Le code est volontaire ; un non-signataire prouve sa conformité autrement et peut recevoir davantage de demandes des autorités.

Droit d'auteur sur une image générée :
- AG München, 13/02/2026 : refus de la qualité d'œuvre pour trois logos générés avec l'IA, faute d'influence créatrice suffisante. L'apport humain peut intervenir pendant la génération (suite de prompts) ou après (retouche). Source : APIE, economie.gouv.fr, 04/06/2026.
- Résolution du Parlement européen du 10/03/2026 (rapport Voss) : un contenu entièrement généré par IA ne devrait pas être protégé. Une résolution n'est pas une loi.
- France : aucune décision n'a reconnu la protection d'une création générée par IA (Seban Avocats, date ⚠️ inconnue).
- Tribunal de Prague, 2024 : refus faute de preuve d'une contribution humaine suffisante.
- Cass. civ. 1re, 9 avril 2026, pourvoi 25-11.711 : il faut démontrer en quoi les choix esthétiques traduisent la personnalité de l'auteur. Arrêt non spécifique à l'IA ⚠️ à vérifier sur Légifrance.

Style d'un illustrateur :
- Le style n'est pas protégé en soi. Une image trop proche d'une œuvre existante peut être contrefaisante.
- Une imitation trop fidèle d'un style identifiable peut constituer du parasitisme commercial.
- Un amendement à l'Assemblée nationale propose un article L. 331-4-2 visant un contenu IA stylistiquement proche d'un auteur identifiable ; statut ⚠️ inconnu.
- Aucune jurisprudence récente trouvée sur l'imitation du style d'un illustrateur par IA.

### 4. Sources pour la liste noire
- INPI, base marques : marques françaises depuis 1976, marques de l'UE en vigueur depuis 1996, API pour les requêtes en masse. https://www.inpi.fr/base-marques
- TMview : marques de tous les offices participants, recherche par image sur EUIPO, INPI et UKIPO. https://www.tmdn.org/tmview
- EUIPO eSearch plus : titulaires, oppositions, nullités, alertes.
- WIPO Global Brand Database : marques Madrid, appellations d'origine, emblèmes de l'article 6ter. https://www.wipo.int/branddb/en/
- Listes de licences (personnages, franchises) : aucune source publique structurée trouvée ⚠️.

## Chiffres

### Sourcés
- Nano Banana Pro : 0,134 $ en 1K ou 2K, 0,24 $ en 4K ; batch à moitié prix. source : benchlm.ai, lu le 11/09/2026.
- Ideogram 4.0 : 0,03 $, 0,06 $, 0,10 $. source : usagepricing.com, capture du 15/06/2026.
- Abonnements Ideogram : Plus 15 $/mois (2 400 crédits), Pro 42 $/mois (7 500 crédits), paiement à l'usage 1 centime le crédit (prix annuels). source : ideogram.ai/pricing, lu le 29/10/2026.
- FLUX.2 pro : 0,03 $ par mégapixel. source : costbench, avril 2026.
- gpt-image-1.5 haute qualité : 0,133 $ à 0,20 $. source : developers.openai.com.
- Stability Ultra 0,08 $ ; Recraft V3 0,04 $ (raster) et 0,08 $ (vecteur). source : stability.ai, recraft.ai.
- Seuil de licence Midjourney et Stability : 1 M$ de chiffre d'affaires annuel.
- AI Act : 2 août 2026, 2 décembre 2026, Omnibus en vigueur le 27 juillet 2026.

### Estimés (calculs, non mesurés)
- 4096 px imprimés à 300 DPI : environ 34,7 cm ; 2048 px : environ 17,3 cm ; 1536 px : environ 13 cm. estimé, calcul px ÷ 300 × 2,54.
- Affiche A3 à 300 DPI : environ 3508 × 4961 px ; aucun modèle listé ne l'atteint nativement sans agrandissement. estimé.
- 100 designs en 4K avec Nano Banana Pro : environ 24 $ (12 $ en batch) ; avec Ideogram 4.0 Quality : environ 10 $. estimé, hors régénérations.
- Zones d'impression mugs et textile chez Printify et Gelato : ⚠️ non recherchées.

## Caveats

Contradictions, non tranchées :
- Prix Ideogram 3.0 : la page officielle indexée affiche 0,04 $, 0,07 $ et 0,10 $ ; un relevé du 18/10/2026 (developersdigest) indique 0,03 $, 0,06 $ et 0,09 $. La table officielle se charge dynamiquement et n'a pas pu être lue.
- Prix Google AI Ultra : 19,99 $ (implicator.ai), 34,99 $ (yingtu.ai), 249,99 $/mois (laozhang.ai).
- C2PA chez Google : une même source dit que Google prévoit de prendre en charge C2PA « dans les mois à venir » et que les images Nano Banana Pro l'incluent déjà.
- Shopify : un blog (rewarx) affirme une obligation de déclaration des images IA depuis 2026 ; un autre texte du même site dit qu'il n'y en a pas. Sources de faible qualité.
- Etsy : page officielle datée du 10/06/2025 ; une source secondaire (nightjar.so) cite une politique vendeur du 14/01/2026 avec une case à cocher IA.

Non vérifié :
- Conditions Google sur la propriété des sorties.
- Politique de données de Flux, OpenAI, Midjourney, Stability.
- Résolutions maximales de chaque modèle.
- Limites de débit de Nano Banana Pro.
- Règle Amazon de juillet 2026.
- Restrictions Meta sur les publicités de produits personnalisés : rien trouvé.
- Survie de SynthID à l'agrandissement et à l'impression.

Qualité des sources : beaucoup de chiffres viennent d'agrégateurs ou de revendeurs. Des outils publics de retrait de SynthID et C2PA existent ; l'un d'eux (remove-ai-watermarks, PyPI) affirme contourner SynthID v2 depuis mai 2026. Documenté, non recommandé.

## Implications pour la génération par agents, la relecture humaine et la liste noire
Points à examiner, pas des décisions.
- Métadonnées : l'AI Act, Google Merchant Center et Meta reposent sur IPTC et C2PA. Vérifier si la chaîne agent, interface, Shopify, CDN, flux Merchant Center les conserve.
- Preuve d'apport humain : la protection éventuelle dépend de l'apport créatif humain (prompt ou retouche). Le journal des prompts et des retouches validées peut servir de preuve.
- Exclusivité : sorties non uniques et sans doute non protégées ; la boutique ne pourrait pas empêcher la copie de ses designs.
- Liste noire : noms de marques (INPI, TMview), personnages, noms d'artistes vivants dans les prompts ; contrôle aussi sur les sorties, car un prompt propre peut produire une image proche d'une œuvre.
- Visages réalistes : ils déclenchent les étiquetages les plus visibles chez Meta et Amazon.
- Stabilité : Nano Banana Pro est en « preview » ; clause d'attribution Ideogram et refonte des conditions Google à suivre.

## Questions ouvertes
1. La boutique est-elle « fournisseur » au sens de l'article 50(2), avec une interface interne devant une API, ou seulement « déployeur » ?
2. Une illustration non photoréaliste sur un mug relève-t-elle de l'article 50(4) (hypertrucages) ?
3. La règle IPTC de Merchant Center s'applique-t-elle à la photo d'un produit réel portant un design IA, ou à une maquette ?
4. Shopify conserve-t-il les métadonnées IPTC et C2PA des images téléversées ?
5. La clause « Powered by Ideogram » s'applique-t-elle à une boutique qui vend les sorties ?
6. Meta restreint-il les publicités pour des produits personnalisés ?
7. Quel agrandissement pour l'A3 et au-delà, et SynthID y survit-il ?
8. Quelle source publique pour les personnages sous licence ?

## Retenu / écarté
*(rempli à la revue)*
