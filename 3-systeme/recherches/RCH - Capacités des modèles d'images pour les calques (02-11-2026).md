---
type: research
title: RCH - Capacités des modèles d'images pour les calques (02-11-2026)
status: validé
related: ["[[14 - Brief visuel, deux gabarits de design déclinés par titre et par occasion, rendu peint aux formes franches]]", "[[RCH - Génération d'images pour l'impression (22-10-2026)]]", "[[RCH - Images IA, modèles et plateformes (29-10-2026)]]", "[[A VERIFIER - Points à valider, vérifier, tester]]"]
decisions: ["[[06 - LangGraph au départ, interface d'images interne avec Nano Banana Pro et Ideogram]]", "[[14 - Brief visuel, deux gabarits de design déclinés par titre et par occasion, rendu peint aux formes franches]]"]
date: 2026-11-02
sources:
  - https://ai.google.dev/gemini-api/docs/generate-content/image-generation
  - https://ai.google.dev/gemini-api/docs/pricing
  - https://ai.google.dev/gemini-api/docs/rate-limits
  - https://ai.google.dev/gemini-api/docs/deprecations
  - https://docs.cloud.google.com/vertex-ai/generative-ai/docs/models/gemini/3-pro-image
  - https://discuss.ai.google.dev/t/how-can-i-make-the-background-transparent/111698
  - https://discuss.ai.google.dev/t/nano-banana-pro-image-quality/134922
  - https://discuss.ai.google.dev/t/nano-banana-pro-unnecessary-centers-image/126945
  - https://discuss.ai.google.dev/t/gemini-3-pro-image-batch-api-returns-up-to-35-billed-images-for-single-image-requests-since-8-oct-2026/196940
  - https://github.com/MegaTroll222/edit-drift/pull/1
  - https://help.apiyi.com/en/nano-banana-edit-red-cast-troubleshooting-en.html
  - https://developer.ideogram.ai/api-reference/images/generate/ideogram-4-5
  - https://developer.ideogram.ai/api-reference/images/precise-edit/ideogram-4-5
  - https://developer.ideogram.ai/api-reference/generate-images/generate-transparent-v4
  - https://developer.ideogram.ai/api-reference/api-reference/generate-v3
  - https://developer.ideogram.ai/api-reference/images/inpaint/ideogram-3
  - https://developer.ideogram.ai/ideogram-api/api-overview/llms.txt
  - https://docs.ideogram.ai/create/models
  - https://ideogram.ai/models/4.5/
  - https://ideogram.ai/features/background-remover/api/
  - https://vidmuse.ai/blog/ideogram-4-5-review
  - https://docs.bfl.ai/api-reference/utility/generate-an-image-with-flux-3
  - https://docs.bfl.ai/flux_3/flux3_image_bounding_boxes
  - https://docs.bfl.ai/flux_tools/flux_1_fill
  - https://docs.bfl.ai/quick_start/pricing
  - https://docs.bfl.ml/quick_start/generating_images
  - https://kingy.ai/blog/flux-3-image-specs-benchmarks-comparison/
  - https://www.virse.ai/blog/nano-banana-2-1-prompt-guide
last-verified: 2026-11-02
tags: [dropshipping, systeme, generation-images]
---
# RCH - Capacités des modèles d'images pour les calques (02-11-2026)

## Contexte posé
La décision 14 fixe deux gabarits. Le premier est « un symbole par prénom » : un calque de symboles,
une variante par nombre de prénoms (1 à 6), un symbole de Noël qui remplace le symbole de base. Le
second est « scène fixe à zone de texte » : une scène, une zone de prénoms vide, un calque de décor
hivernal. Le rendu est la gouache aux formes franches, sans détail sous 1 mm à 85 mm de large.
Le texte est posé par le code (décision 13).

Question posée : que savent faire Nano Banana Pro et Ideogram, avec FLUX en témoin, en novembre 2026 ?
Sept capacités : fond transparent, image de référence, édition locale, zone vide, élément isolé en
gouache, variante contrôlée d'une scène, résolution, formats, coût et débit. Documentation officielle
d'abord, puis retours d'usage datés. Conclusion attendue : pour chaque gabarit, « éléments séparés
composés par code » ou « scène d'un bloc avec zone masquée », et avec quel modèle.

Recherche menée avec le mode recherche avancée de claude.ai, le 02/11/2026. Aucune API n'a été appelée.
Les tests réels sont des scripts à lancer par Antoine (section « Tests à lancer »). Prompt complet dans
la conversation claude.ai du 02/11/2026.

## Conclusion en une phrase
Les tests du 02/11/2026 désignent Nano Banana Pro par défaut pour les deux gabarits : il tient le mieux
la gouache aux formes franches, respecte la zone vide et ne change rien de visible hors de la zone
éditée ; Ideogram 4.5 reste le seul à sortir un fond transparent natif, et son Precise Edit préserve
presque tous les pixels hors masque mais déborde quand l'objet remplacé dépasse du masque.

## Résultats

### Ce qui change par rapport aux recherches précédentes
- **Identifiant Google.** `gemini-3-pro-image-preview` a une date d'arrêt annoncée au 25/06/2026, « au
  plus tôt ». Son remplaçant est `gemini-3-pro-image`, disponible en version stable (GA, « general
  availability ») depuis le 28/05/2026. Nano Banana 2 est remplacé par `gemini-nano-banana-2.1`, stable
  depuis le 06/10/2026. source : ai.google.dev/gemini-api/docs/deprecations, lu le 02/11/2026.
- **Prix d'Ideogram 4.5.** Le prix officiel ne dépend pas de la résolution. Le « 0,22 USD » relevé chez
  fal.ai ne vaut que pour la qualité haute avec images de référence, ou pour Precise Edit.
  source : ideogram.ai/models/4.5.
- **La résolution n'est pas un facteur limitant.** 85 mm à 300 DPI font environ 1 004 px. Une sortie 1K
  suffit pour le bois. Le 2K sert pour le tour du mug. estimé.

### Capacité 1 — Fond transparent natif, ou fond uni à détourer
| Modèle | Réponse | Source | Date |
|---|---|---|---|
| Nano Banana Pro et 2.1 | Non. La doc dit que le modèle ne génère pas de fond transparent, et conseille un fond blanc. | doc Gemini, génération d'images | mise à jour 26/10/2026 |
| Nano Banana Pro | Si on demande un fond transparent, il dessine un damier. | forum Google AI | 11/12/2025 |
| Ideogram 4.5 | Oui. `background=transparent` renvoie une image avec canal alpha. Le canal alpha est la couche qui code la transparence de chaque pixel. | doc API Ideogram 4.5 | non datée, lue le 02/11/2026 |
| Ideogram 4.0 et 3.0 | Oui, par des endpoints dédiés `generate-transparent`. Ces endpoints ne prennent pas d'image de référence. | doc API Ideogram ; docs.ideogram.ai | non datées |
| Ideogram (détourage) | Endpoint `remove-background`, PNG transparent, 0,01 USD. Meilleur que BiRefNet selon Ideogram, non vérifié ⚠️. | page produit Ideogram | non datée |
| FLUX 3 Image | Non documenté. Le schéma n'a ni paramètre de fond ni format de sortie. ⚠️ | doc BFL (OpenAPI) | non datée |

### Capacité 2 — Image de référence pour tenir un style
| Modèle | Réponse | Source | Date |
|---|---|---|---|
| Nano Banana Pro | Jusqu'à 14 images : 6 objets, 5 personnages, **3 références de style**. Aucune mesure de cohérence publiée. | doc Gemini | mise à jour 26/10/2026 |
| Nano Banana 2.1 | 10 objets et 4 personnages, aucune référence de style. | doc Gemini | mise à jour 26/10/2026 |
| Ideogram 3.0 | Seul modèle Ideogram avec références de style (`style_reference_images`, jusqu'à 10), codes de style réutilisables (`style_codes`) et presets. | docs.ideogram.ai ; doc API v3 | non datées |
| Ideogram 4.5 | Champ `images`, 5 au plus : la première est éditée, les autres servent de référence. Ce n'est pas une « référence de style » au sens de la 3.0. | doc API Ideogram 4.5 | non datée |
| FLUX 3 Image | 1 à 10 images de référence ; transfert de style documenté. | doc BFL ; Kingy | Kingy : 22/10/2026 |

### Capacité 3 — Édition locale sans redessiner le reste
L'inpainting est la retouche d'une zone précise, désignée par un masque. Un masque est une image noir et
blanc de même taille qui dit quelle zone modifier.

| Modèle | Réponse | Source | Date |
|---|---|---|---|
| Nano Banana Pro | Pas de masque. Édition par instruction en langage naturel, sans garantie de préservation. | doc Gemini | mise à jour 26/10/2026 |
| Nano Banana Pro | Chaque nouvelle demande dégrade ce qui n'était pas visé, selon un utilisateur. | forum Google AI | date ⚠️ non relevée |
| Nano Banana 2.1 | Sur 40 éditions successives, le mode conversation ne réduit pas la dérive. | GitHub, edit-drift | 08/10/2026 |
| Ideogram 4.5 Precise Edit | Masque explicite : **noir = zone à modifier**, blanc = zone gardée. La doc dit que les pixels non modifiés sont recopiés à l'identique. `context_window` limite le calcul à la zone. | doc API Precise Edit | non datée |
| Ideogram 4.5 | Revue indépendante : prometteur, bords à inspecter. | vidmuse.ai | date ⚠️ |
| FLUX 3 Image | Édition par boîtes sur une grille de 0 à 1000. Le lancement parle de pixels identiques hors boîte, le tutoriel dit « en général identiques ». | doc BFL ; presse | presse : 10/2026 |
| FLUX.1 Fill | Masque inverse : **blanc = zone à repeindre**. | doc BFL | non datée |

### Capacité 4 — Respect d'une zone laissée vide
| Modèle | Réponse | Source | Date |
|---|---|---|---|
| Nano Banana Pro | Par prompt seul, aucune garantie. Un utilisateur rapporte que le modèle recentre ce qu'il remplit. | forum Google AI | date ⚠️ |
| Ideogram 4.5 | Pas de zone réservée à la génération. On repeint la zone après coup par masque. | doc API Ideogram 4.5 | non datée |
| FLUX 3 Image | Meilleur contrôle documenté : chaque élément est placé par une boîte. Un élément peut déborder un peu de sa boîte. | doc BFL, boîtes englobantes | non datée |
| FLUX 3 Image | 28 générations sur 32 passent les quatre contrôles d'un test automatisé. Petit échantillon. | Kingy | 22/10/2026 |

### Capacité 5 — Élément isolé en gouache, sur fond uni
| Modèle | Réponse | Source | Date |
|---|---|---|---|
| Nano Banana Pro | Icônes et stickers sur fond blanc documentés. Aucun style « gouache » prévu. Bords, ombres et texture papier ⚠️ non documentés. | doc Gemini | mise à jour 26/10/2026 |
| Ideogram 4.5 | Sortie transparente native, donc pas de fond à détourer. `magic_prompt=off` garde les termes de style tels quels. Pas de preset de style. | doc API Ideogram 4.5 | non datée |
| Ideogram 3.0 | `style_type` et `style_preset` existent. Preset proche de la gouache ⚠️ non vérifié. | doc API v3 | non datée |
| FLUX 3 Image | Esthétiques peintes dans les exemples officiels. Un exemple ajoute exprès une texture papier, ce qui confirme le risque. | doc BFL | non datée |

### Capacité 6 — Variante contrôlée d'une scène (fenêtre enneigée)
| Modèle | Réponse | Source | Date |
|---|---|---|---|
| Nano Banana Pro | Édition en plusieurs tours, sans garantie sur le reste de l'image. | doc Gemini | mise à jour 26/10/2026 |
| Nano Banana | La dérive de couleur s'accumule d'une édition à l'autre. | blog APIYI | date ⚠️ |
| Ideogram 4.5 | Precise Edit avec masque et `context_window` : la combinaison la mieux garantie. Remix redessine toute l'image, donc à éviter. | doc API Precise Edit | non datée |
| FLUX 3 Image | On garde les boîtes des éléments conservés et on ajoute une boîte pour le nouvel élément. Moins de dérive hors zone que Nano Banana 2.1 sur un banc de 40 éditions. | doc BFL ; virse.ai | virse : date ⚠️ |

### Capacité 7 — Résolution, formats, coût, débit
| Modèle | Réponse | Source | Date |
|---|---|---|---|
| Nano Banana Pro | 1K, 2K, 4K. Rapports d'aspect de 1:8 à 8:1, dont 1:1, 4:5, 16:9, 21:9. Stable depuis le 28/05/2026. | doc Vertex AI | lue le 02/11/2026 |
| Nano Banana Pro | Format : PNG dans les exemples. Liste officielle des formats ⚠️ absente. | doc Gemini | mise à jour 26/10/2026 |
| Nano Banana Pro | Débit par minute non publié, visible seulement dans AI Studio. Plafond de dépense par fenêtre de 10 minutes : 10, 50 ou 200 USD selon le palier. | doc limites de débit | mise à jour 28/10/2026 |
| Nano Banana Pro | Bug du mode batch : jusqu'à 35 images facturées pour une demande d'une image, depuis le 08/10/2026. | forum Google AI | 10/2026 |
| Ideogram 4.5 | 2048 × 2048 px au plus, rapport jusqu'à 6:1. Precise Edit accepte une image d'entrée jusqu'à 8192 × 8192. | page modèle et doc API | non datées |
| Ideogram | 10 requêtes en cours par défaut. Mode asynchrone et paramètre `dry_run` pour un devis sans facturation. | doc API Ideogram | non datée |
| FLUX 3 Image | De 768 px à 4K, largeur et hauteur libres de 256 à 6256 px. Appel asynchrone. 24 tâches actives au plus. | doc BFL | non datée |

### Paramètres d'API utiles aux scripts
- **Gemini** : modèle `gemini-3-pro-image` ; `response_modalities=["TEXT","IMAGE"]` ; `image_config` avec
  `aspect_ratio` et `image_size` (`"1K"`, `"2K"`, `"4K"`). Les références passent dans `contents`.
  L'édition en plusieurs tours passe par `client.chats.create`. La doc classe `generateContent` en
  « Legacy » et met en avant une Interactions API ⚠️ à confirmer selon la version du SDK.
- **Ideogram 4.5** : `POST https://api.ideogram.ai/v2/image/generate/ideogram-4-5`, en-tête `Api-Key`,
  formulaire multipart. Champs `prompt`, `magic_prompt`, `images`, `mask`, `size`, `background`,
  `quality`, `seed`, `num_images`.
- **Ideogram 4.5 Precise Edit** : `POST https://api.ideogram.ai/v2/image/precise-edit/ideogram-4-5`.
  Champs `image`, `prompt`, `mask`, `reference_images`, `context_window`, `quality`, `seed`.
- **Ideogram 3.0** : `POST https://api.ideogram.ai/v1/ideogram-v3/generate`. Champs `prompt`,
  `rendering_speed`, `style_type`, `style_reference_images`, `aspect_ratio` (format `1x1`).
- **FLUX 3 Image** : `POST https://api.bfl.ai/v1/flux-3-image`, en-tête `x-key`. Boîtes en JSON à la fin
  du prompt. Pas de `seed` ni de format de sortie. `grounding=false` pour des tests reproductibles.

### Recommandation par gabarit

**Un symbole par prénom : éléments séparés composés par code, réaliste.**
- Garanti par la doc : Ideogram 4.5 sort un PNG transparent et accepte un symbole maître en image
  source. Nano Banana Pro accepte 3 références de style, mais demande un fond uni et un détourage.
- À dire par les tests : propreté des bords transparents, absence d'ombre et de texture papier, tenue
  du style du symbole maître vers les autres symboles, aucun détail sous 12 px à 1 004 px. ⚠️
- Modèle pressenti : Ideogram 4.5. Témoin : Nano Banana Pro, fond uni, puis détourage.
- Les variantes de 1 à 6 prénoms et le symbole de Noël sont des changements de calque faits par le code.

**Scène fixe à zone de texte : scène d'un bloc avec zone réservée, réaliste.**
- Garanti par la doc : FLUX 3 place les éléments par boîtes. Ideogram 4.5 Precise Edit repeint une zone
  masquée et recopie le reste. Nano Banana Pro ne garantit ni l'un ni l'autre.
- À dire par les tests : respect de la zone vide, et différence de pixels nulle hors masque après
  l'ajout de la fenêtre enneigée. ⚠️
- Repli par code : recoller la zone masquée éditée sur l'image d'origine. La dérive hors zone devient
  impossible par construction.
- Modèle pressenti : Ideogram 4.5 pour la scène et l'hiver. FLUX 3 reste le meilleur pour la zone vide
  selon la doc, mais il n'est pas testé ici, faute de clé. ⚠️
- À écarter pour ce gabarit : l'édition en plusieurs tours de Nano Banana. Les retours datés montrent
  une dérive, et la doc ne promet rien.

## Tests à lancer
Scripts dans `3-systeme/recherches/tests-images/`, avec un module `commun.py` partagé (clés, style,
appels, masques, mesures). Chaque script lit sa clé dans `GEMINI_API_KEY` ou `IDEOGRAM_API_KEY`, ne
l'écrit nulle part, saute un modèle si sa clé manque, et écrit ses images et un journal
`<script>.json` (prompt, paramètres, durée, erreur, réponse sans les URL) dans `tests-images/sorties/`.
FLUX n'est pas testé, faute de clé.

Installation : `pip install google-genai requests pillow numpy`. Lancement depuis le dossier
`tests-images/` : `python test_1_transparence.py`, et ainsi de suite.

Style commun à tous les prompts : « gouache illustration, opaque pigment, no wash, closed contours,
medium to saturated colors, bold simple shapes, no fine detail, no drop shadow, no paper texture ».

| Script | Modèles | Prompt (résumé) | Paramètres | Fichiers attendus | Ce qu'on regarde |
|---|---|---|---|---|---|
| `test_1_transparence.py` | Nano Banana Pro, Ideogram 4.5 | une fleur seule, fond transparent | NB : `1K`, `1:1` ; Ideogram : `background=transparent`, `quality=medium`, 1024 px | `1_transparence_nbpro.png`, `1_transparence_ideo45.png` | canal alpha réel ou damier dessiné (mesuré par le script) |
| `test_2_reference.py` | Nano Banana Pro, Ideogram 4.5 | à partir de `1_transparence_ideo45.png`, un cœur, un oiseau, une boule, une étoile dans le même style | NB : maître en référence, fond blanc ; Ideogram : maître dans `images`, `quality=high`, transparent puis `auto` si refusé | `2_ref_<symbole>_nbpro.png`, `2_ref_<symbole>_ideo45.png` (4 × 2) | tenue de la palette et du trait |
| `test_6_variante.py` | Nano Banana Pro, Ideogram 4.5 | salon familial, puis ajout d'une fenêtre enneigée en haut à droite | NB : 2 tours de conversation, `4:3`, `2K` ; Ideogram : 1536 × 1152, `seed=4242`, puis Precise Edit, masque sur le coin, `context_window=auto` | `6_scene_base_*.png`, `6_hiver_*.png`, `6_diff_*.png` | écart hors masque (mesuré), dérive de couleur |
| `test_3_edition_locale.py` | Nano Banana Pro, Ideogram 4.5 | dans la scène du test 6, remplacer le vase par une théière | NB : instruction seule ; Ideogram : Precise Edit, masque généré par le script | `3_edit_*.png`, `3_masque.png`, `3_diff_*.png` | écart hors masque (mesuré) ; ajuster la zone du vase si besoin |
| `test_4_zone_vide.py` | Nano Banana Pro, Ideogram 4.5 | salon familial, tiers inférieur en aplat crème uni | NB : prompt seul, `3:4`, `2K` ; Ideogram : prompt seul, puis Precise Edit de la zone | `4_zone_nbpro.png`, `4_zone_ideo45.png`, `4_zone_ideo45_masque.png` | écart type des couleurs dans la zone (mesuré) |
| `test_5_element_isole.py` | Nano Banana Pro, Ideogram 4.5 | une boule de Noël seule, centrée, fond blanc uni | NB : `1K` ; Ideogram : `background=opaque` puis `transparent` | `5_boule_nbpro.png`, `5_boule_ideo45_opaque.png`, `5_boule_ideo45_transp.png` | ombre portée, texture du fond (mesurée sur les bords), netteté des bords |
| `test_7_formats.py` | aucun appel | lit les sorties et les journaux précédents | — | `7_rapport.json` | format réel, dimensions, profil couleur, durée, coût annoncé, erreurs |

L'ordre de lancement compte : 1, puis 2, puis 6, puis 3, 4, 5 et 7. Coût total estimé : moins de 5 USD.
Le format exact de la réponse Ideogram n'est pas vérifié : le script cherche la première URL d'image
et journalise la réponse brute. ⚠️

### Résultats des tests
Lancés le 02/11/2026 entre 16 h 50 et 17 h, depuis `tests-images/`. 19 appels, 3 échecs. Un seul
essai par cas : ce sont des indices, pas des mesures stables. ⚠️
Mesures tirées des journaux `sorties/*.json` et `7_rapport.json`, complétées par une lecture des
images et des mesures du canal alpha faites lors de la seconde passe.

#### Scripts en échec
| Script | Appel | Erreur | Cause |
|---|---|---|---|
| `test_1_transparence.py` | Nano Banana Pro | `'NoneType' object is not iterable` | réponse sans image. Au premier essai, le même appel avait réussi. Cause ⚠️ inconnue : le script ne journalise pas le motif d'arrêt du modèle. |
| `test_6_variante.py` | Ideogram 4.5, scène de base | HTTP 400 : « this resolution is not supported by the model » | taille `1536x1152` refusée |
| `test_4_zone_vide.py` | Ideogram 4.5, scène | HTTP 400, même message | taille `1152x1536` refusée |

Conséquence : `test_3` et `test_6` n'ont pas de scène Ideogram, et Precise Edit n'a jamais été appelé.
La doc lue indiquait des tailles libres, multiples de 32. Les tailles acceptées sont en fait limitées
à une liste ⚠️ non relevée. Seul `1024x1024` est confirmé.
Un premier essai avait aussi échoué en HTTP 415 : le script envoyait un formulaire simple au lieu de
`multipart/form-data`. C'est corrigé dans `commun.py`.
Second essai à 17 h, après passage des scènes Ideogram en `1024x1024` : les trois scripts concernés ont
réussi, sans aucune erreur.

#### Capacité 1 — Fond transparent
- Nano Banana Pro : sortie JPEG, sans canal alpha, aucun pixel transparent (premier essai). Le fond
  transparent demandé n'est pas produit. La doc est confirmée.
- Ideogram 4.5 : PNG RGBA, 76,5 % de fond à alpha 0. Les bords sont propres : moins de 2 % des pixels
  de l'objet ont un alpha sous 128. Défaut mesuré : **l'intérieur de l'objet n'est pas opaque**. Son alpha
  médian vaut de 246 à 251 au lieu de 255, donc la couleur du support transparaît légèrement. Correction
  simple par code : forcer à 255 tout alpha supérieur ou égal à 128.

#### Capacité 2 — Référence de style (maître : la fleur Ideogram)
- Ideogram 4.5 : palette tenue sur les quatre symboles (rouge, ocre, vert de gris). Le rendu est doux,
  presque délavé, avec des taches de pinceau internes et peu de contours. Les durées vont de 30 à 133 s
  par image.
- Nano Banana Pro : palette reprise, mais plus saturée. Le modèle ajoute des contours sombres, des
  aplats opaques, et reprend le cœur ocre de la fleur dans l'étoile. Le rendu est plus proche du brief
  « formes franches ». Fond blanc. Durée d'environ 15 s par image.
- Petits détails sous le seuil d'1 mm à 85 mm : l'œil de l'oiseau Ideogram, et les pattes de l'oiseau
  Nano Banana. À surveiller dès que le symbole est plus petit que la pièce entière. ⚠️

#### Capacité 3 — Édition locale (vase remplacé par une théière)
- Nano Banana Pro, instruction seule, sans masque : la théière prend la place exacte du vase, et le
  reste de la scène est inchangé à l'œil. Hors d'une zone élargie autour du vase : écart moyen de 4,2
  sur 255, 5,1 % des pixels changés de plus de 8, et 0,04 % de plus de 40. Ce bruit faible suit les
  contours : c'est du ré-encodage JPEG et de la régénération légère, pas une modification visible.
- Ideogram 4.5 Precise Edit : non testé au premier essai ; testé au second essai, voir plus bas.

#### Capacité 4 — Zone laissée vide (tiers inférieur demandé)
- Nano Banana Pro, prompt seul : la zone est respectée, mais plus petite que demandé. L'aplat crème
  commence à 75 % de la hauteur au lieu de 67 %. Dans cet aplat, l'écart type des couleurs vaut 1,08,
  donc un aplat parfaitement uni. La mesure du script (69,9) incluait le bas de la scène.
- Ideogram 4.5 : non testé au premier essai ; testé au second essai, voir plus bas.

#### Capacité 5 — Élément isolé (boule de Noël)
- Nano Banana Pro : boule pleine page, contours sombres épais, aplats saturés, fond blanc pur. C'est
  le rendu le plus proche du brief. L'écart type du fond (10,1) vient de la boule qui touche les bords
  de la zone mesurée, pas d'une texture.
- Ideogram 4.5 opaque : petite boule (8 % de l'image) sur un fond blanc cassé très uni (écart type
  0,62). Un reflet brillant contredit l'aplat de gouache. Aucune ombre portée.
- Ideogram 4.5 transparent : même boule, bords propres, intérieur à alpha d'environ 251 (même défaut
  qu'en capacité 1).

#### Capacité 6 — Variante hivernale (fenêtre enneigée)
- Nano Banana Pro, deuxième tour de conversation : fenêtre ajoutée en haut à droite, composition,
  personnages et couleurs conservés. Hors du quart haut droit : écart moyen de 4,4 sur 255, 5,4 % des
  pixels changés de plus de 8, 0,09 % de plus de 40. La mesure du script (8,44) était gonflée par la
  fenêtre, plus large que le masque dessiné.
- Ideogram 4.5 Precise Edit : non testé au premier essai ; testé au second essai, voir plus bas.

#### Capacité 7 — Formats, résolution, durée, coût
| Mesure | Nano Banana Pro | Ideogram 4.5 |
|---|---|---|
| Format réel | JPEG, même avec un nom de fichier en `.png` | PNG, RGBA si transparent, RGB sinon |
| Taille obtenue | 1K : 1024 × 1024 ; 2K en 4:3 : 2400 × 1792, marqué 300 DPI | 1024 × 1024 |
| Tailles refusées | aucune | 1536 × 1152 et 1152 × 1536 |
| Durée par appel | 14 à 24 s | 10 à 46 s, et un appel à 133 s |
| Coût annoncé dans la réponse | aucun | aucun champ de coût trouvé ⚠️ |
| Limite de débit atteinte | non | non |

2400 × 1792 px à 300 DPI couvrent 203 × 152 mm : assez pour le tour d'un mug.

#### Second essai (17 h) : scènes Ideogram et nouvelles scènes Nano Banana Pro
Scènes Ideogram en 1024 × 1024, scènes Nano Banana Pro en 2K. Les deux modèles ont régénéré leurs
scènes : ce ne sont pas les mêmes images qu'au premier essai.

| Test | Nano Banana Pro | Ideogram 4.5 |
|---|---|---|
| Variante hivernale, hors zone | écart moyen de 5,1 sur 255 ; 13,8 % des pixels changés de plus de 8 ; 0,15 % de plus de 40 | écart moyen de 0,13 ; 87 % des pixels strictement identiques ; 0,01 % changés de plus de 40 |
| Théière, hors zone | écart moyen de 5,1 ; 10,2 % de plus de 8 ; 0,56 % de plus de 40 | écart moyen de 2,45 ; 2,2 % de plus de 40, dont les tulipes effacées au-dessus du masque |
| Zone vide (tiers inférieur) | scène arrêtée à 64,6 % de la hauteur ; aplat sous la scène à écart type 1,33 | scène arrêtée à 64,7 % ; aplat à écart type 0,92 sur le tiers inférieur |
| Durée | 20 à 25 s | 80,8 s pour la fenêtre, en Precise Edit |

Lecture des images :
- **Precise Edit garde le reste de l'image.** La fenêtre enneigée s'ajoute sans toucher aux
  personnages. Mais pour la théière, le modèle a aussi effacé les tulipes, qui dépassaient du masque :
  29 % des changements nets sont hors masque. Le changement est logique, mais la promesse « hors masque,
  rien ne bouge » ne tient que si **le masque couvre tout l'objet remplacé**. Le recollage par code
  suppose la même règle, sinon il laisserait des demi-tulipes.
- **Style des scènes Ideogram : hors brief.** Grain de papier visible, trait de crayon, aplats doux,
  malgré « no paper texture » dans le prompt. Le prompt réécrit par Ideogram dans sa réponse décrit
  lui-même ce style : grain de papier, crayon de couleur. Taille limitée à 1024 px dans ce test.
- **Nano Banana Pro, deux essais sur deux.** Zone vide respectée, et cette fois à la bonne hauteur.
  Éditions invisibles hors zone. Le bruit faible sur toute l'image vient du JPEG, et le recollage par
  code l'annule. Les scènes restent en gouache opaque à contours francs. Défaut vu : la scène du test 4
  est chargée de petits détails (livres, cubes, cadres), contraires à « no fine detail ». ⚠️
- Dans le test 4, la zone repeinte par Precise Edit est identique à la zone d'origine, déjà unie.

#### Fournisseur par défaut de l'interface
| Gabarit | Par défaut | Pourquoi | Ce qui reste à tester |
|---|---|---|---|
| Un symbole par prénom | **Nano Banana Pro**, fond blanc, puis détourage (provisoire) | rendu le plus fidèle au brief : aplats opaques, contours, couleurs soutenues | qualité du détourage d'un JPEG (BiRefNet ou `remove-background` d'Ideogram) ⚠️ ; si elle déçoit, Ideogram 4.5 transparent avec correction de l'alpha |
| Scène fixe à zone de texte | **Nano Banana Pro** | gouache conforme au brief, zone vide respectée deux fois sur deux, éditions invisibles hors zone | variante hivernale : recollage par code de la zone éditée, avec un masque qui couvre tout l'objet ; piste hybride : Precise Edit d'Ideogram appliqué à une scène Nano Banana Pro ⚠️ non testée ; densité de détails à contraindre ⚠️ |

Ces résultats contredisent la recommandation tirée de la doc seule. Nano Banana Pro n'offre aucune
garantie de préservation, mais il s'est bien comporté sur deux essais. Ideogram préserve mieux les
pixels, mais dessine hors brief. Deux essais ne prouvent pas la stabilité : à confirmer sur plusieurs
scènes avant la production. ⚠️

## Chiffres

### Sourcés
| Chiffre | Source |
|---|---|
| Nano Banana Pro : 0,134 USD en 1K ou 2K, 0,24 USD en 4K ; batch 0,067 et 0,12 USD | source : ai.google.dev/pricing, lu le 02/11/2026 |
| Nano Banana 2.1 : 0,0336 / 0,0504 / 0,113 USD (1K / 2K / 4K) ; batch à moitié prix | source : ai.google.dev/pricing, lu le 02/11/2026 |
| Gemini : plafond de dépense de 10, 50 ou 200 USD par fenêtre de 10 minutes (paliers 1, 2, 3) | source : ai.google.dev/rate-limits, mis à jour le 28/10/2026 |
| Ideogram 4.5 : 0,03 / 0,06 / 0,10 USD (prompt seul) ; 0,22 USD (références ou Precise Edit) ; 0,008 USD (`very_low` avec image source) | source : ideogram.ai/models/4.5 |
| Ideogram : détourage à 0,01 USD par image | source : ideogram.ai, page détourage |
| Ideogram : 10 requêtes en cours par défaut | source : doc API Ideogram |
| FLUX 3 Image : 0,041 / 0,048 / 0,070 / 0,100 / 0,607 USD (768 px, 1k, 1.5k, 2k, 4k) | source : doc BFL ; Kingy, 22/10/2026 |
| FLUX : 24 tâches actives au plus | source : docs.bfl.ml |

### Estimés
| Chiffre | Statut |
|---|---|
| 85 mm à 300 DPI : environ 1 004 px ; 1 mm : environ 12 px | estimé (calcul : mm ÷ 25,4 × 300) |
| Palier 1 Gemini : environ 74 images Nano Banana Pro par fenêtre de 10 minutes (10 ÷ 0,134) | estimé |
| Catalogue du symbole par prénom : 5 symboles × 2 saisons × 8 essais en Ideogram 4.5 avec références, environ 17,60 USD | estimé |
| Scène fixe : 3 scènes × 10 essais en FLUX 3 2k plus 15 éditions Precise Edit, environ 6,30 USD | estimé |
| Le coût des appels est marginal ; le coût réel est le temps de revue humaine | estimé |

## Caveats

Contradictions entre sources, non tranchées :
- Arrêt de `gemini-3-pro-image-preview` au 25/06/2026 selon Google, mais l'identifiant est encore
  documenté chez fal.ai, Helicone et GMI Cloud.
- Jetons d'une image 4K de Nano Banana 2.1 : 3 780 (page des prix) ou 2 520 (guide), comme déjà noté le
  22/10.
- Mode Flex de Nano Banana Pro : prix affiché, mais « non pris en charge » sur la fiche du modèle.
- Prix d'Ideogram 4.5 : officiel 0,03 / 0,06 / 0,10 ; fal.ai 0,03 / 0,06 / 0,22 ; Segmind 0,0375 /
  0,075 / 0,125 ; Venice 0,04 / 0,07 / 0,26 ; Picsart 0,033 / 0,066 / 0,22.
- Prix d'Ideogram 4.0 : 0,03 / 0,06 / 0,10 (usagepricing, 15/06/2026) ou 0,03 / 0,075 / 0,09 (apis.io,
  mai 2026).
- Détourage Ideogram : 0,01 USD sur la page produit, mais retiré de la grille après le 31/05/2026 selon
  usagepricing.
- Taille maximale d'un fichier en Precise Edit : 50 Mo ou 25 Mo selon deux versions de la même doc.
- `safety_tolerance` de FLUX 3 : de 0 à 4 ou de 0 à 7 selon deux pages BFL.
- Préservation chez FLUX 3 : « pixels identiques » au lancement, « en général identiques » dans le
  tutoriel.
- Validité des liens de résultat BFL : 10 minutes (doc générale) ou une heure (Kingy, pour FLUX 3).

Non vérifié :
- Débit par minute réel de `gemini-3-pro-image`. ⚠️
- Formats de sortie de Gemini et de FLUX 3. ⚠️
- Combinaison de `background=transparent` avec une image source sur Ideogram 4.5. ⚠️
- Propreté des bords transparents d'Ideogram 4.5 sur de la gouache. ⚠️
- Liste des presets de style d'Ideogram 3.0. ⚠️
- Suivi d'une image de mise en page par Nano Banana Pro. ⚠️
- Dates de plusieurs retours d'usage (deux fils du forum Google, blogs virse et APIYI). ⚠️

Ce que cette recherche ne couvre pas :
- FLUX n'est pas testé, faute de clé. Ses lignes reposent sur la doc seule.
- Le rendu imprimé sur bois, verre et mug relève de la commande test du 5 novembre (décision 14).

## Retenu / écarté
Revue du 02/11/2026 avec Antoine.

**Retenu**
- Nano Banana Pro par défaut pour les deux gabarits de la décision 14 : rendu conforme au brief
  (gouache opaque, contours francs), zone vide respectée deux fois sur deux, éditions invisibles hors
  zone sur deux essais. La décision 06 est confirmée sans changement.
- Recollage par code de la zone éditée sur l'image d'origine, pour annuler le bruit JPEG et rendre la
  dérive hors zone impossible par construction.
- Ideogram 4.5 en second : seul fond transparent natif (alpha intérieur à corriger par code), Precise
  Edit qui préserve les pixels hors masque si le masque couvre tout l'objet remplacé.
- 1K pour le bois, 2K pour le tour du mug.
- Les sept scripts de `tests-images/` comme banc de test réutilisable à chaque changement de modèle.

**Écarté**
- Ideogram 4.5 pour les scènes : style hors brief (grain de papier, crayon) à 1024 px.
- FLUX 3 Image, non testé ; reste un candidat sur la doc seule.
- Toute conclusion de stabilité au-delà de deux essais.

**Inscrit au registre A VERIFIER**
- Stabilité de Nano Banana Pro sur plusieurs scènes (zone vide, préservation hors zone).
- Densité de petits détails dans les scènes, à contraindre par le prompt.
- Qualité du détourage d'un JPEG Nano Banana Pro par la chaîne de
  [[RCH - Détourage, nettoyage des bords et agrandissement pour l'impression (02-11-2026)]], avec BiRefNet sur le Mac.
