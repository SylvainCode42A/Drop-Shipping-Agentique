---
type: decision
title: 04 - Noël 2026 en test manuel réduit, Fête des grands-mères 2027 pour le système
status: validé
date: 2026-10-25
implemented: non
related: ["[[OVR - Drop shipping agentique]]", "[[SYN - Acquisition]]", "[[SYN - Choix de la niche]]", "[[02 - Lancement avec le mug, la boule en cristal et la décoration en bois, trois imprimeurs UE]]", "[[03 - Approbation unitaire au lancement, paliers d'autonomie, actions toujours bloquées]]", "[[RCH - Calendrier des occasions de cadeaux en France et dans l'UE (25-10-2026)]]"]
decisions: ["[[02 - Lancement avec le mug, la boule en cristal et la décoration en bois, trois imprimeurs UE]]", "[[03 - Approbation unitaire au lancement, paliers d'autonomie, actions toujours bloquées]]", "[[05 - Printify seul fournisseur avec partenaire UE figé, franchise de TVA au départ]]"]
last-verified: 2026-10-31
tags: [dropshipping, acquisition, decision]
---
# 04 - Noël 2026 en test manuel réduit, Fête des grands-mères 2027 pour le système

## Contexte
Quatrième décision attendue par [[OVR - Drop shipping agentique]]. Au 25/10/2026 : aucune boutique,
aucun fournisseur, aucun échantillon, aucune ligne de code. Les recherches donnent la règle : publier
6 à 8 semaines avant une fête, publicité 4 à 6 semaines avant, commandes closes 15 jours avant en décembre ;
le CPM Meta double en novembre et monte encore la semaine du Black Friday ; il faut environ 30 ventes pour
déclarer un gagnant ([[SYN - Acquisition]], [[RCH - Calendrier des occasions de cadeaux en France et dans l'UE (25-10-2026)]]).
Les budgets de test divergent : 600 € pour Noël et 1 400 € pour mars ([[RCH - Choix de la niche de lancement (25-10-2026)]])
contre 3 500 à 4 000 € sur dix semaines ([[RCH - Canaux d'acquisition (22-10-2026)]]).

## Décision
**Noël 2026 : test manuel réduit, sans système d'agents.**
- Pour l'instant, le site met Noël en avant, avec un message centré sur l'amour de sa famille
  (« on pense à eux »). Toutes les publicités sont dirigées sur Noël. (ajouté le 31/10/2026)
- Les 3 produits de la décision 02 (mug, boule en cristal, décoration en bois), chacun en plusieurs
  variantes : une variante par image. Les images sont créées à la main avec les outils d'images et
  validées une par une. (corrigé le 31/10/2026, remplace « 8 à 12 mugs famille illustrée »)
- Boutique Shopify ouverte, fiches Google gratuites, publication sur Etsy en parallèle.
- Meta : une seule campagne, à partir de la mi-novembre, sur trois semaines environ, dans le budget
  ci-dessous. (corrigé le 31/10/2026, remplace « 20 € par jour »)
- Produits en ligne au plus tard le 15/11/2026, commandes closes le 10/12/2026 (estimé, à caler sur
  le délai réel du fournisseur).
- Budget : **500 € en tout** pour le test, hors coût des produits vendus, accepté comme perdu.
  (corrigé le 31/10/2026, remplace « 800 € au plus »)
- Ce qu'on mesure : CPA réel, taux de casse, délai réel fournisseur, erreurs de prénom,
  questions des clients (corpus du futur agent de service client, décision 03).

**Les autres fêtes, après Noël (ajouté le 31/10/2026).**
- On vise aussi les autres fêtes du calendrier ([[RCH - Calendrier des occasions de cadeaux en France et dans l'UE (25-10-2026)]]),
  pas seulement Noël.
- Pour chaque fête, on sélectionne des images pour chaque angle : famille, parents, grands-parents, couple.
  Chaque image devient une variante des 3 produits.
- Les images retenues sont choisies selon les recherches qui performent le plus.
- Le budget de chaque fête est décidé après Noël, avec les chiffres réels de Noël. (ajouté le 31/10/2026)

**Fête des grands-mères, 07/03/2027 : premier vrai test du système.**
- Produits en ligne mi-janvier 2027, Pinterest fin janvier, Meta et Google Shopping début février.
- Budget : décidé après Noël, avec les chiffres réels (corrigé le 31/10/2026, remplace le plafond
  de 2 500 €). Le plan à 3 500-4 000 € sur dix semaines reste la référence si Noël montre un CPA tenable.
- Réussite : au moins 30 ventes sur l'angle principal avec un CPA sous 20 € ([[02 - Lancement avec le mug, la boule en cristal et la décoration en bois, trois imprimeurs UE]]).

## Alternatives écartées
- **Noël seul, tout miser dessus** : CPM au plus haut, pas le temps d'apprendre Meta ni d'atteindre
  30 ventes. Un échec en décembre dirait quelque chose du calendrier, pas du projet.
- **Mars directement, rien à Noël** : le système se construirait sur des estimations jusqu'en mars,
  alors que Noël est la plus grosse occasion de l'angle principal et le seul moyen d'avoir des chiffres réels avant de coder.
- **Noël avec le système d'agents** : pas le temps de le coder en trois semaines.

## Conséquences
- Novembre et décembre : ouverture de la boutique, choix du fournisseur (décision 05) et échantillons
  avant le 15/11, bannière de consentement, pixel Meta, CGV. Le code du système n'est pas prioritaire.
- Janvier : revue des chiffres de Noël, révision des décisions 02 et 04, fixation du budget de chaque
  fête, puis mise en route du système.
- L'agent publicitaire de mars reçoit un plafond (fixé en janvier) et un CPA maximum de 20 €, tous deux
  dans les actions bloquées de la décision 03.
- Les décisions 05 et 06 doivent être prises avant le 15/11/2026 pour le fournisseur, avant janvier pour l'orchestration.
- Tous les chiffres sont estimés. À inscrire dans A VERIFIER : délai réel fournisseur en décembre, seuil
  d'apprentissage Meta (50 événements ou 10 par semaine).
- Une sélection d'images par fête et par angle (famille, parents, grands-parents, couple) est à préparer
  avant chaque fête, à partir des recherches qui performent le plus. Chaque image devient une variante
  des 3 produits.

## Concerne
[[SYN - Acquisition]] · [[SYN - Choix de la niche]] · [[SYN - Modèle économique]] · décisions 05 et 06 · TODO à créer (ouvrir la boutique, commander des échantillons).
