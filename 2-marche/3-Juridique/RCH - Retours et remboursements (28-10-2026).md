---
type: research
title: RCH - Retours et remboursements (28-10-2026)
status: draft
related: ["[[SYN - Juridique]]"]
decisions: []
date: 2026-10-28
sources: ["https://help.printify.com/hc/en-us/articles/4483630299025", "https://donneespersonnelles.fr/commande-personnalisee-retractation"]
last-verified: 2026-10-28
tags: [dropshipping, juridique, retours]
---
# RCH - Retours et remboursements (28-10-2026)

Recherche menée par Maitre avec Claude (Cowork), indépendamment des autres notes du dossier.
Ce n'est pas un avis juridique : CGV à faire relire par un professionnel.

## Contexte posé
Qui gère les remboursements, Printify ou la boutique ? Comment gérer le droit de rétractation de 14 jours
quand le produit n'a aucun défaut, et comment l'éviter ?

## Conclusion en une phrase
Printify ne couvre que les défauts de fabrication et d'impression ; tout le reste est à la charge de la
boutique, et une petite personnalisation saisie par le client (prénom, date) supprime le droit de rétractation.

## Résultats

### Ce que Printify couvre
```
Problème signalé par le client
   ├─ Défaut d'impression ou de fabrication, produit abîmé
   │     → Printify réimprime ou rembourse gratuitement
   │       (photo, réclamation sous 30 jours après livraison, sans retour du produit)
   └─ Le client change d'avis ou se trompe (taille, couleur)
         → Printify ne fait rien : pas de retours ni d'échanges
           → c'est la boutique qui rembourse
```
- Le client contacte **la boutique**, pas Printify. La boutique ouvre la réclamation chez Printify.
- Plusieurs produits défectueux : une seule photo ou vidéo montrant tous les articles.
- Livraison échouée : réimpression payante ou remboursement partiel.
- ⚠️ La garantie légale de conformité dure 2 ans et engage la boutique face au client, même si Printify
  fabrique. Au-delà des 30 jours couverts par Printify, un défaut est à la charge de la boutique.
  ⚠️ à vérifier (durée de 2 ans non sourcée dans cette recherche).

### Droit de rétractation de 14 jours
```
Livraison au client
   │ le client a 14 jours pour se rétracter, sans justification
   ▼
Il renvoie le produit dans les 14 jours suivants
   ▼
La boutique rembourse sous 14 jours après la demande
   (prix + livraison standard de l'aller ; peut attendre le colis ou la preuve d'envoi)
```
⚠️ à vérifier : délais et modalités de remboursement non sourcés dans cette recherche.

- Avec des designs fixes choisis par l'IA (le client prend un modèle dans un catalogue), le produit
  n'est pas considéré comme personnalisé : **la rétractation s'applique**. Printify ne reprenant rien,
  chaque rétractation coûte le produit à la boutique.

### L'éviter avec une petite personnalisation
- Exception (art. L221-28 3° du Code de la consommation) : biens « confectionnés selon les spécifications
  du consommateur ou nettement personnalisés ».
- Il suffit d'un **champ rempli par le client** : prénom, date, nom de famille, texte. Le produit devient
  personnalisé et le droit de rétractation ne s'applique plus.
- On garde les designs choisis par l'IA ; le client ajoute seulement son texte
  (exemple : la boule de Noël IA + « Famille Martin 2026 »).
- Printify gère la personnalisation par le client sur Shopify.
- Double bénéfice : plus de risque de rétractation, et un produit à son nom se vend mieux.
- Limites :
  - choisir une couleur ou un modèle dans une liste prédéfinie **ne suffit pas** ;
  - fabriquer à la commande ou ne pas avoir de stock **ne suffit pas** ;
  - la personnalisation ne supprime **pas** la garantie en cas de défaut.

### Si des produits restent non personnalisés
- Mettre les **frais de retour à la charge du client** dans les CGV (renvoyer un mug coûte environ 6 à 8 €,
  estimé). ⚠️ à vérifier : condition d'information dans les CGV.
- Faire revenir les colis **chez la boutique**, pas chez Printify, pour les revendre en « seconde chance ».
- **Rembourser sans retour** quand le renvoi coûterait plus cher que le produit.
- Garder une **réserve de 3 à 5 % du CA** pour les retours (estimé, à ajuster avec les vrais chiffres).
- Réduire les retours en amont : mockups fidèles, vraies photos, dimensions claires.

### Automatisation par le système
```
Formulaire « Retour » sur la boutique
   ▼
Vérification : livraison + 14 jours ? produit personnalisé ?
   ├─ hors délai ou personnalisé → refus automatique avec la raison
   └─ éligible → adresse de retour et instructions
                 ▼
          numéro de suivi du retour reçu → remboursement via l'API Shopify
```

## Chiffres
| Chiffre | Valeur | Provenance |
|---|---|---|
| Délai de réclamation Printify | 30 jours après livraison | source : Printify Help Center |
| Délai de rétractation | 14 jours | ⚠️ à vérifier sur Légifrance |
| Garantie légale de conformité | 2 ans | ⚠️ à vérifier |
| Coût d'un renvoi de mug | 6 à 8 € | estimé |
| Réserve pour retours | 3 à 5 % du CA | estimé |

## Caveats
- Aucun arrêt consulté ne tranche le cas exact du print-on-demand ; l'analyse « catalogue = non personnalisé »
  découle du raisonnement de la source (choix parmi des options prédéfinies), pas d'une décision de justice.
- Le texte exact de l'article L221-28 n'a pas été lu sur Légifrance. ⚠️ à vérifier.
- La politique Printify peut changer : la relire avant le lancement.

## Retenu / écarté
(à remplir à la revue)
