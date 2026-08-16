# Patterns algorithmiques : reconnaître le signal

En entretien, tu n'as pas le temps d'inventer. Tu dois **reconnaître** la famille du problème
en moins d'une minute. Voici les déclencheurs.

| Le sujet dit... | Pattern | Complexité visée |
|---|---|---|
| « k fois de suite », « sous-tableau de taille k » | fenêtre glissante / compteur | O(n) |
| « maximum de chaque fenêtre » | deque monotone | O(n) |
| « paire dont la somme vaut X », tableau trié | deux pointeurs | O(n) |
| « a-t-on déjà vu ce truc ? », « compter les occurrences » | dict / set / `Counter` | O(n) |
| « somme entre i et j », requêtes répétées | sommes préfixes | O(n) puis O(1) par requête |
| « intervalles », « chevauchement », « fusion » | tri + balayage | O(n log n) |
| « les k plus grands », « flux et médiane » | tas (`heapq`) | O(n log k) |
| « parenthèses », « précédent plus grand élément » | pile | O(n) |
| « chercher dans un espace trié », « plus petite valeur qui marche » | recherche binaire | O(log n) |
| « chemin », « voisins », « réseau », « dépendances » | BFS / DFS, tri topologique | O(V + E) |
| « nombre de façons », « coût minimal », choix successifs | programmation dynamique | O(n·états) |

## Les cinq à maîtriser en priorité pour ton profil

Tes exemples tournent autour de séries de mesures. Ce sont ceux-là qui tomberont :

1. **Fenêtre glissante / compteur consécutif** — exercice 001.
2. **Somme courante et deque monotone** — exercice 002.
3. **Tri + balayage d'intervalles** — exercice 003.
4. **Table de hachage** pour dédoublonner ou compter en un passage.
5. **Deux pointeurs** sur données triées.

## Réflexes de complexité

- Une boucle imbriquée sur les mêmes données → O(n²), cherche un dict ou un tri d'abord.
- Un `sum(...)` ou `max(...)` **dans** une boucle → tu viens de multiplier par k.
- `list.pop(0)` est en O(n) : utilise `collections.deque`.
- `x in liste` est en O(n), `x in set` est en O(1).
- Trier coûte O(n log n) : c'est acceptable, et souvent c'est le prix d'entrée pour
  une solution simple. Annonce-le plutôt que de bricoler.

## Boîte à outils Python à connaître par cœur

```python
from collections import Counter, defaultdict, deque
import heapq
import bisect
import itertools

Counter(mesures).most_common(3)
deque(maxlen=k)                       # fenêtre à taille bornée, gratuite
heapq.nlargest(k, mesures)
bisect.bisect_left(tries, valeur)     # insertion dans une liste triée
itertools.pairwise([1, 2, 3])         # (1,2), (2,3) — Python 3.10+
itertools.groupby(sequence)           # séries consécutives identiques
enumerate(mesures, start=1)
zip(mesures, mesures[1:])             # comparer chaque élément au suivant
```
