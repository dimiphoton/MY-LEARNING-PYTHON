# 001 — Alerte température

**Thème :** fenêtre glissante / compteur de séquence — **Difficulté :** facile → moyen
**Temps cible :** 25 min pour les niveaux 1 et 2, 40 min avec le niveau 3.

## Contexte

Un capteur envoie une séquence de mesures de température. On veut lever une **alerte**
quand la température dépasse un seuil **plusieurs fois de suite**.

## Conventions imposées (ne pas les redécouvrir, c'est le rôle de l'énoncé)

- `mesures` : itérable de `float | None`. `None` = mesure manquante (capteur muet).
- Dépassement = `mesure > seuil` (**strict** : une mesure exactement égale au seuil ne dépasse pas).
- `None` **rompt** la série : on n'a pas la preuve que le dépassement continue, le compteur repart à zéro.
- `k` : nombre de dépassements consécutifs nécessaires. `k < 1` → `ValueError`.
- Une séquence vide ne déclenche jamais d'alerte.

## Niveau 1 — le booléen

```python
alerte_detectee(mesures, seuil, k) -> bool
```

Renvoie `True` si au moins une alerte est présente.

Exemple : `alerte_detectee([18, 31, 32, 19], seuil=30, k=2)` → `True`.

## Niveau 2 — localiser les alertes

```python
plages_alerte(mesures, seuil, k) -> list[tuple[int, int]]
```

Renvoie les **plages maximales** `(index_début, index_fin)` **inclusives** de dépassements
consécutifs dont la longueur est `>= k`.

Exemple : `plages_alerte([31, 32, 33, 10, 40, 41], seuil=30, k=2)` → `[(0, 2), (4, 5)]`
Une plage de 3 dépassements avec `k=2` compte pour **une seule** plage `(0, 2)`, pas deux fenêtres.

## Niveau 3 — le flux (c'est là que se joue l'embauche)

En production, les mesures arrivent une par une et on ne peut pas stocker l'historique.

```python
class DetecteurAlerte:
    def __init__(self, seuil: float, k: int) -> None: ...
    def ajouter(self, mesure: float | None) -> bool: ...
```

`ajouter` renvoie `True` **exactement au moment** où l'alerte se déclenche, c'est-à-dire quand
le compteur atteint `k`. Les dépassements suivants de la même plage renvoient `False`
(on ne réarme qu'après une mesure sous le seuil ou manquante). Mémoire **O(1)**.

## Ce qui est évalué

| Critère | Attendu |
|---|---|
| Complexité | O(n) temps, O(1) mémoire supplémentaire (hors liste résultat) |
| Cas limites | vide, `k > len(mesures)`, `k` invalide, égalité au seuil, `None` |
| Robustesse | fonctionne sur un générateur, ne modifie pas l'entrée |
| Lisibilité | noms explicites, typage, docstring courte, pas de flag inutile |

## Pièges classiques

- Recalculer une fenêtre de taille `k` à chaque index → O(n·k) au lieu de O(n).
- Utiliser `>=` au lieu de `>` sans le signaler.
- Oublier de clôturer la plage en cours à la **fin** de la séquence.
- Traiter `None` comme `0` (donc « sous le seuil ») sans le dire — ici c'est équivalent, mais
  si le seuil était négatif ça deviendrait un bug.
