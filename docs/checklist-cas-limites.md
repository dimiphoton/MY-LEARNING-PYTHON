# Checklist des cas limites

À passer en revue **à voix haute** avant de dire « j'ai fini ». 30 secondes, et c'est souvent
ce qui distingue un candidat retenu.

## Taille de l'entrée

- [ ] entrée vide (`[]`, `""`, `{}`) — le cas oublié n°1
- [ ] un seul élément
- [ ] deux éléments (révèle les erreurs de comparaison par paires)
- [ ] entrée plus petite que le paramètre (`k > len(mesures)`)
- [ ] entrée très grande : ma complexité tient-elle ? faut-il un flux plutôt qu'une liste ?

## Valeurs

- [ ] zéro, négatifs, très grands nombres
- [ ] flottants : comparaison d'égalité (`0.1 + 0.2 != 0.3`), `nan`, `inf`
- [ ] `None` / valeur manquante : ignorer, rompre la série, ou lever ?
- [ ] doublons
- [ ] tous les éléments identiques
- [ ] entrée déjà triée, et triée à l'envers

## Frontières

- [ ] premier et dernier élément traités comme les autres ?
- [ ] plage encore **ouverte à la fin** de la boucle (le bug classique de l'exercice 001)
- [ ] `>` ou `>=` : lequel, et pourquoi ?
- [ ] intervalles : inclusifs `[a, b]` ou semi-ouverts `[a, b[` ?
- [ ] index : décalage d'un cran (`n - k` vs `n - k + 1`)

## Contrat de la fonction

- [ ] paramètres invalides → `ValueError` (pas `assert`, pas un retour `None` silencieux)
- [ ] l'entrée de l'appelant est-elle modifiée ? (`.sort()` vs `sorted()`, mutation de liste)
- [ ] la fonction marche-t-elle sur un générateur, ou exige-t-elle une séquence indexable ?
- [ ] type de retour stable : toujours une liste, jamais parfois `None`
- [ ] valeur par défaut mutable dans la signature (`def f(x=[])`) — jamais

## Concurrence et flux (niveau senior)

- [ ] état interne partagé entre deux appels ?
- [ ] mémoire bornée si le flux ne s'arrête jamais ?
- [ ] réinitialisation : après une alerte, quand réarme-t-on ?
