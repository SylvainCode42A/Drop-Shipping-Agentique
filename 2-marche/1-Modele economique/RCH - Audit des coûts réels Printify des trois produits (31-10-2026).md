---
type: research
title: RCH - Audit des coûts réels Printify des trois produits (31-10-2026)
status: draft
date: 2026-10-31
sources:
  - "Catalogue Printify public, région Europe, devise EUR, lu sans connexion le 31/10/2026 : https://printify.com/app/products/1016/generic-brand/standard-mug-11oz · https://printify.com/app/products/2769/generic-brand/glass-ornament-single · https://printify.com/app/products/697/generic-brand/wooden-ornaments"
  - "API interne du catalogue Printify (product-catalog-service), lue par le navigateur le 31/10/2026 : /api/v2/blueprints/{1016,2769,697}/print-providers ; …/print-providers/{26,86,23}/shipping, /variants, /production"
  - "Code du catalogue Printify (main-EDVRH66W.js), libellé « Shipping • N » (shippingLabelWithCount$), lu le 31/10/2026"
  - "Printify, tarifs d'expédition publics : https://printify.com/shipping-rates/textildruck-europa/ · https://printify.com/shipping-rates/woyc/"
  - "Printify, aide, plusieurs articles : https://help.printify.com/hc/en-us/articles/4483643971473-How-are-shipping-costs-calculated-for-multiple-items"
  - "Printify, aide, devises : https://help.printify.com/hc/en-us/articles/17227301407121 · https://help.printify.com/hc/en-us/articles/12203640151953 · https://help.printify.com/hc/en-us/articles/12203416543505"
  - "Printify, aide, TVA : https://help.printify.com/hc/en-us/articles/4483628906513 · https://help.printify.com/hc/en-us/articles/4483600546705-Can-I-claim-a-VAT-exemption-on-orders-from-Printify"
  - "Printify, aide, prix du catalogue = prix de production : https://help.printify.com/hc/en-us/articles/4483609656721"
  - "Printify, aide, Premium en février 2026 : https://help.printify.com/hc/en-us/articles/42641734110225"
  - "Printify, personnalisation : https://printify.com/personalization/"
  - "Shopify France, tarifs lus le 31/10/2026 : https://www.shopify.com/fr/tarifs"
  - "Kanal, prix de Shopify en 2026 (29/09/2026) : https://getkanal.com/fr/blog/prix-shopify"
  - "BCE, taux de référence EUR/USD : https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/eurofxref-graph-usd.fr.html"
  - "Bpifrance Création, cotisations du micro-entrepreneur 2026 : https://bpifrance-creation.fr/boiteaoutils/travailleurs-independants-cotisations-a-verser-debut-dactivite-regime-normal"
  - "[[RCH - Audit des prix Cadeau Plus et coûts Printify (30-10-2026)]]"
  - "[[RCH - Relevé connecté du catalogue Printify UE (29-10-2026)]]"
  - "[[RCH - Décoration de sapin personnalisée grands-parents (29-10-2026)]]"
related: ["[[SYN - Modèle économique]]", "[[SYN - Fournisseurs]]", "[[TODO - Relever le port Printify de la boule, du bois et du mug]]", "[[RCH - Audit des prix Cadeau Plus et coûts Printify (30-10-2026)]]", "[[RCH - Relevé connecté du catalogue Printify UE (29-10-2026)]]", "[[A VERIFIER - Points à valider, vérifier, tester]]"]
decisions: ["[[02 - Lancement avec le mug, la boule en cristal et la décoration en bois, trois imprimeurs UE]]", "[[09 - Établissement des nouveaux prix, alignés sur Cadeau Plus sans faux prix barrés]]"]
last-verified: 2026-10-31
tags: [dropshipping, modele-economique, fournisseurs, prix, printify, research]
---
# RCH - Audit des coûts réels Printify des trois produits (31-10-2026)

## Contexte posé
Demande de Sylvain, 31/10/2026 : auditer ce que la boutique paiera réellement pour le mug, la boule
en verre et la décoration en bois, refaire de vrais calculs et regarder sur Printify, car les prix du
vault semblent faux depuis le début. Question ouverte par
[[TODO - Relever le port Printify de la boule, du bois et du mug]] : « Shipping • 3 — From EUR 11.82 »
vaut-il pour une boule ou pour trois ?

Méthode : catalogue Printify public (région Europe, devise EUR) et son API interne
product-catalog-service, lus sans connexion le 31/10 ; code du catalogue pour le libellé
« Shipping • N » ; aide Printify ; tarifs Shopify France ; taux BCE. Calculs refaits par script,
vérifiés par un second script indépendant, arrondis au centime ligne par ligne.

## Conclusion en une phrase
Livrés en France, TVA de 20 % comprise et facturés en euros, le mug coûte 13,36 €, la boule 20,80 € et
le bois 15,38 € ; les 11,82 € de la boule paient le port d'une seule boule (« • 3 » compte les modes
d'expédition), les 7,91 $ et 10,68 $ de la TODO ne sont pas des coûts, et aux prix retenus il reste
avant publicité 6,49 € sur un mug, 0,35 € sur une boule et 4,05 € sur un bois.

## Résultats

### 1. Ce que Printify affiche, et ce que ça veut dire
- **« Shipping • 3 »** : le chiffre compte les modes d'expédition prévus (`standard`, `express`,
  `economy`), même vides. Code du catalogue : `Object.keys(min_shipping_prices).length`. Les trois
  produits ont `{standard: …, express: null, economy: null}`, d'où « 3 ». Ce n'est pas un nombre
  d'articles (mesuré le 31/10).
- **« From EUR … » sous Shipping** : le port du 1er article le moins cher **tous pays confondus**,
  pas celui de la France. Mug : 4,78 € = tarif Allemagne (5,49 $). Bois : 4,95 € = tarif Allemagne
  (5,69 $). Boule : 11,82 € = tarif commun à toute l'Europe (13,59 $) (mesuré le 31/10).
- **« Price From EUR … »** : le coût de fabrication. Aide Printify : « The prices displayed in the
  Printify Catalog represent the production prices ».
- **Conversion** : les euros du catalogue sont les dollars × 0,87, sur les onze montants relevés
  (taux compatible : 0,86995 à 0,87013). BCE du 29/10/2026 : 1 € = 1,1130 $, soit 0,8985 € pour 1 $.

### 2. Relevé Printify, destination France (mesuré le 31/10)
| | Mug | Boule en verre | Décoration en bois |
|---|---|---|---|
| Produit Printify (blueprint) | Standard Mug, 11oz (1016) | Glass Ornament, Single (2769), Circle | Wooden Ornaments (697), 6 formes |
| Imprimeur (id) | Textildruck Europa (26) | Chill (86) | WOYC (23) |
| Sites déclarés | Allemagne (Halle) | États-Unis, Pays-Bas | Italie, États-Unis, Corée du Sud, Australie, Royaume-Uni |
| Fabrication std / Premium | 5,91 / 4,42 $ | 6,33 / 4,67 $ | 8,54 / 6,19 $, même prix pour les 6 formes |
| Idem affiché en euros | 5,14 / 3,85 € | 5,51 / 4,06 € | 7,43 / 5,39 € |
| Port France, 1er article | 6,89 $ (5,99 €) | 13,59 $ (11,82 €) | 6,19 $ (5,39 €) |
| Port France, article suivant | 1,99 $ (1,73 €) | 1,99 $ (1,73 €) | 1,49 $ (1,30 €) |
| Délai de livraison promis | 5 à 10 jours ouvrés | **10 à 30 jours ouvrés** | 5 à 10 jours ouvrés |
| Fabrication moyenne | 1,6 jour | 1,6 jour | 1,5 jour |
| Zone d'impression | tour du mug | face avant, UV | une seule zone (« All over print ») |
| Emballage (fiche imprimeur) | carton à cloisons ; plusieurs mugs regroupés dans un carton | « white poly mailer » (sachet plastique) | sachet recyclable |

Source : API product-catalog-service (print-providers, shipping, variants, production). Les ports
France en euros sont convertis à 0,87 (estimé) : Printify n'affiche en euros que le « From ».
Les ports France du mug et du bois sont les mêmes sur les pages publiques shipping-rates
(« European Countries »).

### 3. Coût réel d'un article livré en France
Calcul : (fabrication + port) × 1,2. Printify facture la TVA du pays de destination, port compris
(aide Printify) ; non récupérable en franchise.

Printify facturé en euros (taux du catalogue, 0,87) :

| | Fabrication | Port 1er | HT | TVA 20 % | **TTC** | Article suivant dans le même colis |
|---|---|---|---|---|---|---|
| Mug | 5,14 € | 5,99 € | 11,13 € | 2,23 € | **13,36 €** | + 8,24 € |
| Boule | 5,51 € | 11,82 € | 17,33 € | 3,47 € | **20,80 €** | + 8,68 € |
| Bois | 7,43 € | 5,39 € | 12,82 € | 2,56 € | **15,38 €** | + 10,48 € |

Détail du mug : 5,14 + 5,99 = 11,13 ; 11,13 × 0,20 = 2,226 → 2,23 ; 11,13 + 2,23 = 13,36.
2e mug : colis de deux mugs 21,60 € − colis d'un mug 13,36 € = 8,24 €.

Printify facturé en dollars :

| | TTC au taux BCE (0,8985) | TTC avec 2 % de frais bancaires (estimé) |
|---|---|---|
| Mug | 13,80 € | 14,08 € |
| Boule | 21,48 € | 21,90 € |
| Bois | 15,88 € | 16,20 € |

### 4. Boule : une boule ou trois ?
| Boules dans la commande | Port HT | Port par boule | Coût TTC du colis | Coût TTC par boule |
|---|---|---|---|---|
| 1 | 11,82 € | 11,82 € | 20,80 € | 20,80 € |
| 2 | 13,55 € | 6,78 € | 29,48 € | 14,74 € |
| 3 | 15,28 € | 5,09 € | 38,17 € | 12,72 € |

La lecture « 11,82 € pour 3 boules, soit 3,94 € par boule » ne tient pas : trois boules paient
15,28 € de port, soit 5,09 € chacune. Règle Printify : le tarif « article suivant » vaut pour des
articles du même type chez le même imprimeur ; deux imprimeurs font deux colis, chacun au tarif
« 1er article ». L'aide ajoute que les mugs peuvent ne pas en bénéficier chez certains imprimeurs ;
la table de Textildruck Europa donne pourtant 1,99 $ ⚠️ à vérifier sur une commande de deux mugs.

### 5. Marge d'une commande à un article, avant publicité
Hypothèses : prix retenus le 31/10 (mug 18,45 €, boule 19,95 €, bois 17,95 €, TODO) ; livraison
4,90 € payée par la cliente, offerte dès 60 € (décision 09) ; Shopify Payments 1,5 % + 0,25 €
(carte standard, forfait Basic) ; cotisations 12,4 % de tout l'encaissé ; Printify facturé en euros.

| Commande | La cliente paie | Printify TTC | Frais Shopify | Cotisations | **Marge avant pub** |
|---|---|---|---|---|---|
| Mug, sans texte | 23,35 € | 13,36 € | 0,60 € | 2,90 € | **6,49 €** |
| Mug + texte (1 €) | 24,35 € | 13,36 € | 0,62 € | 3,02 € | **7,35 €** |
| Mug, page blanche (2 €) | 25,35 € | 13,36 € | 0,63 € | 3,14 € | **8,22 €** |
| Boule, sans texte | 24,85 € | 20,80 € | 0,62 € | 3,08 € | **0,35 €** |
| Boule + texte | 25,85 € | 20,80 € | 0,64 € | 3,21 € | **1,20 €** |
| Boule, page blanche | 26,85 € | 20,80 € | 0,65 € | 3,33 € | **2,07 €** |
| Bois, sans texte | 22,85 € | 15,38 € | 0,59 € | 2,83 € | **4,05 €** |
| Bois + texte | 23,85 € | 15,38 € | 0,61 € | 2,96 € | **4,90 €** |
| Bois, page blanche | 24,85 € | 15,38 € | 0,62 € | 3,08 € | **5,77 €** |

Détail du mug sans texte : 18,45 + 4,90 = 23,35 ; frais 23,35 × 1,5 % + 0,25 = 0,60 ;
cotisations 23,35 × 12,4 % = 2,90 ; marge 23,35 − 13,36 − 0,60 − 2,90 = 6,49.
La marge avant pub est aussi le coût publicitaire maximum par commande pour finir à zéro.

Prix de vente seul, sans texte, à partir duquel la commande laisse 0 € puis 5 € avant pub
(estimé) : mug 10,91 € puis 16,71 € ; boule 19,55 € puis 25,35 € ; bois 13,25 € puis 19,06 €.

### 6. Paniers, sans texte, Printify facturé en euros
| Panier | Colis | Marchandises | Livraison cliente | Payé | Printify TTC | Frais | Cotisations | Marge avant pub |
|---|---|---|---|---|---|---|---|---|
| 2 mugs | 1 | 36,90 € | 4,90 € | 41,80 € | 21,60 € | 0,88 € | 5,18 € | 14,14 € |
| 3 mugs | 1 | 55,35 € | 4,90 € | 60,25 € | 29,84 € | 1,15 € | 7,47 € | 21,79 € |
| 2 boules | 1 | 39,90 € | 4,90 € | 44,80 € | 29,48 € | 0,92 € | 5,56 € | 8,84 € |
| 3 boules | 1 | 59,85 € | 4,90 € | 64,75 € | 38,17 € | 1,22 € | 8,03 € | 17,33 € |
| 2 bois | 1 | 35,90 € | 4,90 € | 40,80 € | 25,86 € | 0,86 € | 5,06 € | 9,02 € |
| 3 bois | 1 | 53,85 € | 4,90 € | 58,75 € | 36,34 € | 1,13 € | 7,29 € | 13,99 € |
| Mug + boule | 2 | 38,40 € | 4,90 € | 43,30 € | 34,16 € | 0,90 € | 5,37 € | 2,87 € |
| Mug + bois | 2 | 36,40 € | 4,90 € | 41,30 € | 28,74 € | 0,87 € | 5,12 € | 6,57 € |
| Boule + bois | 2 | 37,90 € | 4,90 € | 42,80 € | 36,18 € | 0,89 € | 5,31 € | 0,42 € |
| Mug + boule + bois | 3 | 56,35 € | 4,90 € | 61,25 € | 49,54 € | 1,17 € | 7,60 € | 2,94 € |
| 2 mugs + bois | 2 | 54,85 € | 4,90 € | 59,75 € | 36,98 € | 1,15 € | 7,41 € | 14,21 € |
| 2 mugs + boule | 2 | 56,85 € | 4,90 € | 61,75 € | 42,40 € | 1,18 € | 7,66 € | 10,51 € |

Lecture : un 2e article chez le même imprimeur coûte 8,24 à 10,48 € TTC ; chaque imprimeur de plus
ajoute un port « 1er article ». Aucun panier de trois articles sans texte n'atteint les 60 € de la
livraison offerte ; trois boules (59,85 €) le ratent de 0,15 €.

### 7. Devise, carte, abonnements
- **Devise de facturation Printify** : AUD, CAD, EUR, GBP ou USD, réglée dans Wallet → Payment
  details, indépendante de la devise d'affichage du catalogue. Printify conseille la devise de la
  carte « to avoid conversion fees ». Hors USD : plus de solde USD ni de coupons, et l'approbation
  automatique débite commande par commande (aide Printify). Le taux appliqué à une facturation en
  euros n'est pas publié ⚠️ à vérifier sur la première facture.
- **Marge d'une commande à un article selon la devise et la carte** :

| | Facturé en EUR (0,87) | Facturé en USD (BCE) | USD + 2 % de banque (estimé) | EUR, carte Amex ou hors UE (2,7 %) |
|---|---|---|---|---|
| Mug | 6,49 € | 6,05 € | 5,77 € | 6,21 € |
| Boule | 0,35 € | −0,33 € | −0,75 € | 0,05 € |
| Bois | 4,05 € | 3,55 € | 3,23 € | 3,77 € |

- **Printify Premium** : 34,99 €/mois depuis le 17/02/2026 (29 € avant), ou 299 €/an ; jusqu'à
  20 % de remise. Gain TTC par article : mug 1,55 €, boule 1,74 €, bois 2,44 €. Seuil : environ
  23 mugs, 20 boules ou 15 bois par mois au mensuel ; 16, 14 ou 10 par mois à l'annuel (estimé,
  TVA éventuelle sur l'abonnement non comptée ⚠️).
- **Shopify Basic** : 36 €/mois, ou 32 €/mois en paiement annuel ; offre du 31/10 : 3 jours d'essai
  puis 1 €/mois pendant 3 mois. TVA sur l'abonnement non affichée ⚠️. À 6,49 € par mug, environ
  6 mugs par mois paient l'abonnement mensuel, avant publicité (36 ÷ 6,49 = 5,5).
- **Autres paiements Shopify France** : Amex et cartes internationales 2,7 % + 0,25 € ; PayPal à
  partir de 2,9 % + 0,35 € ; Klarna 4,99 % + 0,35 €.
- **Personnalisation Printify** : gratuite (« costs nothing for you or your customers, with no hidden
  fees »), et une seule zone d'impression par produit : aucun surcoût d'option.

### 8. Ce qui était faux dans le vault
| Chiffre du vault | Où | Valeur du 31/10 | Effet |
|---|---|---|---|
| Port du bois 4,95 € | RCH du 30/10, décisions 02 et 09, SYN | 5,39 € : 4,95 € est le tarif Allemagne (5,69 $), la France est à 6,19 $ | + 0,53 € TTC par bois ((5,39 − 4,95) × 1,2) ; 15,38 € au lieu de ≈ 14,90 € |
| Port du mug ≈ 6,20 € (estimé) | RCH du 30/10, décision 09, SYN | 5,99 € (6,89 $ × 0,87) ; 6,19 € au taux BCE | − 0,25 € TTC par mug ((5,99 − 6,20) × 1,2) ; 13,36 € au lieu de ≈ 13,60 € |
| « 11,82 € pour 3 boules » | TODO du 31/10 | 11,82 € pour la 1re boule, + 1,73 € par boule suivante | 3 boules : 5,09 € de port chacune, pas 3,94 € |
| Boule à 7,91 $ ≈ 7,08 € | TODO du 31/10 | 6,33 $ (5,51 €) | − 1,88 € TTC par boule ; la marge « ≈ −1,51 € » devient + 0,35 € |
| Bois à 10,68 $ | TODO du 31/10 | 8,54 $ (7,43 €) | aucun calcul ne l'utilisait encore |
| Cotisations 12,3 % | RCH du 28/10 et du 30/10, décision 09 | 12,4 % : 12,3 % + 0,1 % de CFP | ≈ − 0,02 € par commande |
| Taux 0,86 ; 0,87 ; 0,897 ; 0,90 ; 1 / 1,1167 | plusieurs notes | 0,87 si Printify facture en euros ; 0,8985 (BCE du 29/10) en dollars | 0,68 € TTC d'écart par boule entre les deux (20,80 / 21,48 €) |
| Premium à 39 $ par mois | RCH du 29/10 (décoration de sapin) | 34,99 €/mois en euros, ou 299 €/an | — |
| Marges de la décision 09 (17,90 / 19,90 / 17,90 €) | décision 09 | prix retenus le 31/10 : 18,45 / 19,95 / 17,95 € ; marges du § 5 | — |

7,91 ÷ 6,33 = 1,2496 et 10,68 ÷ 8,54 = 1,2506 : les deux montants de la TODO sont le coût du
catalogue × 1,25, au centime près. C'est la forme d'un prix de vente calculé avec 20 % de marge, pas
d'un coût de fabrication (estimé ; l'écran où ils ont été lus n'est pas connu ⚠️ à vérifier). Le
7,31 $ « annoncé plus tôt » ne correspond à aucun coût du blueprint 2769 (Chill 6,33 $ ; SwiftPOD
5,59 $, ou 7,73 $ avec emballage cadeau).

### 9. Délais et emballage de la boule
- Port France de Chill : 10 à 30 jours ouvrés, comme SwiftPOD, qui n'a qu'un site aux États-Unis.
  L'API situe Chill aux États-Unis, avec un second site aux Pays-Bas ; rien ne dit que la France
  est servie depuis les Pays-Bas ⚠️ (contradiction déjà notée le 29/10).
- Avec 2 jours de fabrication et 30 jours ouvrés de transport, le pire cas promis, une boule
  commandée le 15/11 arrive au plus tard vers le 29/12 ; pour tenir le 24/12, il faudrait la
  commander avant le 10/11 (estimé, jours fériés non comptés). Mug et bois commandés le 15/11 :
  livrés entre le 24/11 et le 01/12 ; dernière commande sûre vers le 08/12 (estimé).
- Emballage déclaré par Chill : « white poly mailer », un sachet, pour du verre. Printify ne
  remplace que les articles abîmés signalés sous 30 jours avec photo ([[SYN - Modèle économique]]).
- Fiche : « 100% Crystal glass », 76,2 × 76,2 mm, fond blanc, ruban rouge, « Blank product sourced
  from China ».

## Chiffres

### Sourcés
- Fabrication, ports France, délais, sites et emballages des trois produits : API
  product-catalog-service (mesuré le 31/10), tableau 2.
- Ports « European Countries » du mug (6,89 / 1,99 $) et du bois (6,19 / 1,49 $) : pages publiques
  shipping-rates de Textildruck Europa et de WOYC.
- Libellé « Shipping • N » : code du catalogue Printify (mesuré le 31/10).
- Euros du catalogue = dollars × 0,87 (mesuré le 31/10 sur onze montants affichés).
- BCE : 1 € = 1,1130 $ le 29/10/2026.
- TVA Printify : taux du pays de destination, port compris (aide Printify) ; 20 % en France.
- Shopify France : Basic 36 €/mois ou 32 €/mois à l'annuel ; carte standard 1,5 % + 0,25 € ; Amex et
  cartes internationales 2,7 % + 0,25 € ; PayPal dès 2,9 % + 0,35 € (mesuré le 31/10).
- Cotisations 2026, vente de marchandises : 12,3 % + 0,1 % de CFP ; 13,4 % avec le versement
  libératoire (source : Bpifrance Création).
- Printify Premium : 34,99 €/mois ou 299 €/an depuis le 17/02/2026 (aide Printify).

### Estimés
- Ports France en euros (convertis à 0,87).
- Frais bancaires de change de 2 %.
- Toutes les marges et tous les seuils des parties 5, 6 et 7.
- Dates de livraison de Noël (partie 9).

## Caveats
- Lecture sans connexion : le catalogue donne les coûts standard et Premium, pas une facture. La
  commande test de la décision 02 donnera le coût facturé. ⚠️
- Le taux appliqué par Printify à une facturation en euros n'est pas publié ; 0,87 est le taux
  d'affichage du catalogue ⚠️ à vérifier sur la première facture.
- TVA en franchise, avec ou sans numéro de TVA intracommunautaire : à faire confirmer par
  l'expert-comptable (registre A VERIFIER). Calcul fait avec 20 % non récupérables. ⚠️
- Tarif « article suivant » du mug : possible exception pour les mugs selon l'aide Printify. ⚠️
- Non comptés : publicité, retours, casse non couverte, nom de domaine, applis.
- Prix et ports relevés le 31/10 ; à relire avant de fixer les prix définitifs.

Contradictions, sans trancher :
- Prix du bois : 17,95 € dans la TODO du 31/10, 17,90 € dans la décision 02 (mise à jour du 31/10).
- Prix de la décision 11 (17,90 / 18,90 € ; 19,90 / 20,90 € pour la boule) contre ceux de la TODO
  (18,45 / 19,95 / 17,95 €).
- Chill : « Local Europe providers » dans le catalogue, mais délai de 10 à 30 jours ouvrés et
  localisation principale aux États-Unis dans l'API.
- WOYC : localisation principale aux États-Unis dans l'API, affiché en Europe (site IT), produit
  « Made in South Korea ».
- Shopify Basic à l'annuel : 32 €/mois sur shopify.com/fr le 31/10, 27 €/mois chez Kanal le 29/09.

## Retenu / écarté
Revue du 31/10/2026 : coûts, ports et marges repris dans
[[09 - Établissement des nouveaux prix, alignés sur Cadeau Plus sans faux prix barrés]], réécrite
le même jour avec la simulation de chaque façon de vendre ; bois à 17,95 €.
