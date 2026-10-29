---
type: component
title: Instructions du projet claude.ai
language: prompt
path: réglages du projet claude.ai « drop sheeping agentique » (champ « instructions du projet ») — copie de référence ici
status: validé
related: ["[[_conventions]]"]
decisions: []
last-verified: 2026-10-22
tags: [dropshipping, claude, component, instructions]
---
# CMP - Instructions du projet claude.ai

## Rôle
Le texte que le chat applique au début de chaque conversation du projet claude.ai
« drop sheeping agentique ». Le champ « instructions du projet » de claude.ai ne contient qu'un
**pointeur** vers cette note ; **le texte appliqué est le bloc « Le texte » ci-dessous**, que le chat lit
par le connecteur Filesystem. Une modification est une édition de cette note, sans copie.
Si le pointeur de claude.ai et cette note divergent, c'est claude.ai qui agit et cette note qui est à relire.

## Dans claude.ai (trois lignes, ne changent plus)
```
Au début de chaque conversation, lis par le connecteur Filesystem
20 Projets/Drop shipping agentique/Claude/CMP - Instructions du projet claude.ai.md
et applique le bloc « Le texte » comme s'il était écrit ici.
```

## Le texte (version du 22/10/2026)
```
Une recherche se termine par une note RCH dans le dossier du domaine concerné
(2-marche/<domaine>/ ou 3-systeme/recherches/), et le chat en donne le chemin.

Avant d'écrire dans le vault, lis le _conventions.md du projet et dis-le en une ligne.
Protocole : résumé, une question à la fois, montrer la note complète, attendre le ok, écrire.

Le dossier 4-memoire-agents/ est lu par les agents en production : le chat n'y écrit
que dans propositions/, sauf demande explicite d'Antoine.
```

## Intention
- **Même mécanisme qu'Exogen.** Les instructions du projet sont la seule chose chargée à coup sûr au début
  de chaque conversation. Un pointeur évite de recopier le texte dans claude.ai à chaque changement.
- **Une recherche laisse une trace.** Plusieurs chats de recherche tournent en parallèle ; chacun doit
  déposer sa note `RCH` dans le bon domaine, sinon le rapport reste dans une conversation.
- **La mémoire des agents est protégée.** `4-memoire-agents/` est lu en production ; une note écrite
  par erreur changerait le comportement des agents.

## Ce qu'il ne fait pas
- Il ne garantit rien : un chat peut sauter une lecture. Les contrôles sont les livrables : la ligne
  « je lis `_conventions.md` », le chemin de la note `RCH`.
- Il ne porte aucune règle de fond : elles sont dans [[_conventions]].

## Comment il évolue
On modifie le bloc « Le texte » et sa ligne de version, puis `last-verified`. Rien à recopier dans
claude.ai, sauf si cette note est déplacée.

## Notes liées
Modèle : [[20 Projets/Exogen/Claude/3-artefacts/CMP - Instructions du projet claude.ai]] · Règles : [[_conventions]]
