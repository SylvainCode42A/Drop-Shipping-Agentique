---
type: synthese
title: SYN - Juridique
status: validé
related: ["[[_conventions]]", "[[SYN - Modèle économique]]", "[[SYN - Fournisseurs]]", "[[SYN - Choix de la niche]]", "[[SYN - Système]]", "[[SYN - Acquisition]]", "[[A VERIFIER - Points à valider, vérifier, tester]]"]
decisions: ["[[03 - Approbation unitaire au lancement, paliers d'autonomie, actions toujours bloquées]]", "[[05 - Printify en principal avec partenaire UE figé, Gelato en second, franchise de TVA au départ]]", "[[06 - LangGraph au départ, interface d'images interne avec Nano Banana Pro et Ideogram]]"]
last-verified: 2026-10-29
tags: [dropshipping, juridique, synthese]
---
# SYN - Juridique

État des connaissances sur le cadre juridique de la boutique. Une recherche de cadre général, une recherche sur les images IA (modèles et plateformes), et les points juridiques remontés par treize études produit.
Ce n'est pas un avis juridique ni fiscal : les points marqués « à valider » passent par un avocat ou un expert-comptable.

## Ce qu'on sait

### Contrefaçon
- Reproduire une marque, un logo, un personnage ou une œuvre sans licence est une contrefaçon (CPI, art. L716-4). Le vendeur est responsable, même si le design vient d'une IA et si un tiers imprime ([[RCH - Cadre juridique (22-10-2026)]]).
- Les petits vendeurs sont poursuivis : TJ Paris du 17/09/2026 (upcycling Louis Vuitton, 750 000 €) et du 27/08/2026 (Palme d'or) ⚠️ à vérifier sur le texte intégral ([[RCH - Cadre juridique (22-10-2026)]]).
- Le principal danger pour ce projet est le « trend-jacking » : un slogan viral peut être une marque déposée, copier un best-seller peut être du parasitisme, le fan-art n'est pas une exception ([[RCH - Cadre juridique (22-10-2026)]]). Les études de niche citent déjà des cas concrets : « Libéré, délivré », Obut, marques de motos et de golf ([[SYN - Choix de la niche]]).
- Tous les imprimeurs mettent la propriété intellectuelle des sorties IA à la charge du vendeur : Printify (conditions des outils IA tiers, et depuis le 08/07/2026 le vendeur répond aussi des contenus de personnalisation de ses clients), Gelato (règles PI étendues aux contenus IA, garantie contre les réclamations de tiers), Printful (politique PI du 03/02/2026, résiliation possible) ([[RCH - Images IA, modèles et plateformes (29-10-2026)]]).
- Printify déconseille explicitement les prompts « in the style of Disney Pixar » ; des offres en « style Disney Pixar » existent sur Etsy ([[RCH - Marché des mugs grands-parents avec prénoms (28-10-2026)]]).
- Bases pour la liste noire : INPI (marques françaises depuis 1976, marques UE depuis 1996, API pour requêtes en masse), TMview (recherche par image), EUIPO eSearch plus (alertes), WIPO Global Brand Database. Aucune source publique structurée de personnages sous licence ⚠️ ([[RCH - Cadre juridique (22-10-2026)]], [[RCH - Images IA, modèles et plateformes (29-10-2026)]]).
- Copier une composition identifiable d'un concurrent (figurines Monsieur TShirt, « Family Portrait » d'Ourson Câlin, line art « mains reliées » d'une boutique Etsy à 11 000 avis) expose au parasitisme ou à un signalement de plateforme, même si le style n'est pas protégé ([[RCH - Synthèse comparative des produits d'élargissement (29-10-2026)]]).

### Droits sur les images produites par IA
- Le droit d'auteur exige un auteur humain (CJUE Infopaq, Painer). Le CSPLA (juillet 2026) retient qu'une production entièrement générée n'a pas d'auteur, mais admet les créations hybrides avec une vraie direction humaine ([[RCH - Cadre juridique (22-10-2026)]]).
- Jurisprudence 2026 : AG München (13/02/2026) refuse la qualité d'œuvre à trois logos IA faute d'influence créatrice suffisante, en admettant que l'apport humain intervienne pendant la génération (suite de prompts) ou après (retouche) ; résolution du Parlement européen du 10/03/2026 (rapport Voss) contre la protection d'un contenu entièrement généré ; Cass. civ. 1re du 9 avril 2026 (pourvoi 25-11.711) exige de démontrer en quoi les choix esthétiques traduisent la personnalité de l'auteur, arrêt non spécifique à l'IA ⚠️ ([[RCH - Images IA, modèles et plateformes (29-10-2026)]]).
- Conséquence : les designs des agents ne sont probablement pas protégés et peuvent être copiés. Le journal des prompts et des retouches validées est la seule preuve d'apport humain ; le dépôt de marque et l'action en parasitisme sont les seules défenses ([[RCH - Cadre juridique (22-10-2026)]], [[RCH - Images IA, modèles et plateformes (29-10-2026)]], [[SYN - Modèle économique]]).
- Style d'un illustrateur : non protégé en soi ; une imitation trop fidèle d'un style identifiable peut être du parasitisme ; un amendement propose un article L. 331-4-2 visant les contenus IA stylistiquement proches d'un auteur identifiable, statut ⚠️ inconnu ([[RCH - Images IA, modèles et plateformes (29-10-2026)]]).

### Conditions des modèles d'images
- **Nano Banana Pro** (gemini-3-pro-image-preview) : 0,134 $ par image en 1K ou 2K, 0,24 $ en 4K, moitié prix en batch ; service payant sans entraînement sur prompts ni réponses (conditions Gemini API du 25/09/2025) ; SynthID invisible sur toutes les images, C2PA annoncé ou déjà présent selon la source ; dans l'EEE seules les offres payantes peuvent servir à une application proposée à des utilisateurs ; interdiction des applications destinées aux moins de 18 ans ; modèle toujours en « preview », nouvelles conditions en aperçu sans date d'effet ; propriété des sorties ⚠️ à vérifier ([[RCH - Images IA, modèles et plateformes (29-10-2026)]]).
- **Ideogram** : 4.0 à 0,03 $ (Turbo), 0,06 $ (Default), 0,10 $ (Quality), prix 3.0 contradictoires ; pas de revendication de propriété, usage commercial libre ; pas d'entraînement sur l'API sauf contenu signalé (accord du 14/08/2024) ; clause d'attribution « Powered by Ideogram » dans l'application, portée pour une boutique ⚠️ ; préavis de 14 jours avant changement de prix ; filigrane non documenté ([[RCH - Images IA, modèles et plateformes (29-10-2026)]]).
- Alternatives : Flux (0,03 $ par mégapixel, usage commercial), OpenAI gpt-image-1.5 (0,133 à 0,20 $, C2PA), Stability (licence gratuite sous 1 M$ de CA), Recraft (sortie vectorielle native, droits commerciaux sur plans payants), Midjourney (pas d'API officielle). Résolutions natives 1K à 4K : l'A3 à 300 DPI (3 508 × 4 961 px) exige un agrandissement ([[RCH - Images IA, modèles et plateformes (29-10-2026)]]).
- Coût estimé : 100 designs en 4K avec Nano Banana Pro ≈ 24 $ (12 $ en batch), ≈ 10 $ avec Ideogram 4.0 Quality, hors régénérations ([[RCH - Images IA, modèles et plateformes (29-10-2026)]]).

### Transparence (AI Act, art. 50) et politiques des plateformes
- L'article 50 s'applique depuis le 02/08/2026 ; le marquage lisible par machine (art. 50(2)) a un délai de grâce jusqu'au 02/12/2026 pour les systèmes mis sur le marché avant le 02/08/2026 ; le Digital Omnibus (règlement UE 2026/1744, en vigueur le 27/07/2026) ne modifie pas l'article 50 ; les images générées avant le 02/08/2026 n'ont pas à être marquées rétroactivement ; code de bonnes pratiques du 10/06/2026 à deux couches (métadonnées signées et filigrane imperceptible), volontaire ([[RCH - Cadre juridique (22-10-2026)]], [[RCH - Images IA, modèles et plateformes (29-10-2026)]]).
- Pour la boutique : aucun étiquetage sur un design stylisé imprimé, mais signalement des fausses personnes réalistes dans les publicités et indication qu'un chatbot est une IA. Un mockup IA qui embellit le produit peut être une pratique commerciale trompeuse ([[RCH - Cadre juridique (22-10-2026)]]).
- **Etsy** : mention de l'IA dans la description et déclaration du partenaire de production et du lieu d'expédition, sous peine de retrait (Creativity Standards, 10/06/2025) ([[RCH - Images IA, modèles et plateformes (29-10-2026)]], [[RCH - Marché des mugs grands-parents avec prénoms (28-10-2026)]]).
- **Google Merchant Center** : depuis le 19/02/2024, marqueur IPTC DigitalSourceType trainedAlgorithmicMedia obligatoire sur les images produit générées par IA, retrait interdit ; refus et action sur le compte en cas de tromperie ([[RCH - Images IA, modèles et plateformes (29-10-2026)]]).
- **Meta Ads** : label « AI info » automatique si des métadonnées C2PA sont détectées ; déclaration par l'annonceur sans C2PA pour du contenu photoréaliste ; rejets surtout pour les personnes photoréalistes générées ([[RCH - Images IA, modèles et plateformes (29-10-2026)]]).
- **Amazon** : depuis juillet 2026, marqueur « contains-synthetic-performer » pour les visages photoréalistes IA, source secondaire ⚠️. **Shopify** : interdiction des contrefaçons, aucune règle IA spécifique trouvée dans une source officielle, contradiction entre blogs ([[RCH - Images IA, modèles et plateformes (29-10-2026)]]).
- Point structurant : l'AI Act, Google et Meta reposent sur IPTC et C2PA. La chaîne agent, interface, Shopify, CDN et flux Merchant Center doit conserver ces métadonnées ⚠️ à vérifier, et des outils publics de retrait de SynthID et C2PA existent (documenté, non recommandé) ([[RCH - Images IA, modèles et plateformes (29-10-2026)]]).

### Droit de rétractation et garanties
- 14 jours pour toute vente à distance, remboursement sous 14 jours frais de livraison inclus. Délai prolongé de 12 mois si l'information manque (art. L221-18, L221-20) ([[RCH - Cadre juridique (22-10-2026)]]).
- L'exception « nettement personnalisé » (art. L221-28 3°) s'applique si le client ajoute un prénom, un texte, une date ou une photo, dès la conclusion du contrat (CJUE Möbel Kraft). Elle ne s'applique pas à un design de catalogue, ni au choix d'une taille ou d'une couleur. Aucun arrêt ne tranche le cas exact du print-on-demand ([[RCH - Cadre juridique (22-10-2026)]], cohérent avec [[SYN - Modèle économique]]).
- Les concurrents vont au-delà de la loi : Monsieur TShirt offre 100 jours de retour et des échanges gratuits, YourSurprise « refait gratuitement ». Cela fixe l'attente client, la garantie de conformité de 2 ans restant due même sur un produit personnalisé ([[RCH - Synthèse comparative des produits d'élargissement (29-10-2026)]]).
- Depuis le 19/06/2026, un bouton « Renoncer au contrat ici » avec accusé de réception est obligatoire. Sur Shopify, il faut une application ou un développement dédié ([[RCH - Cadre juridique (22-10-2026)]]).
- Livraison sous 30 jours si aucune date n'est indiquée ([[RCH - Cadre juridique (22-10-2026)]]).

### Sécurité des produits, contact alimentaire, textile
- GPSR (règlement UE 2023/988, applicable depuis le 13/12/2024) : personne responsable établie dans l'UE pour chaque produit, analyse de risque, documentation technique, mentions sur le produit ou l'emballage. Un imprimeur UE facilite ; avec un imprimeur hors UE, la boutique porte le rôle. Sanctions françaises (loi 2024-364, art. L452-5-1 C. conso) jusqu'à cinq ans et 600 000 €. Qui l'assume entre l'imprimeur et la boutique ⚠️ à vérifier par fournisseur ([[RCH - Affiche personnalisée grands-parents (28-10-2026)]], [[RCH - Torchon personnalisé grands-parents (28-10-2026)]]).
- Contact alimentaire (règlement CE 1935/2004) : déclaration de conformité obligatoire en France pour tout objet au contact des aliments (mug, gobelet, planche, boîte). Le bois est autorisé, l'aulne et le hêtre sont listés par la DGCCRF, le bambou non ; la face imprimée ne doit pas toucher l'aliment ; Prodigi exclut l'usage alimentaire de sa boîte ; les fiches fournisseur ne citent que « lead and BPA-free » ou des normes américaines ⚠️ ([[RCH - Planche à découper et planche apéro grands-parents (29-10-2026)]], [[RCH - Boîte à biscuits grands-parents (28-10-2026)]], [[RCH - Gobelet isotherme grands-parents (28-10-2026)]]).
- Étiquetage textile (règlement UE 1007/2011) : composition en fibres en français, noms complets, « 100 % » réservé au mono-fibre, parties distinctes indiquées séparément (housse et garniture d'un coussin, sangles d'un tablier) ([[RCH - Tablier personnalisé grands-parents (28-10-2026)]], [[RCH - Coussin grands-parents (28-10-2026)]]).
- Bougie : étiquette CLP si parfumée, norme NF EN 15494 (7 pictogrammes) et EN 15493 (combustion) ; produits POD fabriqués aux États-Unis aux normes ASTM, pas EN ([[RCH - Bougie personnalisée grands-parents (29-10-2026)]]).
- Inflammabilité des textiles d'ameublement : aucune exigence française spécifique trouvée pour un coussin décoratif ; règles britanniques si vente UK ⚠️ ([[RCH - Coussin grands-parents (28-10-2026)]]).

### Site, CGV, médiation, RGPD
- Mentions légales (LCEN art. 6), CGV avec formulaire type de rétractation, adhésion à un médiateur référencé par la CECMC. La plateforme européenne RLL a fermé le 20/07/2025 : ne plus la citer ([[RCH - Cadre juridique (22-10-2026)]]).
- Cookies : consentement préalable pour les pixels publicitaires, bouton « Tout refuser » au premier niveau, même logique pour l'API Conversions de Meta ([[RCH - Cadre juridique (22-10-2026)]]).
- RGPD : registre des traitements obligatoire même en micro-entreprise, contrats de sous-traitance avec Shopify, l'imprimeur et les outils d'email. Le Data Privacy Framework reste valide, un pourvoi est pendant. Google traite les prompts selon son avenant de sous-traitant, avec cache possible hors UE ([[RCH - Cadre juridique (22-10-2026)]], [[RCH - Images IA, modèles et plateformes (29-10-2026)]]). Les photos d'enfants envoyées par les clients sont des données personnelles à durée de conservation limitée ([[SYN - Choix de la niche]]).

### Statut et fiscalité
- Recommandation du rapport : micro-entreprise au départ, puis société quand les charges dépassent environ la moitié du CA ou vers 60 000 à 80 000 € de ventes par an (estimé). La micro-entreprise taxe le CA, pas la marge ([[RCH - Cadre juridique (22-10-2026)]]).
- ACRE : moins 25 % de cotisations depuis le 01/07/2026, à demander sous 60 jours ([[RCH - Cadre juridique (22-10-2026)]]).
- Franchise en base de TVA : 85 000 € (majoré 93 500 €). Seuil des ventes à distance UE : 10 000 € HT, puis TVA du pays du client via l'OSS ([[RCH - Cadre juridique (22-10-2026)]], [[SYN - Modèle économique]]).
- Piège principal : si l'imprimeur expédie depuis un autre pays de l'UE, le seuil ne joue pas et la TVA du pays du client peut être due dès le premier euro ⚠️ à valider par un expert-comptable avant de choisir le fournisseur ([[RCH - Cadre juridique (22-10-2026)]]).
- Le statut de TVA décide de la rentabilité : toutes les marges estimées des études produit tombent de 4 à 7 € entre franchise et TVA collectée, et une TVA fournisseur non récupérable en franchise en retire 2 à 3 € de plus ([[RCH - Synthèse comparative des produits d'élargissement (29-10-2026)]]).
- Imprimeur hors UE : droit forfaitaire de 3 € par catégorie tarifaire d'article sur les colis ≤ 150 €, du 01/07/2026 au 01/07/2028 (règlement UE 2026/382), en plus de la TVA à l'import ; taxe française de 2 € suspendue depuis le 01/07/2026 ; frais de gestion de 2 € par article annoncés au 01/11/2026 ⚠️ à vérifier sur le texte officiel ([[RCH - Cadre juridique (22-10-2026)]], [[SYN - Fournisseurs]]).

### Suspensions de comptes
- Shopify : atteintes à la propriété intellectuelle et chargebacks (seuil d'alerte estimé 1 %, cible sous 0,5 %, non officiel). Google Merchant Center : « Misrepresentation », première cause, sur les incohérences site et flux. Meta : propriété intellectuelle, affirmations trompeuses, page de destination non conforme ([[RCH - Cadre juridique (22-10-2026)]]).
- Causes typiques en POD : plaintes PI sur des designs de tendance, délais réels plus longs qu'affichés, mockups trompeurs, fausses promotions, retours refusés ([[RCH - Cadre juridique (22-10-2026)]]).

### Garde-fous proposés pour les agents
Dix garde-fous détaillés dans la recherche, à transformer en notes REGLE : sources d'inspiration encadrées (thèmes, jamais un design précis), liste de termes interdits appliquée aux prompts et aux textes, OCR des images, recherche TMview automatisée, comparaison d'images, validation humaine nominative, journal de chaque design conservé 5 ans, circuit de retrait sous 24 h, garde-fous publicitaires, frein d'urgence ([[RCH - Cadre juridique (22-10-2026)]]). La recherche images IA ajoute : contrôle sur les sorties et pas seulement sur les prompts, conservation des métadonnées IPTC et C2PA, exclusion des noms d'artistes vivants des prompts, prudence sur les visages réalistes qui déclenchent les étiquetages Meta et Amazon ([[RCH - Images IA, modèles et plateformes (29-10-2026)]]).

### Contradictions non tranchées
- Droit de 3 € : « par article » ou « par catégorie tarifaire » ; les textes officiels disent par catégorie.
- Prix Ideogram 3.0 (0,04 / 0,07 / 0,10 $ contre 0,03 / 0,06 / 0,09 $) ; prix Google AI Ultra (19,99 à 249,99 $ selon les sources) ; C2PA chez Google « à venir » ou « déjà présent ».
- Obligation de déclaration IA sur Shopify : affirmée et niée par des blogs de faible qualité ; aucune source officielle.
- Etsy : page officielle du 10/06/2025 contre une politique vendeur du 14/01/2026 citée par une source secondaire.

## Ce qui est décidé
- Validation humaine nominative de chaque design et fiche avant publication au lancement ; textes juridiques, remboursements et designs signalés PI toujours bloqués pour les agents ([[03 - Approbation unitaire au lancement, paliers d'autonomie, actions toujours bloquées]]).
- Franchise de TVA et micro-entreprise au départ ; le cas d'un partenaire expédiant depuis un autre pays de l'UE est soumis à un expert-comptable avant janvier 2027 ([[05 - Printify en principal avec partenaire UE figé, Gelato en second, franchise de TVA au départ]]).
- Nano Banana Pro et Ideogram derrière une interface interne ([[06 - LangGraph au départ, interface d'images interne avec Nano Banana Pro et Ideogram]]). Les conditions commerciales relevées le 29/10 sont compatibles avec cette décision ; les points ouverts sont la propriété des sorties chez Google, la clause d'attribution Ideogram et la conservation des marqueurs IA.

Décisions attendues :
- la confirmation du schéma de TVA par l'expert-comptable ;
- la politique de contenus interdits, base de la REGLE des agents ;
- le dépôt ou non du nom de la boutique comme marque ;
- la conservation ou non des métadonnées IPTC et C2PA dans la chaîne de publication.

## Questions ouvertes
- Schéma de TVA selon le pays d'expédition réel de l'imprimeur, et récupérabilité de la TVA fournisseur (à valider, expert-comptable).
- Frontière catalogue ou personnalisé pour les produits de la boutique, et rédaction des CGV (à valider, avocat).
- Solution Shopify pour le bouton de rétractation en ligne.
- La boutique est-elle « fournisseur » au sens de l'article 50(2), avec une interface interne devant une API, ou seulement « déployeur » ? Une illustration non photoréaliste sur un mug relève-t-elle de l'article 50(4) ?
- Shopify conserve-t-il les métadonnées IPTC et C2PA ? La règle IPTC de Merchant Center s'applique-t-elle à la photo d'un produit réel portant un design IA ?
- Propriété des sorties chez Google ; portée de la clause « Powered by Ideogram » ; survie de SynthID à l'agrandissement et à l'impression.
- Meta restreint-il les publicités pour des produits personnalisés ? Règles TikTok et Google Ads non consultées.
- Frais de traitement douaniers au 01/11/2026, sur le texte officiel.
- Personne responsable GPSR entre l'imprimeur et la boutique, par fournisseur ; déclaration de conformité contact alimentaire des mugs, gobelets et planches retenus.
- Statut de l'amendement L. 331-4-2 sur le style d'un auteur identifiable.
- Source publique pour les personnages sous licence.
- Assurance responsabilité civile professionnelle.

## Recherches
- [[RCH - Cadre juridique (22-10-2026)]]
- [[RCH - Images IA, modèles et plateformes (29-10-2026)]]
- Points juridiques remontés par les études produit : [[RCH - Synthèse comparative des produits d'élargissement (29-10-2026)]]
