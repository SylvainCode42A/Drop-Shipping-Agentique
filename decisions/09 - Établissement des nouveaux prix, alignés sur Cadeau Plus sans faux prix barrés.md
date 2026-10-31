---
type: decision
title: 09 - Établissement des nouveaux prix, alignés sur Cadeau Plus sans faux prix barrés
status: draft
date: 2026-10-30
implemented: non
related: ["[[RCH - Audit des coûts réels Printify des trois produits (31-10-2026)]]", "[[RCH - Audit des prix Cadeau Plus et coûts Printify (30-10-2026)]]", "[[RCH - Relevé connecté du catalogue Printify UE (29-10-2026)]]", "[[RCH - Concurrents du mug famille à prénoms (29-10-2026)]]", "[[RCH - Sélection du catalogue de lancement (30-10-2026)]]", "[[RCH - Marge et prix de vente (28-10-2026)]]", "[[RCH - Retours, rétractation et abus (30-10-2026)]]", "[[SYN - Modèle économique]]", "[[SYN - Juridique]]", "[[TODO - Relever le port Printify de la boule, du bois et du mug]]", "[[A VERIFIER - Points à valider, vérifier, tester]]"]
decisions: ["[[02 - Lancement avec le mug, la boule en cristal et la décoration en bois, trois imprimeurs UE]]", "[[01 - Audience visée et nouvelle offre, parents et grands-parents d'abord, nos designs ou la page blanche]]", "[[11 - Texte facultatif à 1 €, frais de retour à la charge du client, retours chez Sylvain]]"]
last-verified: 2026-10-31
tags: [dropshipping, modele-economique, prix, decision]
---
# 09 - Établissement des nouveaux prix, alignés sur Cadeau Plus sans faux prix barrés

> Numérotée 12 jusqu'au 31/10/2026.
> **Réécrite le 31/10/2026** : seule décision qui fixe les prix. Elle regroupe les prix des décisions
> 01, 02 et 11, qui renvoient ici, toutes les recherches de prix et de coûts, et une simulation de
> chaque façon de vendre. Coûts recalculés d'après
> [[RCH - Audit des coûts réels Printify des trois produits (31-10-2026)]].

## Contexte

### Les prix du marché
Les prix de lancement (mug 24,90 €, boule 27,90 €, bois 19,90 €) sont jugés trop élevés par Sylvain
le 30/10/2026 : une boutique sans avis clients ne peut pas être nettement plus chère que Cadeau Plus,
le principal concurrent.

| Produit | Cadeau Plus, prix affiché | Prix barré | Fréquence |
|---|---|---|---|
| Mug | 18,45 € | 30,95 € | 168 mugs sur 250 lus |
| Boule de Noël en verre | 19,95 € | 29,95 € | toute la collection (63) |
| Ornement en bois | 12,95 € | 22,95 € | 216 sur 250 |

Source : cadeauplus.com, mesuré le 30/10 ([[RCH - Audit des prix Cadeau Plus et coûts Printify (30-10-2026)]]).
Livraison 4,95 €, offerte dès 70 € ; prix barrés permanents ; leur boule à 13,95 € est en acrylique
ou en céramique. Livraison offerte chez les autres : CadoMaestro dès 59 €, Koala Bleu dès 39 €.

### Ce que Printify affiche, et les erreurs corrigées le 31/10
- Le prix « From » du catalogue est le coût de fabrication (aide Printify).
- Le « From » sous « Shipping » est le port le moins cher **tous pays confondus**, souvent
  l'Allemagne, pas la France. Le port du bois retenu le 30/10 (4,95 €) était le tarif Allemagne.
- « Shipping • 3 » compte les modes d'expédition (standard, express, economy), pas les articles :
  les 11,82 € paient le port d'une seule boule.
- Les 7,91 $ (boule) et 10,68 $ (bois) notés dans la TODO valent le coût × 1,25 ; ce ne sont pas des
  coûts de fabrication.
- Cotisations : 12,4 % (12,3 % + 0,1 % de formation professionnelle), pas 12,3 %.

### Nos coûts réels chez Printify, destination France
Mesuré le 31/10 dans le catalogue public et son API ([[RCH - Audit des coûts réels Printify des trois produits (31-10-2026)]]).

| | Mug | Boule en verre | Décoration en bois |
|---|---|---|---|
| Produit Printify | Standard Mug, 11oz (1016) | Glass Ornament, Single (2769), Circle | Wooden Ornaments (697), 6 formes |
| Imprimeur | Textildruck Europa (Allemagne) | Chill (États-Unis, Pays-Bas) | WOYC (Italie, et 4 autres sites) |
| Fabrication std / Premium | 5,91 / 4,42 $ = 5,14 / 3,85 € | 6,33 / 4,67 $ = 5,51 / 4,06 € | 8,54 / 6,19 $ = 7,43 / 5,39 € |
| Port France, 1er article | 6,89 $ = 5,99 € | 13,59 $ = 11,82 € | 6,19 $ = 5,39 € |
| Port France, article suivant | 1,99 $ = 1,73 € | 1,99 $ = 1,73 € | 1,49 $ = 1,30 € |
| Délai de livraison annoncé | 5 à 10 jours ouvrés | 10 à 30 jours ouvrés | 5 à 10 jours ouvrés |
| Emballage | carton à cloisons | sachet plastique | sachet recyclable |
| **Coût d'un article livré, TVA comprise** | **13,36 €** | **20,80 €** | **15,38 €** |
| Article suivant dans le même colis | + 8,24 € | + 8,68 € | + 10,48 € |

Calcul : (fabrication + port) × 1,2. Exemple du mug : (5,14 + 5,99) × 1,2 = 13,36 €.
Un imprimeur = un colis : deux produits différents paient chacun un port « 1er article ».

### Ce que paie la cliente pour la livraison, et ce qu'elle nous coûte
| Commande | Livraison payée par la cliente | Port payé à Printify, TVA comprise |
|---|---|---|
| 1 mug | 4,90 € | 7,19 € |
| 1 boule | 4,90 € | 14,18 € |
| 1 bois | 4,90 € | 6,47 € |
| 3 articles de 3 produits différents | 4,90 € | 27,84 € (trois colis) |
| 60 € de marchandises ou plus | 0 € | inchangé |

### Hypothèses de calcul
| Poste | Valeur | Provenance |
|---|---|---|
| Conversion Printify | 0,87 € pour 1 $ si Printify facture en euros | mesuré le 31/10 sur le catalogue ⚠️ à vérifier sur la première facture |
| Taux BCE | 1 € = 1,1130 $ (29/10/2026) | source : BCE |
| TVA Printify | 20 % sur fabrication et port, non récupérable en franchise | source : aide Printify ; expert-comptable ⚠️ |
| Frais Shopify Payments | 1,5 % + 0,25 € (carte standard) ; 2,7 % + 0,25 € (Amex, hors UE) ; PayPal dès 2,9 % + 0,35 € | mesuré le 31/10 sur shopify.com/fr |
| Cotisations | 12,4 % de tout l'encaissé, livraison comprise (13,4 % avec le versement libératoire) | source : Bpifrance Création, 2026 |
| Abonnements (hors marges) | Shopify Basic 36 €/mois (32 € à l'année) ; Printify Premium 34,99 €/mois ou 299 €/an, facultatif | mesuré le 31/10 |
| Personnalisation Printify | gratuite | source : printify.com/personalization |

## Décision
**Prix au niveau de Cadeau Plus, trois façons de vendre chaque produit, livraison payante, aucun
faux prix barré.**

### Les façons de vendre et les prix
| Façon de vendre | Ce que choisit la cliente | Mug | Boule | Bois | Rétractation 14 jours |
|---|---|---|---|---|---|
| **Notre illustration, sans texte** | une des ≈ 10 illustrations | **18,45 €** | **19,95 €** | **17,95 €** | oui (produit de catalogue) |
| **Notre illustration + texte** | l'illustration et son texte (prénoms, phrase, date) | **19,45 €** | **20,95 €** | **18,95 €** | non (bien personnalisé) |
| **Page blanche** | sa propre image et son texte, sur l'objet vierge | **20,45 €** | **21,95 €** | **19,95 €** | non (bien personnalisé) |

Bois : la forme (chaussette, sapin, étoile, cloche, ovale, cœur) est au choix, sans supplément.
Livraison : 4,90 € par commande, quel que soit le nombre de colis ; offerte dès 60 € de marchandises.

### Simulation complète par variante (Printify facturé en euros, carte standard)

| Produit | Façon de vendre | Qté | Marchandises | Livraison cliente | La cliente paie | Fabrication HT | Port HT | TVA Printify | Coût Printify TTC | Frais Shopify | Cotisations 12,4 % | **Marge avant pub** | Marge par article |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Mug | illustration sans texte | 1 | 18,45 € | 4,90 € | 23,35 € | 5,14 € | 5,99 € | 2,23 € | 13,36 € | 0,60 € | 2,90 € | **6,49 €** | 6,49 € |
| Mug | illustration sans texte | 2 | 36,90 € | 4,90 € | 41,80 € | 10,28 € | 7,72 € | 3,60 € | 21,60 € | 0,88 € | 5,18 € | **14,14 €** | 7,07 € |
| Mug | illustration sans texte | 3 | 55,35 € | 4,90 € | 60,25 € | 15,42 € | 9,45 € | 4,97 € | 29,84 € | 1,15 € | 7,47 € | **21,79 €** | 7,26 € |
| Mug | illustration + texte | 1 | 19,45 € | 4,90 € | 24,35 € | 5,14 € | 5,99 € | 2,23 € | 13,36 € | 0,62 € | 3,02 € | **7,35 €** | 7,35 € |
| Mug | illustration + texte | 2 | 38,90 € | 4,90 € | 43,80 € | 10,28 € | 7,72 € | 3,60 € | 21,60 € | 0,91 € | 5,43 € | **15,86 €** | 7,93 € |
| Mug | illustration + texte | 3 | 58,35 € | 4,90 € | 63,25 € | 15,42 € | 9,45 € | 4,97 € | 29,84 € | 1,20 € | 7,84 € | **24,37 €** | 8,12 € |
| Mug | page blanche | 1 | 20,45 € | 4,90 € | 25,35 € | 5,14 € | 5,99 € | 2,23 € | 13,36 € | 0,63 € | 3,14 € | **8,22 €** | 8,22 € |
| Mug | page blanche | 2 | 40,90 € | 4,90 € | 45,80 € | 10,28 € | 7,72 € | 3,60 € | 21,60 € | 0,94 € | 5,68 € | **17,58 €** | 8,79 € |
| Mug | page blanche | 3 | 61,35 € | 0,00 € | 61,35 € | 15,42 € | 9,45 € | 4,97 € | 29,84 € | 1,17 € | 7,61 € | **22,73 €** | 7,58 € |
| Boule | illustration sans texte | 1 | 19,95 € | 4,90 € | 24,85 € | 5,51 € | 11,82 € | 3,47 € | 20,80 € | 0,62 € | 3,08 € | **0,35 €** | 0,35 € |
| Boule | illustration sans texte | 2 | 39,90 € | 4,90 € | 44,80 € | 11,02 € | 13,55 € | 4,91 € | 29,48 € | 0,92 € | 5,56 € | **8,84 €** | 4,42 € |
| Boule | illustration sans texte | 3 | 59,85 € | 4,90 € | 64,75 € | 16,53 € | 15,28 € | 6,36 € | 38,17 € | 1,22 € | 8,03 € | **17,33 €** | 5,78 € |
| Boule | illustration + texte | 1 | 20,95 € | 4,90 € | 25,85 € | 5,51 € | 11,82 € | 3,47 € | 20,80 € | 0,64 € | 3,21 € | **1,20 €** | 1,20 € |
| Boule | illustration + texte | 2 | 41,90 € | 4,90 € | 46,80 € | 11,02 € | 13,55 € | 4,91 € | 29,48 € | 0,95 € | 5,80 € | **10,57 €** | 5,29 € |
| Boule | illustration + texte | 3 | 62,85 € | 0,00 € | 62,85 € | 16,53 € | 15,28 € | 6,36 € | 38,17 € | 1,19 € | 7,79 € | **15,70 €** | 5,23 € |
| Boule | page blanche | 1 | 21,95 € | 4,90 € | 26,85 € | 5,51 € | 11,82 € | 3,47 € | 20,80 € | 0,65 € | 3,33 € | **2,07 €** | 2,07 € |
| Boule | page blanche | 2 | 43,90 € | 4,90 € | 48,80 € | 11,02 € | 13,55 € | 4,91 € | 29,48 € | 0,98 € | 6,05 € | **12,29 €** | 6,15 € |
| Boule | page blanche | 3 | 65,85 € | 0,00 € | 65,85 € | 16,53 € | 15,28 € | 6,36 € | 38,17 € | 1,24 € | 8,17 € | **18,27 €** | 6,09 € |
| Bois | illustration sans texte | 1 | 17,95 € | 4,90 € | 22,85 € | 7,43 € | 5,39 € | 2,56 € | 15,38 € | 0,59 € | 2,83 € | **4,05 €** | 4,05 € |
| Bois | illustration sans texte | 2 | 35,90 € | 4,90 € | 40,80 € | 14,86 € | 6,69 € | 4,31 € | 25,86 € | 0,86 € | 5,06 € | **9,02 €** | 4,51 € |
| Bois | illustration sans texte | 3 | 53,85 € | 4,90 € | 58,75 € | 22,29 € | 7,99 € | 6,06 € | 36,34 € | 1,13 € | 7,29 € | **13,99 €** | 4,66 € |
| Bois | illustration + texte | 1 | 18,95 € | 4,90 € | 23,85 € | 7,43 € | 5,39 € | 2,56 € | 15,38 € | 0,61 € | 2,96 € | **4,90 €** | 4,90 € |
| Bois | illustration + texte | 2 | 37,90 € | 4,90 € | 42,80 € | 14,86 € | 6,69 € | 4,31 € | 25,86 € | 0,89 € | 5,31 € | **10,74 €** | 5,37 € |
| Bois | illustration + texte | 3 | 56,85 € | 4,90 € | 61,75 € | 22,29 € | 7,99 € | 6,06 € | 36,34 € | 1,18 € | 7,66 € | **16,57 €** | 5,52 € |
| Bois | page blanche | 1 | 19,95 € | 4,90 € | 24,85 € | 7,43 € | 5,39 € | 2,56 € | 15,38 € | 0,62 € | 3,08 € | **5,77 €** | 5,77 € |
| Bois | page blanche | 2 | 39,90 € | 4,90 € | 44,80 € | 14,86 € | 6,69 € | 4,31 € | 25,86 € | 0,92 € | 5,56 € | **12,46 €** | 6,23 € |
| Bois | page blanche | 3 | 59,85 € | 4,90 € | 64,75 € | 22,29 € | 7,99 € | 6,06 € | 36,34 € | 1,22 € | 8,03 € | **19,16 €** | 6,39 € |

### Paniers mélangés (un colis par imprimeur)

| Panier | Colis | Façon de vendre | Marchandises | La cliente paie | Coût Printify TTC | Frais | Cotisations | **Marge avant pub** |
|---|---|---|---|---|---|---|---|---|
| Mug + boule | 2 | illustration sans texte | 38,40 € | 43,30 € | 34,16 € | 0,90 € | 5,37 € | **2,87 €** |
| Mug + boule | 2 | illustration + texte | 40,40 € | 45,30 € | 34,16 € | 0,93 € | 5,62 € | **4,59 €** |
| Mug + boule | 2 | page blanche | 42,40 € | 47,30 € | 34,16 € | 0,96 € | 5,87 € | **6,31 €** |
| Mug + bois | 2 | illustration sans texte | 36,40 € | 41,30 € | 28,74 € | 0,87 € | 5,12 € | **6,57 €** |
| Mug + bois | 2 | illustration + texte | 38,40 € | 43,30 € | 28,74 € | 0,90 € | 5,37 € | **8,29 €** |
| Mug + bois | 2 | page blanche | 40,40 € | 45,30 € | 28,74 € | 0,93 € | 5,62 € | **10,01 €** |
| Boule + bois | 2 | illustration sans texte | 37,90 € | 42,80 € | 36,18 € | 0,89 € | 5,31 € | **0,42 €** |
| Boule + bois | 2 | illustration + texte | 39,90 € | 44,80 € | 36,18 € | 0,92 € | 5,56 € | **2,14 €** |
| Boule + bois | 2 | page blanche | 41,90 € | 46,80 € | 36,18 € | 0,95 € | 5,80 € | **3,87 €** |
| Mug + boule + bois | 3 | illustration sans texte | 56,35 € | 61,25 € | 49,54 € | 1,17 € | 7,60 € | **2,94 €** |
| Mug + boule + bois | 3 | illustration + texte | 59,35 € | 64,25 € | 49,54 € | 1,21 € | 7,97 € | **5,53 €** |
| Mug + boule + bois | 3 | page blanche | 62,35 € | 62,35 € | 49,54 € | 1,19 € | 7,73 € | **3,89 €** |
| 2 mugs + bois | 2 | illustration sans texte | 54,85 € | 59,75 € | 36,98 € | 1,15 € | 7,41 € | **14,21 €** |
| 2 mugs + bois | 2 | illustration + texte | 57,85 € | 62,75 € | 36,98 € | 1,19 € | 7,78 € | **16,80 €** |
| 2 mugs + bois | 2 | page blanche | 60,85 € | 60,85 € | 36,98 € | 1,16 € | 7,55 € | **15,16 €** |
| 2 mugs + boule | 2 | illustration sans texte | 56,85 € | 61,75 € | 42,40 € | 1,18 € | 7,66 € | **10,51 €** |
| 2 mugs + boule | 2 | illustration + texte | 59,85 € | 64,75 € | 42,40 € | 1,22 € | 8,03 € | **13,10 €** |
| 2 mugs + boule | 2 | page blanche | 62,85 € | 62,85 € | 42,40 € | 1,19 € | 7,79 € | **11,47 €** |
| 2 boules + bois | 2 | illustration sans texte | 57,85 € | 62,75 € | 44,86 € | 1,19 € | 7,78 € | **8,92 €** |
| 2 boules + bois | 2 | illustration + texte | 60,85 € | 60,85 € | 44,86 € | 1,16 € | 7,55 € | **7,28 €** |
| 2 boules + bois | 2 | page blanche | 63,85 € | 63,85 € | 44,86 € | 1,21 € | 7,92 € | **9,86 €** |

### Sensibilité, un article (marge avant pub)

| Produit | Façon de vendre | Référence | Printify Premium (hors abonnement) | Printify en dollars (BCE) | Dollars + 2 % banque | Carte Amex ou hors UE |
|---|---|---|---|---|---|---|
| Mug | illustration sans texte | 6,49 € | 8,04 € | 6,05 € | 5,77 € | 6,21 € |
| Mug | illustration + texte | 7,35 € | 8,90 € | 6,91 € | 6,63 € | 7,06 € |
| Mug | page blanche | 8,22 € | 9,77 € | 7,78 € | 7,50 € | 7,92 € |
| Boule | illustration sans texte | 0,35 € | 2,09 € | -0,33 € | -0,75 € | 0,05 € |
| Boule | illustration + texte | 1,20 € | 2,94 € | 0,52 € | 0,10 € | 0,89 € |
| Boule | page blanche | 2,07 € | 3,81 € | 1,39 € | 0,97 € | 1,75 € |
| Bois | illustration sans texte | 4,05 € | 6,49 € | 3,55 € | 3,23 € | 3,77 € |
| Bois | illustration + texte | 4,90 € | 7,34 € | 4,40 € | 4,08 € | 4,62 € |
| Bois | page blanche | 5,77 € | 8,21 € | 5,27 € | 4,95 € | 5,47 € |

Toutes les marges sont estimées, avant publicité ; la marge est aussi le coût publicitaire maximum
par commande pour finir à zéro. Règle : chaque texte à 1 € ajoute 0,86 € de marge, chaque page
blanche 1,72 €. Prix affiché minimum pour qu'un article seul laisse 0 € puis 5 € : mug 10,91 € puis
16,71 € ; boule 19,55 € puis 25,35 € ; bois 13,25 € puis 19,06 € (estimé).

Premium : gain de 1,55 € par mug, 1,74 € par boule et 2,44 € par bois ; rentable à partir d'environ
23 mugs, 20 boules ou 15 bois par mois au mensuel, 16, 14 ou 10 à l'année (estimé).

### Règles communes
- **Pas de prix barré inventé.** Article L112-1-1 du Code de la consommation : le prix de référence
  d'une réduction est le prix le plus bas pratiqué dans les 30 jours précédents. À faire relire par un
  juriste. Des promotions réelles restent possibles une fois les prix pratiqués 30 jours.
- **Printify facturé en euros** (Wallet → Payment details) : en dollars, la boule seule perd de
  l'argent (−0,33 €).
- **Offres** (lots, remises) : aucune décidée.
- **Argument** : même prix que les leaders, aperçu en direct, fabrication en Europe, boule en vrai
  verre cristal, « prix justes, sans faux prix barrés ».

## Alternatives écartées
- **Prix de lancement (24,90 / 27,90 / 19,90 €)** : 6 à 8 € plus chers que Cadeau Plus, sans avis clients.
- **Prix du 30/10 (17,90 / 19,90 / 17,90 €)** : remplacés le 31/10 par les prix de Cadeau Plus pour le
  mug et la boule.
- **Page blanche au prix des designs (version du 30/10)** : remplacée par un supplément de 2 €.
- **Copier les prix barrés** : risque de pratique commerciale trompeuse.
- **Boule en verre à 13,95 €** : perte de 4,82 € par boule seule, avant pub (estimé).
- **Bois à 12,95 € comme Cadeau Plus** : perte de 0,26 € par bois seul, avant pub (estimé).
- **Livraison offerte dès 49 €** : la marge d'un panier à 50 € disparaît presque entièrement.

## Conséquences
- Les décisions 01, 02 et 11 ne portent plus de prix : elles renvoient ici.
- **La boule seule ne paie pas la publicité** (0,35 à 2,07 €) : elle se vend par deux ou plus
  (8,84 € pour deux, 17,33 € pour trois) ou en complément.
- **Passer 60 € de peu coûte 4,90 €** : 3 boules avec texte laissent 15,70 €, contre 17,33 € sans texte.
- Un article seul ne couvre pas un CPA de 20 € (décision 02) : les offres restent à décider.
- Fiche produit et panier : afficher « sans texte : rétractation 14 jours » et « avec texte ou page
  blanche : pas de rétractation » ([[11 - Texte facultatif à 1 €, frais de retour à la charge du client, retours chez Sylvain]]).
- Shopify : 3 produits, option « Façon de vendre » (+ 0 / 1 / 2 €) et, pour le bois, « Forme » ;
  livraison 4,90 €, offerte dès 60 €.
- Boule : délai annoncé de 10 à 30 jours ouvrés ; pour livrer avant le 24/12 dans le pire cas, il
  faudrait la commander avant le 10/11 (estimé).
- À vérifier (registre A VERIFIER) : taux de la facturation Printify en euros ; port réel de deux
  mugs dans un colis ; délai et casse de la boule en sachet ; TVA en franchise (expert-comptable).
- Validation d'Antoine attendue avant de passer en `validé`.

## Concerne
[[02 - Lancement avec le mug, la boule en cristal et la décoration en bois, trois imprimeurs UE]] · [[01 - Audience visée et nouvelle offre, parents et grands-parents d'abord, nos designs ou la page blanche]] · [[11 - Texte facultatif à 1 €, frais de retour à la charge du client, retours chez Sylvain]] · [[SYN - Modèle économique]] · [[SYN - Juridique]]
