---
type: registre
title: A VERIFIER - Points à valider, vérifier, tester
status: validé
related: ["[[_conventions]]", "[[OVR - Drop shipping agentique]]", "[[SYN - Fournisseurs]]", "[[SYN - Juridique]]", "[[SYN - Système]]", "[[SYN - Choix de la niche]]", "[[SYN - Modèle économique]]", "[[SYN - Acquisition]]"]
decisions: []
last-verified: 2026-10-30
tags: [dropshipping, registre, a-verifier]
---
# A VERIFIER - Points à valider, vérifier, tester

Registre des points marqués ⚠️ dans les recherches, les synthèses et les décisions. Chaque
ligne dit quoi vérifier, par quel moyen, d'après quelle note, et avant quand. Quand un point
est tranché, on note le résultat et la date, on met à jour la note source, et on garde la
ligne barrée pour la traçabilité.

Moyens : **connecté** (tableau de bord Printify, Gelato, Printful ou Shopify), **échantillon**
(commande réelle), **expert** (expert-comptable, avocat), **test** (campagne ou vente réelle),
**lecture** (texte officiel, page à relire), **manuel** (relevé à la main sur un site).

Priorités : **P1** avant le 15/11/2026 (mise en ligne pour Noël) ; **P2** avant janvier 2027
(construction du système, fête des grands-mères) ; **P3** sans échéance.

## Fournisseurs

| Point à vérifier | Moyen | Source | Priorité | Résultat |
|---|---|---|---|---|
| ~~Imprimeurs Printify UE pour le mug 11 oz blanc, bicolore et magique, destination France~~ | connecté | [[RCH - Relevé connecté du catalogue Printify UE (29-10-2026)]] | — | tranché le 29/10/2026 : aucun sur le 535 ; OPT OnDemand 441 (5,88 $), Textildruck Europa 1016 (5,91 $), Harrier 1125 (5,47 $), port 6,89 $ puis 1,99 à 2,39 $ |
| Site qui expédie vers la France chez Harrier, WOYC, MWW On Demand, Printful et Jondo (plusieurs sites, non affiché) ; pour l'ornament 1676, l'API renvoie Harrier « United Kingdom » alors que le catalogue l'affiche en Europe (droit de 3 € et TVA à l'import si GB) | connecté, échantillon | [[RCH - Relevé connecté du catalogue Printify UE (29-10-2026)]], [[RCH - Décoration de sapin personnalisée grands-parents (29-10-2026)]] | P1 | |
| Identifiant de variante du mug 441 (62327 lu dans l'API interne) à confirmer par l'API publique ; pixels, DPI et format de fichier par imprimeur ; option de routage UE de la boutique | connecté | [[RCH - Relevé connecté du catalogue Printify UE (29-10-2026)]] | P1 | |
| Prix du mug 11 oz en euros chez Gelato France et Printful Lettonie ; tarif du 2e mug ; port réel | connecté | [[RCH - Vérification Printify UE du mug et vue d'ensemble des produits (28-10-2026)]] | P1 | |
| Échantillons de mug chez Printify UE et Gelato : qualité, délai réel, casse | échantillon | [[05 - Printify en principal avec partenaire UE figé, Gelato en second, franchise de TVA au départ]] | P1 | |
| Zone d'impression exacte du mug 11 oz chez l'imprimeur retenu (2475 × 1155, 2480 × 1146, 2700 × 1120 ou 2625 × 1050 px selon les sources) | connecté | [[RCH - Marché des mugs grands-parents avec prénoms (28-10-2026)]], [[RCH - Applications de personnalisation Shopify pour Printify et Gelato (29-10-2026)]] | P1 | |
| Les factures Printify, Gelato et Printful portent-elles une TVA, et est-elle récupérable selon le statut ? Printify facture la TVA sur l'UE, récupérable « si assujetti », sans mention de la franchise en base | expert | [[RCH - Relevé connecté du catalogue Printify UE (29-10-2026)]] | P1 | |
| Dates limites Noël 2026 de Printify, Gelato et Printful pour la France ; non publiées au 22/10, référence 2025 : Posterflow 27/11, Harrier 02/12, OPT 05/12, Textildruck 09/12 | lecture | [[RCH - Relevé connecté du catalogue Printify UE (29-10-2026)]], [[RCH - Décoration de sapin personnalisée grands-parents (29-10-2026)]] | P1 | |
| ~~Un même imprimeur UE fait-il le mug et un autre produit ?~~ | connecté | [[RCH - Relevé connecté du catalogue Printify UE (29-10-2026)]] | — | tranché le 29/10/2026 : OPT OnDemand (mug 441 + affiche 443), Textildruck Europa (mugs 1016-1018, 1117 + tote 731), Printful (mug 478 + tote 1930) |
| Deux blueprints d'un même imprimeur partent-ils dans un seul colis, au tarif « article suivant » ? Non documenté par l'API ; cas du mug 1125 et de l'ornament 1676 chez Harrier ; l'aide Printify dit que deux types de produit paient chacun un premier article, ce qui vise aussi mug 441 + affiche 443 ou sticker 476 (OPT) et mug 1016 + tote 731 (Textildruck) | commande test | [[RCH - Relevé connecté du catalogue Printify UE (29-10-2026)]], [[RCH - Décoration de sapin personnalisée grands-parents (29-10-2026)]], [[RCH - Carte de vœux et étiquette cadeau grands-parents (29-10-2026)]] | P1 | |
| Sticker carré 476 chez OPT : vendu à la pièce ou par lot, zone en pixels, fond perdu, format de fichier ; carte 524 Print Pigeons : recto seul ou recto-verso, intérieur | connecté | [[RCH - Carte de vœux et étiquette cadeau grands-parents (29-10-2026)]] | P2 | |
| ~~Chaussette de Noël chez un imprimeur UE~~ | connecté | [[RCH - Chaussette de Noël personnalisée grands-parents (29-10-2026)]] | — | tranché le 29/10/2026 : aucun ; US, GB (Print Clever) ou CN (Printdoors), coût rendu 18 à 39 € |
| Ornament 1676 chez Harrier : forme ronde ou carrée, format de fichier, rendu des petits textes et des accents sur 990 × 990 px, emballage et casse ; verso affiché dans l'éditeur du bois 697 (WOYC) | connecté, échantillon | [[RCH - Décoration de sapin personnalisée grands-parents (29-10-2026)]] | P1 | |
| Ornament fabriqué dans l'UE chez Gelato (aucun trouvé en public) et chez Printful (céramique au catalogue, site, prix et port France inconnus) | connecté | [[RCH - Décoration de sapin personnalisée grands-parents (29-10-2026)]] | P2 | |
| ~~Nom et pays du fournisseur « only ships from EU » du Corkwood Coaster Set~~ | connecté | [[RCH - Relevé connecté du catalogue Printify UE (29-10-2026)]] | — | tranché le 29/10/2026 : aucun imprimeur UE sur 510 et 480 ; seul sous-verre UE : céramique 1523 chez WOYC (Italie), 8,37 $ l'unité |
| ~~Coussin et tablier chez un imprimeur Printify UE~~ | connecté | [[RCH - Relevé connecté du catalogue Printify UE (29-10-2026)]] | — | tranché le 29/10/2026 : MWW On Demand, site Allemagne, housse 229 (11,71 à 13,89 $), coussin 220, tablier AOP 418 (22,54 $) ; zone en px non relevée |
| ~~Prix Printify du tablier Textildruck et attribution du torchon Greenbomb~~ | connecté | [[RCH - Relevé connecté du catalogue Printify UE (29-10-2026)]] | — | tranché le 29/10/2026 : ni le tablier Textildruck ni le torchon Greenbomb ne sont trouvés en connecté ; le tablier UE est le 418 chez MWW ; aucun torchon UE |
| ~~Prix Posterflow par format d'affiche, avec et sans cadre~~ | connecté | [[RCH - Relevé connecté du catalogue Printify UE (29-10-2026)]] | — | tranché le 29/10/2026 : A4 9,26 $, A3 et 30 × 40 11,15 $, 50 × 70 15,86 $, port 16,29 $ ; encadré 22,66 à 41,54 $ ; OPT OnDemand A4 6,50 $, port 6,09 $ |
| Emballage Posterflow : tube ou plat, taux de casse ; prix Gelato et Printful par format d'affiche livrés en France | échantillon, connecté | [[RCH - Affiche personnalisée grands-parents (28-10-2026)]] | P3 | |
| Affiche 443 OPT : emballage (tube ou plat), grammage, fond perdu, profil couleur, format de fichier ; pays d'origine « Made in China » sur la fiche contre imprimeur en Tchéquie ; production 0,7 jour (catalogue) contre 2 à 5 jours (page réseau) | connecté, échantillon | [[RCH - Validation de l'affiche grands-parents en produit compagnon du mug (29-10-2026)]] | P1 | |
| Tote 731 Textildruck : identifiants de variantes par coloris dans l'API publique ; contenu et langue de l'étiquette cousue ; fichier PNG transparent accepté ou non ; tenue du DTG sur fond foncé ; tote AOP 1389 a-t-il un imprimeur UE avec toile claire ? | connecté, échantillon | [[RCH - Validation du tote bag compagnon du mug (29-10-2026)]] | P1 si le tote est retenu | |
| Housse 229 MWW : départ réel d'Allemagne et TVA facturée ; recto à gauche ou à droite du panneau double ; fichier à 300 DPI accepté pour une zone définie à 150 DPI ; emplacement de la fermeture ; étiquette de composition en français | connecté, échantillon | [[RCH - Validation de la housse de coussin grands-parents (29-10-2026)]] | P1 si la housse est retenue, sinon P2 | |
| Ports vers la France d'Atelier Katanga et de Textildruck Europa | connecté | [[RCH - Textile personnalisé grands-parents, tote bag en priorité (28-10-2026)]] | P2 | |
| ~~Tumbler ou travel mug chez un imprimeur UE ; l'article Textildruck à 12,75 $~~ | connecté | [[RCH - Relevé connecté du catalogue Printify UE (29-10-2026)]] | — | tranché le 29/10/2026 : seul gobelet inox UE, 1927 chez Printful (LV) à 21,79 $ ; le Mason Jar 742 est en verre givré |
| ~~Plaid chez un imprimeur UE ; prix UE par taille~~ | connecté | [[RCH - Relevé connecté du catalogue Printify UE (29-10-2026)]] | — | tranché le 29/10/2026 : Sherpa 238 et 736 chez MWW On Demand (site DE), 24,81 à 49,26 $, port 10,39 à 24,49 $ ; Gelato non vérifié |
| ~~Planche, boîte alimentaire ou bougie chez un fournisseur UE relié à Shopify~~ | connecté | [[RCH - Relevé connecté du catalogue Printify UE (29-10-2026)]] | — | tranché le 29/10/2026 : aucun imprimeur UE chez Printify pour bougies, planches, puzzles et boîtes métal |
| Gelato accepte-t-il de relever le plafond de 5 000 appels par jour ? Printify a-t-il un environnement de test ? Date de l'API T-Pop | lecture | [[SYN - Fournisseurs]] | P3 | |
| Notes Trustpilot et retours français actuels sur Printify, Gelato et Printful | manuel | [[SYN - Fournisseurs]] | P3 | |

## Juridique et fiscal

| Point à vérifier | Moyen | Source | Priorité | Résultat |
|---|---|---|---|---|
| Schéma de TVA selon le pays d'expédition réel de l'imprimeur ; la franchise tient-elle si l'imprimeur expédie depuis l'Allemagne ou la Lettonie ? | expert | [[SYN - Juridique]], [[05 - Printify en principal avec partenaire UE figé, Gelato en second, franchise de TVA au départ]] | P2 (avant janvier 2027) | |
| Frontière catalogue ou personnalisé pour la rétractation, et rédaction des CGV | expert (avocat) | [[SYN - Juridique]] | P1 | |
| Textes de L221-28 3°, L221-5 (information sur l'absence de rétractation) et L221-23 à lire sur Légifrance ; l'image envoyée par la cliente vaut-elle « spécification du consommateur » ? | lecture, expert (avocat) | [[RCH - Retours, rétractation et abus (30-10-2026)]] | P1 | |
| Shopify rend-il les frais de paiement lors d'un remboursement ? | lecture, connecté | [[RCH - Retours, rétractation et abus (30-10-2026)]] | P2 | |
| Professionnel acheteur : seuil « moins de 5 » ou « 5 au plus » salariés, et application à la vente à distance (L221-3) ; abus du droit de rétractation et refus des commandes suivantes en droit français (sources belges seulement) | lecture, expert | [[RCH - Retours, rétractation et abus (30-10-2026)]] | P3 | |
| Solution Shopify pour le bouton « Renoncer au contrat ici » obligatoire depuis le 19/06/2026 | lecture, test | [[RCH - Cadre juridique (22-10-2026)]] | P1 | |
| Personne responsable GPSR pour chaque produit : l'imprimeur UE ou la boutique ? Documentation fournie par Printify, Gelato, Printful | lecture, connecté | [[SYN - Juridique]], [[RCH - Affiche personnalisée grands-parents (28-10-2026)]] | P1 | |
| Déclaration de conformité contact alimentaire (CE 1935/2004) du mug retenu, puis du gobelet et de la planche | lecture, connecté | [[RCH - Gobelet isotherme grands-parents (28-10-2026)]], [[RCH - Planche à découper et planche apéro grands-parents (29-10-2026)]] | P1 pour le mug | |
| Frais de traitement douaniers de 2 € par article annoncés au 01/11/2026, sur le texte officiel | lecture | [[SYN - Juridique]] | P2 | |
| Droit de 3 € : « par article » ou « par catégorie tarifaire » ; les textes officiels disent par catégorie | lecture | [[RCH - Synthèse comparative des produits d'élargissement (29-10-2026)]] | P3 | |
| Propriété des sorties dans les conditions Google (Nano Banana Pro) ; portée de la clause « Powered by Ideogram » pour une boutique | lecture | [[RCH - Images IA, modèles et plateformes (29-10-2026)]] | P2 | |
| La boutique est-elle « fournisseur » (art. 50(2) AI Act) avec une interface interne devant une API, ou « déployeur » ? Un design non photoréaliste sur mug relève-t-il de l'art. 50(4) ? | expert | [[RCH - Images IA, modèles et plateformes (29-10-2026)]] | P2 | |
| Règle Amazon de juillet 2026 sur les visages synthétiques, obligation de déclaration IA sur Shopify, politique vendeur Etsy du 14/01/2026 (sources secondaires) | lecture | [[RCH - Images IA, modèles et plateformes (29-10-2026)]] | P3 | |
| Règles Meta sur les publicités de produits personnalisés ; règles TikTok et Google Ads sur les visuels IA | lecture | [[SYN - Juridique]] | P2 | |
| Statut de l'amendement L. 331-4-2 (style d'un auteur identifiable) | lecture | [[RCH - Images IA, modèles et plateformes (29-10-2026)]] | P3 | |
| Dépôt du nom de la boutique comme marque | expert | [[SYN - Juridique]] | P2 | |
| Assurance responsabilité civile professionnelle | expert | [[SYN - Juridique]] | P2 | |
| Décisions TJ Paris du 17/09/2026 et du 27/08/2026 citées par la recherche juridique, sur le texte intégral | lecture | [[RCH - Cadre juridique (22-10-2026)]] | P3 | |
| Statut de marque éventuel de l'expression « Fête des grands-mères » (origine Café Grand'Mère, 1987) | lecture (INPI) | [[RCH - Marché des mugs grands-parents avec prénoms (28-10-2026)]] | P2 | |
| Étiquetage textile : « 100 % coton » utilisable ou non pour un tablier à enduction polyester | lecture | [[RCH - Tablier personnalisé grands-parents (28-10-2026)]] | P3 | |
| Décorations de Noël : statut au regard de la directive jouets, mention « ne convient pas aux moins de 3 ans », risque du ruban, obligations GPSR | lecture, expert | [[RCH - Décoration de sapin personnalisée grands-parents (29-10-2026)]] | P1 si la décoration est testée à Noël | |

## Système

| Point à vérifier | Moyen | Source | Priorité | Résultat |
|---|---|---|---|---|
| Commande externe Printify avec un fichier d'impression propre à la commande : le schéma `lineItemWithBlueprint` de l'API publique l'accepte ; reste à exécuter une commande réelle avant le 05/11 ; repli Printful si échec | test | [[08 - Personnalisation à la commande en génération interne, test Printify avant le 5 novembre]], [[RCH - Relevé connecté du catalogue Printify UE (29-10-2026)]] | P1 (avant le 05/11) | schéma confirmé dans openapi.json le 29/10 ; commande réelle à faire |
| Absence de double commande après découplage de la synchro Shopify-Printify : aucun réglage par produit trouvé ; une commande sans produit Printify lié arrive dans « Other orders » ; vérifier qu'un produit Shopify non créé par Printify n'est pas importé | test | [[08 - Personnalisation à la commande en génération interne, test Printify avant le 5 novembre]], [[RCH - Relevé connecté du catalogue Printify UE (29-10-2026)]] | P1 | |
| Printify répond-il 409 (code 8503) sur un `external_id` en doublon, en nommant la commande existante ? Source communautaire seulement | test (commande externe du 05/11) | [[FLOW - Personnalisation à la commande]] | P1 (avant le 05/11) | |
| Le réglage d'approbation Manual tient-il pour une commande créée par l'API, sans départ automatique après 24 heures ni facturation avant `send_to_production` ? | connecté, test (commande externe du 05/11) | [[FLOW - Personnalisation à la commande]] | P1 (avant le 05/11) | |
| La boutique appartient-elle à l'organisation Shopify d'Antoine (client credentials grant) ? | connecté | [[SYN - Système]] | P1 | |
| Police et OCR du rendu interne sur é, è, ê, ë, ï, ç, œ et prénoms composés ; limite de 15 caractères et réduction automatique | test | [[08 - Personnalisation à la commande en génération interne, test Printify avant le 5 novembre]] | P1 | |
| ~~Personnalisation à la commande : application tierce ou fichier généré par le système~~ | — | [[RCH - Applications de personnalisation Shopify pour Printify et Gelato (29-10-2026)]] | — | tranché le 29/10/2026 : génération interne, décision 08 |
| La soumission automatique Printify fonctionne-t-elle pour des commandes Shopify personnalisées par une application tierce ? Approbation manuelle obligatoire ou non | connecté, test | [[RCH - Applications de personnalisation Shopify pour Printify et Gelato (29-10-2026)]] | P1 | |
| Règle « 100 commandes gratuites » de Teeinblue : mensuelle ou unique ; plan gratuit Customily existe-t-il encore ? | lecture | [[RCH - Applications de personnalisation Shopify pour Printify et Gelato (29-10-2026)]] | P2 | |
| Import en masse de gabarits (CSV, JSON, PSD) dans une application de personnalisation | lecture, test | [[RCH - Applications de personnalisation Shopify pour Printify et Gelato (29-10-2026)]] | P2 | |
| SynthID, C2PA et IPTC survivent-ils à l'agrandissement, à l'ajout du texte, au téléversement Shopify et au flux Merchant Center ? | test | [[RCH - Images IA, modèles et plateformes (29-10-2026)]] | P2 | |
| C2PA sur les sorties Nano Banana Pro : présent ou « à venir » | test | [[RCH - Images IA, modèles et plateformes (29-10-2026)]] | P2 | |
| Conditions commerciales de Nano Banana Pro et Ideogram au moment du test (modèle en preview, nouvelles conditions Google en aperçu) | lecture | [[06 - LangGraph au départ, interface d'images interne avec Nano Banana Pro et Ideogram]] | P1 | |
| Calculs du rapport statistique à refaire avec scipy et à calibrer par simulation ; seuils de l'analyste | test | [[RCH - Méthodes statistiques pour garder ou retirer un produit (25-10-2026)]] | P2 | |
| `shopifyqlQuery` : regroupement par identifiant produit ; métrique de vues par produit en 2026-10 ; délai d'obtention de `read_all_orders` | connecté | [[SYN - Système]] | P2 | |
| Accès à l'alpha Google Trends et à l'API Pinterest Trends | lecture | [[SYN - Système]] | P2 | |
| Branche maintenue de Pydantic AI (v1 ou v2) | lecture | [[SYN - Système]] | P3 | |
| Taux d'erreur réel du juge vision-langage sur les personnages protégés ; coût par design vendu selon le modèle (A/B sur Noël) | test | [[SYN - Système]] | P2 | |
| Rendu réel d'une illustration riche en sublimation sur sherpa, polaire, polyester de tablier, verre ; tenue au lavage du DTG sur coton écru | échantillon | [[RCH - Plaid personnalisé grands-parents (28-10-2026)]], [[RCH - Tablier personnalisé grands-parents (28-10-2026)]], [[RCH - Torchon personnalisé grands-parents (28-10-2026)]] | P3 | |
| Accents dans les éditeurs de gravure et dans la saisie Printify | test | [[RCH - Planche à découper et planche apéro grands-parents (29-10-2026)]] | P3 | |

## Marché

| Point à vérifier | Moyen | Source | Priorité | Résultat |
|---|---|---|---|---|
| Volumes Google Keyword Planner et courbes Google Trends France pour « mug mamie personnalisé », « cadeau mamie prénoms petits-enfants », « mug fête des grands-mères », « affiche mamie », « plaid mamie » ; jamais obtenus par aucune recherche | manuel | [[SYN - Choix de la niche]] | P1 | |
| Bibliothèque publicitaire Meta : publicités actives de Cadeau Plus, Henriette and Co, Famille de Dingue, Monsieur TShirt, Cadeaux.com, CadoMaestro | manuel | [[SYN - Choix de la niche]] | P2 | |
| Une illustration fixe sans réglage des personnages convertit-elle à 24,90 € face aux avatars réglables au même prix ? | test (Noël 2026) | [[02 - Mug famille illustrée à 24,90 €, panier cible 45 €]], [[RCH - Marché des mugs grands-parents avec prénoms (28-10-2026)]] | P1 | |
| Sites non audités sur plusieurs produits : Famille de Dingue, Jusqu'à la lune, Ma Petite Fabrique, CadoMaestro, Cadeau Plus ; Amazon.fr et Etsy FR en détail pour la planche, la boîte, la bougie | manuel | [[RCH - Synthèse comparative des produits d'élargissement (29-10-2026)]] | P3 | |
| Lot tablier + torchon d'Ourson Câlin, et « Family Portrait » sur sous-verres (présence à confirmer) | manuel | [[RCH - Torchon personnalisé grands-parents (28-10-2026)]], [[RCH - Sous-verres personnalisés pour grands-parents (28-10-2026)]] | P3 | |
| Lien entre Cadeaux.com et Monsieur TShirt (même ville, mêmes paliers de remise) | manuel | [[RCH - Bougie personnalisée grands-parents (29-10-2026)]] | P3 | |
| Fête des grands-mères 2027 : 7 mars (La Poste) ; « 2 mars » chez Cadeaux.com et « 1er mars » sur des sites non mis à jour | lecture | [[SYN - Choix de la niche]] | P3 | tenu : 7 mars 2027, premier dimanche de mars |
| Sondages cités (BVA pour Interflora 2017, IFOP pour Florajet, « 52 % des grands-mères ») : sources primaires à retrouver | lecture | [[RCH - Marché des mugs grands-parents avec prénoms (28-10-2026)]], [[RCH - Torchon personnalisé grands-parents (28-10-2026)]] | P3 | |
| Demande « Papi » comparée à « Mamie » ; déclinaisons UE (Oma, Nonna, Abuela, Bonne-maman) | manuel, test | [[SYN - Choix de la niche]] | P3 | |
| Puzzle : produit non étudié | recherche | [[RCH - Synthèse comparative des produits d'élargissement (29-10-2026)]] | P3 | |
| Décorations de sapin : dates limites de commande Noël 2026 des concurrents, part des ventes en novembre et décembre, offres d'Henriette and Co, Cadeau Plus, Jusqu'à la lune et Ma Petite Fabrique (non trouvées) | manuel | [[RCH - Décoration de sapin personnalisée grands-parents (29-10-2026)]] | P3 | |
| Taux de change à retenir pour les marges : 0,86 et 0,92 utilisés, 0,897 au taux BCE du 27/10/2026 ; marges à 0,86 surestimées d'environ 4 % | lecture | [[RCH - Synthèse comparative des produits d'élargissement (29-10-2026)]] | P3 | |

## Tranchés
(déplacer ici les lignes résolues, avec résultat et date)
