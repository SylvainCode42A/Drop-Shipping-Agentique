---
type: research
title: RCH - Applications de personnalisation Shopify pour Printify et Gelato (29-10-2026)
status: validé
related: ["[[SYN - Fournisseurs]]", "[[NICHE - Grands-parents]]"]
decisions: []
last-verified: 2026-10-29
date: 2026-10-29
sources: [help.printify.com, printify.com/personalization, teeinblue.com/pages/pricing, customily.com/new-pricing, help.customily.com, apps.shopify.com, gelato.com/subscription-plans, support.gelato.com, print.app/compare/zakeke, ecommerce-platforms.com, hackceleration.com, mydesigns.io]
tags: [dropshipping, fournisseurs, personnalisation]
---
# RCH - Applications de personnalisation Shopify pour Printify et Gelato (29-10-2026)

## Contexte posé
Boutique Shopify française en impression à la demande. Produits : mug 11 oz (départ à 24,90 €), affiches, tote bags, sous-verres, coussins. Les designs sont des illustrations fixes générées par IA, avec une zone de texte où la cliente saisit de 1 à 8 prénoms. Les gabarits viennent d'un système Python externe piloté par des agents, qui doit pousser des gabarits et récupérer les fichiers d'impression par API. Fournisseur principal : Printify avec un imprimeur UE. Fournisseur secondaire : Gelato. Acheteuse type : femme adulte ; occasions : Noël, Fête des grands-mères (07/03/2027), Fête des grands-pères (03/10/2027).

Question : documenter les applications compatibles selon dix critères (prix, intégration Printify et Gelato, aperçu, champs texte, gabarits, fichier d'impression, API, fiabilité, mise en place, limites), sans rien décider.

## Conclusion en une phrase
Plusieurs applications automatisent le flux de la commande jusqu'à Printify, mais aucune source trouvée ne montre qu'un système externe peut leur pousser des gabarits par API publique.

## Résultats

### Résumé
1. Seules quatre applications couvrent le flux complet (aperçu en direct, fichier d'impression automatique, envoi au fournisseur) avec Printify : Teeinblue, Customily, HelloCustom et AnywherePOD. Teeinblue et Customily couvrent aussi Gelato.
2. Gelato a son propre outil, Personalization Studio, inclus dans Gelato+. La personnalisation native de Printify est gratuite, mais ses documents se contredisent sur la validation manuelle.
3. Zepto, Infinite Options et Bold collectent du texte, mais ne produisent pas de fichier d'impression envoyé à Printify.
4. Aucune API publique de gabarits trouvée chez Teeinblue, Customily, HelloCustom ou Gelato. Zakeke a une API d'accès restreint et des webhooks.
5. Accents français, changement de mise en page selon le nombre de prénoms et format du bandeau de mug chez l'imprimeur UE : non documentés, à tester.

### Teeinblue
- **Prix.** Un plan à 49 $ par mois. 100 premières commandes sans frais, puis 0,40 $ par article (101 à 1 000), 0,20 $ (1 001 à 10 000), 0,10 $ au-delà. Frais par article personnalisé, pas par régénération ; une quantité de 5 sur une ligne compte une fois. Essai de 14 jours. Source : teeinblue.com/pages/pricing.
- **Printify et Gelato.** Compatible Printful, Dreamship, ShineOn, Gelato, Printify, merchOne (fiche App Store). Liaison par clé API du fournisseur collée dans la page Fulfillments (support.teeinblue.com). Délai commande vers fournisseur : non trouvé.
- **Aperçu.** Aperçu en temps réel et fichier d'impression automatique annoncés (blog Teeinblue, 06/08/2025). Temps de chargement et mobile : non mesurés.
- **Champs et gabarits.** Logique conditionnelle, suppléments de prix, synchronisation d'options entre gabarits, actions en masse annoncés. Accents, texte en arc, police dégressive : non vérifiés.
- **API.** Aucune API publique de gabarits trouvée. Export manuel des commandes en CSV mentionné dans l'aide.
- **Fiabilité.** 4,8 sur 329 avis (93 % de 5 étoiles, 3 % de 1 étoile, relevé mai 2026) ; un relevé plus récent affiche 379 avis. Plainte : mises à jour ayant figé les produits d'un marchand, sans réponse du support pendant l'incident (réponse Teeinblue du 23/01/2026). Support en français : non trouvé ; un avis en français salue la réactivité.

### Customily
- **Prix.** À partir de 49 $ par mois et par plateforme, plus 1 $ par article (1 à 100), 0,50 $ (101 à 1 000), 0,25 $ (1 001 à 10 000). Source : customily.com.
- **Printify et Gelato.** Fiche App Store : Printful, Printify, Gelato, ShineOn, CustomCat, teelaunch. Selon Printify, Customily crée le fichier d'impression après l'achat et l'envoie en production. Soumission automatique réglable dans les paramètres d'approbation Printify (help.customily.com).
- **Champs texte.** Longueur maximale par champ avec compteur ; conditions pour afficher ou masquer une option selon les choix précédents. Correspond au besoin « champ 5 visible seulement si 4 prénoms », sans test réel.
- **Gabarits.** Texte en arc avec taille de police minimale et maximale ; import de polices illimité.
- **API.** Non trouvée pour Shopify. Intégrations personnalisées réservées aux plans illimités, sur une grille distincte (BigCommerce, Magento, Walmart).
- **Fiabilité.** 4,7 sur 245 avis. Un avis d'avril 2026 cite un à deux jours d'apprentissage. Support annoncé en anglais et en vietnamien.

### Zakeke
- **Prix.** Shopify, août 2026 : 69,90 $ pour 10 produits publiés et 1,9 % par vente ; 129,90 $ pour 50 produits et 1,7 % ; 299,90 $ pour 100 produits et 1,5 % (print.app). Commission sur le prix payé, dans la devise du client, seulement si vendu.
- **Printify et Gelato.** Aucune intégration directe trouvée. Déclencheur Zapier à chaque commande personnalisée une fois les fichiers prêts ; webhook utilisé par Order Desk.
- **API.** Documentation derrière authentification.
- **Fiabilité.** 4,5 sur 101 avis ; avis de septembre 2026 sur des limites de stockage et frais ajoutés sur des plans « illimités ».

### HelloCustom
- **Prix.** À partir de 24,99 $ par mois en annuel, plus 0,29 $ par vente, essai de 14 jours (help.printify.com).
- **Fonctionnement.** Reconnaît noms, dates, adresses dans le design ; personnalisation partielle si le design contient une image. Adapté en principe à une illustration fixe avec zone de prénoms, sans test.
- **Gelato, API, note App Store, accents :** non trouvés.

### AnywherePOD
- **Prix.** Basic 9,99 $ (texte seul, un fournisseur) ; PRO 24,99 $ (images, cliparts, mockups, deux fournisseurs). Une version de la fiche indique 0,29 $ par commande personnalisée après 50 sur PRO.
- **Printify et Gelato.** Etsy, Printify, CustomCat, ShineOn, teelaunch, Canva. Gelato non listé.
- **Fiabilité.** 4,4 sur 17 avis. Volume faible.

### Zepto Product Personalizer
- **Prix.** 9,99 $ / 19,99 $ / 29,99 $ / 49,99 $ par mois. Pas de frais par commande trouvés.
- **Printify et Gelato.** Gelato listé dans les compatibilités, note 4,9 sur 1 264 avis. Printful documente une liaison. Printify non listé.
- **Fichier d'impression.** Contradiction : un concurrent dit que Zepto n'en génère pas ; un annuaire dit qu'il exporte des fichiers prêts à imprimer.

### Infinite Options (ShopPad)
- 12,99 $ par mois, 4,8 sur 3 926 avis. Logique conditionnelle, suppléments de prix, choix joints à la commande dans l'admin Shopify.
- Pas d'aperçu sur mockup, pas de fichier d'impression, pas d'intégration Printify ou Gelato trouvée. Le texte arrive comme propriété de ligne de commande.

### Bold Product Options
- Capterra : « contacter le vendeur » pour le prix. Un annuaire compte 2 375 avis. Disponibilité actuelle, prix et intégrations : ⚠️ à vérifier.

### Printify natif (Product Creator)
- **Prix.** Gratuit ; Printify Premium (24,99 $ par mois en annuel) ajoute jusqu'à 20 % de remise.
- **Shopify.** Texte et images saisis sur la fiche produit, synchronisés avec la commande. L'aperçu rendu (Live Previews, juin 2026) est annoncé pour Etsy et l'habillement, pas pour Shopify.
- **Polices et texte.** Import illimité de polices TTF ou OTF ; texte long réduit pour tenir dans le calque.
- **Validation.** Contradiction dans l'aide : approbation manuelle obligatoire d'un côté, soumission automatique possible de l'autre. Un marchand se plaint au contraire de commandes à revoir parties seules en production.

### Gelato Personalization Studio
- **Prix.** Inclus dans Gelato+ (19,99 $ par mois en annuel, 29,99 $ en mensuel). Une source décrit une offre séparée : Starter gratuit à 6 %, ou Regular à 19 $ par mois avec 4 % après le 21e article et 1 $ minimum.
- **Fonctions.** Sur Shopify, options sur la page avec aperçu en direct ; texte avec police, taille et position ; conditions. Réservé à Shopify et Etsy.
- **API.** API de commandes Gelato avec clé X-API-KEY et commandes de test. API de gabarits Personalization Studio : non trouvée.
- **Fiabilité.** Application Gelato notée 4,8 sur 759 avis.

### Autres applications repérées (non approfondies)
- Customix : annonce Printful, Printify et Gelato.
- Personalize.design : annonce Gelato, Printful, Printify ; 19 $ par mois ; sans avis.
- TailorKit : annonce des fichiers SVG et PNG envoyés automatiquement à Printify et ShineOn.

### Tableau comparatif
| Application | Prix de base | Frais par commande | Printify auto | Gelato auto | Aperçu Shopify | Conditions | API gabarits |
|---|---|---|---|---|---|---|---|
| Teeinblue | 49 $ | 0 à 0,40 $ | Oui | Oui | Oui | Oui | Non trouvée |
| Customily | 49 $ | 0,25 à 1 $ | Oui | Annoncé | Oui | Oui | Non trouvée |
| Zakeke | 69,90 à 299,90 $ | 1,5 à 1,9 % | Non trouvé | Non trouvé | Oui | Non vérifié | Restreinte |
| HelloCustom | 24,99 $ | 0,29 $ | Oui | Non trouvé | Non vérifié | Non vérifié | Non trouvée |
| AnywherePOD | 9,99 à 24,99 $ | 0 ou 0,29 $ | Oui | Non | Annoncé | Non vérifié | Non trouvée |
| Zepto | 9,99 à 49,99 $ | 0 | Non | Contradictoire | Oui | Oui | Non trouvée |
| Infinite Options | 12,99 $ | 0 | Non | Non | Non | Oui | Non trouvée |
| Bold | ⚠️ | ⚠️ | Non trouvé | Non trouvé | ⚠️ | ⚠️ | ⚠️ |
| Printify natif | 0 $ | 0 | Natif | Non | Non (Etsy oui) | Non trouvé | Non documentée |
| Gelato natif | Gelato+ | 0 ou 4 à 6 % | Non | Natif | Oui | Oui | Non trouvée |

### Scénarios de coût mensuel
Application seule. Hypothèses : 1 article par commande, paliers remis à zéro chaque mois (estimé).

| Application | 50 commandes | 200 commandes | 500 commandes |
|---|---|---|---|
| Teeinblue | 49 $ | 89 $ | 209 $ |
| Customily | 99 $ | 199 $ | 349 $ |
| HelloCustom | 39,49 $ | 82,99 $ | 169,99 $ |
| AnywherePOD Basic | 9,99 $ | 9,99 $ | 9,99 $ |
| Zakeke (50 produits) | 129,90 $ + 21,17 € | 129,90 $ + 84,66 € | 129,90 $ + 211,65 € |
| Zepto Starter | 9,99 $ | 9,99 $ | 9,99 $ |
| Infinite Options | 12,99 $ | 12,99 $ | 12,99 $ |
| Printify natif | 0 $ | 0 $ | 0 $ |
| Gelato+ annuel | 19,99 $ | 19,99 $ | 19,99 $ |

Exclus : abonnement Shopify, coût produit, livraison. Zepto, Infinite Options et Printify natif impliquent un fichier d'impression produit ailleurs, donc un coût en temps ou en développement non chiffré.

### Implications pour le système d'agents
- **Pousser des gabarits.** Aucune API publique de gabarits trouvée. Les agents ne pourraient pas créer un gabarit directement chez Teeinblue, Customily, HelloCustom ou Gelato sans passer par l'interface ou un import en masse.
- **Récupérer les fichiers.** Zakeke est la seule source avec webhook et déclencheur Zapier « fichiers prêts ». Les autres envoient le fichier directement au fournisseur ; le système le lirait côté Printify.
- **Architecture alternative documentée.** L'API Printify crée un produit avec zones d'impression et images positionnées, et gère des webhooks (création de commande). Le système Python pourrait générer lui-même le fichier et le pousser, avec une simple application de champs pour la saisie. Contrepartie : pas d'aperçu sur mockup, sauf avec Zepto.
- **Mise en page selon le nombre de prénoms.** Aucune application ne documente un changement automatique selon le nombre de champs remplis. Les conditions (Customily, Teeinblue, Gelato) pourraient simuler 1-2, 3-4 et 5-8 avec des calques affichés ou masqués, sans preuve.

### Questions ouvertes
- La règle « 100 commandes gratuites » de Teeinblue est-elle mensuelle ou unique sur la vie du compte ?
- Customily a-t-il encore un plan gratuit, comme l'indique la fiche App Store ?
- L'imprimeur UE de Printify pour le mug 11 oz attend-il 2475 × 1155 px ou un autre format ?
- Quelle application rend correctement é, è, ê, ë, ï, ç, œ et un prénom composé avec tiret, avec quelle police ?
- La soumission automatique Printify fonctionne-t-elle pour des commandes Shopify personnalisées par une application tierce ?
- Quel est le temps de chargement de l'aperçu sur mobile pour chaque application, sur le thème choisi ?
- Une application permet-elle d'importer en masse des gabarits depuis un fichier (CSV, JSON, PSD) ?
- Le support en français existe-t-il chez l'une d'elles ?

## Chiffres

### Sourcés (consultés le 29/10/2026)
| Chiffre | Source et date |
|---|---|
| Teeinblue : 49 $, 100 commandes gratuites, 0,40 / 0,20 / 0,10 $ | teeinblue.com/pages/pricing, page 2026 |
| Teeinblue : 4,8 sur 329 avis | apps.shopify.com, relevé mai 2026 |
| Customily : 49 $ + 1 / 0,50 / 0,25 $ | customily.com, page 2026 |
| Customily : 4,7 sur 245 avis | apps.shopify.com, avis avril 2026 |
| Zakeke : 69,90 / 129,90 / 299,90 $ et 1,9 / 1,7 / 1,5 % | print.app/compare/zakeke, août 2026 |
| HelloCustom : 24,99 $ + 0,29 $ | help.printify.com, date non affichée |
| AnywherePOD : 9,99 $ et 24,99 $ | apps.shopify.com, 2026 |
| Zepto : 9,99 à 49,99 $ | analyzify.com, date non affichée |
| Infinite Options : 12,99 $, 4,8 sur 3 926 avis | apps.shopify.com, 2026 |
| Gelato+ : 19,99 $ annuel, 29,99 $ mensuel | gelato.com/subscription-plans, 2026 |
| Gelato Personalization Studio séparé : 6 %, ou 19 $ + 4 % | ecommerce-platforms.com, 2026 |
| Mug 11 oz : 2475 × 1155 px (District Photo), 2625 × 1050 px (SwiftPOD) | mydesigns.io, date non affichée |

### Estimés
- Scénarios de coût : estimés (1 article par commande, paliers mensuels).
- Zakeke : 1,7 % de 24,90 € par commande, estimé.
- Mise en place pour 10 à 30 produits : non sourcé. Estimé à 1 à 3 jours pour Printify natif ou Gelato, 3 à 10 jours pour Teeinblue ou Customily.

## Caveats
- ⚠️ La page Printify listant les outils tiers a pu être tronquée à la lecture : elle s'arrête après AnywherePOD.
- ⚠️ Contradiction Customily : paiement à l'usage sans engagement (Printify), 49 $ par mois plus frais (Customily), plan gratuit (App Store).
- ⚠️ Contradiction Gelato+ : 29,99 $ en mensuel (gelato.com) contre 23,99 $ (hackceleration.com, juin 2026).
- ⚠️ Contradiction Printify : approbation manuelle obligatoire ou soumission automatique possible.
- ⚠️ Contradiction AnywherePOD : PRO sans frais ou avec 0,29 $ après 50 commandes.
- ⚠️ Contradiction Zepto : fichier d'impression exporté ou non.
- ⚠️ Format du mug : un outil tiers attribue 2700 × 1100 px au mug 11 oz de Printify, différent du 2475 × 1155 px du brief.
- ⚠️ Aucune source sur les accents, CMJN, A3, résolution des fichiers générés ou incidents de Noël propres aux applications. Printify a publié des retards de production chez certains imprimeurs en décembre 2025 (printify.com/network-fulfillment-status).
- Les notes App Store bougent vite ; plusieurs relevés différents existent pour une même application.

## Retenu / écarté
(rempli à la revue)
