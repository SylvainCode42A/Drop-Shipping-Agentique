---
type: synthese
title: SYN - Acquisition
status: validé
related: ["[[_conventions]]", "[[SYN - Modèle économique]]", "[[SYN - Choix de la niche]]", "[[SYN - Juridique]]", "[[SYN - Système]]", "[[A VERIFIER - Points à valider, vérifier, tester]]"]
decisions: ["[[04 - Noël 2026 en test manuel réduit, Fête des grands-mères 2027 pour le système]]"]
last-verified: 2026-10-25
tags: [dropshipping, acquisition, synthese]
---
# SYN - Acquisition

État des connaissances sur les canaux qui amènent du trafic à la boutique. Une recherche dédiée, complétée par les études de niche sur le comportement d'achat et le calendrier. Rien n'est décidé ici.

## Ce qu'on sait

### Les canaux
- **Google Shopping** : clic le moins cher d'Europe (0,36 € en médiane, avril 2026), capte une demande existante. Coût par vente estimé 26 à 29 €. Démarrer en Shopping standard ; Performance Max demande environ 50 conversions par mois et 30 jours d'historique ([[RCH - Canaux d'acquisition (22-10-2026)]]).
- **Meta** : sert à tester les visuels et les designs. 30 à 50 € par jour sur une seule campagne, 7 jours avant de juger, sortie d'apprentissage vers 50 événements en 7 jours. Coût par achat souvent supérieur à la marge d'un article seul ([[RCH - Canaux d'acquisition (22-10-2026)]], [[SYN - Modèle économique]]).
- **Etsy** : validation gratuite des designs. Depuis le 10/06/2025, le design doit être original et le partenaire de production déclaré ; les créations par IA sont acceptées si mentionnées. Commission 6,5 %, Offsite Ads 15 % ([[RCH - Canaux d'acquisition (22-10-2026)]]).
- **TikTok, Pinterest, influence** : deuxième phase. TikTok exige au moins 10 vidéos par mois et 50 $ par jour par campagne ; Pinterest mesure à 7 et 30 jours et impose une validation humaine de chaque action automatisée ; l'influence paie en nano-créateurs ou coûte 3 000 € et plus en agence ([[RCH - Canaux d'acquisition (22-10-2026)]]).
- **SEO** : aucun seuil publicitaire, 4 mois à 1 an de délai. Automatisable via l'API Admin Shopify, mais les textes générés en masse sont une erreur classique ([[RCH - Canaux d'acquisition (22-10-2026)]]).
- **Amazon** : Handmade refuse l'impression à la demande, Merch on Demand est sur invitation et sans personnalisation ([[RCH - Canaux d'acquisition (22-10-2026)]]).

### Le ciblage
- Depuis 2025, Meta a supprimé les exclusions de ciblage et traite les centres d'intérêt comme des suggestions : le visuel et le texte sélectionnent l'acheteur ([[SYN - Choix de la niche]]).
- On cible l'acheteur, pas le destinataire : surtout une femme adulte qui gère les cadeaux de la famille ([[SYN - Choix de la niche]]).
- Pinterest capte la recherche d'idées en amont, Google les recherches précises (« mug personnalisé mamie ») ([[RCH - Comportement d'achat des cadeaux personnalisés (25-10-2026)]]).

### Le calendrier publicitaire
- Publier 6 à 8 semaines avant une grande fête, lancer la publicité 4 à 6 semaines avant, Pinterest 2 semaines avant Meta et Google. Le CPM Meta monte d'environ 57 à 59 % la semaine du Black Friday ; octobre est la fenêtre de test la moins chère ([[RCH - Calendrier des occasions de cadeaux en France et dans l'UE (25-10-2026)]]).
- Un calendrier publicitaire distinct par pays de l'UE pour les fêtes des mères et des pères ([[SYN - Choix de la niche]]).

### Ce que l'agent peut juger
- Éliminer un produit est possible tôt : après 300 visites sans vente, son taux de conversion réel est très probablement sous 1 % ([[RCH - Canaux d'acquisition (22-10-2026)]]).
- Déclarer un gagnant demande environ 30 ventes ; sous 10 ventes, l'incertitude est d'environ 60 %. Comparer deux produits proches demande environ 5 000 visites par produit ([[RCH - Canaux d'acquisition (22-10-2026)]]).
- Juger les familles de designs avant les produits, et utiliser les signaux intermédiaires : clic, ajout au panier, début de paiement ([[RCH - Canaux d'acquisition (22-10-2026)]]).
- Advantage+ et Performance Max concentrent les dépenses sur quelques produits : un produit peu exposé n'est pas forcément mauvais ([[RCH - Canaux d'acquisition (22-10-2026)]]).
- L'agent juge sur les ventes Shopify, complètes. Les conversions des plateformes sont partielles à cause du refus des cookies (39 % déclarés, près de 50 % si le refus est mis en avant) ([[RCH - Canaux d'acquisition (22-10-2026)]]).
- Ces règles sont à rapprocher de la recherche statistique dans [[SYN - Système]].

### La stratégie de lancement proposée
- Semaines 1 et 2 (300 à 500 €) : bannière de consentement et Consent Mode v2, pixel Meta et Conversions API, échantillons, fiches gratuites Google, 8 à 12 produits, publication sur Etsy ([[RCH - Canaux d'acquisition (22-10-2026)]]).
- Semaines 3 à 8 (environ 3 000 €) : Google Shopping standard 25 € par jour, Meta Advantage+ 30 € par jour, 5 nano-créateurs ([[RCH - Canaux d'acquisition (22-10-2026)]]).
- Semaines 9 et 10 : couper les produits sans vente après 300 visites, concentrer sur 3 ou 4 gagnants, ajouter Pinterest à 10 à 15 € par jour ([[RCH - Canaux d'acquisition (22-10-2026)]]).
- Total estimé : 3 500 à 4 000 € hors coût des produits ; 80 à 120 ventes attendues, soit 7 à 10 par produit ([[RCH - Canaux d'acquisition (22-10-2026)]]).

### Ce qui reste manuel
- Vérification de la marque chez Google, validation des applications développeur TikTok et Pinterest, validation des publicités par chaque plateforme, négociation avec les influenceurs, déclaration du partenaire de production sur Etsy ([[RCH - Canaux d'acquisition (22-10-2026)]]).

### Les contraintes
- Cookies : refuser doit être aussi simple qu'accepter (CNIL) ; Google exige les signaux de consentement depuis mars 2024 ([[RCH - Canaux d'acquisition (22-10-2026)]], [[SYN - Juridique]]).
- DSA art. 30 : les marketplaces affichent publiquement nom, adresse, téléphone et email du vendeur ([[RCH - Canaux d'acquisition (22-10-2026)]]).
- Changements d'API : Google en septembre 2026, Meta en mai 2026 ([[RCH - Canaux d'acquisition (22-10-2026)]]).

### Contradictions non tranchées
- Panier minimum pour une publicité défendable : 45 € ici, 35 € dans [[RCH - Choix de la niche de lancement (25-10-2026)]], 50 à 60 € dans [[SYN - Modèle économique]].
- Budget de test : 3 500 à 4 000 € sur dix semaines ici, contre 600 € pour Noël 2026 et 1 400 € pour mars 2027 dans [[RCH - Choix de la niche de lancement (25-10-2026)]].
- CPM TikTok : 4,08 $ ou 9 à 13 $. CPC Pinterest : 0,45 à 1,30 € ou 1,50 $. CPM Meta France : voir [[SYN - Modèle économique]].
- Seuil d'apprentissage Meta : 50 événements selon la documentation, 10 par semaine selon une source de 2024 ⚠️ à vérifier.

## Ce qui est décidé
- Premier test : Noël 2026 en manuel réduit (8 à 12 mugs, Shopify, Etsy, Meta 20 € par jour, 800 € au plus), puis Fête des grands-mères 2027 comme premier test du système, plafond 2 500 € révisé en janvier ([[04 - Noël 2026 en test manuel réduit, Fête des grands-mères 2027 pour le système]]).
- Panier cible 45 € et CPA maximum 20 € ([[02 - Mug famille illustrée à 24,90 €, duo à 44,90 €, panier cible 45 €]]). Budget publicitaire toujours bloqué pour les agents ([[03 - Approbation unitaire au lancement, paliers d'autonomie, actions toujours bloquées]]).

Décisions attendues :
- les seuils d'élimination et de validation d'un produit, communs avec [[SYN - Système]].

## Questions ouvertes
- Quel budget accepte-t-on de perdre pendant l'apprentissage ?
- L'agent publicitaire agit-il seul, ou propose-t-il des actions validées par Antoine ?
- Peut-on produire au moins 10 vidéos par mois pour TikTok ?
- Conversions API Meta et visiteurs ayant refusé les cookies : aucune position officielle trouvée ⚠️ à vérifier.
- Frais réglementaires Etsy pour la France après le 22/06/2026 ⚠️ à vérifier dans le compte vendeur.
- Options de ciblage Meta réellement disponibles pour les grands-parents et les futurs retraités ([[SYN - Choix de la niche]]).
- Nombre de publicités Meta actives par concurrent, relevé manuel dans la bibliothèque publicitaire ([[SYN - Choix de la niche]]).

## Recherches
- [[RCH - Canaux d'acquisition (22-10-2026)]]
- [[RCH - Comportement d'achat des cadeaux personnalisés (25-10-2026)]]
- [[RCH - Calendrier des occasions de cadeaux en France et dans l'UE (25-10-2026)]]
