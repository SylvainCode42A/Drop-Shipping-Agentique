---
type: research
title: RCH - Capacités de FLUX.2 Klein 4B en local pour les deux gabarits (02-11-2026)
status: validé
related: ["[[RCH - Génération d'images pour l'impression (22-10-2026)]]", "[[A VERIFIER - Points à valider, vérifier, tester]]"]
decisions: ["[[14 - Brief visuel, deux gabarits de design déclinés par titre et par occasion, rendu peint aux formes franches]]", "[[06 - LangGraph au départ, interface d'images interne avec Nano Banana Pro et Ideogram]]"]
date: 2026-11-02
sources:
  - https://ollama.com/blog/image-generation
  - https://ollama.com/x/flux2-klein/tags
  - https://github.com/ollama/ollama/issues/17893
  - https://help.bfl.ai/articles/8642316687-flux-2-klein-fast-generation-guide
  - https://github.com/oddlantern/imagery
  - https://git.minecraftlegacy.com/ihateninjas/ollama/src/branch/main/x/imagegen
last-verified: 2026-11-02
tags: [dropshipping, systeme, generation-images]
---
# RCH - Capacités de FLUX.2 Klein 4B en local pour les deux gabarits (02-11-2026)

## Contexte posé
Niveau 1 de la recherche sur les modèles d'images : vérifier ce qu'un modèle local sait faire pour les
deux gabarits de la [[14 - Brief visuel, deux gabarits de design déclinés par titre et par occasion, rendu peint aux formes franches|décision 14]],
avant de tester les fournisseurs de la [[06 - LangGraph au départ, interface d'images interne avec Nano Banana Pro et Ideogram|décision 06]].

Montage : Mac M2 Pro, 16 Go de mémoire unifiée ; Ollama 0.32.5 lancé à la main ; modèle
`x/flux2-klein:4b` (fp4, 5,7 Go, Apache 2.0) ; appels par le connecteur MCP local `ollama-image`
(`~/dev/ollama-image-mcp`) depuis Claude Desktop ; toutes les images en 1024 × 1024, graine fixée.
Images et paramètres : `3-systeme/recherches/tests-images/ollama/`, un `.json` par PNG avec le prompt
exact, la graine, le temps et la taille.

Rendu cible ajouté à chaque prompt : gouache opaque, formes franches, contours fermés, couleurs moyennes
à soutenues, pas de lavis ni de dégradé, aucun visage réaliste, aucun personnage ou marque reconnaissable,
style illustration de livre pour enfants sans référence à un illustrateur nommé.

Les cinq tests demandés :
> T1. Élément isolé : une fleur, puis une boule de Noël, chacune seule, centrée, sur fond uni vert
> saturé (#00FF00) pour détourage par couleur. Deux graines par élément.
> T2. Zone vide par prompt : la même fleur en haut, et « le tiers inférieur de l'image est un aplat
> uni couleur crème, sans aucun élément ». Trois graines.
> T3. Scène fixe : une scène de salon chaleureux sans personnage (fauteuil, plaid, lampe, plante,
> fenêtre), avec un grand mur uni crème sur la moitié droite, prévu pour du texte. Deux graines.
> T4. Stabilité du style : le prompt T1 fleur, cinq graines différentes.
> T5. Déclinaison contrôlée : le prompt T3 avec « une fenêtre enneigée et un petit sapin décoré
> dans le coin gauche », même graine que la meilleure T3.

> T6, ajouté à la revue : vérifier si FLUX.2 Klein par l'API d'Ollama utilise une image en entrée
> (référence de style, puis édition), avec un témoin sans image. Script `test_img2img.py`, hors connecteur.

Chaque image a été regardée, puis mesurée au pixel près (couleur et dispersion du fond, lignes de
rupture, différence entre images) par un script Python.

## Conclusion en une phrase
FLUX.2 Klein 4B en local produit des éléments isolés à palette stable mais à forme et contour instables,
ne sait ni garder une scène continue autour d'une zone vide ni décliner une scène sans la redessiner ;
il sert à calibrer les prompts, pas à produire.

## Résultats

### Capacité par capacité
| Test | Capacité | Fait | Ne fait pas | Instable | Fichiers |
|---|---|---|---|---|---|
| T1 | Élément isolé sur fond uni | Élément entier, centré, marges de 200 px au moins ; matière opaque sur fond vert | Fond #00FF00 exact (écart de 60 à 83) ; pas d'ombre sur les boules | Couleur du fond d'une image à l'autre ; franges vertes sur 14 à 39 % des pixels de bord | `t1-fleur-seed42`, `t1-fleur-seed43`, `t1-boule-seed42`, `t1-boule-seed43` |
| T2 | Zone vide demandée par le prompt | Tiers inférieur vide et uni sur 3 graines sur 3 ; la fleur reste au-dessus | Fond continu : une bande crème distincte, ligne d'horizon vers 60 % au lieu de 67 % | Rendu : pétales marbrés, proches de l'aquarelle | `t2-fleur-zone-vide-seed42`, `-seed43`, `-seed44` |
| T3 | Scène fixe avec zone de texte | Éléments demandés, sans personnage ; moitié droite parfaitement unie | Mur dans la pièce : page blanche collée, coupure verticale nette à x ≈ 505 ; gouache : lavis, dégradés, trait fin | — | `t3-salon-seed42`, `t3-salon-seed43` |
| T4 | Même style sur cinq graines | Palette stable (pétales à quelques points du même corail, feuilles du même olive) | — | Contour (net sur 45 et 48, absent sur 44 et 46) ; matière (lisse, grain, feutre) ; forme (5 ou 8 pétales, corolle festonnée, nuage) ; cœur (jaune, brun, noir, absent) | `t4-fleur-seed44` à `t4-fleur-seed48` |
| T5 | Déclinaison par ajout au prompt, même graine | Demande respectée (neige, sapin décoré) ; zone de texte identique au pixel près | Garder le reste : 64 % de la moitié gauche change, 46 % hors sapin et fenêtre (lampe déplacée, pot disparu, rideau supprimé, fenêtre et plaid modifiés) | — | `t5-salon-hiver-seed43` comparé à `t3-salon-seed43` |
| T6 | Image de référence et édition par l'API (`images` dans `/api/generate`) | — | Utiliser l'image : sortie identique octet pour octet au témoin sans image ; édition du salon redessinée à 93 % | — | `t6-ref-fleur-bleue-seed42` et `t6-sans-ref-fleur-bleue-seed42` ; `t6-edition-salon-hiver-seed43` comparé à `t3-salon-seed43` |

### Les deux gabarits de la décision 14
- **Éléments séparés composés par code** (un symbole par prénom) : réaliste avec du code autour, pas
  avec le modèle seul. Le modèle donne un élément isolé utilisable, mais pas six symboles cohérents :
  il faut choisir une fleur de référence à la main puis la dupliquer ou la recolorer par code. Le
  détourage doit mesurer la couleur du fond sur chaque image et retirer le vert des bords, ou passer
  par un détoureur comme BiRefNet.
- **Scène d'un bloc avec zone masquée** : pas réaliste avec ce modèle. La zone reste vide mais comme une
  page séparée, sans continuité de la pièce ; le rendu sort de la gouache ; et la déclinaison hivernale
  redessine la scène au lieu d'ajouter un calque. Ce gabarit demande une édition locale avec masque,
  ou une scène figée sur laquelle le code pose les calques de décor.

### Ollama en production
- **Version figée** : la génération d'images a été retirée d'Ollama à partir de la 0.32.6 ; seule la
  0.32.5 la garde (source : issue ollama#17893). Plus de correctifs ni de mises à jour sur cette voie.
- **Pas d'édition locale avec masque** : l'API utilisée ne prend qu'un prompt, une taille et une graine
  (`width` et `height` à la racine, graine dans `options.seed`, mesuré le 02/11).
- **Pas d'image de référence ni d'édition par l'API** : le champ `images` de `/api/generate` est accepté
  sans erreur mais ignoré ; même prompt et même graine donnent la même image, octet pour octet, avec ou
  sans référence (mesuré le 02/11, T6). Un projet tiers annonce l'édition d'image à image avec FLUX.2 Klein
  par Ollama (source : github.com/oddlantern/imagery), peut-être par la ligne de commande ; non testé
  ⚠️ à vérifier, sans effet sur notre chaîne qui passe par l'API.
- **Matériel** : Z-Image Turbo ne tient pas sur 16 Go (11,9 Go demandés, 11,3 disponibles pour le GPU,
  mesuré le 02/11).
- Donc : **calibration des prompts et brouillons seulement**, jamais derrière l'interface d'images de la
  décision 06.

### Tests à lancer quand une clé sera disponible (Nano Banana Pro, Ideogram)
Mêmes prompts, mêmes mesures, mêmes noms de fichiers préfixés par le fournisseur.
1. **Image de référence** : donner `t4-fleur-seed45.png` en référence et demander six fleurs ; mesurer
   contour, forme et palette comme en T4, avec un témoin sans référence comme en T6.
2. **Édition locale avec masque** : sur `t3-salon-seed43.png`, masquer le coin gauche et la fenêtre,
   demander sapin et neige ; mesurer la part des pixels changés hors du masque (T5 : 46 %, T6 : 93 %).
3. **Scène continue avec zone de texte** : refaire T3 ; vérifier que le mur droit appartient à la pièce
   (plinthe et sol continus, pas de coupure verticale).
4. **Fond** : refaire T1 ; mesurer l'écart à la couleur demandée, l'ombre et les franges ; tester la
   sortie transparente si le fournisseur la propose ⚠️ à vérifier dans sa documentation.
5. **Rendu gouache** : refaire T2 et T3 sur fond clair ; vérifier l'absence de lavis et de dégradé.
6. **Coût et temps** par image, relevés à chaque appel.

## Chiffres

### Mesurés
| Chiffre | Statut |
|---|---|
| 52,5 à 59,6 s par image 1024 × 1024, modèle chargé (18 images) | mesuré le 02/11 |
| 497 Ko à 1,54 Mo par PNG | mesuré le 02/11 |
| T1 : fond moyen de (10, 204, 44) à (38, 231, 70), écart à #00FF00 de 60 à 83 | mesuré le 02/11 |
| T1 : 14 à 39 % des pixels de bord teintés de vert | mesuré le 02/11 |
| T2 : tiers inférieur, 0 % des pixels à plus de 15 d'écart ; bande à 59-60 % de la hauteur | mesuré le 02/11 |
| T3 : coupure verticale à x = 504 et 509 ; zone droite de 507 à 512 px, 0 % des pixels à plus de 15 d'écart | mesuré le 02/11 |
| T4 : écart de teinte au bord des pétales de 3 à 18 selon la graine | mesuré le 02/11 |
| T5 : 64 % des pixels de la moitié gauche changés de plus de 40 ; moitié droite 0 % | mesuré le 02/11 |
| T6 : 0 pixel différent entre la sortie avec référence et le témoin sans référence | mesuré le 02/11 |
| T6 : édition du salon, 93 % de la moitié gauche changés par rapport à `t3-salon-seed43` | mesuré le 02/11 |
| Z-Image Turbo : 11,9 Go demandés, 11,3 Go disponibles | mesuré le 02/11 |

### Sourcés
| Chiffre | Source |
|---|---|
| FLUX.2 Klein 4B : 5,7 Go en fp4 ; 9B : 12 Go | source : ollama.com/x/flux2-klein/tags |
| 4B sous Apache 2.0 ; 9B sous licence non commerciale | source : help.bfl.ai |
| Génération d'images retirée à partir d'Ollama 0.32.6 | source : issue ollama#17893 |

## Caveats
- Un seul modèle, en quantification fp4 ; la version fp8 (9,5 Go) n'a pas été testée.
- Deux à cinq graines par test : assez pour voir une instabilité, pas pour la chiffrer.
- Prompts en anglais, sans prompt négatif séparé (Ollama ne l'expose pas par l'API utilisée).
- Mesures par script maison (seuils de couleur choisis à la main) ; elles comparent les images entre
  elles, elles ne valent pas un contrôle d'impression.
- Trois appels sur une vingtaine ont dépassé le délai de 4 minutes de Claude Desktop alors que la
  génération avait pris moins d'une minute ; cause non trouvée.
- T6 passe par un script hors connecteur ; l'édition par la ligne de commande d'Ollama n'a pas été testée.
- Le rendu « gouache » n'a été jugé qu'à l'écran, pas imprimé.

## Retenu / écarté
Revue du 02/11/2026 avec Antoine.

**Retenu**
- Ollama et FLUX.2 Klein 4B comme banc de calibration gratuit : tester la mécanique d'un prompt
  (élément isolé, zone vide, cadrage) avant de payer un appel Nano Banana Pro.
- La méthode de mesure au pixel (couleur et dispersion du fond, lignes de rupture, différence entre
  images) comme contrôle réutilisable sur les sorties des modèles payants.
- Le constat qu'un modèle sans référence de style ne donne pas six symboles cohérents : la cohérence
  vient d'une référence ou du code (dupliquer, recolorer), jamais de la graine.

**Écarté**
- Ollama comme fournisseur derrière l'interface d'images : version figée en 0.32.5, pas de référence,
  pas d'édition, pas de masque. Inscrit dans la décision 06 comme troisième voie écartée.
- Z-Image Turbo : ne tient pas sur 16 Go.
- La scène d'un bloc avec ce modèle : page collée, hors gouache, redessinée à chaque variante.

**Conséquence**
- Une ligne dans [[06 - LangGraph au départ, interface d'images interne avec Nano Banana Pro et Ideogram]].
- Les tests à lancer listés ci-dessus sont couverts par
  [[RCH - Capacités des modèles d'images pour les calques (02-11-2026)]].