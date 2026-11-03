---
type: component
title: CMP - Brief de génération des illustrations de Noël 2026
status: validé
related: ["[[CMP - Personnalisation par produit]]", "[[MOD - Connecteur nolaprint-image]]", "[[RCH - Production des illustrations de Noël 2026, ce que les prompts ont appris (02-11-2026)]]", "[[SYN - Système]]", "[[RCH - Capacités des modèles d'images pour les calques (02-11-2026)]]", "[[RCH - Détourage, nettoyage des bords et agrandissement pour l'impression (02-11-2026)]]", "[[RCH - Rendu des trois procédés d'impression et planche de test (02-11-2026)]]", "[[RCH - Rendu du texte, polices et OCR des accents (02-11-2026)]]", "[[A VERIFIER - Points à valider, vérifier, tester]]"]
decisions: ["[[06 - LangGraph au départ, interface d'images interne avec Nano Banana Pro et Ideogram]]", "[[13 - Texte en trois champs facultatifs, couleur du texte en palette, police fixée, page blanche recadrée par la cliente]]", "[[14 - Brief visuel, deux gabarits de design déclinés par titre et par occasion, rendu peint aux formes franches]]", "[[15 - Catalogue de Noël 2026, six destinataires, fleurs de naissance et table de goûter, neuf produits]]"]
last-verified: 2026-11-02
tags: [dropshipping, systeme, generation-images, brief, component]
---
# CMP - Brief de génération des illustrations de Noël 2026

## Rôle
Ce que la conversation de production (ou plus tard l'agent créateur) donne à Nano Banana Pro pour
produire les 18 éléments isolés et les 7 scènes de la décision 15, et comment chaque sortie est
jugée. Le brief ne décide rien : il applique les décisions 14 et 15 et les contraintes de rendu de
[[CMP - Personnalisation par produit]].

## Intention
- **Un seul style pour tout le catalogue** : la signature de la boutique est le rendu, pas le sujet.
- **Des éléments faits pour être placés par le code** : isolés, centrés, sans ombre, sur un fond uni
  éloigné de toute la palette, pour un détourage par réseau et clé de couleur.
- **Lisible à 85 mm** : une fleur doit se reconnaître à sa silhouette, pas à ses détails.

## Diagramme
```mermaid
flowchart LR
    B[Brief : style + prompt élément] --> G[Nano Banana Pro, 2K, fond uni]
    G --> V{Validation humaine}
    V -->|refus + raison| G
    V -->|ok| R[Référence de style pour les suivants]
    V -->|ok| D[Détourage, décontamination, PNG alpha]
    D --> C[Composition par code, gabarits par support]
```

## 1. Style commun
Préfixe de tous les prompts, en anglais, inchangé. Version v3 du 02/11/2026 : le v1 (« opaque flat
pigment, closed bold contours ») donnait du vecteur à contour noir ; le v2 (traces de pinceau, sans
contour) a réglé la matière mais ramené du lavis sur les feuilles et des fonds en dégradé. Les deux
restent en commentaire dans `brief.py`.

> gouache painting, hand-painted with visible brush strokes inside the shapes, fully opaque paint,
> no wash, no watercolor, no transparency, no faded or ghosted parts, every shape ends with a clean
> crisp edge, thick painterly shapes, no black outline, no vector look, no gradient, medium to
> saturated colors, simple bold shapes, no fine detail, no drop shadow, no text, no letters,
> no watermark, children's book illustration, no realistic face, no recognizable character or brand

Suffixe des éléments isolés (v2 du 02/11/2026, renforcé contre les fonds en dégradé) :

> single object, centered, fully inside the frame with wide margins, the background is one single
> flat color {FOND} with no gradient, no vignette, no halo, no glow, nothing else in the image

Suffixe des scènes :

> cozy family scene, no people, no animals, the right third of the image is a plain uniform wall in
> color {FOND} with nothing on it, soft even lighting

Paramètres : `gemini-3-pro-image`, `image_size` `2K`, `aspect_ratio` `1:1` pour les éléments et
`4:3` pour les scènes, graine notée à chaque appel (elle fixe le dessin, pas les pixels).
**Pas d'image de référence par défaut** (*corrigé le 02/11/2026*,
[[RCH - Production des illustrations de Noël 2026, ce que les prompts ont appris (02-11-2026)]]) :
le modèle recopie le sujet de la référence autour du nôtre (feuilles de la rose sur la jonquille,
couronne de souci autour de la tulipe). Le style tient par le préfixe seul. Une référence reste
possible pour un cas précis, décidé en chat, jamais en règle.

Fond des éléments : vert #00C853, hors de toute la palette. Si un élément contient du vert (feuilles),
le fond passe au magenta #E600E6 pour cet élément, noté dans le journal.

## 2. Palettes (décision 15, fixées le 02/11/2026)
| Destinataire | Fond | Accents | Texte au choix |
|---|---|---|---|
| Mamie | #F3E6D3 | #E07A5F, #8AA587, #D4A537 | #6B4430, #C8453C, #5E8A6E, #2B3A67 |
| Papy | #D6DEE6 | #D4A537, #2E5E4E, #B5533C | #2B3A67, #B5533C, #2E5E4E, #6B4430 |
| Maman | #F2D9DC | #7B3F61, #D8A62A, #5E8A6E | #7B3F61, #6B4430, #5E8A6E, #2B3A67 |
| Papa | #E3DED6 | #2F4FA8, #8A5A3B, #D8A62A | #2B3A67, #8A5A3B, #2F4FA8, #1A1A1A |
| Couple | #F5EFE0 | #7A1E2E, #B8923E, #5E8A6E | #7A1E2E, #6B4430, #5E8A6E, #2B3A67 |
| Famille | #F5EFE0 | #5E8A6E, #C8623C, #D4A537 | #2E5E4E, #6B4430, #C8623C, #2B3A67 |

Les fleurs et les ornements gardent leurs couleurs propres ; seules les scènes prennent la palette.
Contraste : toutes les couleurs de texte dépassent 4,5:1 sur leur fond, sauf le corail #C8453C sur
le crème Mamie (environ 3:1), à réserver aux textes de 4 mm et plus.

## 3. Les douze fleurs de naissance
Un prompt par fleur : « a single {fleur}, {silhouette}, {couleurs} » entre le préfixe et le suffixe.
La colonne « silhouette » dit ce qui rend la fleur reconnaissable à 85 mm ; c'est le critère de
validation.

| Mois | Fleur | Silhouette à obtenir | Couleurs |
|---|---|---|---|
| janvier | œillet | tête ronde ébouriffée aux pétales dentelés, une tige | rose vif, feuilles vert gris |
| février | violette | cinq pétales arrondis, deux en haut, trois en bas, feuille en cœur | violet, cœur jaune |
| mars | jonquille | trompette centrale entourée de six pétales, tige droite | jaune, trompette orangée |
| avril | marguerite | pétales blancs fins et nombreux autour d'un cœur rond | blanc, cœur jaune |
| mai | muguet | tige courbée portant des clochettes blanches, une grande feuille | blanc, feuille vert franc |
| juin | rose | bouton ouvert aux pétales enroulés, une tige avec deux feuilles | rouge ou corail |
| juillet | pied-d'alouette | épi vertical de petites fleurs serrées | bleu, violet |
| août | glaïeul | tige droite avec plusieurs fleurs en trompette étagées | orange, rouge |
| septembre | aster | marguerite à pétales fins et nombreux, plus petite, violette | violet, cœur jaune |
| octobre | souci | tête ronde dense aux pétales serrés, **une tige courte et droite** (corrigé le 02/11, pour être planté) | orange vif |
| novembre | chrysanthème | pompon rond très fourni, **une tige courte et droite** (corrigé le 02/11) | jaune ou bronze |
| décembre | houx | trois feuilles dentelées brillantes et une grappe de baies | vert foncé, rouge |

Deux fleurs se ressemblent (marguerite et aster) : elles se distinguent par la taille et la couleur ;
la validation vérifie qu'on les reconnaît côte à côte.

## 4. Les six ornements de Noël
| Ornement | Silhouette à obtenir | Couleurs |
|---|---|---|
| boule | sphère avec capuchon et petit ruban, un reflet simple en aplat | rouge, or |
| étoile | étoile à cinq branches, bords francs, un peu épaisse | or, jaune |
| sapin | triangle à trois étages avec un tronc court, trois boules | vert, rouge, or |
| flocon | six branches symétriques, épaisses, sans détail fin | blanc cassé, bleu clair |
| bonhomme de pain d'épice | silhouette brune arrondie, trois boutons, sourire au glaçage, pas de visage réaliste | brun, blanc, rouge |
| cœur de Noël | cœur rouge avec une bordure blanche tricotée simple | rouge, blanc |

Le flocon et le bonhomme sont les plus fragiles sur bois (blanc, détails) : à juger sur l'échantillon.

## 4 bis. Les deux supports des symboles (ajouté le 02/11/2026)
Les fleurs sont plantées et les ornements pendent (décision 15, précision du 02/11). Deux éléments de
plus, générés une fois en 16:9 sur fond magenta, détourés, puis découpés par le code en trois
morceaux (15 % à gauche, milieu répété, 15 % à droite) pour tenir toute largeur.

| Élément | Silhouette à obtenir | Couleurs |
|---|---|---|
| bande de sol | bande horizontale d'herbe courte avec une fine bande de terre en dessous, bouts arrondis, sans motif marqué (la jonction du milieu doit être invisible), hauteur environ un cinquième de la largeur | vert franc, brun |
| branche de sapin | branche horizontale de sapin, aiguilles franches, deux bouts naturels, sans motif marqué, hauteur environ un cinquième de la largeur | vert foncé, brun |

Prompt : « a horizontal strip of {élément}, {silhouette}, {couleurs} » entre le préfixe et le suffixe des
éléments, `aspect_ratio` `16:9`. Critère supplémentaire de validation : le tiers central est répétable
sans rupture visible (on colle deux copies du tiers central et on regarde).

## 5. La scène : table de goûter
Prompt de base, entre le préfixe et le suffixe de scène :

> a cozy afternoon tea table seen from the front, slightly from above: a round table with a
> tablecloth in {ACCENT1}, a teapot and three cups in {ACCENT2}, a cake on a stand, a small vase,
> a few wooden toys on the floor, a chair on the left, warm interior, wall color {FOND}, floor in
> {ACCENT3}

Six scènes, une par palette, avec la même composition. *Corrigé le 02/11/2026, deux fois* : la graine
fixe le dessin mais pas la mise en place (mesure dans [[MOD - Connecteur nolaprint-image]], confirmée
sur cinq scènes), donc ni la régénération à la même graine ni l'édition locale par palette ne sont
retenues. Méthode retenue :
1. générer et valider la scène Mamie (deux graines, prompt ci-dessus avec les codes Mamie) ;
2. obtenir les cinq autres palettes par **recoloration de code** (`recolorer.py`) : chaque zone d'un
   rôle (mur, nappe, vaisselle, sol) est retrouvée en Lab et ramenée sur le code de la palette cible,
   nuances et traces de pinceau gardées ; composition identique par construction, aucun appel ;
3. prolonger par code la bande de sol vers la droite sous la zone de texte, pour que la pièce ne se
   lise pas comme un panneau collé (à ajouter à `recolorer.py`).
Limite connue : les petites feuilles du bouquet suivent la couleur de la vaisselle.

Calque d'hiver, une fois sur la scène Mamie validée, par édition en second tour :

> add a window on the left wall showing falling snow outside, and a small decorated Christmas tree
> in the left corner; keep everything else exactly the same

Puis recollage par code de la zone éditée sur l'image d'origine (RCH modèles d'images), et le même
calque est reporté sur les cinq autres palettes par `recolorer.py`, pas par régénération. Mesuré le
02/11 : écart hors zone de 2,63 sur 255 avant recollage, zéro après.

## 6. Procédure
1. Un script par série (fleurs, ornements, scènes), dans `3-systeme/recherches/tests-images/production/`,
   réutilisant `commun.py`. Clé dans `GEMINI_API_KEY`, jamais écrite.
2. Ordre : la rose en premier (sujet simple) pour caler le préfixe ; puis les onze autres fleurs, puis
   les ornements, puis la scène Mamie, puis la recoloration et l'hiver. Sans image de référence.
3. Deux essais par élément, graines 1 et 2 ; un troisième seulement si les deux sont refusés, avec un
   prompt corrigé selon la raison du refus. Pas plus de quatre.
4. Journal `production.json` : élément, prompt complet, graine, fichier, verdict, raison du refus en
   une ligne, date. C'est la preuve d'apport humain ([[SYN - Juridique]]).
5. Validation humaine de chaque sortie, à l'écran puis réduite à 1 004 px de large (85 mm).
6. Les éléments validés passent dans la chaîne de détourage de
   [[RCH - Détourage, nettoyage des bords et agrandissement pour l'impression (02-11-2026)]], sortie
   PNG alpha sRGB 300 DPI dans `production/valides/`.

## 7. Critères de validation
Un élément est validé si tout est vrai :
- reconnaissable à sa silhouette, à 1 004 px de large comme en pleine taille ;
- même matière et même épaisseur de contour que la référence ;
- aucun détail sous 12 px à 1 004 px (1 mm) ;
- pas d'ombre portée, pas de texture de fond, fond uni (écart type sous 3) ;
- pas de texte, de lettre, de visage réaliste, de personnage ou de marque reconnaissable ;
- pour les scènes : le tiers droit est un aplat uni (écart type sous 3), rien n'y est dessiné.
Un refus porte une raison courte parmi : silhouette, matière, détail fin, ombre ou texture, texte,
zone de texte envahie, autre (précisé).

## Entrées et sorties
- Implémentation : `brief.py` (ce brief en données, seule source des prompts), `generer.py` (un appel
  par élément, journal), `analyse.py` (mesures, planche contact, verdicts) dans
  `3-systeme/recherches/tests-images/production/`, pilotés par [[MOD - Connecteur nolaprint-image]].
- Entrées : ce brief, `commun.py`, la clé API.
- Sorties : 20 PNG alpha d'éléments (12 fleurs, 6 ornements, sol, branche), 6 scènes et 1 calque d'hiver
  en PNG, `production.json`.
- Coût estimé : 36 à 70 appels Nano Banana Pro en 2K, soit 5 à 10 USD (estimé, 0,134 USD l'appel).

## Cas limites
- Le modèle dessine du texte ou un visage : refus, prompt renforcé, nouvelle graine.
- Une fleur n'est pas reconnaissable après quatre essais : on la remplace par la fleur de repli
  (tulipe pour mars, pivoine pour juin, tournesol pour août, dahlia pour septembre), noté dans la
  décision 15 à la revue. *02/11/2026 : le glaïeul a été remplacé par le tournesol ; la jonquille a
  passé au septième essai, la tulipe reste en réserve.*
- La scène déborde sur le mur : on repeint la zone par masque (Precise Edit) ou on recadre.
- Dérive de style au fil des appels : on compare à la planche contact des éléments validés et on
  régénère les derniers éléments avec une autre graine.
- Cadrage vu seulement à l'œil : fleur peinte dans un rectangle plus clair que le fond, ou sur une carte
  à bordure blanche. La mesure de bordure ne les voit pas ; la planche contact, si.

## Notes liées
[[15 - Catalogue de Noël 2026, six destinataires, fleurs de naissance et table de goûter, neuf produits]] ·
[[14 - Brief visuel, deux gabarits de design déclinés par titre et par occasion, rendu peint aux formes franches]] ·
[[CMP - Personnalisation par produit]] · [[RCH - Capacités des modèles d'images pour les calques (02-11-2026)]]
