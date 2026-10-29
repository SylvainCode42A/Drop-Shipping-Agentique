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

### Le mug 11 oz : fournisseur UE non confirmé
- Sur le catalogue public Printify, le blueprint 535 « 11oz White Mug » n'affiche qu'un imprimeur au Royaume-Uni (T Shirt and Sons, 5,34 $, 3,99 $ avec Premium) et un en Australie ; la page indique « no local providers available » et le blueprint 827 « White Ceramic Mug » est marqué « discontinued ». Aucun imprimeur UE n'a pu être relié au mug depuis les pages publiques, chargées en JavaScript ([[RCH - Vérification Printify UE du mug et vue d'ensemble des produits (28-10-2026)]]).
- Le retrait du mug blanc pour l'Europe n'est donc ni confirmé ni infirmé ; les prix de 6,38 € (mug couleur) et 10,48 € (15 oz) qui circulaient n'apparaissent dans aucune source ⚠️ à vérifier dans le tableau de bord connecté, destination France, filtre « Ships from : Europe » ([[RCH - Vérification Printify UE du mug et vue d'ensemble des produits (28-10-2026)]]).
- Repli vérifiable : Gelato (6,26 $, port France 4,99 € selon une source tierce) et Printful (5,95 $, port Europe 6,09 $ puis 2,05 $ par mug, production à Riga, mugs toujours expédiés séparément). Marge estimée d'un mug à 24,90 € port offert : environ 13,8 € en franchise de TVA, 9,6 € si assujetti ([[RCH - Vérification Printify UE du mug et vue d'ensemble des produits (28-10-2026)]]).

### Les imprimeurs UE par produit
Treize études produit ont cherché un imprimeur dans l'UE chez Printify, Gelato et Printful ([[RCH - Synthèse comparative des produits d'élargissement (29-10-2026)]]).
| Produit | Imprimeur UE confirmé | Statut |
|---|---|---|
| Affiche | Posterflow (Mannheim, DE) chez Printify, dès 9,08 $ ; Gelato dès 5,29 € HT ; Printful dès 8,32 $ | Confirmé ([[RCH - Affiche personnalisée grands-parents (28-10-2026)]]) |
| Tote bag, t-shirt | Textildruck Europa (DE) pour le tote W801 à 13,00 $ ; Atelier Katanga (Cornebarrieu, FR) pour le t-shirt Stanley/Stella à 14,93 $ ; Gelato et Printful | Confirmé ([[RCH - Textile personnalisé grands-parents, tote bag en priorité (28-10-2026)]]) |
| Torchon | Textildruck Europa, Greenbomb 10,87 $ ; Gelato et Printful : aucun | Confirmé ([[RCH - Torchon personnalisé grands-parents (28-10-2026)]]) |
| Tablier | Textildruck Europa, polyester sublimé, prix contradictoire (6,90 à 22,51 $) ; Printful SOL'S coton bio « livrable en Europe », site non confirmé | Partiel ([[RCH - Tablier personnalisé grands-parents (28-10-2026)]]) |
| Sous-verres | Printify Corkwood Coaster Set, un fournisseur « only ships from EU » non nommé (Colorway, Pays-Bas probable) ; Printful lieu inconnu ; Gelato aucun | À vérifier connecté ([[RCH - Sous-verres personnalisés pour grands-parents (28-10-2026)]]) |
| Coussin | Printful Lettonie (housse 17,11 € TTC, garni expédié non assemblé) ; Printify n'affiche que MWW (US) ; Gelato aucun | Partiel ([[RCH - Coussin grands-parents (28-10-2026)]]) |
| Gobelet isotherme | Aucun confirmé ; tumblers Printify et Printful aux États-Unis ; un article Textildruck à 12,75 $ non identifié | À vérifier ([[RCH - Gobelet isotherme grands-parents (28-10-2026)]]) |
| Plaid | Aucun confirmé ; Printify Choice EU et Printful LV avec blanks chinois ; Gelato « coming soon » | Absent ([[RCH - Plaid personnalisé grands-parents (28-10-2026)]]) |
| Bougie | Aucun ; tous les fournisseurs Printify et Printful sont aux États-Unis | Absent ([[RCH - Bougie personnalisée grands-parents (29-10-2026)]]) |
| Boîte à biscuits | Aucun ; Prodigi (UK) exclut l'usage alimentaire | Absent ([[RCH - Boîte à biscuits grands-parents (28-10-2026)]]) |
| Planche | Aucun ; gravure JDS et verre sublimé aux États-Unis | Absent ([[RCH - Planche à découper et planche apéro grands-parents (29-10-2026)]]) |
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
- Lots : Printful emballe les mugs à part ; Printify expédie séparément les produits d'imprimeurs différents, chacun au tarif « premier article ». Un lot en un seul colis suppose un imprimeur qui fait le mug et l'autre produit ; Textildruck Europa a des mugs 11 oz au catalogue ⚠️ à vérifier ([[RCH - Textile personnalisé grands-parents, tote bag en priorité (28-10-2026)]], [[RCH - Tablier personnalisé grands-parents (28-10-2026)]]).

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
- Printify en principal avec un partenaire UE figé pour le mug (France sinon Allemagne), Gelato en second et en repli, échantillons chez les deux avant le 15/11/2026, franchise de TVA au départ ([[05 - Printify en principal avec partenaire UE figé, Gelato en second, franchise de TVA au départ]]). Cette décision repose sur l'existence d'un partenaire Printify UE pour le mug, que les recherches du 28/10 n'ont pas pu confirmer : à relire après la vérification connectée.

Décisions attendues :
- le partenaire Printify figé, après vérification connectée et échantillons ;
- le fournisseur de complément pour les produits suivants ;
- l'application de personnalisation, ou la génération du fichier par le système ;
- la politique de lots et de port.

## Questions ouvertes
- Connecté à Printify, France en destination, filtre « Ships from : Europe » : quels imprimeurs pour le mug 11 oz blanc, bicolore et magique, les sous-verres, le coussin, le tablier, le tumbler, et un même imprimeur fait-il mug plus un autre produit ?
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
- [[RCH - Applications de personnalisation Shopify pour Printify et Gelato (29-10-2026)]]
- [[RCH - Synthèse comparative des produits d'élargissement (29-10-2026)]]
- Études produit : [[RCH - Marché des mugs grands-parents avec prénoms (28-10-2026)]], [[RCH - Affiche personnalisée grands-parents (28-10-2026)]], [[RCH - Textile personnalisé grands-parents, tote bag en priorité (28-10-2026)]], [[RCH - Plaid personnalisé grands-parents (28-10-2026)]], [[RCH - Tablier personnalisé grands-parents (28-10-2026)]], [[RCH - Gobelet isotherme grands-parents (28-10-2026)]], [[RCH - Sous-verres personnalisés pour grands-parents (28-10-2026)]], [[RCH - Coussin grands-parents (28-10-2026)]], [[RCH - Torchon personnalisé grands-parents (28-10-2026)]], [[RCH - Boîte à biscuits grands-parents (28-10-2026)]], [[RCH - Bougie personnalisée grands-parents (29-10-2026)]], [[RCH - Planche à découper et planche apéro grands-parents (29-10-2026)]]
