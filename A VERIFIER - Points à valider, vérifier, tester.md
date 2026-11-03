---
type: registre
title: A VERIFIER - Points à valider, vérifier, tester
status: validé
related:
  - "[[Drop-Shipping-Agentique/_conventions]]"
  - "[[OVR - Drop shipping agentique]]"
  - "[[SYN - Fournisseurs]]"
  - "[[SYN - Juridique]]"
  - "[[SYN - Système]]"
  - "[[SYN - Choix de la niche]]"
  - "[[SYN - Modèle économique]]"
  - "[[SYN - Acquisition]]"
decisions: []
last-verified: 2026-11-02
tags:
  - dropshipping
  - registre
  - a-verifier
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
| Échantillons de mug chez Printify UE et Gelato : qualité, délai réel, casse | échantillon | [[05 - Printify seul fournisseur avec partenaire UE figé, franchise de TVA au départ]] | P1 | |
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
| Réimpression Printify après défaut ou casse : port refacturé ou non (« free reprints » selon Merchant Protection, non précisé par l'aide) ; formulaire « Submit issue » à voir sur une vraie commande (types de problème, champs) | connecté, échantillon | [[RCH - Défauts produit, casse et réclamations Printify (31-10-2026)]] | P1 | |
| API Printify : aucun point d'accès pour signaler un problème ou demander une réimpression, d'après une copie de la spécification (api-evangelist) ; à recouper sur developers.printify.com | lecture | [[RCH - Défauts produit, casse et réclamations Printify (31-10-2026)]] | P2 | |
| Printify Connect (Premium) : langue de l'e-mail et de la page vus par une cliente française | connecté | [[RCH - Défauts produit, casse et réclamations Printify (31-10-2026)]] | P3 | |

## Juridique et fiscal

| Point à vérifier | Moyen | Source | Priorité | Résultat |
|---|---|---|---|---|
| Schéma de TVA selon le pays d'expédition réel de l'imprimeur ; la franchise tient-elle si l'imprimeur expédie depuis l'Allemagne ou la Lettonie ? | expert | [[SYN - Juridique]], [[05 - Printify seul fournisseur avec partenaire UE figé, franchise de TVA au départ]] | P2 (avant janvier 2027) | |
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
| Garantie légale de conformité sur un article personnalisé : articles exacts (durée 2 ans, présomption 24 mois, risque du transport L216-4) à lire sur Légifrance ; peut-on inviter à signaler sous 30 jours sans clause abusive ? | lecture, expert (avocat) | [[RCH - Défauts produit, casse et réclamations Printify (31-10-2026)]] | P1 | |
| Lots remisés : formulation « 3 pour 49,95 € au lieu de 55,35 € à l'unité » au regard de L112-1-1 ; montant remboursé quand un seul article sans texte d'un lot est rétracté | lecture, expert (avocat) | [[12 - Lots de 3 à environ moins 10 %, lot un de chaque sans remise]] | P1 | |
| Rattachement au foyer fiscal parental (CGI, art. 6-3) : âge apprécié au 1er janvier de quelle année, statut d'étudiant de 42 ; simulation rattaché ou détaché | lecture, expert (centre des impôts) | [[RCH - Création de la micro-entreprise, impôts, délais et nom sur le site (02-11-2026)]] | P1 | |
| Seuil du versement libératoire 2026 (29 315 € par part, une seule source) et délai d'option pour un créateur | lecture (impots.gouv.fr, URSSAF) | [[RCH - Création de la micro-entreprise, impôts, délais et nom sur le site (02-11-2026)]] | P1 | |
| Shopify Payments active-t-il un compte d'entreprise individuelle sans SIREN, dossier déposé ? (Paramètres → Paiements) | connecté | [[TODO - Déclarer la micro-entreprise sur le guichet unique]] | P1 | vu le 02/11/2026 : l'étape 1 sur 4 propose « Un particulier » (sans entité enregistrée) ou « Une entreprise immatriculée » ; aucun SIREN demandé à ce stade. Reste à voir : les étapes 2 à 4, et si le type peut passer à « entreprise immatriculée » sans blocage des versements une fois le SIREN reçu |
| Règlement de copropriété de l'appartement de la mère de Sylvain, si retenu comme adresse : clause d'habitation bourgeoise exclusive | lecture | [[RCH - Création de la micro-entreprise, impôts, délais et nom sur le site (02-11-2026)]] | P1 | |
| « Domicile » (LCEN, art. 1-1) ou « adresse où elle est établie » (art. 19) : l'adresse de l'entreprise suffit-elle dans les mentions légales ? | lecture, expert (avocat) | [[RCH - Création de la micro-entreprise, impôts, délais et nom sur le site (02-11-2026)]] | P2 | |
| Facturation entre le dépôt et le SIREN : mention « en cours d'immatriculation » ou facture différée (source contradictoire) | lecture, expert | [[RCH - Création de la micro-entreprise, impôts, délais et nom sur le site (02-11-2026)]] | P2 | |
| Mentions légales complètes de Cadeau Plus (forme sociale, SIREN) | manuel | [[RCH - Création de la micro-entreprise, impôts, délais et nom sur le site (02-11-2026)]] | P3 | |

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
| Dimensions en pixels des placeholders du mug 1016/26, de la boule 2769/86 et du bois 697/23 par `variants.json` avec le jeton ; noms de positions (`front`, `all`, `aop`) et identifiants de variantes à confirmer par l'API publique | connecté (jeton Printify) | [[RCH - Contraintes d'impression Printify des trois produits (01-11-2026)]] | P1 | |
| Limite de prénoms par support (6 sur le mug ; moins sur la boule de 76 mm et sur l'étoile et la cloche en bois) ; hauteur minimale des lettres sur bois | test (rendu), échantillon | [[13 - Texte en trois champs facultatifs, couleur du texte en palette, police fixée, page blanche recadrée par la cliente]] | P1 | |
| Palette de 4 à 6 couleurs lisible sur verre à dos blanc et sur bois ; police et palette communes de la page blanche | échantillon | [[13 - Texte en trois champs facultatifs, couleur du texte en palette, police fixée, page blanche recadrée par la cliente]], [[CMP - Personnalisation par produit]] | P1 | |
| Page blanche : conversion HEIC côté serveur ; seuil de 1 200 px suffisant sur le tour complet du mug (environ 3 000 px attendus à 300 DPI, estimé) ; pixels transparents et sous-couche blanche sur bois et verre | test, échantillon | [[13 - Texte en trois champs facultatifs, couleur du texte en palette, police fixée, page blanche recadrée par la cliente]], [[RCH - Contraintes d'impression Printify des trois produits (01-11-2026)]] | P1 | |
| Rendu peint sur les trois supports : traits fins, pastels et texte à 3 mm sur bois (grain), verre UV à dos blanc et mug en sublimation ; pastille de test dans le fichier de la commande du 05/11 ; si échec, repli aplats avec trait (décision 14, options en réserve) | échantillon | [[14 - Brief visuel, deux gabarits de design déclinés par titre et par occasion, rendu peint aux formes franches]] | P1 (avant le 05/11) | |
| Ventes comparées des deux gabarits de design (symbole par prénom, scène fixe) à Noël 2026 | test (Noël 2026) | [[14 - Brief visuel, deux gabarits de design déclinés par titre et par occasion, rendu peint aux formes franches]] | P1 | |
| Stabilité de Nano Banana Pro sur plusieurs scènes : zone vide respectée, éditions invisibles hors zone (deux essais seulement) ; densité de petits détails à contraindre par le prompt | test (scripts `tests-images/`) | [[RCH - Capacités des modèles d'images pour les calques (02-11-2026)]] | P1 | |
| Détourage d'un JPEG Nano Banana Pro par la chaîne mesurée (isnet ou BiRefNet + clé Lab, pymatting) ; BiRefNet contre isnet sur le Mac ; Lanczos contre RealESRGAN_x2plus sur une vraie gouache ; fichiers dans `tests-images/sorties/` | test (local) | [[RCH - Détourage, nettoyage des bords et agrandissement pour l'impression (02-11-2026)]] | P1 | |
| Liste des tailles acceptées par Ideogram 4.5 (`dry_run`) ; combinaison fond transparent et image source ; motif d'arrêt de Gemini quand aucune image n'est renvoyée | test | [[RCH - Capacités des modèles d'images pour les calques (02-11-2026)]] | P2 | |
| Texte : effet des 29 niveaux de gris de resvg à l'impression ; lisibilité réelle sur objet (3 mm bâton, 4 à 5 mm pinceau) ; seuil d'alerte OCR à fixer sur les vrais gabarits ; police payante gouache (Stay Enjoy) non testée | échantillon, test | [[RCH - Rendu du texte, polices et OCR des accents (02-11-2026)]] | P1 | |
| Mockups : CGU Dynamic Mockups (usage interne seulement ?) ; réutilisation publique des URL `images.printify.com` ; ressource Personalization de Printify pour des aperçus | lecture, connecté | [[RCH - Mockups réalistes par code des trois produits (02-11-2026)]] | P2 | |
| Rendu physique : blanc et alpha sur verre UV et sur bois (sous-couche blanche ?) ; forme réelle de la boule (disque biseauté ou sphère) ; recto-verso du bois ; question au support Printify avant la commande ; aucun avis client avec photo sur les trois références | support, échantillon | [[RCH - Rendu des trois procédés d'impression et planche de test (02-11-2026)]] | P1 (avant le 05/11) | |
| Zone du mug : panneau de 2475 × 1155 px (environ 210 × 98 mm) et non tour complet, environ 40 mm sous l'anse ; à confirmer par `variants.json` | connecté (jeton Printify) | [[RCH - Rendu des trois procédés d'impression et planche de test (02-11-2026)]] | P1 | |
| Concurrents : réparer le CSV (30 premières lignes à 35-38 colonnes) ; vérifier le design 0065 de Cadeau Plus ; nombre de publicités Cadeau Plus gonflé par la recherche par mot-clé | relevé | [[RCH - Publicités Meta et designs Monsieur TShirt et Etsy (02-11-2026)]] | P2 | |
| Rendu imprimé des éléments validés : flocon (blanc cassé et bleu clair) sur la céramique blanche du mug ; mailles blanches du cœur à 12-15 px ; guirlandes et boules du sapin d'hiver sous 12 px à 1 004 px | échantillon (commande test, puis première commande réelle) | [[RCH - Production des illustrations de Noël 2026, ce que les prompts ont appris (02-11-2026)]] | P1 | |
| Recoloration par code (`recolorer.py`) sur une scène à ombres fortes ou à couleurs proches entre rôles ; feuilles du bouquet qui suivent la vaisselle | test | [[RCH - Production des illustrations de Noël 2026, ce que les prompts ont appris (02-11-2026)]] | P2 | |
| Journal `production.json` : `oeillet-seed3.png` généré deux fois, une entrée sans verdict ; `analyse.py --verdict` n'écrit que sur la dernière entrée | relevé | [[RCH - Production des illustrations de Noël 2026, ce que les prompts ont appris (02-11-2026)]] | P3 | |
| Boule A à 4 à 6 prénoms : rangées à −10 et +12 mm trop serrées (prénoms du haut sur la branche du bas, prénoms du bas hors du cercle) ; la branche croise le titre en arc à toute valeur de N | test (rendu) | [[MOD - Module de rendu]] | P1 | Réglé le 03/11 : symboles de 14 mm, rangées à −12 et +14,5 mm, titre omis à Noël et au-delà de N = 3 ([[CMP - Gabarits de support]]) |
| Grilles du bois trop hautes avec sol, branche et mois : ovale 6 à 153,8 mm (utile 120), étoile 4 à 96,1 (70), chaussette 5 à 121,4 (103), cœur 1 à 76,6 (75) ; tailles de symboles ou N max à revoir | test (rendu) | [[MOD - Module de rendu]] | P1 | En partie réglé le 03/11 : ovale à 5 et 6 en 20 mm au pas de 30 (base) et 16 mm au pas de 31 (Noël) ; étoile, chaussette et cœur restent |
| Zones de titre et de phrase absentes de `gabarits.json` pour l'étoile, le cœur, la cloche et la chaussette (estimées par le module) ; ovale B sans zone de phrase | test (rendu) | [[MOD - Module de rendu]] | P1 | |
| Contour réel des six formes de bois : des éléments peuvent tomber hors des branches de l'étoile ou de la pointe du cœur | connecté (gabarit de découpe) | [[MOD - Module de rendu]] | P1 | Calque de contour ajouté le 03/11 (estimé sauf l'ovale) : titre et seconde rangée hors des branches de l'étoile, titre dans le creux du cœur, branche qui dépasse sur la cloche et la chaussette |
| Mug B : phrase posée sur le sol prolongé, peu lisible (prune sur vert pour Maman) ; boule B : titre en arc sur la théière, fenêtre enneigée hors du recadrage à Noël | test (rendu) | [[MOD - Module de rendu]] | P1 | En partie réglé le 03/11 : phrase du mug B sur le mur, boule B recadrée à 68 % avec les prénoms sur le mur ; restent le titre en arc de la boule B sur le gâteau et la fenêtre enneigée coupée. Boule B réglée le 03/11 : titre en deux lignes droites au-dessus du gâteau, recadrage calé en haut ; reste la fenêtre enneigée coupée |
| Tournure des titres de famille (« Le sapin de Famille », « Le goûter chez Famille », « Chez nous », « Notre tribu ») | décision | [[MOD - Module de rendu]] | P1 | |
| Règles du module à reporter dans [[CMP - Gabarits de support]] et `gabarits.json` : titres B, décalage du mug à Noël, phrase à 2,5 mm, titre A du bois sur deux lignes, mois sous le prénom, écart des rangées à Noël | lecture (revue) | [[MOD - Module de rendu]] | P1 | Reporté le 03/11 dans [[CMP - Gabarits de support]] et `gabarits.json` |
| Branche à 12 % du symbole : 2,9 mm de haut pour 24 mm, aiguilles sous 1 mm, tuile répétée visible comme une frise ; lisibilité imprimée | échantillon | [[MOD - Module de rendu]] | P1 | |
| Aperçu du thème : environ 1 s par rendu, autant que l'impression ; mois à 7 px de capitale à 25 % sur le mug 3D (échelle 0,5 ?) ; éléments réduits à préparer une fois pour accélérer | test | [[MOD - Module de rendu]] | P2 | |
| Serveur de rendu : libraqm et fribidi disponibles (sur le Mac, `DYLD_FALLBACK_LIBRARY_PATH=/opt/homebrew/lib`) | test | [[MOD - Module de rendu]] | P2 | |
| Placeholders de l'API différents de `gabarits.json` : mug 2 244 × 945 px (gabarit : 2 475 × 1 155, panneau 210 × 98 mm), ovale 1 085 × 1 545 (gabarit : 1 004 × 1 476) ; relever la taille imprimée en mm et recalculer les zones avant tout fichier du module chez Printify | connecté (`variants.json`, éditeur Printify) | [[MOD - Module de rendu]] | P1 | |
| Ovale B : les coins bas de la scène sortent de l'ellipse ; masquer la scène à l'ellipse ou la réduire | test (calque de contour) | [[MOD - Module de rendu]] | P1 | |
| Boule B pour un Couple : « Le goûter chez Papy et Mamie » ne tient pas en deux lignes à 4 mm, tâche humaine | décision | [[MOD - Module de rendu]] | P2 | |
| Boule A en base : le titre en arc frôle la feuille de houx à droite | échantillon | [[MOD - Module de rendu]] | P3 | |
| Intégration des éléments d'Antoine dans le thème : 10 écarts avec rendu.py (taille 400 px, tulipe absente, texte canvas, pas d'eviter_titre ni de rogner_au_cercle, aperçu qui ne refuse jamais, scènes B dessinées par code, un seul ornement boule/bois, cœur à 78 %, symboles des exemples) | lecture (Antoine) | [[FLOW - Des éléments d'Antoine aux visuels de la boutique]] | P1 | |
| Lots : la fiche et « Nos offres » annoncent une remise fixe par article dès 3 du même objet (1,80 / 1,97 / 1,80 €), le panier annonce −10 % dès 3 articles mélangés (`np_lot_pct`) ; une seule règle à retenir, puis aligner panier, fiche et remises Shopify | décision, test | [[FLOW - Lots et trio]] | P1 | |
| Trio à −5,20 € contre « sans remise » dans la décision 12 : décision 13 bis à écrire | décision | [[FLOW - Lots et trio]] | P1 | |

## Marché

| Point à vérifier | Moyen | Source | Priorité | Résultat |
|---|---|---|---|---|
| Volumes Google Keyword Planner et courbes Google Trends France pour « mug mamie personnalisé », « cadeau mamie prénoms petits-enfants », « mug fête des grands-mères », « affiche mamie », « plaid mamie » ; jamais obtenus par aucune recherche | manuel | [[SYN - Choix de la niche]] | P1 | |
| Bibliothèque publicitaire Meta : publicités actives de Cadeau Plus, Henriette and Co, Famille de Dingue, Monsieur TShirt, Cadeaux.com, CadoMaestro | manuel | [[SYN - Choix de la niche]] | P2 | |
| Une illustration fixe sans réglage des personnages convertit-elle à 24,90 € face aux avatars réglables au même prix ? | test (Noël 2026) | [[02 - Lancement avec le mug, la boule en cristal et la décoration en bois, trois imprimeurs UE]], [[RCH - Marché des mugs grands-parents avec prénoms (28-10-2026)]] | P1 | |
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

| Point | Moyen | Source | Priorité | Résultat |
|---|---|---|---|---|
| La graine de Nano Banana Pro reproduit-elle une image à l'identique ? | test | [[MOD - Connecteur nolaprint-image]] | — | **Non** (02/11/2026) : même prompt, même graine, même dessin mais proportions différentes (tête 17,3 % contre 13,9 %), écart moyen 9,5 sur 255. Une image validée se garde en fichier ; les six palettes de la scène se font par recoloration de code (brief, section 5). |
| Rendu gouache atteignable par Nano Banana Pro | test | [[CMP - Brief de génération des illustrations de Noël 2026]] | — | **Oui** (02/11/2026), avec le préfixe v3 et sans image de référence : douze fleurs et six ornements validés, style cohérent sur 22 éléments. Glaïeul remplacé par le tournesol. |
| Image de référence de style : utile ou nuisible ? | test | [[RCH - Production des illustrations de Noël 2026, ce que les prompts ont appris (02-11-2026)]] | — | **Nuisible** (02/11/2026) : le modèle recopie le sujet de la référence autour du nôtre (feuilles de la rose, couronne de souci). Le style tient par le préfixe seul. |
| Déclinaisons de palette d'une scène : régénération ou code ? | test | [[RCH - Production des illustrations de Noël 2026, ce que les prompts ont appris (02-11-2026)]] | — | **Code** (02/11/2026) : cinq régénérations à la même graine ont donné cinq mises en place ; `recolorer.py` donne six scènes identiques à la couleur près, sans appel. |
