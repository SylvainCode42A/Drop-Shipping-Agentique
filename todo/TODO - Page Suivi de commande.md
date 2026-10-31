---
type: todo
title: TODO - Page Suivi de commande
status: en cours
priority: moyenne
decision: "[[10 - Notre serveur produit l'image finale, Printify la reçoit par l'API]]"
created: 2026-10-31
related: ["[[MOD - Pages légales et rétractation]]", "[[TODO - Page Expédition et Livraison]]", "[[TODO - Page Échange et Remboursement]]", "[[FLOW - De la commande personnalisée à Printify]]"]
decisions: ["[[10 - Notre serveur produit l'image finale, Printify la reçoit par l'API]]"]
last-verified: 2026-10-31
tags: [dropshipping, boutique, livraison, todo]
---
# TODO - Page Suivi de commande

## Pourquoi
Page d'aide de la colonne « Aide » : elle réduit les messages « où est ma commande ? » et fixe les
règles de modification et d'annulation. Les commandes partent chez Printify sans validation, donc
le texte ne promet aucun délai de modification ([[10 - Notre serveur produit l'image finale, Printify la reçoit par l'API]]).
Le suivi d'expédition ne remonte pas seul de Printify vers Shopify ⚠️ à vérifier (webhooks Printify).

## Ce qu'il faut faire
1. Remplacer chaque `[À REMPLIR : …]`.
2. Shopify : **Boutique en ligne → Pages → Ajouter une page** « Suivi de commande », coller le texte de
   la section « Texte à coller » ; lien dans le menu du pied de page et en haut du site.
3. S'assurer que le numéro de suivi Printify arrive dans Shopify (commande marquée expédiée, e-mail
   d'expédition au client), sinon l'e-mail promis dans le texte ne part pas.
4. Facultatif : ajouter un formulaire de suivi (app de suivi Shopify) en haut de la page.

---

## Texte à coller

# Suivi de commande

## Les étapes de votre commande
1. **Confirmation** — juste après le paiement, vous recevez un e-mail avec votre numéro de commande,
   vos articles, vos textes de personnalisation et le montant payé.
2. **Fabrication** — votre article est imprimé à la commande : environ 2 jours ouvrés.
3. **Expédition** — vous recevez un e-mail avec le numéro et le lien de suivi de chaque colis.
4. **Livraison** — selon l'article : voir la page Expédition & Livraison.

## Suivre mon colis
- **Par e-mail** : cliquez sur le lien de suivi de l'e-mail d'expédition.
- **Depuis votre compte** : si vous avez un compte client, connectez-vous ; chaque commande affiche son
  statut et ses liens de suivi.
- **Sans compte** : utilisez le lien « Voir ma commande » de l'e-mail de confirmation.

Le suivi peut mettre jusqu'à 48 heures à s'activer après l'expédition.

## Je n'ai pas reçu l'e-mail de confirmation
- Regardez dans vos courriers indésirables (spam, promotions).
- Vérifiez l'adresse e-mail saisie à la commande.
- Toujours rien après quelques heures ? Écrivez-nous à [À REMPLIR : e-mail] **avant de repasser
  commande**, pour éviter un doublon.

## Mon numéro de suivi ne fonctionne pas
- Vérifiez qu'il n'y a pas de faute de frappe.
- Attendez 24 à 48 heures : le suivi s'active au premier scan du transporteur.
- Au-delà de 48 heures, écrivez-nous avec votre numéro de commande.

## Je n'ai reçu qu'une partie de ma commande
C'est normal si vous avez commandé des produits différents : le mug, la boule et la décoration en bois
viennent d'ateliers différents et arrivent séparément, chacun avec son suivi. La boule en verre a un
délai de transport plus long. Si un colis n'est toujours pas arrivé à la fin du délai indiqué pour son
article, écrivez-nous.

## Modifier ou annuler ma commande
Votre commande part en fabrication très rapidement après le paiement.
- Écrivez-nous **immédiatement** à [À REMPLIR : e-mail], objet « URGENT – commande n° … », en
  indiquant précisément la correction voulue (texte, adresse, article) ou votre demande d'annulation.
- **Si la fabrication n'a pas commencé** : nous corrigeons, ou nous annulons et remboursons
  intégralement.
- **Si la fabrication a commencé** : la commande ne peut plus être modifiée ni annulée. Vos droits
  restent ceux décrits dans la page Échange & Remboursement.

Envoyez un seul message par commande : plusieurs messages ralentissent le traitement. Nous vous
confirmons par e-mail si la modification a pu être faite ; sans confirmation de notre part, la commande
est fabriquée telle que validée.

## Vérifiez bien votre texte
Nous imprimons les prénoms et textes exactement comme vous les saisissez. Avant l'ajout au panier puis
avant le paiement, vous confirmez avoir vérifié l'orthographe, les accents et les majuscules. Relisez
attentivement : une faute de saisie ne peut plus être corrigée après la fabrication et ne donne pas
lieu à remplacement gratuit.

## Un problème à la réception ?
- **Article cassé, défectueux ou mal imprimé** : envoyez-nous une photo et votre numéro de commande,
  nous le refaisons gratuitement. Voir la page Échange & Remboursement.
- **Colis en retard, perdu ou marqué « livré » sans l'avoir reçu** : voir la page Expédition & Livraison.

## Nous contacter
- Formulaire de contact (vous pouvez joindre une photo) ou [À REMPLIR : e-mail]
- Réponse sous 48 heures ouvrées
- Indiquez toujours votre numéro de commande

---

## Comment prouver
- La page publiée ne contient plus aucun `[À REMPLIR`.
- Commande test : l'e-mail d'expédition avec lien de suivi arrive au client sans action manuelle.
- Le lien « Voir ma commande » de l'e-mail de confirmation ouvre la page de statut Shopify sans compte.

## Points à faire relire (⚠️)
- Remontée du suivi Printify → Shopify non vérifiée ([[10 - Notre serveur produit l'image finale, Printify la reçoit par l'API]]).
- Pas de délai chiffré de modification ou d'annulation : cohérent tant que l'envoi à Printify est automatique.

## État
- 2026-10-31 : créée, texte complet ; restent l'e-mail de contact et la vérification du suivi Printify.
