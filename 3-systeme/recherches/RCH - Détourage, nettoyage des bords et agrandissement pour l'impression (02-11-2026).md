---
type: research
title: RCH - Détourage, nettoyage des bords et agrandissement pour l'impression (02-11-2026)
status: validé
related: ["[[RCH - Génération d'images pour l'impression (22-10-2026)]]", "[[RCH - Contraintes d'impression Printify des trois produits (01-11-2026)]]", "[[A VERIFIER - Points à valider, vérifier, tester]]"]
decisions: ["[[06 - LangGraph au départ, interface d'images interne avec Nano Banana Pro et Ideogram]]", "[[14 - Brief visuel, deux gabarits de design déclinés par titre et par occasion, rendu peint aux formes franches]]"]
date: 2026-11-02
sources:
  - "Tests réels dans l'environnement d'exécution de claude.ai (Linux, 1 cœur, 3 Go de mémoire), mesurés le 02/11/2026 ; scripts et résultats bruts dans tests-detourage/scripts/"
  - "rembg (modèles u2net, isnet-general-use, birefnet-general-lite) : https://github.com/danielgatis/rembg"
  - "BiRefNet : https://github.com/ZhengPeng7/BiRefNet"
  - "pymatting, estimation du premier plan : https://pymatting.github.io/foreground.html"
  - "Real-ESRGAN (x4plus, x2plus, anime_6B, general-x4v3 et wdn) : https://github.com/xinntao/Real-ESRGAN"
  - "SwinIR (003_realSR_BSRGAN_DFO_s64w8_SwinIR-M_x4_GAN) : https://github.com/JingyunLiang/SwinIR"
  - "spandrel (chargement des poids) : https://github.com/chaiNNer-org/spandrel"
  - "4x-UltraSharp, licence CC BY-NC-SA 4.0 : https://huggingface.co/Kim2091/UltraSharp"
  - "Bria RMBG 2.0, licence CC BY-NC 4.0 : https://github.com/Bria-AI/RMBG-2.0"
  - "Taille d'impression du mug 11 oz Printify (source tierce) : https://printreadypod.com/mug-design-size-guide"
last-verified: 2026-11-02
tags: [dropshipping, systeme, generation-images, impression, research]
---
# RCH - Détourage, nettoyage des bords et agrandissement pour l'impression (02-11-2026)

## Contexte posé
Demande d'Antoine, 02/11/2026, recopiée telle quelle :

> Contexte : nos éléments d'illustration sont en gouache aux formes franches, générés sur fond uni,
> détourés puis agrandis pour l'impression (décisions 06 et 14).
> Recherche technique avec tests réels si possible dans ton environnement : prends ou crée une image
> test d'un élément peint (bords texturés, pas d'aplat) sur fond uni.
> 1. Détourage : BiRefNet, rembg, et le détourage par couleur de fond. Qualité des bords sur une
>    texture peinte, halos, îlots.
> 2. Nettoyage des bords : seuillage de l'alpha, érosion, suppression des franges ; effet sur un
>    fond blanc puis sur un fond coloré.
> 3. Agrandissement ×2 et ×4 : Real-ESRGAN, et une alternative ; conservation de la matière peinte,
>    artefacts sur les bords détourés.
> 4. Ordre des opérations : détourer puis agrandir, ou l'inverse.
> Images avant et après dans 3-systeme/recherches/tests-detourage/, temps et coût par image.
> Conclusion : la chaîne recommandée pour un élément de 85 mm sur bois et pour le tour du mug.

Méthode. Une recherche documentaire (mode recherche avancée de claude.ai) a précédé les tests. Elle
recommandait d'agrandir avant de détourer ; **les tests ci-dessous la contredisent**, et c'est leur
résultat qui est retenu ici.

Image test. Une pomme peinte de synthèse sur fond crème uni, avec feuille, texture de pigment, bord
droit à brosse sèche, un trou intérieur, 12 éclaboussures et un reflet crème presque de la couleur du
fond. Elle est rendue en 4096 px puis réduite en 1024 px. La version 1024 joue le rôle de l'image
générée. Les versions 2048 et 4096 servent de **vérité de référence** : on sait exactement ce qu'un
agrandissement parfait devrait donner.

Mesures. Erreur de l'alpha par rapport à la vérité (l'alpha est le canal de transparence, de 0 à 1).
Éclaboussures gardées, îlots parasites, trou ouvert, reflet gardé. Écart de couleur ΔE sur la bande de
bord, une fois l'élément posé sur trois fonds : blanc (le mug), bois clair, bleu soutenu. Le ΔE est une
distance de couleur perçue ; sous 2 à 3, l'œil voit à peine l'écart.

## Conclusion en une phrase
Sur une gouache générée sur fond uni, la meilleure chaîne mesurée est : détourer à la taille native
en combinant un réseau et une clé de couleur, décontaminer les couleurs du bord, puis seulement
agrandir le RGB décontaminé, avec l'alpha agrandi en bicubique ; l'érosion et l'agrandissement de
l'alpha par un modèle d'IA dégradent les bords.

## Résultats

### 1. Détourage
Mesuré le 02/11 sur l'image de 1024 px, après décontamination
(planche `tests-detourage/01-detourage-comparaison.png`).

| Méthode | Erreur alpha | Éclaboussures | Reflet gardé | ΔE bord, bois | ΔE bord, bleu |
|---|---|---|---|---|---|
| rembg u2net | 1,48 % | 5 sur 12 | 52 % | 7,4 | 14,9 |
| rembg isnet-general-use | 0,64 % | 6 sur 12 | 99 % | 4,1 | 8,2 |
| Clé de couleur Lab seule | 0,98 % | 12 sur 12 | 8 % | 2,9 | 4,4 |
| **Fusion isnet et clé Lab** | **0,33 %** | **12 sur 12** | **100 %** | **3,0** | **4,7** |

Fusion brute, sans décontamination : erreur 0,33 %, ΔE bois 4,6, ΔE bleu 5,6.

- **Le réseau seul perd la moitié des éclaboussures.** Il les juge hors de l'objet.
- **La clé de couleur seule perd le reflet.** Une zone peinte de la couleur du fond devient transparente.
- **La fusion garde les deux.** Le réseau donne la zone de l'objet et son cœur sûr. La clé donne le bord
  exact, les éclaboussures et le trou. Le trou est ouvert par toutes les méthodes sur cette image.
- Réglage de la clé : distance Lab au fond, transparente sous 10, opaque au-dessus de 60, rampe entre
  les deux. Les seuils sont à recalibrer si le fond ou la palette changent.
- Cœur sûr : partout où le réseau est confiant à plus de 0,9 et où la distance au fond dépasse 1,7 fois
  le bruit du fond. C'est ce qui sauve le reflet.
- **BiRefNet n'a pas pu tourner** : il dépasse 3 Go de mémoire, même en version allégée et sans
  optimisation. isnet tient sa place dans la fusion. Comme le réseau ne sert qu'à tracer la zone et le
  cœur, un réseau moyen suffit sur ce cas ⚠️ à confirmer avec BiRefNet.

### 2. Nettoyage des bords
Mesuré le 02/11, sur la sortie de la fusion (planche `tests-detourage/02-nettoyage-bords.png`).

| Geste | Erreur alpha | Éclaboussures | ΔE blanc | ΔE bois | ΔE bleu |
|---|---|---|---|---|---|
| Aucun | 0,33 % | 12 sur 12 | 3,1 | 4,6 | 5,6 |
| Seuillage seul (0,04 et 0,96) | 0,33 % | 12 sur 12 | 3,1 | 4,6 | 5,7 |
| **Décontamination seule (pymatting)** | **0,33 %** | **12 sur 12** | **2,5** | **3,0** | **4,7** |
| Seuillage, ouverture, îlots, décontamination | 0,36 % | 12 sur 12 | 3,1 | 3,3 | 5,1 |
| Idem et érosion de 1 px | 0,68 % | 9 sur 12 | 9,1 | 6,1 | 10,1 |
| Idem et érosion de 2 px | 1,43 % | 6 sur 12 | 19,7 | 12,3 | 21,8 |

- La **décontamination** est le seul geste qui compte. Elle recalcule la vraie couleur de la peinture
  sous les pixels semi-transparents, ce qui supprime la frange teintée du fond.
- Le seuillage ne change presque rien quand l'alpha vient de la clé.
- **L'érosion est nuisible.** Elle ronge le bord sec et efface les petites éclaboussures. Sur le blanc
  du mug, l'écart triple dès 1 px.
- La suppression des îlots reste utile contre le bruit, avec un seuil bas (8 px à 1024 px). Le brief
  interdit déjà tout détail sous 1 mm à 85 mm, soit environ 12 px à 300 DPI (estimé).

### 3. Agrandissement ×2 et ×4
Mesuré le 02/11 sur une zone de 256 px avec bord sec, reflet et éclaboussure, comparée à la vérité
(planche `tests-detourage/03-agrandissement-x4.png`). « Texture » vaut 1 quand le grain intérieur a la
même énergie que la référence ; au-dessus de 1, l'outil invente du grain ; en dessous, il lisse.

| Outil | ΔE global ×2 | ΔE bord ×2 | Texture ×2 | ΔE global ×4 | ΔE bord ×4 | Texture ×4 |
|---|---|---|---|---|---|---|
| Lanczos (interpolation classique) | 0,7 | 1,2 | 0,68 | 0,7 | 1,4 | 0,79 |
| RealESRGAN_x2plus | 2,7 | 6,4 | 0,85 | — | — | — |
| RealESRGAN_x4plus | 3,0 | 7,9 | 1,16 | 3,0 | 7,8 | 1,47 |
| general-x4v3, débruitage 0,2 | 2,9 | 10,1 | 1,28 | 3,0 | 10,1 | 1,52 |
| general-x4v3, débruitage 1,0 | 3,3 | 12,6 | 0,48 | 3,3 | 12,5 | 0,75 |
| anime_6B | 4,0 | 11,1 | 0,39 | 4,1 | 11,3 | 0,84 |
| SwinIR-M (alternative) | 4,0 | 9,1 | 0,78 | 4,0 | 9,0 | 1,23 |

- **Aucun modèle d'IA ne bat Lanczos en fidélité** sur cette image.
- À l'œil, les modèles d'IA durcissent les bords et aplatissent le grain en taches lisses. Ils
  ajoutent aussi un liseré clair autour des formes (planche 03).
- anime_6B et le débruitage fort font de la gouache un aplat : à écarter pour notre rendu.
- Ce résultat **favorise sans doute Lanczos**, car la texture de synthèse est un bruit simple que
  Lanczos reproduit bien. Sur une vraie gouache générée, un modèle d'IA pourrait mieux faire ⚠️ à vérifier.

### 4. Ordre des opérations
Mesuré le 02/11 sur la même zone, élément posé sur bois
(planches `tests-detourage/04-ordre-operations-x4-bois.png` et `05-ordre-reflet-perdu.png`).
A = détourer à 1024 puis agrandir. B = agrandir l'image entière, fond compris, puis détourer.

| Chaîne | Erreur alpha ×4 | Reflet | ΔE blanc | ΔE bois | ΔE bleu |
|---|---|---|---|---|---|
| **A, Lanczos, RGB décontaminé, alpha bicubique** | **1,03 %** | **100 %** | **3,2** | **4,7** | **6,6** |
| A, x4plus, RGB décontaminé, alpha bicubique | 1,03 % | 100 % | 4,1 | 4,8 | 7,5 |
| A, x4plus, RGB original, alpha bicubique | 1,03 % | 100 % | 8,8 | 8,7 | 12,6 |
| A, x4plus, RGB décontaminé, alpha par le modèle | 1,70 % | 100 % | 7,7 | 6,0 | 11,3 |
| B, Lanczos | 1,19 % | 100 % | 3,0 | 5,6 | 7,5 |
| B, x4plus | 4,59 % | 48 % | 9,9 | 7,1 | 13,6 |
| B, general-x4v3 débruitage 0,2 | 4,46 % | 52 % | 11,9 | 8,7 | 14,0 |

À ×2, même classement : A Lanczos décontaminé donne ΔE bois 3,9, contre 4,4 pour B Lanczos et 5,4 pour
B x2plus.

- **Détourer puis agrandir gagne.** C'est l'ordre des décisions 06 et 14.
- **Mais il faut décontaminer avant d'agrandir.** Sous l'alpha nul, le RGB original garde la couleur du
  fond. L'agrandisseur la mélange au bord et crée un liseré clair : ΔE bois 8,7 au lieu de 4,8.
- **L'alpha s'agrandit en bicubique.** Agrandi par le modèle d'IA, il gagne une frange rose et durcie.
- **Agrandir d'abord casse le détourage avec un modèle d'IA.** Le modèle ajoute du grain au fond uni. Le
  seuil du cœur sûr monte, et le reflet proche du fond redevient à moitié transparent.

### 5. Temps et coût par image
Temps mesurés le 02/11 sur 1 cœur de processeur. Les temps pour 1024 px sont extrapolés des mesures
sur 256 px (facteur 16, estimé). Un Mac Apple Silicon avec tous ses cœurs ou sa puce graphique
sera nettement plus rapide (non mesuré).

| Étape | Mesuré | Pour une image de 1024 px | Coût |
|---|---|---|---|
| rembg u2net | 1,2 s à 1024 px | 1,2 s | 0 en local |
| rembg isnet-general-use | 3,2 s à 1024 px | 3,2 s | 0 en local |
| Fusion avec la clé Lab | 1,7 s à 1024 px | 1,7 s | 0 |
| Décontamination et nettoyage | 0,3 s à 1024 px | 0,3 s | 0 |
| Lanczos ×2 ou ×4 | 0,01 s pour 256 px | moins de 0,2 s (estimé) | 0 |
| general-x4v3 | 1,2 s pour 256 px | environ 20 s (estimé) | 0 en local |
| RealESRGAN_x2plus | 5,6 s pour 256 px | environ 1,5 min (estimé) | 0 en local |
| RealESRGAN_x4plus | 27 s pour 256 px | environ 7 min (estimé) | 0 en local ; environ 0,002 USD sur Replicate (source : RCH du 22/10) |
| SwinIR-M | 54 s pour 256 px | environ 14 min (estimé) | 0 en local |
| BiRefNet | non mesurable ici | — | environ 0,51 USD pour 1 000 images sur Replicate (source : RCH du 22/10) |

Chaîne recommandée complète, sur 1 cœur : environ 5 à 6 s par élément de 1024 px (estimé, somme des
mesures). Coût en local : nul hors électricité.

### 6. Ce que la taille d'impression demande
- Élément de 85 mm à 300 DPI : 1 004 px (estimé, calcul 85 ÷ 25,4 × 300). La forme la plus haute,
  la chaussette de 162 mm, demande 1 913 px (estimé).
- Mug Printify chez Textildruck Europa : 95 mm de haut et 80 mm de diamètre (source : RCH du 01/11).
  Les pixels de la zone ne sont pas relevés. Une source tierce donne 2 480 × 1 146 px pour le mug
  11 oz Printify ⚠️ à vérifier dans l'éditeur Printify.
- Nano Banana Pro coûte le même prix en 1K et en 2K (0,134 USD, source : RCH du 22/10). En 2K, un
  élément qui occupe au moins la moitié de la largeur dépasse déjà 1 004 px : **pas d'agrandissement
  pour le bois** (estimé).
- Pour le tour du mug, l'agrandissement reste nécessaire depuis une image 2K, d'un facteur proche de
  1,2 à 2 selon la composition (estimé).

### 7. Chaîne recommandée par la recherche
Proposition de la recherche, rien n'est décidé.

**Commun aux deux supports.**
1. Générer en 2K sur un fond uni éloigné de toute la palette ; aucune zone peinte de la couleur du fond.
2. Détourer à la taille native par fusion : un réseau (isnet, ou BiRefNet si le test sur Mac est
   meilleur) donne la zone et le cœur, la clé Lab (10 à 60) donne le bord.
3. Décontaminer avec pymatting. Supprimer les îlots sous 8 px (à 1024 px). Ni érosion ni ouverture.
4. Agrandir seulement si la taille cible l'exige : le RGB décontaminé en Lanczos, l'alpha en bicubique.
5. Ramener à la taille exacte, PNG avec alpha, sRGB, 300 DPI.

**Élément de 85 mm sur bois.** Étapes 1 à 3 et 5, sans agrandissement si l'élément fait au moins
1 004 px. Le bois ne couvre pas tout le grain et n'a peut-être pas de sous-couche blanche (RCH du
01/11) : la frange claire est le risque principal, c'est la décontamination qui le traite.

**Tour du mug.** Étapes 1 à 5. Agrandissement de 1,2 à 2 en Lanczos sur le RGB décontaminé. Alpha
progressif conservé : en sublimation, le blanc du mug sert de fond, et c'est le cas où la
décontamination gagne le plus (ΔE blanc 2,5 au lieu de 3,1).

**Si l'échantillon du 5 novembre trouve le bord trop mou.** Essayer RealESRGAN_x2plus à la place de
Lanczos, toujours sur le RGB décontaminé, et comparer sur la pièce imprimée.

## Chiffres

### Sourcés
| Chiffre | Source |
|---|---|
| Tous les résultats des parties 1 à 5 | mesuré le 02/11 (tests-detourage/scripts/, résultats bruts res_up.json et res_ordre.json) |
| Mug 95 mm de haut, 80 mm de diamètre | source : [[RCH - Contraintes d'impression Printify des trois produits (01-11-2026)]] |
| Formes en bois de 85 à 92 mm de large, de 97 à 162 mm de haut | source : idem |
| Nano Banana Pro : 0,134 USD en 1K ou 2K, 0,24 USD en 4K | source : [[RCH - Génération d'images pour l'impression (22-10-2026)]] |
| Real-ESRGAN sur Replicate : environ 0,002 USD par image | source : idem |
| BiRefNet sur Replicate : environ 0,51 USD pour 1 000 images | source : idem |
| 4x-UltraSharp sous licence CC BY-NC-SA 4.0 | source : huggingface.co/Kim2091/UltraSharp |
| Bria RMBG 2.0 sous licence CC BY-NC 4.0, modèle par défaut des versions récentes de rembg | source : github.com/Bria-AI/RMBG-2.0, pypi.org/project/rembg |
| Mug 11 oz Printify : 2 480 × 1 146 px | source tierce : printreadypod.com ⚠️ à vérifier |

### Estimés
| Chiffre | Statut |
|---|---|
| 1 004 px pour 85 mm, 1 913 px pour 162 mm, 12 px pour 1 mm, à 300 DPI | estimé (calcul) |
| Temps pour 1 024 px des agrandisseurs | estimé (×16 sur la mesure à 256 px) |
| Chaîne complète en 5 à 6 s sur 1 cœur | estimé (somme des mesures) |
| Facteur 1,2 à 2 pour le tour du mug depuis une image 2K | estimé |

## Caveats
- **Image de synthèse.** La texture est un bruit, pas une vraie gouache générée. Le classement des
  agrandisseurs peut changer sur une vraie image ⚠️ à vérifier.
- **BiRefNet non testé** faute de mémoire dans l'environnement ⚠️ à tester sur le Mac.
- **Topaz, Recraft Crisp, HAT et les modèles communautaires** n'ont pas été testés.
- Temps mesurés sur 1 cœur de processeur ; temps sur Mac non mesurés.
- Une seule image et une seule couleur de fond. Le cas « peinture de la couleur du fond » a été forcé
  par le reflet ; un fond très proche d'un aplat de la palette casserait la clé.
- Rendu réel sur bois (grain, absence de sous-couche blanche), sur verre UV et sur le mug : seule la
  commande test du 5 novembre le dira ⚠️.

Contradictions entre sources, non tranchées :
- La recherche documentaire du 02/11 recommandait d'agrandir avant de détourer ; les tests du 02/11
  donnent l'ordre inverse.
- La recherche du 22/10 recommande Real-ESRGAN pour les aplats et le trait ; sur la matière peinte de
  synthèse, Lanczos mesure mieux.

À inscrire au registre A VERIFIER à la revue : BiRefNet contre isnet sur le Mac ; Lanczos contre
x2plus sur une vraie gouache générée ; pixels de la zone du mug dans l'éditeur Printify ; rendu des
bords décontaminés sur la commande test.

## Retenu / écarté
Revue du 02/11/2026 avec Antoine.

**Retenu**
- La chaîne mesurée : détourer à la taille native par fusion d'un réseau (isnet, ou BiRefNet si
  meilleur sur le Mac) et d'une clé de couleur Lab ; décontaminer les bords avec pymatting ; supprimer
  les îlots sous 8 px ; agrandir seulement si nécessaire, le RGB décontaminé en Lanczos, l'alpha en
  bicubique ; PNG alpha sRGB 300 DPI.
- L'ordre « détourer puis agrandir », qui confirme les décisions 06 et 14.
- Générer en 2K sur un fond uni éloigné de toute la palette : pas d'agrandissement pour le bois,
  facteur 1,2 à 2 pour le tour du mug.
- Le principe de la vérité de référence (rendu en 4096 px réduit en 1024 px) pour mesurer un agrandisseur.

**Écarté**
- L'érosion et l'ouverture des bords : elles rongent le bord sec et effacent les éclaboussures.
- Real-ESRGAN et SwinIR comme agrandisseurs par défaut : moins fidèles que Lanczos sur cette image.
  RealESRGAN_x2plus gardé en repli si l'échantillon trouve le bord trop mou.
- L'agrandissement de l'alpha par un modèle d'IA.
- Bria RMBG 2.0 et 4x-UltraSharp : licences non commerciales.

**Conséquence**
- Contredit [[RCH - Génération d'images pour l'impression (22-10-2026)]] sur Real-ESRGAN : à noter
  dans [[SYN - Système]] comme remplacé par Lanczos sur la matière peinte, à confirmer sur une vraie
  gouache.
- Au registre A VERIFIER : BiRefNet contre isnet sur le Mac ; Lanczos contre x2plus sur une vraie
  gouache Nano Banana Pro (fichiers dans `tests-images/sorties/`) ; rendu des bords décontaminés sur
  la commande test.
