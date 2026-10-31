---
type: todo
title: TODO - Personnalisation au choix sur toute la surface du mug, de la boule et de la déco en bois
status: validé
priority: haute
decision: "[[10 - Notre serveur produit l'image finale, Printify la reçoit par l'API]]"
created: 2026-10-31
related: ["[[FLOW - De la personnalisation à la commande]]", "[[FLOW - Personnalisation à la commande]]", "[[MOD - Catalogue et fiche produit]]", "[[CMP - Produit]]"]
decisions: ["[[10 - Notre serveur produit l'image finale, Printify la reçoit par l'API]]", "[[02 - Lancement avec le mug, la boule en cristal et la décoration en bois, trois imprimeurs UE]]"]
last-verified: 2026-10-31
tags: [dropshipping, boutique, personnalisation, todo]
---
# TODO - Personnalisation au choix sur toute la surface du mug, de la boule et de la déco en bois

## Pourquoi
Quand on choisit « au choix » (page blanche) sur notre site, l'image de la cliente ne modifie qu'un
rond. Chez Printify, l'image couvre toute la zone imprimable du produit : pour la décoration en bois,
toute la forme (capture de l'éditeur Printify, forme « Tree », le 31/10/2026). Notre aperçu doit
montrer ce qui sera vraiment imprimé. Signalé par Sylvain le 31/10/2026.

## Ce qu'il faut faire
1. **Mug** : l'image au choix fait tout le tour du mug (bandeau complet), pas un rond.
   Aperçu en **petite simulation 3D** : le mug tourne (ou se fait tourner à la souris / au doigt)
   pour voir l'image sur tout le tour.
2. **Boule en verre** : l'image au choix remplit toute la surface imprimable de la boule, pas un cercle.
3. **Décoration en bois** : l'image remplit toute la forme choisie (les six formes), découpée au contour
   de la forme, comme dans l'éditeur Printify.
4. **Forme de l'image** (sur les trois produits) : si la cliente ne veut pas que son image prenne
   toute la surface, elle choisit une forme dans laquelle l'image est découpée :
   - **Tout** (par défaut) : l'image couvre toute la zone imprimable ;
   - **Sapin** ;
   - **Étoile** ;
   - **Rond**.
   Autour de la forme : **fond blanc** (décidé par Sylvain le 31/10/2026). L'aperçu (et la
   simulation 3D du mug) montre la forme choisie sur le fond blanc.
5. **Gabarits** : pour chaque support, reprendre les dimensions et la zone de sécurité de Printify
   (ligne pointillée de l'éditeur, zone de l'anse pour le mug) ⚠️ à relever dans Printify.
6. **Fichier envoyé à Printify** : le PNG final produit par notre serveur couvre toute la zone, aux
   mêmes proportions que l'aperçu, avec la forme appliquée et le fond blanc autour.
7. **Décision 10** : remplacer « bandeau du mug, cercle de la boule » par « tour complet du mug,
   toute la zone imprimable de la boule, forme au choix (tout, sapin, étoile, rond) sur fond blanc ».

## Comment prouver
- Sur le site, une image au choix couvre tout le tour du mug, toute la boule et chaque forme en bois.
- Les formes sapin, étoile et rond découpent bien l'image, avec un fond blanc autour, sur les trois produits.
- La simulation 3D du mug tourne et montre l'image sur 360°.
- L'aperçu du site et l'aperçu Printify du même fichier montrent le même cadrage.

## État
- 2026-10-31 : créée. Aujourd'hui, seul le rond change, sur les trois produits.
- 2026-10-31 : ajout du choix de forme de l'image (tout, sapin, étoile, rond), fond blanc autour.
