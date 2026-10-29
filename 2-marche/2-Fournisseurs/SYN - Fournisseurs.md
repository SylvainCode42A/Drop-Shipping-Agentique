---
type: synthese
title: SYN - Fournisseurs
status: validé
related: ["[[_conventions]]", "[[SYN - Choix de la niche]]", "[[SYN - Juridique]]", "[[SYN - Modèle économique]]", "[[SYN - Système]]", "[[A VERIFIER - Points à valider, vérifier, tester]]"]
decisions: ["[[05 - Printify en principal avec partenaire UE figé, Gelato en second, franchise de TVA au départ]]"]
last-verified: 2026-10-29
tags: [dropshipping, fournisseurs, synthese]
---
# SYN - Fournisseurs

État des connaissances sur les fournisseurs d'impression à la demande, leurs API et les applications de personnalisation. Une recherche fournisseurs, une recherche applications, une vérification Printify UE et treize études produit. Rien n'est décidé ici.

## Ce qu'on sait

### Les fournisseurs et leurs API
- **Printify** : API REST complète (catalogue, produits, commandes, uploads, webhooks), avec publication vers Shopify par un endpoint dédié. Le catalogue donne les dimensions en pixels de chaque zone d'impression, donc un agent peut adapter le visuel seul. La qualité dépend du partenaire : il faut figer des partenaires européens ([[RCH - Fournisseurs print-on-demand et API (25-10-2026)]]).
- **Gelato** : création de produit par API à partir d'un modèle préparé dans le tableau de bord, réservée aux boutiques Shopify. Un agent ne peut pas créer un nouveau type de produit sans modèle. Production dans 32 pays dont la France, commandes de test en mode « draft » ([[RCH - Fournisseurs print-on-demand et API (25-10-2026)]]).
- **Printful** : documentation la plus complète, qualité la plus régulière, ateliers en propre en Espagne et en Lettonie. Mais l'API ne crée des produits que dans une boutique « Manual orders / API » : pour Shopify, créer le produit via l'API Admin puis le lier. Printful et Printify appartiennent au même groupe ([[RCH - Fournisseurs print-on-demand et API (25-10-2026)]]).
- **T-Pop** : atelier en France (Barjac), prix en euros HT, livraison France en 2 à 3 jours ouvrés. Pas d'API publique, une API de commandes est annoncée. Création de produits manuelle ([[RCH - Fournisseurs print-on-demand et API (25-10-2026)]]).
- **Prodigi** : API de commandes avec sandbox, fort sur l'art mural, mug produit dans l'UE mais sous-verres, tabliers, torchons et boîtes métal expédiés du Royaume-Uni. **Spreadconnect** : API de création d'articles, ateliers en Allemagne, Tchéquie et Pologne ([[RCH - Fournisseurs print-on-demand et API (25-10-2026)]], [[RCH - Assiettes et objets de table pour compléter le mug (25-10-2026)]], [[RCH - Boîte à biscuits grands-parents (28-10-2026)]]).
- Écartés : Gooten et CustomCat (États-Unis), Teemill et Inkthreadable (Royaume-Uni, douane), Peecho (racheté par Prodigi) ([[RCH - Fournisseurs print-on-demand et API (25-10-2026)]]).

### Le mug 11 oz : trois imprimeurs UE, mais pas sur le blueprint 535
- Le blueprint 535 « 11oz White Mug » n'a aucun imprimeur UE, en public comme en connecté : seul T Shirt and Sons (Royaume-Uni, 5,34 $, port France 15,49 $). Le blueprint 827 renvoie 404. Le retrait du mug blanc pour l'Europe ne vaut que pour ce blueprint ([[RCH - Vérification Printify UE du mug et vue d'ensemble des produits (28-10-2026)]], [[RCH - Relevé connecté du catalogue Printify UE (29-10-2026)]]).
- Relevé connecté du 29/10, destination France, filtre « Ships from : Europe » : trois imprimeurs UE font un mug 11 oz blanc. **OPT OnDemand** (Tchéquie, note 9,27) : blueprint 441 « Ceramic Mug (EU) », 5,88 $ (4,39 $ Premium), port 6,89 $ puis 1,99 $, 5 à 8 jours, lave-vaisselle. **Textildruck Europa** (Allemagne, note 8,65) : 1016 Standard Mug 5,91 $ (4,42 $), bicolore 1018 à 6,90 $, magique 1017 à 8,19 $, noir 1117 à 9,31 $, port 6,89 $ puis 1,99 $, 5 à 10 jours. **Harrier** (sites Tchéquie et Royaume-Uni, note 9,57) : 1125 à 5,47 $ (4,08 $), accent 635 à 7,91 $, port 6,89 $ puis 2,39 $, 5 à 15 jours, site expéditeur vers la France non affiché ⚠️ ([[RCH - Relevé connecté du catalogue Printify UE (29-10-2026)]]).
- Les prix de 6,38 € et 10,48 € qui circulaient étaient faux. Le mug 441 en 15 oz coûte 9,87 $ chez OPT ([[RCH - Relevé connecté du catalogue Printify UE (29-10-2026)]]).
- Repli : Gelato (6,26 $, port France 4,99 € selon une source tierce) et Printful (mug 478 à 5,02 $ sur Printify mais port « Rest of the World » 22,09 $ ; 5,95 $ et port Europe 6,09 $ puis 2,05 $ en direct, production à Riga, mugs toujours expédiés séparément). Marge estimée d'un mug à 24,90 € port offert chez OPT ou Textildruck : coût livré ≈ 11,0 € à 0,86 $ par euro ; environ 13,1 € en franchise de TVA, 9,0 € si assujetti (estimé, avant TVA fournisseur) ([[RCH - Vérification Printify UE du mug et vue d'ensemble des produits (28-10-2026)]], [[RCH - Relevé connecté du catalogue Printify UE (29-10-2026)]]).
- TVA : Printify facture la TVA sur les commandes vers l'UE ; elle est récupérable « si vous êtes assujetti » ; Printify ne mentionne pas la franchise en base ⚠️ expert-comptable ([[RCH - Relevé connecté du catalogue Printify UE (29-10-2026)]]).

### Les imprimeurs UE par produit
Treize études produit ont cherché un imprimeur dans l'UE chez Printify, Gelato et Printful ([[RCH - Synthèse comparative des produits d'élargissement (29-10-2026)]]).
| Produit | Imprimeur UE confirmé | Statut |
|---|---|---|
| Mug 11 oz | OPT OnDemand (CZ) 441 à 5,88 $ ; Textildruck Europa (DE) 1016 à 5,91 $ ; Harrier (CZ/GB) 1125 à 5,47 $ ; port 6,89 $ puis 1,99 à 2,39 $ | Confirmé connecté ([[RCH - Relevé connecté du catalogue Printify UE (29-10-2026)]]) |
| Affiche | Posterflow (DE) 1033 : A4 9,26 $, A3 et 30 × 40 11,15 $, 50 × 70 15,86 $, port 16,29 $ puis 0,29 $ ; encadrée 1275 dès 22,66 $ ; OPT OnDemand 443 : A4 6,50 $, A3 7,09 $, port 6,09 $ puis 0,29 $ ; Print Pigeons (LV), Jondo (ES) ; Gelato dès 5,29 € HT ; Printful dès 8,32 $ | Confirmé connecté ([[RCH - Relevé connecté du catalogue Printify UE (29-10-2026)]], [[RCH - Affiche personnalisée grands-parents (28-10-2026)]]) |
| Tote bag, t-shirt | Textildruck Europa (DE) tote W801 731 à 13,00 $, port 5,69 $ puis 1,19 $ ; Printful (LV) tote 1930 à 18,68 $ ; Atelier Katanga (FR) pour le t-shirt Stanley/Stella à 14,93 $ ; Gelato | Confirmé connecté ([[RCH - Relevé connecté du catalogue Printify UE (29-10-2026)]], [[RCH - Textile personnalisé grands-parents, tote bag en priorité (28-10-2026)]]) |
| Sous-verres | Printify 1523 sous-verre céramique chez WOYC (site Italie) 8,37 $ l'unité, port 5,99 $ puis 1,49 $ ; Corkwood Coaster Set 510 et Cork Back 480 : aucun imprimeur UE en connecté ; Printful lieu inconnu ; Gelato aucun | Confirmé connecté, céramique unitaire seulement ([[RCH - Relevé connecté du catalogue Printify UE (29-10-2026)]], [[RCH - Sous-verres personnalisés pour grands-parents (28-10-2026)]]) |
| Coussin | Printify housse 229 (11,71 à 13,89 $, port 5,99 $) et coussin garni 220 (16,67 à 20,38 $, port 12,79 à 13,89 $) chez MWW On Demand, site Allemagne ; Printful Lettonie (housse 17,11 € TTC) ; Gelato aucun | Confirmé connecté ([[RCH - Relevé connecté du catalogue Printify UE (29-10-2026)]], [[RCH - Coussin grands-parents (28-10-2026)]]) |
| Tablier | Printify tablier AOP 418 chez MWW On Demand (site DE) 22,54 $ (16,85 $ Premium), port 6,69 $ ; Textildruck Europa non retrouvé en connecté ; tabliers 713, 830 (GB) et 858 (CN) sans UE ; Printful SOL'S coton bio « livrable en Europe » | Confirmé connecté, polyester AOP seulement ([[RCH - Relevé connecté du catalogue Printify UE (29-10-2026)]], [[RCH - Tablier personnalisé grands-parents (28-10-2026)]]) |
| Torchon | Greenbomb chez Textildruck Europa non retrouvé en connecté ; torchons 677, 1003, 1169, 11032 sans imprimeur UE ; Gelato et Printful aucun | Infirmé en connecté ⚠️ ([[RCH - Relevé connecté du catalogue Printify UE (29-10-2026)]], [[RCH - Torchon personnalisé grands-parents (28-10-2026)]]) |
| Gobelet isotherme | Printify gobelet inox 20 oz 1927 chez Printful (site LV) 21,79 $, port 7,79 $ puis 4,90 $ ; le Mason Jar 742 de Textildruck (12,81 $) est en verre givré, pas en inox ; travel mugs sans UE | Un seul, cher ([[RCH - Relevé connecté du catalogue Printify UE (29-10-2026)]], [[RCH - Gobelet isotherme grands-parents (28-10-2026)]]) |
| Plaid | Printify Sherpa 238 et 736 chez MWW On Demand (site DE) 24,81 à 49,26 $, port 10,39 à 24,49 $ ; blanks chinois ; Gelato « coming soon » | Confirmé connecté, port lourd ([[RCH - Relevé connecté du catalogue Printify UE (29-10-2026)]], [[RCH - Plaid personnalisé grands-parents (28-10-2026)]]) |
| Bougie, planche, boîte métal, puzzle | Aucun imprimeur UE en connecté ; Prodigi (UK) exclut l'usage alimentaire de sa boîte | Absent ([[RCH - Relevé connecté du catalogue Printify UE (29-10-2026)]]) |
- Imprimeurs UE actifs chez Printify en 2026 : Atelier Katanga (FR), OPT OnDemand (CZ), Print Pigeons, Drukātava, Ideju Druka, Uniqcube (LV), Textildruck Europa, Posterflow, Shirt-King (DE), HFT71, FlexMerch (PL), Sticky Products Europe, Invition (NL). Depuis le 1er juillet 2026, Printify route les commandes UE vers un imprimeur UE quand il existe ([[RCH - Vérification Printify UE du mug et vue d'ensemble des produits (28-10-2026)]], [[RCH - Gobelet isotherme grands-parents (28-10-2026)]]).
- Les blanks des imprimeurs UE viennent souvent de Chine, du Pakistan ou du Bangladesh ; c'est l'impression et l'expédition depuis l'UE qui comptent pour la douane ([[RCH - Tablier personnalisé grands-parents (28-10-2026)]], [[RCH - Torchon personnalisé grands-parents (28-10-2026)]]).

### La douane et les fabrications hors UE
- Depuis le 1er juillet 2026 et jusqu'au 1er juillet 2028, tout colis de 150 € ou moins entrant dans l'UE depuis un pays tiers paie un droit forfaitaire de 3 € par catégorie tarifaire d'article, en plus de la TVA à l'import ; un colis mug + autre produit relève de deux catégories, soit 6 €. La taxe française de 2 € est suspendue depuis la même date ; des frais de gestion de 2 € par article sont annoncés dès novembre 2026 ⚠️ ([[RCH - Synthèse comparative des produits d'élargissement (29-10-2026)]], [[SYN - Juridique]]).
- Conséquence : sous 40 € de prix de vente, un produit fabriqué aux États-Unis, au Royaume-Uni ou en Chine (gobelet, plaid, bougie, boîte, planche) n'a pas de marge ([[RCH - Synthèse comparative des produits d'élargissement (29-10-2026)]]).

### Les limites techniques
- Printify : 600 requêtes par minute, 100 sur le catalogue, 200 publications par 30 minutes, jeton valable un an. Gelato : 100 requêtes par seconde, plafond de 5 000 appels par jour sauf accord. Printful : 120 requêtes par minute, 2 à 10 tâches de mockups par minute ([[RCH - Fournisseurs print-on-demand et API (25-10-2026)]]).
- Shopify : 100 profils d'expédition maximum par boutique, ce qui bloque la publication Printify sur les forums ; plafond de 1 000 variantes par jour au-delà de 50 000 ([[RCH - Fournisseurs print-on-demand et API (25-10-2026)]]).

### Les fichiers d'impression
- Formats PNG et JPG partout, SVG chez Printify, PDF chez Gelato. Profil sRGB. Résolution 150 à 300 DPI à taille réelle ; 300 DPI pour le papier et les coques ([[RCH - Fournisseurs print-on-demand et API (25-10-2026)]]).
- Mug 11 oz : 200 x 96 mm chez Gelato ; 2475 × 1155 px (guide Printify), 2480 × 1146 (PrintSizer), 2700 × 1120 (comparatif tiers), 2625 × 1050 (SwiftPOD) selon les sources ⚠️ contradictoire, à lire sur le gabarit de l'imprimeur retenu ([[RCH - Marché des mugs grands-parents avec prénoms (28-10-2026)]], [[RCH - Applications de personnalisation Shopify pour Printify et Gelato (29-10-2026)]]).
- Formats maîtres par support : bandeau 2,4:1 (mug, gobelet conique à part), carré (tote, coussin, sous-verres), portrait (affiche, tablier, torchon), grand format 5:6 à 150 dpi (plaid, 7 875 × 9 375 px). Un visuel ne se redimensionne pas, il se recompose ([[RCH - Synthèse comparative des produits d'élargissement (29-10-2026)]]).

### Les applications de personnalisation
- Quatre applications couvrent le flux complet avec Printify (aperçu en direct, fichier d'impression automatique, envoi au fournisseur) : Teeinblue, Customily, HelloCustom et AnywherePOD. Teeinblue et Customily couvrent aussi Gelato. Gelato a son propre Personalization Studio, inclus dans Gelato+ ; la personnalisation native de Printify est gratuite mais sans aperçu rendu sur Shopify ([[RCH - Applications de personnalisation Shopify pour Printify et Gelato (29-10-2026)]]).
- Prix : Teeinblue 49 $ par mois plus 0 à 0,40 $ par article ; Customily 49 $ plus 0,25 à 1 $ ; HelloCustom 24,99 $ plus 0,29 $ ; Zakeke 69,90 à 299,90 $ plus 1,5 à 1,9 % ; Printify natif gratuit ; Gelato+ 19,99 $ en annuel. À 200 commandes par mois : Teeinblue 89 $, Customily 199 $, HelloCustom 83 $ (estimé) ([[RCH - Applications de personnalisation Shopify pour Printify et Gelato (29-10-2026)]]).
- Aucune API publique de gabarits trouvée chez Teeinblue, Customily, HelloCustom ni Gelato : un système externe ne peut pas pousser de gabarits sans passer par l'interface. Zakeke est le seul avec webhook « fichiers prêts ». Architecture alternative documentée : le système Python génère lui-même le fichier et le pousse par l'API Printify, avec une simple application de champs pour la saisie, au prix de l'absence d'aperçu sur mockup ([[RCH - Applications de personnalisation Shopify pour Printify et Gelato (29-10-2026)]]).
- Aucune application ne documente un changement automatique de mise en page selon le nombre de prénoms ; les conditions (Customily, Teeinblue, Gelato) pourraient le simuler par calques affichés ou masqués, sans preuve. Accents français et prénoms composés : non documentés, à tester ([[RCH - Applications de personnalisation Shopify pour Printify et Gelato (29-10-2026)]]).

### Les produits visés par le projet
- Mug : production 2 à 5 jours chez Printful et chez les partenaires Printify de l'UE, 1 à 6 jours chez Gelato. Printful facture chaque mug comme un premier article à l'expédition ([[RCH - Fournisseurs print-on-demand et API (25-10-2026)]], [[SYN - Modèle économique]]).
- Assiette : aucun fournisseur européen relié à Shopify ; écartée le 25/10 ([[SYN - Choix de la niche]]).
- Lots : Printful emballe les mugs à part ; Printify expédie séparément les produits d'imprimeurs différents, chacun au tarif « premier article ». Deux imprimeurs UE font le mug et un autre produit : OPT OnDemand (mug 441 et affiche 443), Textildruck Europa (mugs 1016 à 1018, 1117 et tote 731) ; Printful fait le mug 478 et le tote 1930. La documentation API n'applique le tarif « article suivant » qu'aux articles du même blueprint et du même imprimeur ; l'envoi de deux blueprints dans un seul colis n'est pas documenté ⚠️ ([[RCH - Relevé connecté du catalogue Printify UE (29-10-2026)]]).
- Commande par l'API sans produit créé : `POST /v1/shops/{shop_id}/orders.json` accepte une ligne avec `blueprint_id`, `print_provider_id`, `variant_id`, `quantity` et `print_areas` (une URL par position, ou image avec échelle, position et angle). C'est le préalable de la décision 08 ; l'identifiant de variante lu dans l'API interne reste à confirmer par l'API publique ⚠️. Désactiver la synchronisation Shopify par produit : aucun réglage trouvé ; une commande sans produit Printify lié arrive dans « Other orders » et s'importe à la main ([[RCH - Relevé connecté du catalogue Printify UE (29-10-2026)]]).
- Dates limites Noël 2026 : non publiées au 22/10/2026. Référence 2025, livraison standard Europe : Posterflow 27 novembre, Print Pigeons 28 novembre, Harrier 2 décembre, OPT OnDemand et Printful 5 décembre, Textildruck Europa 9 décembre ([[RCH - Relevé connecté du catalogue Printify UE (29-10-2026)]]).

### Les retours d'expérience
- Printful : commandes ou tarifs qui ne se synchronisent plus après réinstallation de l'app ; coussin garni expédié non assemblé avec garniture difficile à insérer. Printify : limite des profils d'expédition ; retards de production chez certains imprimeurs en décembre 2025 ; « no holiday delivery guarantee » du 10 au 24 décembre. Gelato : rapide en Europe mais variable selon le partenaire. Notes Trustpilot et retours français ⚠️ à vérifier ([[RCH - Fournisseurs print-on-demand et API (25-10-2026)]], [[RCH - Coussin grands-parents (28-10-2026)]], [[RCH - Plaid personnalisé grands-parents (28-10-2026)]]).
- Abonnements : Printify Premium à 39 $ par mois en mensuel depuis le 17/02/2026, 24,99 $ en annuel, jusqu'à 20 % de remise ; Gelato+ 29,99 $ en mensuel, 19,99 $ en annuel. Le Premium décide de la marge sur tablier, plaid et tote ([[RCH - Synthèse comparative des produits d'élargissement (29-10-2026)]]).

### Les règles d'implémentation proposées
- File d'attente par endpoint, créations idempotentes, validation des visuels avant upload, variantes limitées, validation humaine avant publication, échantillons avant vente, visuels stockés chez soi ([[RCH - Fournisseurs print-on-demand et API (25-10-2026)]]). À reprendre dans [[SYN - Système]].

### Le lien avec la TVA
- Le pays d'expédition du fournisseur décide du schéma de TVA : si l'imprimeur expédie depuis un autre pays de l'UE, la TVA du pays du client peut être due dès le premier euro ⚠️ à valider par un expert-comptable avant de choisir ([[SYN - Juridique]]).
- Les factures des fournisseurs POD portent-elles une TVA récupérable ? Non vérifié ; en franchise, une TVA fournisseur non récupérable réduit chaque marge de 2 à 3 € ([[RCH - Vérification Printify UE du mug et vue d'ensemble des produits (28-10-2026)]]).

### Contradictions non tranchées
- Site Printful en Espagne : Barcelone ou Madrid. Partenaires Gelato : 130, 140 ou 250 selon les pages.
- Délai Printify vers l'Europe : 2 à 5 jours de production selon Printify, 10 à 15 jours ouvrés selon un ancien comparatif.
- Prix du mug Printful : 5,95 à 6,75 $ selon les sites tiers. Prix plancher du mug Printify : 4,93, 3,68 ou 3,56 $ selon les sources.
- Port Printful de plusieurs mugs : « +2,05 $ » (tableau) ou « single product » (FAQ).
- Prix Printify du tablier Textildruck : 6,90, 18,36 ou 22,51 $ selon l'extrait.
- Customily : paiement à l'usage, 49 $ par mois, ou plan gratuit selon la source. Printify natif : approbation manuelle obligatoire ou soumission automatique possible.
- Droit de 3 € : « par article » ou « par catégorie tarifaire » ; les textes officiels disent par catégorie.
- La recherche fournisseurs du 25/10 est orientée textile ; le mug y est peu chiffré.

## Ce qui est décidé
- Printify en principal avec un partenaire UE figé pour le mug (France sinon Allemagne), Gelato en second et en repli, échantillons chez les deux avant le 15/11/2026, franchise de TVA au départ ([[05 - Printify en principal avec partenaire UE figé, Gelato en second, franchise de TVA au départ]]). Le relevé connecté du 29/10 confirme que des partenaires UE existent pour le mug : aucun en France, deux en Allemagne et en Tchéquie (Textildruck Europa, OPT OnDemand), plus Harrier. La décision tient ; le choix entre OPT et Textildruck est attendu après échantillons.

Décisions attendues :
- le partenaire Printify figé entre OPT OnDemand (441, lot avec l'affiche 443) et Textildruck Europa (1016, lot avec le tote 731), après échantillons ;
- le fournisseur de complément pour les produits suivants ;
- ~~l'application de personnalisation, ou la génération du fichier par le système~~ : prise, génération interne ([[08 - Personnalisation à la commande en génération interne, test Printify avant le 5 novembre]]) ;
- la politique de lots et de port.

## Questions ouvertes
- Site qui expédie vers la France chez Harrier, WOYC, MWW On Demand, Printful et Jondo (plusieurs sites, non affiché).
- Deux blueprints d'un même imprimeur partent-ils dans un seul colis, au tarif « article suivant » ?
- Identifiant de variante du mug 441 par l'API publique ; pixels, DPI et format de fichier par imprimeur ; option de routage UE de la boutique.
- Prix, délais et taux de casse réels d'un mug fabriqué en Europe chez Printify et Gelato, mesurés avec des échantillons.
- Prix Gelato exacts pour la France hors promotion, et tarif du 2e mug.
- Prix en euros Printful pour la production lettone, et site réel du tablier SOL'S et du tumbler.
- Gelato accepte-t-il de relever le plafond de 5 000 appels par jour ? Printify a-t-il un environnement de test ?
- Date et périmètre de l'API T-Pop.
- Quelle application rend correctement les accents et un prénom composé, et avec quelle police ? Une application permet-elle d'importer des gabarits en masse ?
- La soumission automatique Printify fonctionne-t-elle pour des commandes Shopify personnalisées par une application tierce ?
- Dates limites Noël 2026 de Printify, Gelato et Printful pour la France.
- Documentation GPSR et contact alimentaire fournie par chaque imprimeur UE.
- Notes Trustpilot et retours français actuels sur Printify, Gelato et Printful.

## Recherches
- [[RCH - Fournisseurs print-on-demand et API (25-10-2026)]]
- [[RCH - Assiettes et objets de table pour compléter le mug (25-10-2026)]]
- [[RCH - Vérification Printify UE du mug et vue d'ensemble des produits (28-10-2026)]]
- [[RCH - Relevé connecté du catalogue Printify UE (29-10-2026)]]
- [[RCH - Applications de personnalisation Shopify pour Printify et Gelato (29-10-2026)]]
- [[RCH - Synthèse comparative des produits d'élargissement (29-10-2026)]]
- Études produit : [[RCH - Marché des mugs grands-parents avec prénoms (28-10-2026)]], [[RCH - Affiche personnalisée grands-parents (28-10-2026)]], [[RCH - Textile personnalisé grands-parents, tote bag en priorité (28-10-2026)]], [[RCH - Plaid personnalisé grands-parents (28-10-2026)]], [[RCH - Tablier personnalisé grands-parents (28-10-2026)]], [[RCH - Gobelet isotherme grands-parents (28-10-2026)]], [[RCH - Sous-verres personnalisés pour grands-parents (28-10-2026)]], [[RCH - Coussin grands-parents (28-10-2026)]], [[RCH - Torchon personnalisé grands-parents (28-10-2026)]], [[RCH - Boîte à biscuits grands-parents (28-10-2026)]], [[RCH - Bougie personnalisée grands-parents (29-10-2026)]], [[RCH - Planche à découper et planche apéro grands-parents (29-10-2026)]]
