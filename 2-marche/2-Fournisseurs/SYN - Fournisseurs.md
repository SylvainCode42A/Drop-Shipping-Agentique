---
type: synthese
title: SYN - Fournisseurs
status: validé
related: ["[[_conventions]]", "[[SYN - Choix de la niche]]", "[[SYN - Juridique]]", "[[SYN - Modèle économique]]", "[[SYN - Système]]", "[[A VERIFIER - Points à valider, vérifier, tester]]"]
decisions: ["[[05 - Printify en principal avec partenaire UE figé, Gelato en second, franchise de TVA au départ]]"]
last-verified: 2026-10-25
tags: [dropshipping, fournisseurs, synthese]
---
# SYN - Fournisseurs

État des connaissances sur les fournisseurs d'impression à la demande et leurs API. Une recherche dédiée, complétée par l'étude sur les assiettes et objets de table. Rien n'est décidé ici.

## Ce qu'on sait

### Les fournisseurs et leurs API
- **Printify** : API REST complète (catalogue, produits, commandes, uploads, webhooks), avec publication vers Shopify par un endpoint dédié. Le catalogue donne les dimensions en pixels de chaque zone d'impression, donc un agent peut adapter le visuel seul. La qualité dépend du partenaire : il faut figer des partenaires européens ([[RCH - Fournisseurs print-on-demand et API (25-10-2026)]]).
- **Gelato** : création de produit par API à partir d'un modèle préparé dans le tableau de bord, réservée aux boutiques Shopify. Un agent ne peut pas créer un nouveau type de produit sans modèle. Production dans 32 pays dont la France, commandes de test en mode « draft » ([[RCH - Fournisseurs print-on-demand et API (25-10-2026)]]).
- **Printful** : documentation la plus complète, qualité la plus régulière, ateliers en propre en Espagne et en Lettonie. Mais l'API ne crée des produits que dans une boutique « Manual orders / API » : pour Shopify, créer le produit via l'API Admin puis le lier. Printful et Printify appartiennent au même groupe ([[RCH - Fournisseurs print-on-demand et API (25-10-2026)]]).
- **T-Pop** : atelier en France (Barjac), prix en euros HT, livraison France en 2 à 3 jours ouvrés. Pas d'API publique, une API de commandes est annoncée. Création de produits manuelle ([[RCH - Fournisseurs print-on-demand et API (25-10-2026)]]).
- **Prodigi** : API de commandes avec sandbox, fort sur l'art mural, mug produit dans l'UE mais sous-verres, tabliers et torchons expédiés du Royaume-Uni. **Spreadconnect** : API de création d'articles, ateliers en Allemagne, Tchéquie et Pologne ([[RCH - Fournisseurs print-on-demand et API (25-10-2026)]], [[RCH - Assiettes et objets de table pour compléter le mug (25-10-2026)]]).
- Écartés : Gooten et CustomCat (États-Unis), Teemill et Inkthreadable (Royaume-Uni, douane), Peecho (racheté par Prodigi) ([[RCH - Fournisseurs print-on-demand et API (25-10-2026)]]).

### Les limites techniques
- Printify : 600 requêtes par minute, 100 sur le catalogue, 200 publications par 30 minutes, jeton valable un an. Gelato : 100 requêtes par seconde, plafond de 5 000 appels par jour sauf accord. Printful : 120 requêtes par minute, 2 à 10 tâches de mockups par minute ([[RCH - Fournisseurs print-on-demand et API (25-10-2026)]]).
- Shopify : 100 profils d'expédition maximum par boutique, ce qui bloque la publication Printify sur les forums ; plafond de 1 000 variantes par jour au-delà de 50 000 ([[RCH - Fournisseurs print-on-demand et API (25-10-2026)]]).

### Les fichiers d'impression
- Formats PNG et JPG partout, SVG chez Printify, PDF chez Gelato. Profil sRGB. Résolution 150 à 300 DPI à taille réelle ; 300 DPI pour le papier et les coques. Zone d'impression du mug 11 oz chez Gelato : 200 x 96 mm ([[RCH - Fournisseurs print-on-demand et API (25-10-2026)]]).

### Les produits visés par le projet
- Mug : production 2 à 5 jours chez Printful et chez les partenaires Printify de l'UE, 1 à 6 jours chez Gelato. Printful facture chaque mug comme un premier article à l'expédition ([[RCH - Fournisseurs print-on-demand et API (25-10-2026)]], [[SYN - Modèle économique]]).
- Assiette : aucun fournisseur européen relié à Shopify. Seul Contrado (Londres) la propose, avec une conformité alimentaire non prouvée. Après le mug, l'ordre recommandé est sous-verres, tablier, boîte à thé, torchon ([[SYN - Choix de la niche]]).
- Lots : Printful emballe les mugs à part et expédie séparément les produits de lieux différents ; Contrado est le seul à faire tout en un lieu, mais hors UE ([[RCH - Assiettes et objets de table pour compléter le mug (25-10-2026)]]).

### Les retours d'expérience
- Printful : commandes ou tarifs qui ne se synchronisent plus après réinstallation de l'app. Printify : limite des profils d'expédition. Gelato : rapide en Europe mais variable selon le partenaire. Notes Trustpilot et retours français ⚠️ à vérifier ([[RCH - Fournisseurs print-on-demand et API (25-10-2026)]]).

### Les règles d'implémentation proposées
- File d'attente par endpoint, créations idempotentes, validation des visuels avant upload, variantes limitées, validation humaine avant publication, échantillons avant vente, visuels stockés chez soi ([[RCH - Fournisseurs print-on-demand et API (25-10-2026)]]). À reprendre dans [[SYN - Système]].

### Le lien avec la TVA
- Le pays d'expédition du fournisseur décide du schéma de TVA : si l'imprimeur expédie depuis un autre pays de l'UE, la TVA du pays du client peut être due dès le premier euro ⚠️ à valider par un expert-comptable avant de choisir ([[SYN - Juridique]]).

### Contradictions non tranchées
- Site Printful en Espagne : Barcelone ou Madrid. Partenaires Gelato : 130, 140 ou 250 selon les pages.
- Délai Printify vers l'Europe : 2 à 5 jours de production selon Printify, 10 à 15 jours ouvrés selon un ancien comparatif.
- Prix du mug Printful : 5,95 à 6,75 $ selon les sites tiers ([[SYN - Choix de la niche]]).
- La recherche fournisseurs est orientée textile ; le mug y est peu chiffré et l'assiette absente.

## Ce qui est décidé
- Printify en principal avec un partenaire UE figé pour le mug (France sinon Allemagne), Gelato en second et en repli, échantillons chez les deux avant le 15/11/2026, franchise de TVA au départ ([[05 - Printify en principal avec partenaire UE figé, Gelato en second, franchise de TVA au départ]]).

Décisions attendues :
- le partenaire Printify figé, après échantillons ;
- le fournisseur de complément pour les produits suivants (sous-verres, tablier, boîte à thé).

## Questions ouvertes
- Prix, délais et taux de casse réels d'un mug fabriqué en Europe chez Printify et Gelato, mesurés avec des échantillons ([[SYN - Choix de la niche]]).
- Meilleurs partenaires Printify en France et en Allemagne pour le mug.
- Prix Gelato exacts pour la France, hors promotion.
- Gelato accepte-t-il de relever le plafond de 5 000 appels par jour ?
- Printify a-t-il un environnement de test ?
- Date et périmètre de l'API T-Pop.
- Politiques des fournisseurs et de Shopify sur les designs générés par IA.
- Sublimateur français en marque blanche relié à Shopify, pour l'assiette ([[SYN - Choix de la niche]]).
- Notes Trustpilot et retours français actuels sur Printify, Gelato et Printful.

## Recherches
- [[RCH - Fournisseurs print-on-demand et API (25-10-2026)]]
- [[RCH - Assiettes et objets de table pour compléter le mug (25-10-2026)]]
