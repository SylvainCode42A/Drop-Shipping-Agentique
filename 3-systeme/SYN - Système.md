---
type: synthese
title: SYN - Système
status: validé
related: ["[[_conventions]]", "[[SYN - Fournisseurs]]", "[[SYN - Acquisition]]", "[[SYN - Juridique]]", "[[SYN - Choix de la niche]]", "[[A VERIFIER - Points à valider, vérifier, tester]]"]
decisions: ["[[03 - Approbation unitaire au lancement, paliers d'autonomie, actions toujours bloquées]]", "[[06 - LangGraph au départ, interface d'images interne avec Nano Banana Pro et Ideogram]]"]
last-verified: 2026-10-29
tags: [dropshipping, systeme, synthese]
---
# SYN - Système

État des connaissances techniques sur le système d'agents : Shopify, génération d'images, personnalisation à la commande, décision statistique, architecture et mémoire. Quatre recherches système, une recherche applications, une recherche images IA et les contraintes de design remontées par quatorze études produit. Les notes MOD, CMP et FLOW de ce dossier s'appuieront sur cette synthèse. Rien n'est décidé ici.

## Ce qu'on sait

### Shopify
- Version stable 2026-10, tout en GraphQL, une mise à jour par trimestre. Cycle produit complet : `productSet` (upsert, envoyer toutes les variantes), `productUpdate` pour le statut, `stagedUploadsCreate` puis `fileCreate` pour les images (attendre `READY`), `metafieldsSet`, `publishablePublish`. Un produit `ACTIVE` non publié n'est visible nulle part ([[RCH - API Shopify pour la boutique agentique (22-10-2026)]]).
- Type d'app : créée dans le Dev Dashboard pour sa propre boutique. Les custom apps de l'admin ne se créent plus depuis le 01/01/2026. Token client credentials valable 24 h si app et boutique sont dans la même organisation ([[RCH - API Shopify pour la boutique agentique (22-10-2026)]]).
- Ventes par produit fiables via `orders` et `shopifyqlQuery` (table `sales`). Aucune métrique officielle de vues ou de conversion par produit : il faut un Web Pixel (`product_viewed`, `product_added_to_cart`) ou GA4 ([[RCH - API Shopify pour la boutique agentique (22-10-2026)]]).
- Sans `read_all_orders`, les commandes de plus de 60 jours sont invisibles sans erreur ; ce scope et `shopifyqlQuery` demandent une approbation de Shopify ([[RCH - API Shopify pour la boutique agentique (22-10-2026)]]).
- Limites : 100 points par seconde en Basic, erreur `THROTTLED` à traiter par backoff, bulk operations hors limite. Webhooks non garantis : vérifier le HMAC, répondre en moins de 5 s, dédupliquer, réconcilier chaque nuit ([[RCH - API Shopify pour la boutique agentique (22-10-2026)]]).
- Conditions API : interdiction d'entraîner un modèle avec les données ; l'inférence seule n'est pas restreinte ([[RCH - API Shopify pour la boutique agentique (22-10-2026)]]).
- Plan Basic suffisant ; boutique de développement gratuite pour tester ([[RCH - API Shopify pour la boutique agentique (22-10-2026)]]).
- Garde-fous proposés : création en `DRAFT`, `productDelete` interdit aux agents, archiver plutôt que supprimer, metafields de traçabilité (`ai.design_id`, `ai.prompt_hash`, `ai.model`, `ai.review_status`), un seul système maître par champ ([[RCH - API Shopify pour la boutique agentique (22-10-2026)]]).

### Génération d'images
- Modèles à API et licence commerciale : FLUX.2 ou FLUX 3, GPT Image, Nano Banana, Ideogram 4.5, Recraft (seul vrai SVG). Midjourney exclu, pas d'API officielle. Pour le texte dans l'image : Nano Banana Pro, GPT Image, Ideogram ([[RCH - Génération d'images pour l'impression (22-10-2026)]]).
- Conditions 2026 des deux modèles retenus : Nano Banana Pro à 0,134 $ par image en 1K ou 2K, 0,24 $ en 4K, moitié prix en batch, sans entraînement sur l'API payante, SynthID invisible sur toutes les sorties, modèle encore en « preview » ; Ideogram 4.0 à 0,03 à 0,10 $, usage commercial libre, pas d'entraînement sur l'API, préavis de 14 jours avant changement de prix, clause d'attribution « Powered by Ideogram » à portée incertaine. 100 designs en 4K ≈ 24 $ avec Nano Banana Pro, ≈ 10 $ avec Ideogram Quality, hors régénérations (estimé). Détail et politiques des plateformes dans [[SYN - Juridique]] ([[RCH - Images IA, modèles et plateformes (29-10-2026)]]).
- Les licences des poids ouverts se durcissent en 2026. Seul Adobe Firefly offre une indemnisation PI, en contrat entreprise. OpenAI retire des modèles en octobre et décembre 2026 : cacher le fournisseur derrière une interface interne ([[RCH - Génération d'images pour l'impression (22-10-2026)]]).
- Format cible : PNG transparent, sRGB, 150 DPI minimum, 300 pour papier et coques. Aucun générateur ne sort la taille d'impression (1K à 4K natif) : agrandissement obligatoire, ×4 à ×6 pour un plaid, ×2 pour une affiche A3 (Real-ESRGAN pour les aplats), détourage (BiRefNet), nettoyage des bords pour éviter les halos ([[RCH - Génération d'images pour l'impression (22-10-2026)]], [[RCH - Images IA, modèles et plateformes (29-10-2026)]], [[RCH - Plaid personnalisé grands-parents (28-10-2026)]]).
- Métadonnées : l'AI Act (art. 50, marquage lisible par machine), Google Merchant Center (IPTC DigitalSourceType obligatoire sur les images produit IA, retrait interdit) et Meta (label automatique si C2PA détecté) reposent sur IPTC, C2PA et SynthID. La chaîne agent, interface, agrandissement, Shopify, CDN et flux Merchant Center doit conserver ces marqueurs ⚠️ à vérifier, et la survie de SynthID à l'agrandissement et à l'impression est inconnue ([[RCH - Images IA, modèles et plateformes (29-10-2026)]]).
- Mockups : API Printful gratuite mais lente, ou rendu PSD (Dynamic Mockups, SudoMock). Jamais d'édition IA sur la vue du produit vendu ([[RCH - Génération d'images pour l'impression (22-10-2026)]]).
- Contrôle avant publication : vérifications déterministes, OCR du texte, score esthétique en filtre grossier, juge vision-langage calibré, liste noire et détection de logos, déduplication par hachage perceptuel. Printify impose une relecture humaine de tout contenu IA et met la PI des sorties à la charge du vendeur. Le contrôle porte sur les sorties et pas seulement sur les prompts : un prompt propre peut produire une image proche d'une œuvre ([[RCH - Génération d'images pour l'impression (22-10-2026)]], [[RCH - Images IA, modèles et plateformes (29-10-2026)]]).
- Coût estimé : environ 0,12 $ par design publié ([[RCH - Génération d'images pour l'impression (22-10-2026)]]).

### Formats et gabarits par support
Les études produit donnent les contraintes de composition que le créateur doit respecter ([[RCH - Synthèse comparative des produits d'élargissement (29-10-2026)]]).
| Support | Format maître | Fichier | Contraintes |
|---|---|---|---|
| Mug 11 oz | bandeau ≈ 2,4:1 | 2475 × 1155 px (Printify) ; 200 × 96 mm (Gelato) ; autres valeurs selon les sources ⚠️ | l'anse coupe le visuel : deux faces ou une face décentrée, zone de l'anse vide ; marges ≈ 75 px haut et bas |
| Gobelet isotherme | wrap presque carré, conique | 2776 × 2374 px (Printful) | fichier « straight » ou « tapered » selon le blank ; 1 cm de sécurité au couvercle et à la base |
| Affiche | portrait | A4 2 480 × 3 508 px ; A3 3 508 × 4 961 ; 30 × 40 cm 3 543 × 4 724 ; 50 × 70 cm 5 906 × 8 268 | ratios A (1:1,414) et 30 × 40 (1:1,333) différents : deux compositions ou marge de recadrage ; rien d'important près des bords (cadre) |
| Tote bag | carré | 3600 × 3600 ou 4500 × 4800 px selon les sources ⚠️ | DTG sur toile écrue : aplats nets, contours fermés, pas de dégradé vers la transparence |
| Coussin | carré 40 × 40 ou 45 × 45 cm | 2 362 à 5 315 px selon DPI | 1 à 2 cm de fond perdu, prénoms et visages à 3 cm des bords, verso uni |
| Sous-verres | carré 9,5 cm, coins arrondis | ≈ 1 200 × 1 200 px avec 3 mm de fond perdu | fond plein sans cadre, personnage à 8 mm des bords, un prénom par pièce jusqu'à 4 |
| Tablier | vertical 70 × 80 à 70 × 96 cm | ≈ 4 410 × 4 880 px à 150 dpi | zone de la poche (bas-centre) à éviter ; sublimation = fond clair ; DTG coton coloré = sous-couche blanche et halo |
| Torchon | vertical 50 × 70 cm | 2 953 × 4 134 px à 150 dpi | lisible plié en deux ou quatre ; DTG sur écru : pas de blanc, pastels ternis, lignes fines perdues |
| Plaid | 5:6 ou 3:4, 130 × 150 à 150 × 200 cm | 7 875 × 9 375 à 9 375 × 12 375 px (≈ 155 dpi), max 23 000 px et 50 Mo | zone de sécurité 8 à 10 cm ; formes franches ; capitales 3 à 8 cm |
| Planche | paysage 30 × 20 à 39 × 28 cm | gravure 1 950 × 1 575 px ; verre ≈ 2 400 × 3 300 px | gravure monochrome au trait, traits ≥ 0,3 mm, marge de bois nu 2 cm ; chaîne séparée de la sublimation |
- Règle commune : un visuel ne se redimensionne pas d'un support à l'autre, il se recompose. Générer en calques séparés (fond, famille, zone prénoms) permet la recomposition sans régénération ([[RCH - Plaid personnalisé grands-parents (28-10-2026)]], [[RCH - Sous-verres personnalisés pour grands-parents (28-10-2026)]]).
- Une chaîne de génération par technique d'impression : sublimation (couleur), DTG (aplats, halos), gravure (monochrome au trait), broderie (6 couleurs maximum chez Printify) ([[RCH - Planche à découper et planche apéro grands-parents (29-10-2026)]], [[RCH - Textile personnalisé grands-parents, tote bag en priorité (28-10-2026)]]).

### Personnalisation à la commande
- Mécanique observée chez tous les concurrents : illustration fixe et zone de texte remplie à la commande, par champ libre limité en caractères ou par champs séparés avec sélecteur du nombre de personnes ; rappel « relisez prénoms, dates et accents » ; aperçu avant commande chez les leaders, absent chez les petits ([[RCH - Marché des mugs grands-parents avec prénoms (28-10-2026)]], [[RCH - Coussin grands-parents (28-10-2026)]]).
- Gabarits par nombre de prénoms (1-2, 3-4, 5-6, 7-8) plutôt qu'un champ qui rétrécit : plafonds concurrents 6, 8, 9 à 12 ; mécanique dominante « un élément graphique par petit-enfant » ; avis « inscriptions peu visibles » (Cadeaux.com, 19/10/2026) sur la lisibilité ; police avec é, è, ê, ë, ï, ç, œ et prénoms composés à tester par support ([[RCH - Synthèse comparative des produits d'élargissement (29-10-2026)]]).
- Applications Shopify : quatre couvrent le flux complet avec Printify (aperçu en direct, fichier d'impression automatique, envoi au fournisseur) : Teeinblue (49 $ par mois plus 0 à 0,40 $ par article), Customily (49 $ plus 0,25 à 1 $), HelloCustom (24,99 $ plus 0,29 $), AnywherePOD (9,99 à 24,99 $). Teeinblue et Customily couvrent aussi Gelato ; Gelato a son Personalization Studio dans Gelato+ ; Printify natif est gratuit mais sans aperçu rendu sur Shopify ([[RCH - Applications de personnalisation Shopify pour Printify et Gelato (29-10-2026)]]).
- Aucune API publique de gabarits chez Teeinblue, Customily, HelloCustom ni Gelato : les agents ne peuvent pas pousser un gabarit sans passer par l'interface ou un import en masse. Zakeke est le seul avec webhook « fichiers prêts ». Aucune application ne documente un changement de mise en page selon le nombre de prénoms ; les conditions (Customily, Teeinblue, Gelato) pourraient le simuler par calques affichés ou masqués, sans preuve ([[RCH - Applications de personnalisation Shopify pour Printify et Gelato (29-10-2026)]]).
- Architecture alternative : le système génère lui-même le fichier d'impression (illustration fixe plus texte rendu par code) et le pousse par l'API Printify (produit avec zones d'impression et images positionnées, webhooks de commande), avec une simple application de champs pour la saisie. Contrepartie : pas d'aperçu sur mockup, sauf Zepto. Les deux voies restent à trancher ([[RCH - Applications de personnalisation Shopify pour Printify et Gelato (29-10-2026)]]).
- Printify : contradiction entre approbation manuelle obligatoire et soumission automatique possible pour les commandes personnalisées ⚠️ ([[RCH - Applications de personnalisation Shopify pour Printify et Gelato (29-10-2026)]]).

### Décision statistique
- Les petits nombres trompent : un produit à 1,4 % fait zéro vente sur 100 visites une fois sur quatre. Une règle « zéro vente après 100 visites » éliminerait un bon produit sur quatre ([[RCH - Méthodes statistiques pour garder ou retirer un produit (25-10-2026)]]).
- Méthode centrale : Beta-Binomial avec prior tiré du catalogue (force bornée entre 50 et 500 visites fictives), décision sur la probabilité que la marge par visite passe sous un seuil, et perte attendue ([[RCH - Méthodes statistiques pour garder ou retirer un produit (25-10-2026)]]).
- Règles de départ : exposition minimale de 300 visites, 14 jours et 4 ventes attendues ; retrait si probabilité sous le seuil d'au moins 90 % deux revues de suite ; garder si au-dessus à 80 % ; revue hebdomadaire à jour fixe ; au plus 10 % de retraits par semaine ; fenêtre de 90 jours ou escompte gamma 0,98 à 0,99 ; pause saisonnière au lieu de retrait ([[RCH - Méthodes statistiques pour garder ou retirer un produit (25-10-2026)]]).
- Avec 8 à 12 mugs et 300 visites par mug, l'apprentissage par les ventes est lent ; les validations humaines de la phase de calibration (oui, non, raison courte) donnent un signal en quelques heures et doivent devenir des leçons dans Obsidian ([[SYN - Choix de la niche]]).
- Visibilité par échantillonnage de Thompson, récompense = taux tiré multiplié par la marge unitaire. Priors par catégorie pour les nouveaux produits ([[RCH - Méthodes statistiques pour garder ou retirer un produit (25-10-2026)]]).
- Pièges : biais de position, sources de trafic, budgets pub inégaux, peeking, comparaisons multiples, biais du survivant, suivi cassé. Décider sur les ventes Shopify, pas sur les conversions des plateformes ([[RCH - Méthodes statistiques pour garder ou retirer un produit (25-10-2026)]], [[SYN - Acquisition]]).
- Les calculs du rapport ont été faits à la main et le pseudo-code n'a pas été exécuté ⚠️ à recalculer avec scipy et à calibrer par simulation ([[RCH - Méthodes statistiques pour garder ou retirer un produit (25-10-2026)]]).

### Architecture
- Colonne vertébrale : une exécution durable qui sauvegarde l'état à chaque étape et reprend après un crash ou une attente humaine. Option principale Temporal avec des agents Pydantic AI ; option légère LangGraph avec checkpointer Postgres et `interrupt()`. Toute action externe doit être idempotente ([[RCH - Architecture multi-agents et mémoire (25-10-2026)]]).
- Agents étroits à rôle séparé ; le script de publication reste du code testé. Project Vend : un agent superviseur du même modèle n'a rien apporté, les procédures imposées ont été le meilleur levier ([[RCH - Architecture multi-agents et mémoire (25-10-2026)]]).
- Les agents ne parlent jamais directement à Shopify : une passerelle unique détient le token, expose des opérations fermées, journalise ; une file d'attente par boutique applique le budget de points et l'idempotence ([[RCH - API Shopify pour la boutique agentique (22-10-2026)]]).
- Fournisseur : file d'attente par endpoint, créations idempotentes, visuels stockés chez soi ([[SYN - Fournisseurs]]).

### Mémoire
- Faits chiffrés en Postgres ; leçons dans Obsidian avec statut, date de revue et lien vers la requête SQL qui les prouve ; agents limités à une boîte de réception ; consolidation périodique qui relance la preuve avant promotion. Un agent ne cite jamais un chiffre lu dans une note sans le recalculer ([[RCH - Architecture multi-agents et mémoire (25-10-2026)]]). C'est le modèle retenu dans [[_conventions]], section 6.
- Le journal des prompts et des retouches validées sert aussi de preuve d'apport humain pour une éventuelle protection par le droit d'auteur ([[RCH - Images IA, modèles et plateformes (29-10-2026)]]).
- Mem0, Letta et Zep visent la mémoire conversationnelle : inutiles au départ. Markdown source de vérité, index reconstructible, versionnement git ([[RCH - Architecture multi-agents et mémoire (25-10-2026)]]).

### Validation humaine et supervision
- Démarrer en mode fantôme, puis monter l'autonomie par type d'action et par paliers : approbation unitaire, par lot, revue après coup. Critère estimé de passage : 50 décisions, 95 % approuvées sans modification, zéro incident PI ([[RCH - Architecture multi-agents et mémoire (25-10-2026)]]).
- Toujours bloqués : budget publicitaire, prix sous le plancher de marge, designs signalés PI, nouvelle catégorie, textes juridiques et promesses de délai, remboursements ([[RCH - Architecture multi-agents et mémoire (25-10-2026)]]).
- Traces OpenTelemetry GenAI vers Langfuse ou Phoenix, coût par exécution avec coupe-circuit, jeu de cas rejoué à chaque changement de prompt, juge LLM recalibré chaque mois, métriques business par design ([[RCH - Architecture multi-agents et mémoire (25-10-2026)]]).

### Sources de tendances
- Shopify est la source de vérité des ventes. Google Trends API en alpha sur candidature, pytrends à éviter, Pinterest Trends API officielle ⚠️ accès à vérifier, Amazon et Reddit peu utiles, calendriers d'événements en table SQL ([[RCH - Architecture multi-agents et mémoire (25-10-2026)]]). Aucune des quinze recherches de marché n'a obtenu de volume Google ni de courbe Trends : la source reste à ouvrir ([[SYN - Choix de la niche]]).
- Cadre UE : exception de fouille sauf opposition lisible par machine, droit des bases de données, conditions d'utilisation opposables, RGPD. Collecter des agrégats, jamais de profils ([[RCH - Architecture multi-agents et mémoire (25-10-2026)]]).

### Retours d'expérience
- Project Vend : agent complaisant poussé aux remises. Automaton : un agent autonome a rapporté 0 $ en un mois. Les agents réduisent le coût d'exécution, pas le coût d'avoir raison sur la demande. Les suspensions POD viennent des marques et personnages, pas de l'usage de l'IA ([[RCH - Architecture multi-agents et mémoire (25-10-2026)]]).

### Contradictions non tranchées
- Plafond de variantes Shopify : 500 000 puis 10 000 par jour (doc actuelle) contre 50 000 puis 1 000 (sources 2025). Retries des webhooks : 8 sur 4 h ou 19 sur 48 h.
- Benchmarks de mémoire : chiffres fournisseurs (Mem0 92,5 %) contre test indépendant (Letta 52 %, Mem0 50 %).
- Fenêtre d'observation : 14 jours (Shopify et statistiques), 30 jours « sans vente » (architecture).
- Débit des mockups Printful : 2 à 10 par minute selon la doc, selon l'ancienneté de la boutique selon un tiers.
- Zone d'impression du mug 11 oz et du tote bag : plusieurs valeurs selon les sources ; seul le gabarit de l'imprimeur retenu fait foi.
- Printify : approbation manuelle obligatoire ou soumission automatique possible des commandes personnalisées.
- C2PA chez Google : « à venir » ou « déjà présent » selon la source.

## Ce qui est décidé
- Approbation unitaire de chaque design et fiche au lancement, analyste en proposition seulement, service client humain et documenté, paliers d'autonomie par type d'action (unitaire, lot, après coup ; 50 décisions, 95 %, zéro incident PI), liste des actions toujours bloquées dont `productDelete` ([[03 - Approbation unitaire au lancement, paliers d'autonomie, actions toujours bloquées]]).
- Deux choix de structure sont fixés dans [[_conventions]] : faits en base, leçons dans Obsidian, agents limités à `propositions/`, l'humain tranche.
- Orchestration LangGraph au départ (checkpointer Postgres, `interrupt()`), étapes idempotentes pour garder Temporal possible ; interface d'images interne avec Nano Banana Pro par défaut et Ideogram en second, choix par A/B sur Noël ([[06 - LangGraph au départ, interface d'images interne avec Nano Banana Pro et Ideogram]]). Les conditions relevées le 29/10 sont compatibles ; points ouverts : propriété des sorties chez Google, clause d'attribution Ideogram, conservation des marqueurs IA.

Décisions attendues :
- le suivi des vues produit (Web Pixel ou GA4) ;
- les seuils de décision de l'analyste, après simulation ;
- la personnalisation à la commande : application tierce (Teeinblue, Customily, HelloCustom) ou fichier généré par le système et poussé par l'API Printify ;
- le brief visuel de la « famille illustrée » et les gabarits de prénoms par support ;
- la conservation ou non des métadonnées IPTC et C2PA dans la chaîne de publication.

## Questions ouvertes
- La boutique appartient-elle à l'organisation Shopify d'Antoine ? Sinon le client credentials grant est impossible.
- `sales` permet-il de regrouper par identifiant produit ? Une métrique de vues par produit existe-t-elle en 2026-10 ?
- Délai d'obtention de `read_all_orders` et de l'accès de niveau 2.
- Quel modèle d'images donne le meilleur coût par design vendu (test A/B à faire) ? Taux d'erreur réel du juge sur les personnages protégés.
- Quelle application rend correctement les accents et un prénom composé, avec quelle police, et sur quel thème mobile ? Une application permet-elle d'importer des gabarits en masse ?
- L'imprimeur UE retenu attend-il 2475 × 1155 px pour le mug, ou un autre format ?
- SynthID et C2PA survivent-ils à l'agrandissement, à l'ajout du texte et à l'impression ? Shopify conserve-t-il les métadonnées IPTC ?
- Accès à l'alpha Google Trends et à Pinterest Trends.
- Taille d'échantillon minimale pour valider une leçon dans une petite boutique.
- Branche maintenue de Pydantic AI (v1 ou v2) ⚠️ à vérifier.
- Le fournisseur de LLM garantit-il par contrat l'absence d'entraînement ? Pour Google et Ideogram, oui sur l'API payante selon leurs conditions ; à relire à chaque changement.

## Recherches
- [[RCH - API Shopify pour la boutique agentique (22-10-2026)]]
- [[RCH - Génération d'images pour l'impression (22-10-2026)]]
- [[RCH - Méthodes statistiques pour garder ou retirer un produit (25-10-2026)]]
- [[RCH - Architecture multi-agents et mémoire (25-10-2026)]]
- [[RCH - Applications de personnalisation Shopify pour Printify et Gelato (29-10-2026)]]
- [[RCH - Images IA, modèles et plateformes (29-10-2026)]]
- Contraintes de design par support : [[RCH - Synthèse comparative des produits d'élargissement (29-10-2026)]]
