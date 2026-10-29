---
type: research
title: Canaux d'acquisition
status: validé
related: ["[[SYN - Acquisition]]", "[[_conventions]]"]
decisions: []
date: 2026-10-22
sources:
  - https://www.superads.ai/facebook-ads-costs/cpm-cost-per-mille/france
  - https://topgrowthmarketing.com/dtc-ecommerce-benchmarks/meta-ads-benchmarks/
  - https://coinis.com/glossary/meta-ads-learning-phase
  - https://www.pigeondigital.com/insight/facebook-ads-learning-phase-50-conversions-rule-2026
  - https://developers.facebook.com/documentation/ads-commerce/marketing-api/overview/rate-limiting
  - https://www.trendtrack.io/blog-post/meta-ad-spend-by-industry
  - https://aiadvantageagency.com/tiktok-ads-cost-for-ecommerce/
  - https://www.trackbee.ai/blog/tiktok-ads-cost-cpc-cpm-budget-best-strategies
  - https://www.stackmatix.com/blog/tiktok-ads-cost-2026-pricing-breakdown
  - https://www.z.media/insights/how-to-sell-on-tiktok-shop-france-2026
  - https://www.postzen.dev/blog/tiktok-api
  - https://www.trackbee.ai/blog/pinterest-ads-cost
  - https://www.benchmarketing.org/benchmarks/pinterest-ads
  - https://vorplabs.com/agent-tools/pinterest-api
  - https://shopiator.com/blog/google-ads-benchmarks-ecommerce-brands
  - https://ppc.land/google-drops-developer-tokens-from-ads-api-access-decisions/
  - https://www.be-hype.com/blog/tarif-influenceur-grille-prix-complete-2026
  - https://www.shaare-agency.com/blog/cout-campagne-influence-2026
  - https://blog.marmalead.com/etsy-fees-explained/
  - https://blog.marmalead.com/etsy-print-on-demand/
  - https://developers.etsy.com/documentation/
  - https://www.growtsy.com/etsy-print-on-demand
  - https://merchtitans.com/blog/amazon-handmade-guide
  - https://merchtitans.com/blog/print-on-demand-europe-guide
  - https://www.printful.com/blog/what-is-a-good-profit-margin-for-print-on-demand
  - https://www.syncost.com/blogs/how-much-profit-print-on-demand-t-shirts
  - https://www.cnil.fr/fr/refuser-les-cookies-doit-etre-aussi-simple-quaccepter-bilan-de-la-deuxieme-campagne-de-mises-en
  - https://linc.cnil.fr/etude-protection-des-donnees-et-cookies-leclairage-des-sciences-comportementales
  - https://support.google.com/google-ads/answer/14009343?hl=en
  - https://taxation-customs.ec.europa.eu/system/files/2020-12/vatecommerceexplanatory_28102020_en.pdf
  - https://help.printful.com/hc/en-us/articles/360014067279-How-will-VAT-apply-to-orders-shipped-to-Europe
  - https://legalviz.eu/dsa/article/30/
last-verified: 2026-10-22
tags: [dropshipping, acquisition, research]
---
# RCH - Canaux d'acquisition (22-10-2026)

## Contexte posé
Recherche approfondie lancée depuis le chat le 22/10/2026. Prompt de départ :

> Contexte : je prépare une boutique Shopify de produits personnalisés en impression à la demande, pour la France et l'Union européenne. Un agent IA analysera les ventes pour savoir quels produits garder. Il faut donc assez de trafic pour obtenir des données fiables.
>
> Mission : fais une recherche approfondie sur les canaux d'acquisition adaptés à ce type de boutique en 2026.
> Pour chaque canal (publicité Meta, TikTok, Pinterest, Google Shopping, SEO, influence, marketplaces comme Etsy) je veux :
> - le coût typique (CPC, CPM, coût par achat) dans ce secteur ;
> - le budget minimum pour obtenir des résultats exploitables ;
> - le délai avant les premiers résultats ;
> - ce qui peut être automatisé par API et ce qui ne peut pas l'être ;
> - les erreurs courantes des débutants.
>
> Format de sortie : un tableau comparatif, puis 1) un résumé en 5 lignes, 2) une stratégie de lancement recommandée avec un budget de test, 3) les risques, 4) les questions ouvertes. Cite tes sources.

Vocabulaire. Le CPM est le coût pour mille affichages. Le CPC est le coût par clic. Le CPA est le coût par achat.

## Conclusion en une phrase
Avec 3 500 à 4 000 €, la combinaison Google Shopping et Meta, avec Etsy en appoint, permet d'éliminer les produits morts, mais pas de classer finement les gagnants.

## Résultats

### Tableau comparatif
| Canal | Budget minimum exploitable | Délai | Automatisable par API | Reste manuel | Erreurs de débutant |
|---|---|---|---|---|---|
| Meta | 30 à 50 € par jour sur une seule campagne, en acceptant « apprentissage limité » (estimé) | 7 jours minimum avant de juger | Campagnes, budgets et statistiques via la Marketing API | Validation des publicités, moyen de paiement, restrictions de compte | Trop d'ensembles de publicités, modifications pendant l'apprentissage, pas de Conversions API |
| TikTok Ads | Minimum officiel de 50 $ par jour par campagne | 7 à 14 jours | Campagnes et rapports via la Marketing API v1.3, après validation d'une application développeur | Production des vidéos | Visuels statiques recyclés, pas assez de vidéos natives |
| TikTok Shop | Inscription avec SIREN, SIRET et numéro de TVA | Variable, dépend des créateurs | API vendeur du Partner Center, intégration Shopify | Contenu vidéo et relations avec les créateurs | Prix hors de la zone qui convertit |
| Pinterest | 50 à 100 $ par jour en test selon une agence (probablement haut) | Conversions différées, mesurer à 7 et 30 jours | API v5 gratuite | Vidéo de démonstration exigée, chaque action doit être validée par l'utilisateur | Juger sur 7 jours, visuels non verticaux |
| Google Shopping et Performance Max | Environ 50 conversions par mois recommandées pour Performance Max. Démarrer en Shopping standard | Environ 30 jours pour Performance Max | Google Ads API et Merchant API | Vérification de la marque, refus de produits gérés par Google | Lancer Performance Max sans historique, titres de flux négligés, pas de Consent Mode v2 |
| SEO | Aucun seuil publicitaire | 4 mois à 1 an | Fiches, balises et textes alternatifs via l'API Admin Shopify | Qualité éditoriale | Fiches dupliquées, textes générés en masse |
| Influence | Envoi gratuit à des nano-créateurs, ou 3 000 € pour une formule d'agence | Pic en quelques jours, puis baisse rapide | Suivi par codes promo et liens affiliés via l'API Shopify | Toute la négociation | Payer au nombre d'abonnés, oublier la mention publicitaire |
| Etsy | Quelques dizaines d'euros pour 50 annonces (estimé) | Plusieurs semaines (estimé) | Open API v3, validée automatiquement pour sa propre boutique | Déclaration du partenaire de production | Designs non originaux, Offsite Ads sur des produits à faible marge |
| Amazon | Merch on Demand sur invitation | 2 à 6 semaines après acceptation | Pas d'API Merch vérifiée | Tout | Croire que Handmade accepte l'impression à la demande |

### Résumé en 5 lignes
1. Google Shopping capte une demande existante au clic le moins cher d'Europe : c'est le premier canal à financer.
2. Meta sert à tester les visuels et les designs, mais son coût par vente dépasse souvent la marge d'un t-shirt simple.
3. Etsy valide gratuitement des designs, à condition qu'ils soient originaux et que le partenaire d'impression soit déclaré.
4. TikTok, Pinterest et l'influence sont des canaux de deuxième phase, car ils demandent beaucoup de contenu ou mesurent mal à court terme.
5. Avec 3 500 à 4 000 €, l'agent IA peut éliminer les produits morts, mais pas classer finement les produits gagnants.

### Ce que l'agent IA peut juger
- Éliminer un produit est possible tôt. Après 300 visites sans vente, son taux de conversion réel est très probablement sous 1 % (règle de trois statistique).
- Déclarer un gagnant demande environ 30 ventes. En dessous de 10 ventes, l'incertitude est d'environ 60 %.
- Comparer deux produits proches (1,5 % contre 2,25 %) demande environ 5 000 visites par produit.
- Il vaut mieux juger les familles de designs avant les produits, et utiliser les signaux intermédiaires : clic, ajout au panier, début de paiement.
- Les algorithmes Advantage+ et Performance Max concentrent les dépenses sur quelques produits. Un produit peu exposé n'est pas forcément mauvais.
- L'agent doit juger sur les ventes Shopify, qui sont complètes. Les conversions rapportées par les plateformes sont partielles à cause du refus des cookies.

### Stratégie de lancement proposée par le rapport
- Semaines 1 et 2, préparation, 300 à 500 € : bannière de consentement et Consent Mode v2, pixel Meta et Conversions API, échantillons pour les photos, fiches gratuites Google, 8 à 12 produits, publication sur Etsy sans Offsite Ads.
- Semaines 3 à 8, test payant, environ 3 000 € : Google Shopping standard à 25 € par jour (environ 1 050 €), Meta Advantage+ à 30 € par jour (environ 1 260 €), 5 nano-créateurs (environ 500 €).
- Semaines 9 et 10, décision : couper les produits sans vente après 300 visites, concentrer le budget sur 3 ou 4 gagnants, ajouter Pinterest à 10 à 15 € par jour, tester TikTok seulement avec au moins 10 vidéos par mois.

### Ce qui reste manuel dans l'automatisation
- Vérification de la marque chez Google.
- Validation des applications développeur chez TikTok et Pinterest.
- Vidéo de démonstration pour l'accès Standard de Pinterest.
- Validation des publicités par chaque plateforme.
- Négociation avec les influenceurs.
- Déclaration du partenaire de production sur Etsy.
- Pinterest interdit les actions automatiques non validées une à une, donc l'agent doit prévoir une validation humaine sur ce canal.

### Contraintes européennes
- **Cookies.** La CNIL exige que refuser soit aussi simple qu'accepter. Google exige les signaux de consentement pour l'Espace économique européen depuis mars 2024.
- **TVA.** Au-delà de 10 000 € de ventes à distance dans l'Union, on applique la TVA du pays du client via le guichet unique OSS, chaque trimestre.
- **DSA.** Les marketplaces collectent l'identité, l'immatriculation et une auto-certification du vendeur (article 30). Nom, adresse, téléphone et email sont affichés publiquement.
- **Etsy.** Depuis le 10 juin 2025, les objets produits par impression doivent venir d'un design original du vendeur. Les designs achetés ne sont plus acceptés. Le partenaire de production doit être déclaré. Les créations par IA à partir de ses propres instructions sont acceptées si on le mentionne.
- **Amazon Handmade** refuse l'impression à la demande. Merch on Demand ne propose pas de personnalisation par l'acheteur.

### Risques listés par le rapport
- Marge insuffisante face à un coût par vente de 30 € ou plus : c'est le risque principal.
- Décisions de l'agent prises sur du bruit statistique, avant 30 ventes.
- Biais d'exposition créé par les algorithmes publicitaires.
- Perte de mesure due au refus des cookies.
- Suspension de boutique Etsy ou de compte publicitaire Meta.
- Changements d'API (Google en septembre 2026, Meta en mai 2026).
- Saisonnalité des prix publicitaires, plus chers au quatrième trimestre.
- Propriété intellectuelle des designs.
- Erreur de TVA sur le seuil de 10 000 €.

### Questions ouvertes
- Quel panier moyen viser ? Au-dessus de 45 €, la publicité payante devient défendable.
- Quels produits exactement ? Affiches, mugs et plaids conviennent mieux à Pinterest et Etsy que les t-shirts.
- Quel imprimeur, et depuis quel pays expédie-t-il ?
- Peut-on produire au moins 10 vidéos par mois ?
- Quel budget accepte-t-on de perdre pendant l'apprentissage ?
- L'agent agit-il seul, ou propose-t-il des actions validées par Antoine ?

## Chiffres

### Sourcés
| Chiffre | Valeur | Source | Zone |
|---|---|---|---|
| CPM Meta | environ 8 $ en moyenne de juillet 2025 à juillet 2026, pic à 21,74 $ en juillet 2026 | Superads | France |
| CPC Meta e-commerce | 0,57 $ (médiane) | Top Growth Marketing | États-Unis |
| Coût par achat Meta | 49 $ (médiane) | Top Growth Marketing | États-Unis |
| CPC Meta vêtements | 0,45 $ | Trendtrack | Monde |
| Sortie d'apprentissage Meta | environ 50 événements en 7 jours | Meta Business Help Center via Coinis et Pigeon Digital | Monde |
| Accès « Full » à la Marketing API Meta | 500 appels en 15 jours, moins de 15 % d'erreurs | Documentation Meta | Monde |
| CPM TikTok e-commerce | 4,08 $ (médiane Triple Whale) ; 9 à 13 $ en campagnes de conversion | AI Advantage Agency, Kixmon | Monde |
| CPC TikTok | environ 1 € | Trackbee | Europe |
| Coût par achat TikTok | 32,74 $ (médiane) | AI Advantage Agency | États-Unis |
| Budget minimum TikTok | 50 $ par jour par campagne, 20 $ par jour par groupe | Stackmatix | Monde |
| Commission TikTok Shop | 9 % depuis le 8 janvier 2026 ; 4 % les 60 premiers jours ; affiliés 10 à 20 % en plus | Z Media | France |
| CPC Pinterest | 0,45 à 1,30 € | Trackbee | Europe |
| CPM Pinterest | 3 à 8 € | Trackbee | Europe |
| CPC et CPM Pinterest | 1,50 $ et 5,10 $ (médianes) | Benchmarketing | Monde |
| CPC Google | Shopping 0,36 €, Performance Max 0,41 €, recherche 0,42 € (médianes, avril 2026) | smec | Europe |
| Coût par achat Performance Max | 46,10 $ ; de 67,98 $ au T1 à 38,59 $ au T3 2026 | Shopiator | Pays anglophones |
| Accès Google Ads API | sans jeton développeur depuis le 9 septembre 2026 ; Basic à 15 000 opérations par jour | PPC Land | Monde |
| Délai SEO | 4 mois à 1 an | Google Search Central | Monde |
| Micro-influenceur Instagram | 200 à 1 500 € par publication ; TikTok 20 à 40 % moins cher ; droits d'usage +30 à 100 % | Be-Hype | France |
| Test d'influence crédible | 3 000 € en démarrage, 10 000 à 15 000 € pour un test crédible (source intéressée) | Shaare Agency | France |
| Frais Etsy | annonce 0,20 $ ; commission 6,5 % ; Offsite Ads 15 %, ou 12 % au-delà de 10 000 $ | Marmalead | Monde |
| Limite API Etsy | 10 requêtes par seconde, 10 000 par jour | Documentation Etsy | Monde |
| Taux de conversion Shopify | 1,4 % (médiane, 433 boutiques) ; top 20 % à 2,7 % ; mode 1,1 % | Littledata, octobre 2026 | Monde |
| Taux de conversion Shopify | 1,74 % (médiane, 745 boutiques, S1 2026) | Shogun | Monde |
| Coût de base t-shirt Gelato | 8,50 à 11 €, plus 3,50 à 5 € de livraison | Merch Titans | Europe |
| Surcoût Printful | 15 à 20 % de plus que Gelato | Merch Titans | Europe |
| Marge nette impression à la demande | 20 à 40 % | Printful | Monde |
| Refus des cookies | 39 % déclarés en juin 2022 ; près de 50 % si le refus est mis en avant | CNIL | France |
| Perte de données marketing après mise en conformité | 10 à 80 % (chiffre de fournisseur) | Elevar | Monde |
| Sanctions cookies | 325 M€ à Google, 150 M€ à Shein (septembre 2025) | CNIL | France |
| Seuil TVA ventes à distance | 10 000 € | Commission européenne | UE |

### Estimés
| Chiffre | Valeur | Base du calcul |
|---|---|---|
| Visites par vente | 60 à 70 | inverse des taux de conversion médians Shopify |
| Incertitude sur un nombre de ventes | environ 60 % à 10 ventes, 36 % à 30 ventes, 20 % à 100 ventes | loi de Poisson, plus ou moins 2 divisé par la racine du nombre de ventes |
| Seuil d'abandon d'un produit | 300 visites sans vente | règle de trois statistique |
| Visites pour comparer 1,5 % et 2,25 % | environ 5 000 par produit | test standard, 95 % de confiance, 80 % de puissance |
| Budget Meta pour sortir de l'apprentissage | environ 1 750 € par semaine | 50 ventes à 35 € |
| Marge brute d'un t-shirt à 29,90 € TTC | environ 10 € | 24,92 € HT, moins 14 € de production et livraison, moins 0,75 € de paiement |
| Coût par vente Google en Europe | environ 26 à 29 € | 0,36 à 0,41 € par clic divisé par 1,4 % |
| Panier moyen rendant la publicité défendable | 45 € ou plus | marge nécessaire face à 30 € de coût par vente |
| Ventes attendues pendant le test | 80 à 120, soit 7 à 10 par produit | 3 000 € de budget de test |
| Budget pour 30 ventes par produit sur 12 produits | 10 000 à 15 000 € | coût par vente de 30 à 40 € |
| Budget de lancement total | 3 500 à 4 000 €, hors coût des produits vendus | somme des phases |

## Caveats
- La plupart des coûts par vente viennent d'études américaines ou mondiales. Ils servent d'ordre de grandeur, pas de prévision pour la France.
- Contradictions entre sources, non tranchées :
  - Le CPM TikTok vaut 4,08 $ en médiane e-commerce selon une source, et 9 à 13 $ en campagne de conversion selon d'autres.
  - Le CPC Pinterest vaut 0,45 à 1,30 € selon Trackbee, et 1,50 $ en médiane selon Benchmarketing.
  - Meta : une source mentionne un seuil réduit d'environ 10 conversions par semaine (juin 2024), alors que la documentation récente cite toujours 50. ⚠️ à vérifier
- La page Meta sur la phase d'apprentissage n'a pas été consultée directement, seulement citée par des sources secondaires. ⚠️ à vérifier
- La phrase de Google sur le délai SEO aurait disparu de la version de juin 2026 de la page. ⚠️ à vérifier
- TVA : si l'imprimeur expédie depuis un autre pays de l'UE (Printful depuis la Lettonie ou l'Espagne), le seuil de 10 000 € ne s'appliquerait probablement pas. La TVA du pays du client serait due dès le premier euro. C'est une déduction du rapport. ⚠️ à vérifier avec un expert-comptable
- La Conversions API de Meta ne doit probablement pas recevoir les événements des visiteurs qui ont refusé les cookies. Aucune position officielle de Meta trouvée. ⚠️ à vérifier
- Frais réglementaires Etsy pour la France après le 22 juin 2026 : une source cite un passage de 0,47 % à 1,14 %. ⚠️ à vérifier dans le compte vendeur
- Le budget Pinterest de 50 à 100 $ par jour vient d'une agence et paraît haut.
- Le budget d'influence de 10 000 à 15 000 € vient d'une agence qui vend ce service.

## Retenu / écarté
