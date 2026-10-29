---
type: research
title: Méthodes statistiques pour garder ou retirer un produit
status: validé
related: ["[[_conventions]]", "[[RCH - API Shopify pour la boutique agentique (22-10-2026)]]"]
decisions: []
date: 2026-10-25
sources:
  - https://www.littledata.io/benchmarks/add-to-cart-rate
  - https://www.triplewhale.com/blog/ecommerce-benchmarks
  - https://www.statsmodels.org/stable/generated/statsmodels.stats.proportion.proportion_confint.html
  - https://globalcalcs.com/en/math/wilson-score-interval/
  - https://tonyelhabr.rbind.io/posts/xg-ratio-empirical-bayes/
  - https://arxiv.org/pdf/1012.1161
  - https://www.pymc.io/projects/examples/en/latest/generalized_linear_models/GLM-hierarchical-binomial-model.html
  - https://web.stanford.edu/~bvr/pubs/TS_Tutorial.pdf
  - https://onlinelibrary.wiley.com/doi/abs/10.1002/asmb.2104
  - http://proceedings.mlr.press/v115/traca20a/traca20a.pdf
  - https://mlanthology.org/neurips/2008/chakrabarti2008neurips-mortal/
  - https://proceedings.mlr.press/v151/hong22c.html
  - https://arxiv.org/abs/2111.06929
  - https://mlanthology.org/jair/2020/trovo2020jair-slidingwindow/
  - https://arxiv.org/pdf/2409.05181
  - https://arxiv.org/abs/1707.09727
  - https://vwo.com/downloads/VWO_SmartStats_technical_whitepaper.pdf
  - https://donnuab.com/blog/en/expected-loss-in-bayesian-ab-testing/
  - https://www.evanmiller.org/how-not-to-run-an-ab-test.html
  - https://dl.acm.org/doi/10.1145/3097983.3097992
  - https://www.alexmolas.com/2025/10/30/bayesian-ab-test-peeking.html
  - http://varianceexplained.org/r/bayesian-ab-testing/
  - https://arxiv.org/abs/1812.09338
  - https://fidelity.github.io/mabwiser/
  - https://github.com/VowpalWabbit/vowpal_wabbit/wiki/Contextual-Bandit-algorithms
  - https://github.com/david-cortes/contextualbandits
last-verified: 2026-10-25
tags: [dropshipping, systeme, statistiques, analyste]
---
# RCH - Méthodes statistiques pour garder ou retirer un produit (25-10-2026)

## Contexte posé
Question : avec peu de ventes par produit, comment un agent peut-il décider de garder, retirer ou remplacer un produit sans se tromper à cause du bruit ?

Prompt de départ, recopié tel quel :

> Contexte : je construis un système d'agents IA qui gère une boutique Shopify de produits personnalisés. Un agent analysera les métriques de vente pour décider quels produits garder, retirer ou remplacer. Le volume de ventes par produit sera faible au début.
>
> Mission : fais une recherche sur les méthodes statistiques adaptées à ce problème.
> Je veux comprendre :
> - combien de visites ou de ventes il faut avant de conclure qu'un produit marche ou non ;
> - les métriques pertinentes (taux de conversion, taux d'ajout au panier, marge par visite, etc.) et leurs biais ;
> - les approches exploration et exploitation, notamment les bandits manchots (multi-armed bandits) et l'échantillonnage de Thompson, appliquées à un catalogue e-commerce ;
> - comment tenir compte de la saisonnalité et des effets de la publicité ;
> - comment éviter de retirer un produit à cause du bruit statistique.
>
> Format de sortie : 1) un résumé en 5 lignes, 2) les méthodes recommandées expliquées simplement avec un exemple chiffré, 3) des règles de décision concrètes utilisables par un agent, 4) les pièges, 5) des références (articles, bibliothèques Python).

## Conclusion en une phrase
L'agent ne doit jamais décider sur un taux brut : il doit utiliser un modèle Beta-Binomial avec un prior tiré du catalogue, décider sur la probabilité que la marge par visite passe sous un seuil après une exposition minimale, et allouer la visibilité par échantillonnage de Thompson avec oubli progressif.

## Résultats

### Pourquoi les petits nombres trompent
- Aux taux de conversion habituels (environ 1,5 %), le hasard domine sur quelques centaines de visites.
- Un produit dont le vrai taux est 1,4 % fait zéro vente sur 100 visites environ une fois sur quatre.
- Une règle « zéro vente après 100 visites, on retire » éliminerait donc environ un bon produit sur quatre.

### Intervalles de confiance pour petites proportions
- L'intervalle « classique » de Wald est mauvais pour les petits taux. Brown, Cai et DasGupta (2001) recommandent Wilson ou Jeffreys pour les petits échantillons, et Agresti-Coull pour les plus grands.
- Exemple : 3 ventes sur 200 visites donnent un intervalle de Wilson d'environ 0,5 % à 4,3 %. On ne peut pas conclure.
- Règle de trois : avec 0 vente sur n visites, la borne haute à 95 % vaut environ 3 divisé par n.
- Outil : `statsmodels.stats.proportion.proportion_confint(3, 200, method="wilson")`.

### Taille d'échantillon
| Question | Hypothèse | Visites nécessaires |
|---|---|---|
| Le produit bat-il un seuil fixe de 1 % ? | Vrai taux 2 %, risque 5 %, puissance 80 % | environ 1 000 |
| A bat-il B ? | 1 % contre 2 %, risque 5 %, puissance 80 % | environ 2 300 par produit |
| 1,4 % contre 1,7 % | Écart relatif de 20 % | plusieurs dizaines de milliers |

Avec peu de trafic, seuls les très gros écarts sont détectables. Il faut donc une méthode qui décide sous incertitude.

### Méthode centrale : Beta-Binomial bayésien
- Prior Beta(a, b), puis s ventes sur n visites : posterior Beta(a + s, b + n − s).
- Exemple : prior catalogue Beta(2, 98) (2 % avec un poids de 100 visites fictives), puis 3 ventes sur 200 visites. Posterior Beta(5, 295), moyenne 1,67 %.
- Probabilité que le vrai taux dépasse 1 % : environ 82 %. Qu'il dépasse 2 % : environ 28 %. Verdict : produit correct, pas candidat au retrait.
- Avec un prior neutre Beta(1, 1), la probabilité de dépasser 1 % serait d'environ 86 %. Le prior change peu la conclusion à 200 visites.
- Outil : `scipy.stats.beta(5, 295).sf(0.01)`.

### Shrinkage : empirical Bayes et modèle hiérarchique
- Le shrinkage tire les produits peu observés vers la moyenne du groupe.
- L'empirical Bayes estime le prior sur tous les produits (Robinson, exemple du baseball ; Efron sur la « preuve indirecte »).
- Le modèle hiérarchique estime aussi l'incertitude du prior, sur plusieurs niveaux : boutique, catégorie, produit. Exemple PyMC « Rat Tumor », d'après Gelman et al. (2013), chapitre 5.
- Recette de départ proposée par le rapport :
  1. Prendre les produits avec au moins 300 visites.
  2. Calculer la moyenne m et la variance v de leurs taux.
  3. Force du prior k = m × (1 − m) / v − 1, bornée entre 50 et 500.
  4. Prior a = m × k et b = (1 − m) × k.
  5. Recalculer chaque mois, puis par catégorie dès que possible.

### Métriques
| Métrique | Avantage | Limite |
|---|---|---|
| Taux de conversion | Lié à la vente | Très bruité |
| Taux d'ajout au panier | Environ 5 fois plus d'événements | Un ajout n'est pas une vente |
| Revenu par session | Tient compte du prix | Ignore les coûts |
| Marge par visite | Mesure ce qui compte | Demande les coûts |
| Marge par visite moins coût pub | Rentabilité réelle | Dépend de l'attribution |

- Le rapport recommande la marge par visite comme récompense finale.
- En print-on-demand, la marge unitaire est presque connue d'avance, donc l'inconnue principale est le taux de conversion.
- Le taux d'ajout au panier sert de signal précoce ou de prior, pas de critère de retrait.

### Exploration et exploitation : bandits
- Un bras égale un produit. Tirer un bras égale lui donner de la visibilité (accueil, collection, budget pub).
- Échantillonnage de Thompson : tirer un taux dans le posterior de chaque produit, mettre en avant le plus haut. L'incertitude crée l'exploration.
- Chapelle et Li (2011) le jugent très compétitif et simple. Scott (2015) le relie au coût d'opportunité dans les services en ligne.

| Problème catalogue | Solution | Référence |
|---|---|---|
| Produits qui entrent et sortent | Bandit « mortel » | Chakrabarti et al., NIPS 2008 |
| Nouveau produit sans données | Prior hiérarchique de sa catégorie | Hong et al., AISTATS 2022 (HierTS) |
| Récompense = marge | Taux tiré multiplié par la marge unitaire | Russo et al., 2018 |
| Produits similaires | Bandit contextuel | Vowpal Wabbit `--cb_explore_adf` |

Le rapport conseille de commencer sans contexte, avec des priors par catégorie.

### Saisonnalité et publicité
- Oubli des vieilles données : fenêtre glissante (Garivier et Moulines 2011 ; Trovò et al. 2020, corrigé par Fiandri et al. 2024) ou escompte quotidien gamma (Raj et Kalyani 2017).
- Avec peu de trafic, garder une fenêtre de 60 à 90 jours, ou gamma entre 0,98 et 0,99.
- Comparer chaque produit au catalogue sur la même période, pas à un seuil absolu.
- Tenir un posterior par produit et par source (organique, payant, e-mail, réseaux), puis un taux standardisé.
- Budgets pub inégaux : c'est un biais de sélection. Remèdes : budget d'exploration égal pour chaque nouveau produit, décision de retrait surtout sur le trafic organique, marquage du trafic « poussé ».

### Éviter les retraits dus au bruit
- Cinq outils combinés : shrinkage, probabilité d'être sous le seuil, perte attendue, exposition minimale, limite de retraits.
- Perte attendue : ce qu'on perd en moyenne si la décision est mauvaise (Stucchio, VWO). Le seuil d'indifférence est un choix métier en euros.
- Comparaisons multiples : sur 50 produits testés à 5 %, environ 2 à 3 « perdants » apparaissent par hasard.
- Peeking : décider dès qu'un seuil est franchi fausse les erreurs (Evan Miller ; Johari et al. 2017). L'approche bayésienne n'est pas immunisée (Molas 2025 ; Robinson).
- Conséquence : recalculer chaque jour, mais décider seulement à date fixe.

### Règles de décision proposées par le rapport
| Paramètre | Valeur de départ |
|---|---|
| Prior | Beta par catégorie, force entre 50 et 500 visites fictives |
| Exposition minimale | 300 visites, 14 jours et au moins 4 ventes attendues sous le prior |
| Seuil de marge par visite | Le plus haut entre 0,5 fois la médiane du catalogue et le coût par clic payant |
| Retrait | Probabilité d'être sous le seuil d'au moins 0,90 |
| Conservation | Probabilité d'être au-dessus d'au moins 0,80 |
| Fréquence | Une fois par semaine, jour fixe |
| Retraits maximum | 10 % du catalogue actif par semaine |
| Fenêtre | 90 jours, ou gamma entre 0,98 et 0,99 |
| Gel saisonnier | Pas de retrait hors saison |

1. Exposition insuffisante : état EXPLORATION, aucun retrait, visibilité minimale garantie.
2. Probabilité sous le seuil d'au moins 90 % et perte attendue au-dessus du seuil d'indifférence : CANDIDAT AU RETRAIT.
3. Candidat deux revues de suite : retrait et remplacement par un produit de la meilleure catégorie.
4. Probabilité au-dessus d'au moins 80 % : GARDER, visibilité par Thompson.
5. Sinon : SURVEILLER, avec un peu plus d'exploration.
6. Produit saisonnier hors saison : PAUSE au lieu de retrait.
7. Payant et organique divergent : décider sur le taux standardisé et alerter un humain.
8. Plus de 10 % du catalogue candidat la même semaine : suspendre les retraits (bug de suivi, panne, fin de saison).

Pseudo-code du rapport :

```python
import numpy as np
from scipy.stats import beta

def prior_categorie(taux_produits):
    m, v = np.mean(taux_produits), np.var(taux_produits)
    k = m * (1 - m) / v - 1 if v > 0 else 200
    k = float(np.clip(k, 50, 500))
    return m * k, (1 - m) * k

def evaluer(produit, a0, b0, marge_unitaire, seuil_marge_visite,
            seuil_indifference, n_tirages=20000, rng=np.random.default_rng(0)):
    s, n = produit["ventes"], produit["visites"]
    jours = produit["jours_en_ligne"]
    a, b = a0 + s, b0 + n - s
    ventes_attendues = n * a0 / (a0 + b0)
    if n < 300 or jours < 14 or ventes_attendues < 4:
        return "EXPLORATION"
    taux = beta(a, b).rvs(n_tirages, random_state=rng)
    marge_visite = taux * marge_unitaire
    p_sous = np.mean(marge_visite < seuil_marge_visite)
    p_dessus = 1 - p_sous
    perte_garder = np.mean(np.maximum(seuil_marge_visite - marge_visite, 0))
    if produit.get("saisonnier") and not produit.get("en_saison"):
        return "PAUSE_SAISON"
    if p_sous >= 0.90 and perte_garder > seuil_indifference:
        return "CANDIDAT_RETRAIT"
    if p_dessus >= 0.80:
        return "GARDER"
    return "SURVEILLER"

def thompson_mise_en_avant(produits, a0, b0, k_places, rng=np.random.default_rng()):
    scores = {}
    for p in produits:
        a = a0 + p["ventes"]; b = b0 + p["visites"] - p["ventes"]
        scores[p["id"]] = rng.beta(a, b) * p["marge_unitaire"]
    return sorted(scores, key=scores.get, reverse=True)[:k_places]

def escompter(produit, gamma=0.985):
    produit["ventes"] *= gamma
    produit["visites"] *= gamma
```

Le rapport demande aussi d'enregistrer la position d'affichage avec chaque visite, pour comparer à position égale.

### Pièges
| Piège | Parade |
|---|---|
| Petits nombres | Exposition minimale et prior |
| Biais de position | Enregistrer la position, rotation aléatoire (Aslanyan et Porwal, eBay) |
| Sources de trafic | Posterior par source, taux standardisé |
| Budgets pub inégaux | Budget d'exploration égal |
| Effet nouveauté ou primauté | Juger sur au moins 14 jours (Kohavi et al., KDD 2012) |
| Saisonnalité | Indice relatif au catalogue, gel saisonnier |
| Biais du survivant | Garder les produits retirés dans le calcul du prior |
| Peeking | Décider à jour fixe, règle écrite d'avance |
| Comparaisons multiples | Shrinkage et limite de retraits |
| Prior trop fort | Force bornée à 500 |
| Oubli trop rapide | Fenêtre de 60 à 90 jours |
| Suivi cassé | Suspendre si trop de produits chutent ensemble |
| Données adaptatives du bandit | Part d'exploration minimale par produit |

### Bibliothèques Python
| Bibliothèque | Usage |
|---|---|
| scipy.stats | Lois Beta, probabilités au-dessus d'un seuil |
| statsmodels | Intervalles Wilson, Jeffreys, Agresti-Coull, Clopper-Pearson |
| PyMC et ArviZ | Modèles hiérarchiques |
| MABWiser (Fidelity) | Bandits, dont Thompson, avec simulation |
| Vowpal Wabbit | Bandits contextuels, actions variables |
| contextualbandits (David Cortes) | Bandits contextuels, récompenses binaires, outil de recherche |

### Références principales
- Brown, Cai et DasGupta, Statistical Science, 2001 ; Agresti et Coull, The American Statistician, 1998.
- Russo, Van Roy et al., « A Tutorial on Thompson Sampling », 2018 ; Chapelle et Li, NIPS 2011 ; Slivkins, « Introduction to Multi-Armed Bandits », 2019.
- Scott, Applied Stochastic Models in Business and Industry, 2015.
- Chakrabarti et al., « Mortal Multi-Armed Bandits », NIPS 2008 ; Hong et al., « Hierarchical Bayesian Bandits », AISTATS 2022.
- Garivier et Moulines, ALT 2011 ; Trovò et al., JAIR 2020 ; Fiandri et al., arXiv 2409.05181 ; Raj et Kalyani, arXiv 1707.09727.
- Johari et al., KDD 2017 ; Kohavi, Tang et Xu, « Trustworthy Online Controlled Experiments », 2020.
- Efron, Statistical Science, 2010 ; Gelman et al., « Bayesian Data Analysis », 3e édition, 2013.
- Robinson (Variance Explained), Evan Miller, Molas, Stucchio (VWO).

## Chiffres

### Sourcés
| Chiffre | Source |
|---|---|
| Conversion médiane Shopify 1,4 % ; top 20 % au-dessus de 2,7 % ; top 10 % au-dessus de 3,6 % (433 boutiques, 20/07 au 17/10/2026) | source : Littledata |
| Ajout au panier médian 6,8 % ; top 20 % au-dessus de 12 % | source : Littledata |
| Ajout au panier médian 5,4 % sur mobile contre 9,7 % sur ordinateur | source : Littledata |
| Conversion moyenne mondiale e-commerce 2,66 % | source : Triple Whale |
| Conversion médiane du trafic payant 1,69 % (août 2025 à juillet 2026, plus de 53 000 marques) | source : Triple Whale |
| Regarder 10 fois une expérience demande 1 % de significativité affichée pour garder 5 % réel | source : Evan Miller |
| Exemple de Morris : 18 joueurs | source : Efron, 2010 |
| Exemple PyMC : 71 expériences | source : PyMC, Rat Tumor Example |

### Estimés
| Chiffre | Provenance |
|---|---|
| Zéro vente sur 100 visites à 1,4 % : environ 24 % ; sur 200 visites : environ 6 % | estimé (calcul du rapport) ⚠️ à vérifier |
| Intervalle de Wilson de 3/200 : environ 0,51 % à 4,32 % | estimé (calcul du rapport) ⚠️ à vérifier |
| Environ 1 000 visites contre un seuil fixe ; environ 2 300 par produit pour comparer deux produits | estimé (calcul du rapport) ⚠️ à vérifier |
| Beta(5, 295) : 82 % au-dessus de 1 %, 28 % au-dessus de 2 % ; Beta(4, 198) : 86 % au-dessus de 1 % | estimé (calcul du rapport) ⚠️ à vérifier |
| Marge par visite d'environ 0,20 € (marge 12 €, taux 1,67 %) contre 0,35 € par clic | estimé (exemple illustratif) |
| Environ 5 fois plus d'ajouts au panier que de ventes | estimé (6,8 % divisé par 1,4 %) |
| 50 produits testés à 5 % : environ 2 à 3 erreurs par cycle | estimé (calcul du rapport) |
| Gamma de 0,98 : une vente de 35 jours pèse environ moitié moins | estimé (calcul du rapport) |
| Seuils 90 % et 80 %, 300 visites, 14 jours, 4 ventes attendues, 10 % de retraits par semaine, force du prior de 50 à 500, fenêtre de 60 à 90 jours | estimé (choix prudents du rapport, pas des normes publiées), à calibrer par simulation |

### Contradictions entre sources (non tranchées)
- Taux de conversion de référence : 1,4 % (médiane Shopify, Littledata) contre 2,66 % (moyenne mondiale e-commerce, Triple Whale). L'une est une médiane Shopify, l'autre une moyenne tous sites.

## Caveats
- Les chiffres de référence sont des médianes Shopify toutes catégories, pas propres au print-on-demand. ⚠️ à vérifier sur nos propres données dès qu'elles existent.
- Les calculs (intervalles, probabilités, tailles d'échantillon) ont été faits à la main par le rapport. ⚠️ à recalculer avec scipy avant de les inscrire dans l'agent.
- Les seuils de décision sont des points de départ. Le rapport recommande de les régler par simulation : produits à taux connus, agent en boucle, mesure des bons produits retirés à tort.
- La littérature sur les bandits optimise le gain cumulé. Retirer un produit est irréversible, donc la prudence prime sur la vitesse.
- Le pseudo-code n'a pas été exécuté.
- La conversion par produit dépend d'un suivi des vues produit (Web Pixel ou GA4), voir [[RCH - API Shopify pour la boutique agentique (22-10-2026)]].

## Retenu / écarté

