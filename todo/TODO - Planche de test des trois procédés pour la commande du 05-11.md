---
type: todo
title: TODO - Planche de test des trois procédés pour la commande du 05-11
status: en cours
priority: haute
decision: ""
created: 2026-11-02
related: ["[[RCH - Rendu des trois procédés d'impression et planche de test (02-11-2026)]]", "[[RCH - Mockups réalistes par code des trois produits (02-11-2026)]]", "[[RCH - Contraintes d'impression Printify des trois produits (01-11-2026)]]", "[[RCH - Rendu du texte, polices et OCR des accents (02-11-2026)]]", "[[CMP - Personnalisation par produit]]", "[[A VERIFIER - Points à valider, vérifier, tester]]"]
decisions: ["[[14 - Brief visuel, deux gabarits de design déclinés par titre et par occasion, rendu peint aux formes franches]]", "[[10 - Notre serveur produit l'image finale, Printify la reçoit par l'API]]", "[[08 - Personnalisation à la commande en génération interne, test Printify avant le 5 novembre]]"]
last-verified: 2026-11-02
tags: [dropshipping, fournisseurs, impression, test, todo]
---
# TODO - Planche de test des trois procédés pour la commande du 05-11

## Pourquoi
La décision 14 retient un rendu gouache aux formes franches, avec des hypothèses non prouvées sur le
blanc, l'alpha, les pastels, les traits fins et le texte minimal sur bois, verre et mug. La RCH du 02/11
spécifie une planche de test par support qui mesure tout cela en une commande. La commande test
Printify est attendue avant le 05/11 (décision 08). Au 02/11, la planche n'existe pas en fichier.

## Ce qu'il faut faire
Produire trois fichiers PNG sRGB 300 DPI par code (Pillow, resvg pour le texte), selon la section
« Planche de test du 05/11 » de [[RCH - Rendu des trois procédés d'impression et planche de test (02-11-2026)]] :

| Support | Dimensions | Contenu principal |
|---|---|---|
| Mug 11 oz | 2244 × 945 px (placeholder `front`, API `variants.json`, 01/11 et 02/11) | réglets de bord, bande de couture, 3 rangées de 8 pastilles, tons chair, quasi-blancs, traits 0,2 à 1 mm, texte 2 à 5 mm, dégradés, motif gouache de 40 mm |
| Boule en verre | disque de 76,2 mm, 900 px ; deux disques A (fond transparent) et B (fond bleu) | 18 pastilles de 7 mm, témoins alpha 0 / blanc / alpha 50 %, traits, texte, cercle de centrage |
| Bois, ovale | pièce 85 × 125 mm, zone 1085 × 1545 px (placeholder `front`, API), zone utile 75 × 115 mm | 18 pastilles de 9 mm, témoins blanc / alpha 0 / noir, gris, dégradé ocre, traits dans les deux sens, texte, aplat de grain, bande de contour |

Détails communs : nuancier sRGB de la RCH (pastels, moyennes, soutenues, chair, gris, quasi-blancs) ;
nom du fichier, date et « HAUT » en 3 mm ; texte « Mamie Josette 0123 » dans une police retenue
(Nunito, Caveat Brush) ; alpha partiel sur un témoin seulement.

Puis : commander un exemplaire par support chez les imprimeurs de la décision 02 par l'API
(`lineItemWithBlueprint`), noter l'`external_id`, et photographier à la réception selon le protocole
de la RCH (lumière du jour, écran et réglet à côté).

Si le budget le permet, ajouter une étoile en bois avec un prénom de 5 mm et un motif réel.

Ajout du 02/11 (revue de [[RCH - Mockups réalistes par code des trois produits (02-11-2026)]]) : commander
aussi, par support, un exemplaire imprimé d'une **mire** (damier et marqueurs ArUco couvrant toute la zone,
repères « haut » et « anse ») pour calibrer plus tard les mockups par carte UV. Si le budget ne permet
qu'un exemplaire par support, mettre la mire sur une moitié de la planche de test. À la réception,
photographier selon le protocole de cette RCH (fond seul, plaque blanche, objet vierge, objet imprimé ;
caméra et lumière figées).

## Comment prouver
- Les trois PNG ont exactement les dimensions de la zone, le profil sRGB et 300 DPI dans leurs métadonnées.
- Chaque élément de la RCH est présent et nommé sur la planche.
- La commande est créée chez Printify sans erreur et apparaît en attente d'approbation.
- À réception : une ligne par point dans le registre A VERIFIER, avec la photo.

## État
- 2026-11-02 : créée. Spécification complète dans la RCH, fichiers non produits.
- 2026-11-02 : fichiers produits et rangés dans 3-systeme/recherches/planche-test/ (4 planches, 3 mires, script). Reste : commande Printify.
- 2026-11-02 : planches du mug et de l'ovale régénérées à 300 DPI aux dimensions des placeholders API
  (mug 2244 × 945, ovale 1085 × 1545) ; boule inchangée. Anciennes planches supprimées.
- 2026-11-02 : commande test créée par l'API (`api/commande_test.py`), external_id
  `nolaprint-test-2026-11-05`, identifiant `6ae8c55103ba762f8b0a59f3`, une commande pour les trois
  imprimeurs, sans les mires. Coût à la relecture : 20,78 $ d'articles et 26,67 $ d'expédition, soit
  47,45 $, taxes 0,00 $ (mesuré le 02/11). Statut `pending`, lignes `on-hold`. Reste : vérifier le
  placement dans Printify, approuver.
