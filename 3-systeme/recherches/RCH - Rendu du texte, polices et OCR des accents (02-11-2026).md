---
type: research
title: RCH - Rendu du texte, polices et OCR des accents (02-11-2026)
status: validé
date: 2026-11-02
sources: ["tests réels, environnement Python de Claude, 02/11/2026", "changelog resvg (github.com/linebender/resvg)", "documentation CairoSVG (cairosvg.org)", "documentation Pillow ImageFont", "FAQ SIL OFL", "documentation Tesseract, Improving the quality of the output", "PP-OCRv5, CVPR 2026", "PP-OCRv6, arXiv 2606.13108", "aide Gelato, zone d'impression des mugs"]
related: ["[[CMP - Personnalisation par produit]]", "[[FLOW - Personnalisation à la commande]]", "[[SYN - Système]]", "[[A VERIFIER - Points à valider, vérifier, tester]]"]
decisions: ["[[08 - Personnalisation à la commande en génération interne, test Printify avant le 5 novembre]]", "[[10 - Notre serveur produit l'image finale, Printify la reçoit par l'API]]", "[[13 - Texte en trois champs facultatifs, couleur du texte en palette, police fixée, page blanche recadrée par la cliente]]"]
last-verified: 2026-11-02
tags: [dropshipping, systeme, personnalisation, rendu, polices, ocr, research]
---
# RCH - Rendu du texte, polices et OCR des accents (02-11-2026)

## Contexte posé
Notre serveur compose l'illustration et pose le texte : titre, prénoms jusqu'à 6, phrase. La couleur
vient d'une palette et la police est fixée par le gabarit. Il exporte un PNG sRGB à 300 DPI
([[10 - Notre serveur produit l'image finale, Printify la reçoit par l'API]],
[[13 - Texte en trois champs facultatifs, couleur du texte en palette, police fixée, page blanche recadrée par la cliente]]).

Questions posées :
1. Pillow seul, ou SVG rendu par resvg ou cairosvg ? Critères : lissage, texte en arc sur le disque
   de la boule, texte sur le tour du mug, réduction automatique, multiligne. Code minimal de chaque option.
2. Trois polices gouache ou manuscrites et une bâton, sous licence compatible avec la vente d'objets
   imprimés. Rendu de « Léa, Inès, Noé, Maëlle, Jean-François, Œuvre » à 3 mm et à 8 mm de haut.
3. OCR par PaddleOCR ou Tesseract sur ces rendus : taux de lecture exacte des accents par police.

Chiffres mesurés demandés, pas estimés. Une recherche documentaire a précédé les tests.

## Conclusion en une phrase
Rendre le texte en SVG avec resvg, mesurer et finaliser le PNG avec Pillow, écarter cairosvg ;
les quatre polices OFL testées couvrent tous les accents français et Tesseract en lit 24 à 26 sur 26,
à condition de contrôler une vignette droite de 24 à 32 px de capitale, jamais le visuel final.

## Résultats

### 1. Stack de rendu
Environnement de test (mesuré le 02/11) : Python 3.12, Pillow 12.1.1 avec libraqm active,
resvg_py 0.5.0, CairoSVG 2.9.1, fontTools 4.62.1.

**resvg (via `resvg_py`) est retenu pour le rendu.**
- Il rend le texte sans aucune frange colorée (0 pixel coloré, mesuré le 02/11).
- Il gère `textPath`, donc le texte en arc, avec crénage et accents corrects.
- Sa largeur de texte égale celle mesurée par Pillow à 1 px près sur 8 lignes de test (mesuré le 02/11).
  La réduction automatique peut donc mesurer avec Pillow et rendre avec resvg.
- Il ne lit que les polices passées par `font_files`, avec `skip_system_fonts=True` : le rendu ne
  dépend pas des polices installées sur le serveur.
- Son lissage n'utilise que 29 niveaux de gris, contre 256 pour Pillow (mesuré le 02/11). À 300 DPI,
  la différence n'est pas visible à l'écran agrandi 4 fois. Son effet à l'impression n'est pas
  mesuré ⚠️ à vérifier sur commande test.

**Pillow est retenu pour mesurer et finaliser.**
- Il mesure le texte (`getbbox`, `getlength`) pour la réduction automatique.
- Il écrit `dpi=(300, 300)` et le profil sRGB. resvg n'écrit ni l'un ni l'autre.
- Il sert de repli complet si resvg pose problème. Le texte en arc se fait alors glyphe par glyphe :
  il fonctionne et garde le crénage, mais perd les ligatures.
- libraqm est obligatoire. Sans elle, un prénom saisi en Unicode décomposé (NFD, accent séparé de
  la lettre) s'affiche mal : 4 prénoms sur 4 cassés, par exemple « Léa » lu « Le[ a ». Avec libraqm :
  4 sur 4 corrects (mesuré le 02/11). Normaliser chaque champ en NFC reste la règle.

**cairosvg est écarté.**
- Par défaut, il lisse le texte en sous-pixels RGB : 98,9 % des pixels de bord sont colorés
  (79 311 sur 80 213, mesuré le 02/11). Ces franges orange et bleues seraient imprimées.
- L'attribut `text-rendering="geometricPrecision"` supprime les franges (0 pixel coloré), mais rend
  alors le texte en arc illisible (mesuré le 02/11).
- Sa largeur de texte s'écarte jusqu'à 17 px de la mesure Pillow (mesuré le 02/11).
- Sa documentation dit elle-même que le texte et les polices sont mal gérés (source : cairosvg.org).

**Texte en arc, disque de la boule** (76,2 mm, soit 900 px à 300 DPI).
- Avec resvg, un texte plus long que le chemin est coupé aux deux bouts : « Joyeux » devient « eux »
  (mesuré le 02/11). Le gabarit doit donc ajuster la taille à la longueur de l'arc.
- Exemple mesuré : la phrase « Joyeux Noël Maëlle et Jean-François » (35 caractères) sur un
  demi-cercle de rayon 360 px tient en corps 82 px, soit 4,6 mm de capitale en Caveat Brush.
- Un second arc en bas, parcouru dans l'autre sens, garde le texte à l'endroit.
- Temps de rendu du disque : resvg 68 à 127 ms, Pillow 144 à 183 ms, cairosvg 129 à 214 ms
  (mesuré le 02/11, une machine, deux passages).

**Tour du mug, réduction automatique et multiligne.**
- Zone de test : 2965 × 1122 px, soit 251 × 95 mm (dimensions de [[CMP - Personnalisation par produit]],
  estimées). Panneau à gauche de l'anse, 986 × 980 px, marges de 6 mm, bande d'anse de 30 mm
  (valeurs de test, pas un gabarit).
- 16 cas testés : 4 polices × 4 listes (1, 3 et 6 prénoms, puis 6 prénoms longs comme
  « Marie-Bérénice » et « François-Xavier »). Taille trouvée par Pillow, rendu par resvg.
  Les 16 restent dans la zone, avec au moins 3 px de marge (mesuré le 02/11).
- Temps de rendu : 79 à 173 ms par fichier (mesuré le 02/11).
- Avec 6 prénoms longs, Nunito descend à 2,8 mm de capitale, sous le minimum de 3 mm. C'est le cas
  « taille minimale atteinte, puis tâche humaine » de [[FLOW - Personnalisation à la commande]].

**Code minimal.** Les scripts testés sont dans `tests-texte/scripts/` :
- `render.py` : fonctions communes de rendu et de finalisation PNG ;
- `arc.py` : texte en arc, en resvg, en Pillow et en cairosvg ;
- `mug.py` : réduction automatique et multiligne ;
- `ocr.py` et `ocr2.py` : les deux séries d'OCR.

Le cœur du rendu resvg :
```python
png = resvg_py.svg_to_bytes(svg_string=svg, font_files=[POLICE], skip_system_fonts=True)
img = Image.open(io.BytesIO(bytes(png))).convert("RGBA")
img.save(chemin, dpi=(300, 300), icc_profile=SRGB_ICC)
```
Le texte en arc :
```xml
<defs><path id="h" d="M {cx-r},{cy} A {r},{r} 0 0 1 {cx+r},{cy}"/></defs>
<text font-family="Caveat Brush" font-size="82">
  <textPath href="#h" startOffset="50%" text-anchor="middle">Joyeux Noël Maëlle</textPath>
</text>
```

### 2. Polices
Trois polices manuscrites et une bâton, toutes sous SIL Open Font License 1.1 (fichiers OFL.txt
téléchargés depuis le dépôt google/fonts). La FAQ OFL autorise l'impression sur des objets vendus.
Seule la vente du fichier de police seul est interdite (source : FAQ SIL OFL).

| Police | Style | Glyphes français manquants | Capitale réelle (H, sur 1000) | Corps pour 3 mm | Corps pour 8 mm |
|---|---|---|---|---|---|
| Caveat Brush | pinceau épais | aucun sur 38 | 660,5 | 53,6 px | 143,1 px |
| Kalam | manuscrite, stylo | aucun sur 38 | 720 | 49,2 px | 131,2 px |
| Patrick Hand | manuscrite, capitales | aucun sur 38 | 662 | 53,5 px | 142,7 px |
| Nunito, graisse 400 | bâton arrondie | aucun sur 38 | 712 | 49,8 px | 132,9 px |

Tous les chiffres du tableau sont mesurés le 02/11 avec fontTools. Les 38 caractères vérifiés sont
é è ê ë à â ä ç î ï ô ö û ù ü ÿ œ Œ æ Æ É È Ê Ë À Â Ä Ç Î Ï Ô Ö Û Ù Ü Ÿ, le trait d'union et les deux apostrophes.

Formule : corps en px = hauteur en mm × 11,811 × 1000 / hauteur réelle du H.
La hauteur déclarée dans la police peut être fausse : Kalam déclare 739, son H mesure 720.
Il faut donc mesurer le glyphe.

Aucune police n'est vraiment « gouache ». La recherche documentaire n'a trouvé aucune police gouache
vendue avec une licence d'impression à la demande (source : recherche du 02/11). La piste payante
reste une licence « Merchandise » ou « POD ». Exemple : Stay Enjoy de Din Studio, 49 $ pour
1 000 produits (source : din-studio.com). Elle n'est pas testée ⚠️.

Rendus : 24 images de la ligne de test, 4 polices × 2 tailles × 3 moteurs, dans
`tests-texte/prenoms/`. Nom des fichiers : `<police>_<taille>_<moteur>.png`.

### 3. OCR
Tesseract 5.3.4, langue `fra`, moteur LSTM (`--oem 1`). Deux modèles ont été testés :
le modèle standard d'Ubuntu, et `tessdata_best` téléchargé depuis GitHub.
Images rendues par Pillow, noir sur blanc, en ligne droite, sans flou d'impression.

**Série 1 : les 6 prénoms demandés, à leur taille d'impression** (mesuré le 02/11).

| Police | 3 mm, standard, psm 7 | 8 mm, standard, psm 7 | 3 mm, best, psm 7 | 8 mm, best, psm 7 |
|---|---|---|---|---|
| Caveat Brush | 6/6 | 5/6 | 6/6 | 5/6 |
| Kalam | 6/6 | 6/6 | 6/6 | 6/6 |
| Patrick Hand | 6/6 | 5/6 | 6/6 | 6/6 |
| Nunito | 6/6 | 5/6 | 6/6 | 5/6 |

Erreurs à 8 mm, modèle standard : « Inès » lu « Ines » (Caveat Brush), « Noé » lu « Noë »
(Patrick Hand), « Noé » lu « Noëé » (Nunito).

Tesseract lit moins bien à 8 mm qu'à 3 mm. C'est cohérent avec sa taille idéale d'environ 30 px
(source : documentation Tesseract). Avec `--psm 8` (mot seul), la lecture à 3 mm tombe à 2 à 4
prénoms sur 6 : ce mode est écarté.

**Série 2 : 26 prénoms en vignette normalisée** : les 6 demandés, plus 20 autres comme Zoé,
Anaïs, Gaëtan, Maïwenn, Ève, Benoît ou Raphaël, soit 29 lettres accentuées. Modèle `tessdata_best`,
`--psm 7`. Résultats en « prénoms exacts sur 26 » (mesuré le 02/11) :

| Police | Capitale 24 px | 32 px | 40 px | 48 px | Accents corrects à 32 px |
|---|---|---|---|---|---|
| Caveat Brush | 22 | 24 | 24 | 25 | 29/29 |
| Kalam | 22 | 25 | 25 | 24 | 28/29 |
| Patrick Hand | 26 | 24 | 26 | 22 | 27/29 |
| Nunito | 26 | 26 | 23 | 20 | 29/29 |

Erreurs à 32 px :
- Caveat Brush : « Gaëtan » lu « Gaëtau », « Maïwenn » lu « Moïweun ». Les lettres n et u se confondent.
- Kalam : « Ève » lu « Êve ».
- Patrick Hand : « Ève » lu « Êve », « Zoé » lu « Zoê ».

Avec le modèle standard à 32 px : Caveat Brush 22, Kalam 24, Patrick Hand 25, Nunito 25 sur 26
(mesuré le 02/11). Le modèle `tessdata_best` fait aussi bien ou mieux pour 3 polices sur 4.

**PaddleOCR n'est pas mesuré.** PaddleOCR 3.7.0 s'installe, mais le téléchargement de ses modèles
est bloqué dans l'environnement de test. Littérature seulement : le modèle latin de PP-OCRv5 lit
84,7 % des lignes exactement sur un jeu de 3 111 images latines (source : documentation PaddleOCR) ;
PP-OCRv5 lit 49,4 % des lignes manuscrites anglaises (source : papier PP-OCRv5, CVPR 2026).

**Polices qui passent l'OCR.** Si on fixe le seuil à au moins 25 prénoms sur 26 en vignette de
32 px, sans erreur sur une lettre accentuée :
- Nunito passe : 26/26 et 29/29 accents.
- Caveat Brush rate deux lettres (n et u), mais aucun accent.
- Kalam et Patrick Hand ratent un accent sur Ève, et Patrick Hand un second sur Zoé.
Ce seuil est une proposition, pas une décision.

## Chiffres
Sourcés :
- cairosvg dit mal gérer le texte et les polices (source : cairosvg.org, documentation).
- resvg gère `textPath` depuis sa version 0.7.0 (source : changelog resvg).
- Tesseract a une taille idéale vers 30 px et peu de chances de bien lire sous 10 px de hauteur x
  (source : documentation Tesseract).
- Modèle latin PP-OCRv5 : 84,7 % de lignes exactes (source : documentation PaddleOCR).
- PP-OCRv5 sur l'écriture manuscrite anglaise : 49,4 % (source : papier PP-OCRv5, CVPR 2026).
- Mug 11 oz chez Gelato : 200 × 96 mm (source : aide Gelato). Autre imprimeur que le nôtre.

Mesurés le 02/11 : tous les chiffres des sections Résultats marqués ainsi. Ce sont 624 lectures en
série 1 et 832 en série 2. Fichiers bruts : `tests-texte/ocr/*.csv`.

Estimés :
- Zone du mug 251 × 95 mm : estimée dans [[CMP - Personnalisation par produit]], pas le gabarit Printify.
- Taille minimale lisible à l'impression : 3 mm pour la bâton, 4 à 5 mm pour le pinceau (estimé,
  non mesuré sur objet).

## Caveats
- Tous les rendus sont numériques : ni flou d'impression, ni sublimation, ni verre. Les taux d'OCR
  ne disent rien de la lisibilité sur l'objet ⚠️ à vérifier sur commande test.
- L'échantillon est petit : 26 prénoms, une passe, noir sur blanc. Un écart d'un prénom fait 4 points.
- Tesseract n'est pas monotone : une police peut perdre deux prénoms entre 24 et 32 px.
  Le seuil d'alerte doit se fixer sur nos vrais gabarits.
- PaddleOCR et la police payante ne sont pas testés.
- L'effet des 29 niveaux de gris de resvg sur l'impression n'est pas mesuré.
- Les points ⚠️ de cette note sont à inscrire au registre [[A VERIFIER - Points à valider, vérifier, tester]].
  Ce n'est pas fait : cette recherche n'écrit dans aucune autre note.

## Retenu / écarté
Revue du 02/11/2026 avec Antoine.

**Retenu**
- Stack de rendu : SVG rendu par resvg (`resvg_py`, polices passées en fichiers, jamais les polices
  système), mesure et finalisation par Pillow (`dpi`, profil sRGB). Normalisation NFC de chaque champ,
  libraqm obligatoire.
- Texte en arc par `textPath` ; le gabarit ajuste la taille à la longueur de l'arc, sinon le texte est coupé.
- Quatre polices OFL candidates : Caveat Brush, Kalam, Patrick Hand, Nunito. Hauteur de capitale
  mesurée sur le glyphe, pas sur la valeur déclarée.
- Contrôle OCR par Tesseract `tessdata_best`, `--psm 7`, sur une vignette droite de 24 à 32 px de
  capitale, jamais sur le visuel final.
- Le cas « 6 prénoms longs sous 3 mm » comme déclencheur de la tâche humaine.

**Écarté**
- cairosvg : franges colorées de sous-pixels, texte en arc illisible en mode précis.
- Tesseract `--psm 8`.
- Une police « gouache » : aucune sous licence POD ; la piste payante (Stay Enjoy) reste notée, non testée.

**Conséquence**
- Précise la décision 13 : la police fixée par gabarit se choisit parmi ces quatre, Nunito en bâton
  pour la page blanche. À écrire dans [[CMP - Personnalisation par produit]].
- Au registre A VERIFIER : effet des 29 niveaux de gris de resvg à l'impression ; lisibilité réelle sur
  objet (3 mm bâton, 4 à 5 mm pinceau) ; seuil d'alerte OCR à fixer sur les vrais gabarits.
