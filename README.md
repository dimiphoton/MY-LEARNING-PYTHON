# Entraînement aux entretiens de codage

Repo d'entraînement personnel. Deux choses à l'intérieur :

- **Des exercices Python corrigés automatiquement** par des tests `pytest` qui vérifient le
  résultat, **les cas limites et la complexité attendue** — pas seulement « ça passe ».
- **Une préparation complète** : parcours de révision sur 8 semaines, liste des classiques,
  ressources, et deux documents sur ce qui se joue vraiment pendant les 45 minutes.

L'objectif n'est pas de résoudre le problème. C'est de le résoudre **comme on attend qu'un
candidat le fasse** : cadrage, complexité annoncée, cas limites traités, code lisible, testé.

## Par où commencer

1. Lire `docs/preparation-mentale.md` — **les 90 premières secondes**, à connaître par cœur.
2. Lire `docs/dans-la-tete-du-correcteur.md` — ce qui est réellement noté.
3. Faire l'exercice `001_alerte_temperature`, chronométré.
4. Ouvrir `docs/parcours-revision.md` et commencer la semaine 1.
5. Remplir `SUIVI.md` tous les jours.

## Sites essentiels

| Site | Lien | Rôle |
|---|---|---|
| LeetCode | [leetcode.com](https://leetcode.com) | Problèmes d'entretien |
| NeetCode | [neetcode.io](https://neetcode.io) | Roadmap par pattern |
| France-IOI | [france-ioi.org](https://www.france-ioi.org) | Algo en français |
| Exponent Practice | [tryexponent.com/practice](https://www.tryexponent.com/practice) | Mock interviews |
| Python Tutor | [pythontutor.com](https://pythontutor.com) | Visualiser le code |

Liste complète avec conseils d'usage : [`docs/ressources.md`](docs/ressources.md).

## Démarrage technique

### Linux / macOS

```bash
git clone https://github.com/dimiphoton/MY-LEARNING-PYTHON.git
cd MY-LEARNING-PYTHON
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
```

### Windows (PowerShell)

```powershell
git clone https://github.com/dimiphoton/MY-LEARNING-PYTHON.git
cd MY-LEARNING-PYTHON
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
```

| Commande | Effet | Windows (sans `make`) |
|---|---|---|
| `make test` | lance tous les tests sur **ton** code | `.\scripts\test.ps1` |
| `make exo EXO=001_alerte_temperature` | tests d'un seul exercice, en mode verbeux | `.\scripts\exo.ps1 -Exo 001_alerte_temperature` |
| `make corrige` | lance les tests sur les **corrigés** (garde-fou, utilisé par la CI) | `.\scripts\corrige.ps1` ou `python outils/pytest_corrige.py` |
| `make new NOM=detection-pics` | crée le squelette d'un nouvel exercice | `python outils/nouvel_exo.py detection-pics` |
| `make chrono` | minuteur de 25 min pour simuler la pression | `python -c "import time; time.sleep(1500)"` |
| `make lint` | `ruff` sur tout le repo | `ruff check .` |

Au premier `make test`, tout est rouge : c'est normal, les fonctions lèvent
`NotImplementedError`. Ton travail est de faire passer au vert.

## Documentation

### La méthode

- **[`docs/methode-entretien.md`](docs/methode-entretien.md)** — les 6 étapes des 45 minutes,
  et les erreurs qui coûtent le poste.
- **[`docs/preparation-mentale.md`](docs/preparation-mentale.md)** — protocole anti-page
  blanche, escalier de déblocage quand tu sèches, règles anti-code-bâclé, gestion du stress,
  rituel de la veille, banque de phrases toutes faites.
- **[`docs/dans-la-tete-du-correcteur.md`](docs/dans-la-tete-du-correcteur.md)** — les 4 axes
  de la fiche d'évaluation, décodage de ses interventions, ce qu'il pardonne et ce qu'il ne
  pardonne pas, grille d'auto-évaluation.

### Le contenu

- **[`docs/parcours-revision.md`](docs/parcours-revision.md)** — 8 semaines, une famille de
  patterns par semaine, avec checkpoints.
- **[`docs/classiques.md`](docs/classiques.md)** — ~70 problèmes canoniques groupés par
  pattern, avec le piège de chacun. À cocher au fur et à mesure.
- **[`docs/patterns-algo.md`](docs/patterns-algo.md)** — reconnaître la famille d'un problème
  en moins d'une minute.
- **[`docs/checklist-cas-limites.md`](docs/checklist-cas-limites.md)** — à passer en revue à
  voix haute avant de dire « j'ai fini ».
- **[`docs/ressources.md`](docs/ressources.md)** — plateformes, mocks, livres : laquelle sert
  à quoi, et les pièges de chacune.
- **[`docs/backlog-exercices.md`](docs/backlog-exercices.md)** — les 19 exercices suivants à créer.
- **[`SUIVI.md`](SUIVI.md)** — journal, répétition espacée, patterns qui résistent.

## Structure

```
exercices/001_alerte_temperature/
├── ENONCE.md                     # sujet, conventions, niveaux, critères d'évaluation
├── alerte_temperature.py         # <- TON code, à compléter
├── test_alerte_temperature.py    # tests (ne pas modifier pour "faire passer")
└── NOTES.md                      # ton retour d'expérience après la session

corriges/001_alerte_temperature/  # à n'ouvrir qu'APRÈS avoir rempli NOTES.md
docs/                             # méthode, mental, correcteur, parcours, classiques
harness/                          # charge ton module, ou le corrigé si CORRIGE=1
outils/nouvel_exo.py              # générateur d'exercice
SUIVI.md                          # journal de progression
```

## Boucle d'entraînement

1. `make chrono`, puis ouvrir `ENONCE.md` — **et rien d'autre**.
2. Appliquer les 90 premières secondes : reformuler, questionner, exemples, signature.
3. Annoncer la complexité visée en commentaire.
4. Coder, puis `make exo EXO=...` jusqu'au vert.
5. Remplir `NOTES.md` et la grille d'auto-évaluation **avant** d'ouvrir le corrigé.
6. Comparer avec `corriges/`, retenir **une** chose, la noter dans `SUIVI.md`.
7. Refaire à J+7 puis J+30. C'est cette répétition qui transforme une solution comprise en
   réflexe disponible sous stress.

## Exercices disponibles

| # | Exercice | Pattern | Difficulté |
|---|---|---|---|
| 001 | Alerte température | fenêtre glissante / compteur consécutif | facile → moyen |
| 002 | Moyenne et maximum glissants | somme courante, deque monotone | moyen |
| 003 | Fusion d'intervalles de panne | tri + balayage | moyen |

## Ce que les tests vérifient (au-delà du résultat)

- **Cas limites** : entrée vide, paramètre plus grand que la donnée, valeurs manquantes,
  égalité stricte aux bornes, valeurs négatives.
- **Contrat** : paramètre invalide → `ValueError` ; l'entrée de l'appelant n'est jamais modifiée.
- **Complexité** : certains tests refusent une solution qui stocke tout l'historique quand
  O(1) mémoire est demandé, ou comparent au résultat d'une implémentation naïve sur des
  entrées aléatoires.

## Intégration continue

La CI GitHub Actions lance les tests avec `CORRIGE=1` : elle vérifie que les **corrigés**
passent, pas ton code en cours. Un échec signifie qu'un test ou un corrigé est faux — pas que
ton exercice n'est pas fini.
