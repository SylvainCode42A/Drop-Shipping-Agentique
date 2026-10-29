---
type: todo
title: TODO - Compléter les champs légaux de la boutique
status: à faire
priority: haute
decision: "[[07 - La maquette est le cahier des charges du thème Shopify]]"
created: 2026-10-29
related: ["[[OVR - Boutique NolaPrint]]", "[[SYN - Juridique]]", "[[SYN - Fournisseurs]]", "[[TODO - Choisir les apps de rétractation et de consentement]]", "[[TODO - Corriger la maquette de la boutique]]"]
decisions: ["[[05 - Printify en principal avec partenaire UE figé, Gelato en second, franchise de TVA au départ]]", "[[07 - La maquette est le cahier des charges du thème Shopify]]"]
last-verified: 2026-10-29
tags: [dropshipping, boutique, juridique, todo]
---
# TODO - Compléter les champs légaux de la boutique

## Pourquoi
Le thème Shopify (dossier `~/Documents/nolaprint-theme`, thème Horizon #209933369689) reprend les textes
de la maquette. Les informations qui manquent y sont surlignées en jaune (classe `.todo`) : 39 zones dans
les six pages légales, et 12 ailleurs (pied de page 3, contact 2, fiche produit 3, accueil 3, rétractation 1).
Elles ne viennent pas du vault : ce sont des informations personnelles du vendeur, ou des décisions pas
encore prises (imprimeur, médiateur, délais mesurés). Sans elles, les mentions légales (LCEN art. 6), les
CGV, la médiation et les obligations GPSR ne sont pas respectées ([[SYN - Juridique]]).

## Ce qu'il faut faire
| # | Information | Où elle apparaît | Dépend de |
|---|---|---|---|
| 1 | Identité du vendeur (prénom NOM, EI), SIREN, adresse ou domiciliation | CGV §1 et annexe, mentions légales, confidentialité, pied de page | statut juridique ([[SYN - Juridique]]) |
| 2 | E-mail, téléphone et horaires du service client | CGV §1 et §9, mentions, confidentialité, livraison, contact | — |
| 3 | Nom de domaine | CGV §1 | achat du domaine |
| 4 | Date de mise en ligne | CGV | ouverture de la boutique |
| 5 | Imprimeur retenu et son pays | CGV §6, livraison, FAQ, confidentialité (destinataires) | [[05 - Printify en principal avec partenaire UE figé, Gelato en second, franchise de TVA au départ]], vérification Printify connectée |
| 6 | Délais réels (fabrication + transport) et dates limites de Noël | CGV §6, livraison, FAQ, fiche produit, bandeau d'accueil | échantillons avant le 15/11/2026 |
| 7 | Colis cadeau sans facture ni prix | FAQ | confirmation de l'imprimeur |
| 8 | Médiateur de la consommation référencé par la CECMC | CGV §10, pied de page | adhésion |
| 9 | Encadré de la garantie légale, mot pour mot (décret n° 2022-946) | CGV §8 | texte officiel |
| 10 | Fabricant, personne responsable dans l'UE, avertissements (GPSR) | fiche produit, encadré « Sécurité du produit » | imprimeur retenu ([[SYN - Juridique]]) |
| 11 | Outil d'e-mail, outil de statistiques | confidentialité, cookies | choix des outils |
| 12 | Adresse de l'hébergeur Shopify | mentions légales | conditions Shopify à la mise en ligne |
| 13 | Antériorité du nom NolaPrint (INPI, EUIPO, TMview) | mentions légales | décision attendue sur le dépôt de marque ([[SYN - Juridique]]) |
| 14 | Relecture des CGV par un avocat | CGV | — |
| 15 | Politiques Shopify (conditions d'utilisation, remboursement, expédition, mentions) | Paramètres → Politiques, affichées pendant le paiement | textes des points 1 à 9 |
| 16 | Envoi de l'accusé de rétractation par e-mail | page Renoncer au contrat | [[TODO - Choisir les apps de rétractation et de consentement]] |
| 17 | Note et avis d'exemple | accueil | application d'avis, premières ventes |

Où modifier : éditeur de thème (Personnaliser → la page → section « Contenu de page NolaPrint », champ HTML),
ou `templates/page.*.json` dans `nolaprint-theme` ; pied de page dans `sections/np-footer.liquid` ;
encadré GPSR dans les réglages de la section « Fiche produit NolaPrint ».

## Comment prouver
- Sur l'accueil, les huit pages (`/pages/cgv`, `mentions-legales`, `confidentialite`, `cookies`,
  `livraison-retours`, `faq`, `contact`, `retractation`) et une fiche produit :
  `document.querySelectorAll('.todo').length === 0`.
- `/policies/terms-of-service`, `refund-policy`, `shipping-policy` et `legal-notice` répondent 200.
- La relecture par l'avocat est datée dans `## État`.

## État
- 2026-10-29 : créée après l'intégration du thème Shopify. Champs laissés en jaune sur décision de Sylvain,
  en attendant les informations et les décisions listées ci-dessus.
