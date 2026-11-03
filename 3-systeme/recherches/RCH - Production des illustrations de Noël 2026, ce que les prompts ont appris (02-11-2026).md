---
type: research
title: RCH - Production des illustrations de Noël 2026, ce que les prompts ont appris (02-11-2026)
status: validé
related: ["[[CMP - Brief de génération des illustrations de Noël 2026]]", "[[RCH - Capacités des modèles d'images pour les calques (02-11-2026)]]", "[[RCH - Détourage, nettoyage des bords et agrandissement pour l'impression (02-11-2026)]]", "[[A VERIFIER - Points à valider, vérifier, tester]]"]
decisions: ["[[14 - Brief visuel, deux gabarits de design déclinés par titre et par occasion, rendu peint aux formes franches]]", "[[15 - Catalogue de Noël 2026, six destinataires, fleurs de naissance et table de goûter, neuf produits]]"]
date: 2026-11-02
sources:
  - "Journal production.json : 74 appels Nano Banana Pro (gemini-3-pro-image, 2K), verdicts et raisons, 02/11/2026"
  - "Scripts de tests-images/production/ : brief.py (versions commentées), generer.py, analyse.py, recolorer.py, detourage.py"
  - "Planches contact-*.png et controle-detourage.png de tests-images/production/"
last-verified: 2026-11-02
tags: [dropshipping, systeme, generation-images, brief, research]
---
# RCH - Production des illustrations de Noël 2026, ce que les prompts ont appris (02-11-2026)

## Contexte posé
Production du 02/11/2026, menée par le chat avec Antoine, selon le brief de génération : la rose
d'abord comme référence de style, puis les onze autres fleurs, les six ornements, la scène Mamie,
les cinq autres palettes, le calque d'hiver, et le détourage des éléments validés. Antoine a tranché
chaque verdict ; chaque refus porte sa raison dans `production.json`. La question de cette note :
qu'est-ce que la production a appris sur les prompts et la méthode du brief ?

## Conclusion en une phrase
Le style tient par le texte du préfixe et non par une image de référence, qui se recopie dans les
sorties ; la graine ne fixe pas la composition, donc les déclinaisons de palette se font par code ;
et le détourage doit forcer opaque la peinture franche, car le réseau rate les couleurs proches du fond.

## Résultats

### 1. Le préfixe de style, en trois versions
- **v1** (celui du brief) : « gouache illustration, opaque flat pigment, closed bold contours… ».
  Les deux roses sont sorties en dessin vectoriel, l'une à contour noir. Les mots « flat » et
  « closed bold contours » tirent vers le vecteur.
- **v2** : « gouache painting, hand-painted with visible brush strokes, slightly uneven opaque paint,
  no black outline, no vector look… ». La matière gouache est obtenue dès le premier essai (rose
  seed 4, validée). Mais le v2 a perdu « no wash » et « opaque flat pigment » : sur les fleurs,
  8 fonds sur 22 étaient non unis (dégradé, halo, deux tons) et plusieurs feuilles étaient en lavis
  transparent.
- **v3** : le v2 plus « fully opaque paint, no wash, no watercolor, no transparency, no faded or
  ghosted parts, every shape ends with a clean crisp edge ». Suffixe des éléments renforcé : « the
  background is one single flat color {FOND} with no gradient, no vignette, no halo, no glow ».
  Le pied-d'alouette et le muguet passent à l'essai 3.
- Les trois versions sont conservées en commentaire dans `brief.py`, avec la date et la raison.

### 2. L'image de référence se recopie dans les sorties
- Avec la rose en référence, sa paire de feuilles revient à la même place sur la jonquille, le
  glaïeul, le pied-d'alouette et la violette, souvent en lavis. Le glaïeul seed 4 montre une rose
  fantôme derrière la fleur. Une partie du « lavis » attribué au préfixe v2 venait en fait de là.
- Une phrase de référence corrigée (« use the reference image only for its painting style… do not
  copy its subject ») n'a rien changé.
- Avec le souci en référence (sans tige ni feuille), la tulipe sort entourée d'une couronne de souci
  fantôme. Le modèle comble l'espace vide autour du sujet avec la référence, quelle qu'elle soit.
- **Sans référence**, la tulipe, la jonquille et les six ornements sortent propres, dans la même
  matière que la rose. Le style a tenu par le préfixe seul sur 22 générations d'éléments.

### 3. Silhouettes qui ont demandé une correction
- Jonquille et glaïeul : bas de tige fondu à chaque essai avec référence. Silhouettes précisées
  (« stem ending in a clean blunt cut », « no leaves » pour le glaïeul). La jonquille passe sans
  référence (seed 7) ; le glaïeul sort en clochettes alternées qui se lisent comme un lis.
- **Glaïeul remplacé par le tournesol pour août**, fleur de repli prévue par le brief, validé du
  premier coup. La tulipe (repli de mars) est validée et gardée en réserve.
- Défauts de silhouette propres aux ornements : flocon à huit branches, boule verte invisible sur un
  sapin vert, bordure du cœur en mailles détachées. Chaque fois, l'autre graine était juste.
- Défauts de cadrage vus seulement à l'œil : fleur peinte dans un rectangle plus clair que le fond,
  fleur peinte sur une carte à bordure blanche. La mesure de bordure de 8 px ne les voit pas.

### 4. La graine ne fixe pas la composition
- Les cinq palettes générées avec la graine de la scène Mamie ont la même idée mais pas la même mise
  en place : table plus grande, jouets différents, fenêtre ajoutée chez Papa et Couple.
- Les cinq scènes sont faites par **recoloration de la scène Mamie** (`recolorer.py`) : chaque zone
  d'un rôle (mur, nappe, vaisselle, sol) est ramenée en Lab sur le code de la palette cible, en
  gardant les nuances. Composition identique garantie, sans appel.
- Effet secondaire utile : le mur et le panneau de texte, peints en deux crèmes proches, finissent
  sur la même couleur, ce qui efface la jointure.
- Limite : les petites feuilles du bouquet suivent la vaisselle (dorées, brunes, orangées).

### 5. La scène et le calque d'hiver
- Le tiers droit uni est peint comme un panneau séparé : le sol s'arrête net à la verticale. C'est
  la conséquence directe du brief (un tiers droit sans sol). Accepté.
- La zone de texte commence à 69 % de la largeur, pas à 66,7 % : `analyse.py` mesure un écart type
  de 13 au lieu de 1,1 à cause de cette bande.
- Le calque d'hiver par édition en second tour change très peu hors zone : écart moyen 2,63 sur 255,
  0,66 % des pixels à plus de 8. Le recollage par code rend la scène exactement identique hors zone.

### 6. Détourage
- La chaîne de la RCH du 02/11 a fonctionné, avec deux ajouts nés de cette production.
- **Le réseau rate une couleur proche du fond** : l'œillet rose sur magenta sortait à 71 %
  d'opacité, et des tiges étaient coupées. Correction : l'intérieur de la peinture franche (plus de
  15 du fond en Lab) est forcé opaque, ce que le brief autorise puisqu'il interdit le lavis.
- **La clé Lab juge opaque un pixel mêlé** de jaune et de magenta, loin du fond en Lab : liseré rose.
  Correction : l'alpha du bord est recalculé comme un mélange de la peinture voisine et du fond.
- Les parties détachées de moins de 1 % de la plus grande sont retirées (bout de tige fantôme).
- Temps mesuré sur le Mac : environ 6,4 s par élément, isnet compris.

### 7. Points techniques du circuit
- Nano Banana Pro renvoie du JPEG, enregistré sous un nom en .png. Sans effet visible sur les fonds
  (écart type de 1,5 à 2,5) ni sur le détourage.
- Le plafond de dépenses mensuel du projet Google est distinct du crédit : relevé en cours de route.
- `analyse.py --verdict` écrivait sur une entrée en erreur portant le même nom de fichier : corrigé.
  Il écrit toujours sur la dernière entrée d'un fichier généré deux fois (un `oeillet-seed3.png`
  reste sans verdict).

### 8. Ajouts du 02/11 soir : sol, branche, tiges
Après la revue des maquettes face aux meilleures ventes (décision 15, précision du 02/11), les fleurs
sont plantées dans une bande de sol et les ornements pendent à une branche de sapin. Quatre éléments,
sans image de référence, 8 appels.
- **Tiges courtes** : la silhouette du souci et du chrysanthème a reçu « on a short straight stem
  ending in a clean blunt cut ». Les quatre essais ont une tige nette et opaque du premier coup. Le
  choix s'est fait sur la distinction entre les deux : souci seed 3 orange franc à tête dense,
  chrysanthème seed 3 jaune bronze ; le chrysanthème seed 4, doré orangé, se confondait avec le souci,
  et le souci seed 4, à pétales lâches, se lisait comme un zinnia.
- **Sol et branche** en 16:9 : une image sur deux est bonne (sol seed 1, branche seed 1). Le sol seed 2
  porte une bande fantôme en lavis et un motif en volutes ; la branche seed 2 sort en diagonale et
  fourchue, malgré « horizontal » dans le prompt.
- **Aucun des deux ne se répète tel quel** : collé à lui-même, le tiers central brut casse à la
  jonction (saut moyen de 27 pour le sol et de 45 pour la branche, contre 3 à 4 entre deux colonnes
  voisines). Le prompt « no marked pattern so that the middle can be repeated » ne suffit pas.
- **Le raccord se fait par code** (`detourage.py`, fonction `raccorder`) : coupes cherchées entre 15 et
  30 % et entre 70 et 85 % de la largeur là où les bandes se ressemblent le plus, puis fondu de 48 px
  au début de la tuile. Saut à la jonction ramené à 3,2 (sol) et 3,4 (branche), invisible à l'œil.
  La branche garde une répétition régulière de ses grappes, qui se lit comme une guirlande.
- Le détourage a gardé les bouts du sol et de la branche entiers ; aucune partie n'a été retirée comme
  détachée. Sortie : `sol`, `branche` et leurs morceaux `-gauche`, `-tuile`, `-droite` dans `valides/`.
- Le connecteur ne connaissait pas les supports : `prod.py` (fonction `valider`) a reçu
  `brief.SUPPORTS`, et `list_elements` les affiche. L'aspect 16:9 venait déjà de `generer.py`.
- Coût : 8 appels, soit 1,07 USD (estimé). Total du jour : 74 appels réussis, soit 9,92 USD (estimé).

## Chiffres

### Mesurés le 02/11
| Chiffre | Valeur |
|---|---|
| Appels réussis | 66, soit 8,84 USD (estimé à 0,134 USD l'appel 2K) |
| dont tests du connecteur | 3 appels |
| Appels en erreur, non facturés | 8 |
| Éléments validés au premier ou second essai | 14 sur 19 |
| Essais pour la jonquille | 7 ; pour le glaïeul, 7 sans succès |
| Fonds non unis, préfixe v2 avec référence | 8 sur 22 |
| Fonds non unis, sans référence (ornements) | 0 sur 12 |
| Écart hors zone du calque d'hiver | 2,63 en moyenne, 0,66 % des pixels à plus de 8 |
| Opacité de la tête de l'œillet avant correction | 0,71 |
| Détourage | environ 6,4 s par élément sur le Mac |

### Estimés
| Chiffre | Statut |
|---|---|
| Coût en USD | estimé, prix unitaire de la RCH du 22/10 |

## Caveats
- Une seule séance, un seul jugeur. Le style « tenu sans référence » est jugé à l'œil sur 22 images.
- Les ornements ont tous été générés sans référence, donc la comparaison avec référence ne porte que
  sur les fleurs.
- La recoloration est testée sur une seule scène ; une scène avec des ombres fortes la mettrait en
  difficulté.
- Rendu imprimé non vu : flocon sur le blanc du mug, mailles du cœur à 12 à 15 px, guirlandes du
  sapin d'hiver sous 12 px ⚠️ à vérifier sur la commande test.

## Retenu / écarté
Revue du 02/11/2026 avec Antoine.

**Retenu**
- Le préfixe v3 comme style de la boutique : gouache opaque, traces de pinceau, bords nets, sans contour
  noir. Il tient seul sur 22 éléments ; c'est lui, pas une image, qui porte la signature.
- **Pas d'image de référence** pour les éléments isolés : le modèle recopie son sujet autour du
  nôtre. Le brief est corrigé dans ce sens ; `reference.png` reste possible pour un cas précis, jamais
  par défaut.
- Les déclinaisons de palette par **recoloration de code** (`recolorer.py`) sur une scène validée,
  et le calque d'hiver par édition en second tour puis recollage. Remplace l'édition locale par
  palette que le brief prévoyait.
- Les deux ajouts au détourage (intérieur forcé opaque au-delà de 15 du fond en Lab, alpha du bord
  recalculé comme mélange peinture-fond, parties détachées sous 1 % retirées) : à reporter dans la
  RCH détourage et [[SYN - Système]].
- Tournesol pour août, jonquille pour mars, tulipe en réserve (décision 15 mise à jour).
- Les fleurs de repli du brief ont servi : le mécanisme est bon.

**Écarté**
- La référence de style par image comme règle, et la phrase « use the reference only for its style »
  qui n'a rien changé.
- La régénération d'une scène par palette à la même graine : compositions différentes, fenêtres
  ajoutées qui entrent en conflit avec le calque d'hiver.
- Le glaïeul : sept essais, jamais lisible.
- Le « panneau » de la scène (sol coupé net sous la zone de texte) tel quel sur le mug : à corriger
  par code en prolongeant la bande de sol vers la droite, avant tout rendu.

**Conséquence**
- Brief corrigé (section 1 : pas de référence ; section 5 : recoloration par code ; procédure).
- Au registre A VERIFIER : flocon sur le blanc du mug, mailles du cœur à 12-15 px, guirlandes du
  sapin d'hiver sous 12 px, recoloration sur une scène à ombres fortes, `oeillet-seed3.png` sans
  verdict dans le journal.
- Prochaine étape : les gabarits de support et le module de rendu, sur les fichiers de `valides/`.
