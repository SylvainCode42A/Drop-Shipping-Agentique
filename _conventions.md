---
type: conventions
title: Conventions — Drop shipping agentique
status: validé
last-verified: 2026-10-22
tags: [dropshipping, conventions]
---
# Conventions — Drop shipping agentique

Ces règles s'appliquent à tout agent (humain ou IA) qui écrit ou lit ce dossier.
Modèle : les conventions d'Exogen (`20 Projets/Exogen/Bot-exec/Backtester/_conventions.md`).
Ce fichier est autonome : il reprend ce qui sert ici et dit ce qui diffère.

## 1. Périmètre
Une boutique Shopify de produits personnalisés en impression à la demande, gérée par des agents IA :
le marché (modèle économique, fournisseurs, juridique, acquisition, niches), le système (agents,
données, flux) et la mémoire lue par les agents en production.
Hors périmètre : le code lui-même (il vit dans le dépôt), les données de vente (elles vivent en base).

Ce dossier a **deux lecteurs** :
- les humains et le chat, pour tout sauf `4-memoire-agents/` ;
- les agents en production, pour `4-memoire-agents/` seulement.

## 2. Structure
```
20 Projets/Drop shipping agentique/
├── Drop-shipping-agentique.canvas   point d'entrée visuel (généré en dernier)
├── _conventions.md                  ce fichier
├── A VERIFIER - Points à valider, vérifier, tester.md   registre de ce qui n'est pas sûr
├── 1-vue-ensemble/                  OVR - Drop shipping agentique : le projet, la boucle, l'état
├── 2-marche/                        un dossier par domaine, numéroté
│   ├── 1-Modele economique/         SYN - Modèle économique + RCH - …
│   ├── 2-Fournisseurs/              SYN - Fournisseurs + RCH - …
│   ├── 3-Juridique/                 SYN - Juridique + RCH - …
│   ├── 4-Acquisition/               SYN - Acquisition + RCH - …
│   └── 5-Niches/                    SYN - Choix de la niche + NICHE - <angle> + RCH - …
├── 3-systeme/
│   ├── 2-agents/                    MOD - <agent> : un par agent ou script
│   ├── 3-donnees/                   CMP - <objet> : un par objet du schéma de données
│   ├── 4-flux/                      FLOW - <parcours> : un par parcours de bout en bout
│   └── recherches/                  RCH - <sujet> : recherches techniques
├── 4-memoire-agents/                LU PAR LES AGENTS EN PRODUCTION
│   ├── regles/                      REGLE - <sujet>
│   ├── lecons/                      LECON - <apprentissage>
│   ├── calendrier/                  CAL - <occasion>
│   └── propositions/                ce que les agents proposent ; jamais lu en production
├── decisions/                       NN - <décision> : série propre, à partir de 01
├── todo/                            TODO - <sujet>
└── Claude/                          CMP - Instructions du projet claude.ai
```

## 3. Nommage
| Type | Format | Exemple |
|---|---|---|
| Vue d'ensemble | `OVR - <nom>` | `OVR - Drop shipping agentique` |
| Synthèse de domaine | `SYN - <domaine>` | `SYN - Juridique` |
| Angle de niche | `NICHE - <angle>` | `NICHE - Grands-parents` |
| Recherche | `RCH - <sujet> (JJ-MM-AAAA)` | `RCH - Cadre juridique (23-10-2026)` |
| Agent ou script | `MOD - <nom>` | `MOD - Créateur` |
| Objet de données | `CMP - <objet>` | `CMP - Produit` |
| Parcours | `FLOW - <parcours>` | `FLOW - Du signal au produit publié` |
| Décision | `NN - <décision>` | `01 - L'humain valide avant publication` |
| Todo | `TODO - <sujet>` | `TODO - Ouvrir une boutique de développement` |
| Règle agent | `REGLE - <sujet>` | `REGLE - Contenus interdits` |
| Leçon agent | `LECON - <apprentissage>` | `LECON - Les prénoms manuscrits convertissent mieux` |
| Occasion | `CAL - <occasion>` | `CAL - Fête des grands-mères` |

## 4. Frontmatter des notes humaines
```yaml
---
type: overview    # overview | synthese | niche | research | module | component | flow | decision | todo
title: <titre>
status: draft     # draft | validé → "validé" après le ok d'Antoine
related: ["[[...]]"]
decisions: ["[[NN - ...]]"]
last-verified: AAAA-MM-JJ
tags: [dropshipping, <domaine>]
---
```
Une `research` ajoute `date:` et `sources:`. Une `decision` ajoute `date:` et `implemented: oui | non`.
Un `todo` ajoute `priority:`, `decision:` et `created:`.

## 5. Sections par type
- **SYN** : `## Ce qu'on sait` (chaque point lié à sa RCH) · `## Ce qui est décidé` (liens NN)
  · `## Questions ouvertes` · `## Recherches`. La SYN se met à jour à chaque nouvelle RCH du domaine.
- **NICHE** : `## Public` · `## Acheteur et destinataire` · `## Demande` · `## Concurrence`
  · `## Saisonnalité` · `## Risques` · `## Note sur 10`, chaque fait lié à sa RCH.
- **RCH** : `## Contexte posé` (la question, le prompt) · `## Conclusion en une phrase`
  · `## Résultats` · `## Chiffres` (sourcés puis estimés) · `## Caveats` · `## Retenu / écarté`
  (rempli à la revue). Une recherche ne décide rien ; une décision la cite.
- **MOD / CMP / FLOW** : `## Rôle` · `## Intention` · `## Diagramme` (Mermaid) · `## Entrées et sorties`
  · `## Cas limites` · `## Notes liées`. Un FLOW numérote ses étapes et dit qui agit à chaque étape.
- **Décision** : `## Contexte` · `## Décision` · `## Alternatives écartées` · `## Conséquences` · `## Concerne`.
- **Todo** : `## Pourquoi` · `## Ce qu'il faut faire` · `## Comment prouver` · `## État` (journal daté).

## 6. Mémoire des agents (4-memoire-agents/)
Une note égale une règle, une leçon ou une occasion. Courte, à l'impératif, filtrable par son frontmatter.
```yaml
---
type: lecon             # regle | lecon | calendrier
titre: <une phrase>
agents: [createur]      # veille | createur | analyste | publication
niche: grands-parents   # ou toutes
statut: active          # proposee | active | expiree | remplacee
confiance: moyenne      # faible | moyenne | forte
preuves: ["[[NN - ...]]", "decision:<id>"]
source: analyste        # humain | analyste
cree: AAAA-MM-JJ
revoir-le: AAAA-MM-JJ
---
```
Sections : `## Règle` (une phrase) · `## Pourquoi` · `## Exemples` (un bon, un mauvais).
Règles :
- **L'humain tranche.** Les agents écrivent seulement dans `propositions/`, avec `statut: proposee`.
  Antoine passe une note en `active` et la déplace dans son dossier.
- **Les chiffres restent en base.** Une note cite des identifiants Postgres, elle ne recopie pas les ventes.
- **Une note expirée ne se supprime pas** : elle passe `expiree` ou `remplacee` avec un lien vers sa remplaçante.
- Le chat n'écrit dans ce dossier que dans `propositions/`, sauf demande explicite d'Antoine.

## 7. Chiffres et sources
Tout chiffre porte sa provenance : `source : …`, `estimé`, ou `mesuré le JJ/MM`. Pas de chiffre nu.
Ce qui n'est pas vérifié porte `⚠️ à vérifier` et va dans le registre `A VERIFIER`.
Les contradictions entre sources sont listées, pas tranchées.

## 8. Protocole de rédaction
Résumé en 5 lignes au plus → une question à la fois → montrer la note complète → attendre le « ok »
→ écrire et passer `status: validé`. N'inventer aucune intention ; ne rien écrire sans ok.
Ordre de construction : `_conventions` → OVR → SYN et NICHE (au fil des recherches) → MOD → CMP → FLOW
→ mémoire des agents → decisions / todo → A VERIFIER → canvas.
