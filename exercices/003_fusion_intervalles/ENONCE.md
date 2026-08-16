# 003 — Fusion d'intervalles de panne

**Thème :** tri + balayage — **Difficulté :** moyen
**Temps cible :** 25 min.

## Contexte

Plusieurs capteurs signalent des périodes de panne. Elles se chevauchent. On veut le
calendrier consolidé, puis la durée réellement couverte.

## Conventions

- Un intervalle est un tuple `(debut, fin)` **semi-ouvert** : `[debut, fin[`.
  Donc `(0, 5)` et `(5, 9)` sont **contigus** et fusionnent en `(0, 9)`.
- Les intervalles arrivent **dans un ordre quelconque**.
- `fin < debut` → `ValueError`. Un intervalle vide (`debut == fin`) est valide et
  disparaît de la sortie s'il n'est pas absorbé (il ne couvre rien).
- La sortie est triée par début, sans chevauchement.

## Niveau 1

```python
fusionner(intervalles) -> list[tuple[float, float]]
```

`fusionner([(5, 9), (0, 5), (12, 14), (13, 20)])` → `[(0, 9), (12, 20)]`

## Niveau 2

```python
duree_couverte(intervalles) -> float
```

Durée totale réellement en panne. `duree_couverte([(0, 10), (2, 5)])` → `10`
(pas 13 : le second est inclus dans le premier).

## Ce qui est évalué

| Critère | Attendu |
|---|---|
| Complexité | O(n log n), dominé par le tri — savoir le dire |
| Cas limites | vide, un seul intervalle, inclusion totale, contiguïté exacte, intervalle vide |
| Robustesse | ne modifie pas la liste d'entrée (attention à `.sort()` en place) |

## Pièges classiques

- `intervalles.sort()` modifie l'entrée de l'appelant → utiliser `sorted()`.
- Ne comparer qu'avec l'intervalle précédent au lieu de la fin **courante fusionnée** :
  `[(0, 10), (2, 3), (4, 12)]` casse si on oublie que la fin courante vaut 10.
- Traiter `fin == debut_suivant` comme un non-chevauchement alors que la convention
  semi-ouverte impose la fusion.
