# 002 — Moyenne et maximum glissants

**Thème :** somme courante + deque monotone — **Difficulté :** moyen
**Temps cible :** 20 min pour le niveau 1, 35 min avec le niveau 2.

## Contexte

Suite de l'exercice 001 : avant de comparer à un seuil, on veut lisser le signal du capteur.

## Conventions

- `mesures` : séquence de `float` (pas de `None` ici).
- `k` : taille de la fenêtre, `k < 1` → `ValueError`.
- Si `k > len(mesures)` → liste vide (aucune fenêtre complète).
- La sortie contient exactement `len(mesures) - k + 1` valeurs, une par fenêtre.

## Niveau 1

```python
moyennes_glissantes(mesures, k) -> list[float]
```

`moyennes_glissantes([1, 2, 3, 4], 2)` → `[1.5, 2.5, 3.5]`

**La solution naïve en O(n·k) est refusée.** Attendu : somme courante, O(n).

## Niveau 2

```python
maxima_glissants(mesures, k) -> list[float]
```

`maxima_glissants([1, 3, 2, 5, 4], 3)` → `[3, 5, 5]`

`max()` sur chaque fenêtre donne O(n·k). Attendu : **O(n)** avec une `collections.deque`
maintenue décroissante (chaque élément entre et sort au plus une fois).

## Ce qui est évalué

| Critère | Attendu |
|---|---|
| Complexité | O(n) temps, O(k) mémoire pour le niveau 2 |
| Cas limites | `k = 1`, `k = len`, `k > len`, liste vide, valeurs négatives |
| Numérique | savoir dire que la somme courante accumule l'erreur flottante (voir NOTES.md) |

## Pièges classiques

- Boucle imbriquée `sum(mesures[i:i+k])` → O(n·k). C'est le piège principal.
- Se tromper d'un cran sur le nombre de fenêtres (`n - k` au lieu de `n - k + 1`).
- Dans la deque : stocker les valeurs au lieu des **index**, et ne plus pouvoir expulser
  l'élément sorti de la fenêtre.
