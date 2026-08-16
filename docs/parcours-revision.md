# Parcours de révision — 8 semaines

Un plan est un engagement, pas une décoration. Celui-ci suppose **1 h par jour en semaine +
2 h le samedi**. Si tu as moins, étale sur 12 semaines plutôt que de sauter des étapes : le
facteur qui décide, c'est la régularité, pas le volume horaire.

## Les trois règles qui font toute la différence

**Règle des 45 minutes.** Bloqué depuis 45 min sur un problème ? Tu lis la solution. Tu ne
la copies pas : tu la comprends, tu fermes l'onglet, tu la réécris de mémoire. Puis tu
refais le problème **à blanc 48 h plus tard**. S'acharner 3 h sur un problème n'apprend rien
de plus que 45 min — ça apprend juste à détester la préparation.

**Règle des 3 passages.** Chaque problème est fait 3 fois : jour J, J+7, J+30. Un problème
« compris » qu'on ne revoit pas est perdu à 80 % en deux semaines. Un problème revu 3 fois
devient un réflexe disponible sous stress. C'est là que se joue la différence entre savoir
et savoir **sous pression**.

**Règle du volume raisonnable.** 60 à 80 problèmes bien digérés battent 300 problèmes
survolés. La quantité rassure, elle ne recrute pas. <!-- cf. docs/classiques.md -->

## Routine quotidienne (1 h)

| Durée | Activité |
|---|---|
| 5 min | relire `docs/patterns-algo.md` — le tableau des signaux, à voix haute |
| 40 min | 1 problème neuf, **chronométré**, en appliquant les 6 étapes de la méthode |
| 10 min | comparer à la solution de référence, noter **une seule** chose apprise |
| 5 min | mettre à jour `SUIVI.md` |

Le samedi : session longue de 2 h = 1 mock interview (à voix haute, même seul, même face à
ton téléphone qui filme) + reprise des problèmes marqués « à revoir ».

---

## Semaine 0 — Mise en route

**Objectif :** installer la méthode avant d'installer les algorithmes.

- Lire `docs/methode-entretien.md`, `docs/dans-la-tete-du-correcteur.md`,
  `docs/preparation-mentale.md`. Ce sont les trois documents qui rapportent le plus par
  minute de lecture.
- Faire l'exercice local **001 (alerte température)**, niveaux 1 à 3, chronométré.
- Créer ton compte [LeetCode](https://leetcode.com), ouvrir la roadmap [NeetCode](https://neetcode.io).
- Rédiger ta première fiche `NOTES.md` complète.

**Checkpoint :** tu sais réciter les 6 étapes sans regarder, et tu as verbalisé une
complexité à voix haute au moins une fois.

---

## Semaine 1 — Tableaux, chaînes, tables de hachage

**Pattern :** « ai-je déjà vu cette valeur ? » → `dict` / `set` / `Counter`. C'est le pattern
le plus rentable de tous : il transforme des O(n²) en O(n) et il tombe partout.

**Classiques :** Contains Duplicate (217), Valid Anagram (242), Two Sum (1),
Group Anagrams (49), Product of Array Except Self (238), Longest Consecutive Sequence (128).

**Exercice local à écrire toi-même :** 009 du backlog (top-k des capteurs les plus bavards).

**Erreur typique :** partir sur une double boucle par réflexe. Avant de coder, demande-toi
toujours : *« qu'est-ce qu'un dictionnaire me donnerait en O(1) ici ? »*

**Checkpoint :** Two Sum et Group Anagrams écrits en moins de 10 min chacun, sans hésitation
sur `defaultdict`.

---

## Semaine 2 — Deux pointeurs et fenêtre glissante

**Pattern :** sous-segment contigu, ou parcours par les deux bouts d'un tableau trié.
C'est la famille de ton exercice 001 — tu pars avec de l'avance.

**Classiques :** Valid Palindrome (125), Two Sum II (167), 3Sum (15),
Container With Most Water (11), Best Time to Buy and Sell Stock (121),
Longest Substring Without Repeating Characters (3),
Longest Repeating Character Replacement (424).

**Exercice local :** 004 (plus longue plage sans dépassement) + refaire 002.

**Erreur typique :** recalculer la fenêtre entière à chaque cran → O(n·k). La fenêtre doit
être **mise à jour**, pas recalculée : un élément entre, un élément sort.

**Checkpoint :** tu sais expliquer pourquoi la fenêtre glissante est O(n) alors qu'il y a
deux boucles imbriquées dans le code (chaque élément entre une fois et sort une fois).

---

## Semaine 3 — Pile, file, recherche binaire

**Pattern pile :** « le précédent / le prochain élément qui vérifie X ».
**Pattern binaire :** l'espace de recherche est trié, ou monotone (« la plus petite valeur
qui marche »).

**Classiques :** Valid Parentheses (20), Min Stack (155), Daily Temperatures (739),
Binary Search (704), Search in Rotated Sorted Array (33),
Find Minimum in Rotated Sorted Array (153), Koko Eating Bananas (875).

**Exercice local :** 016 (prochaine mesure supérieure).

**Erreur typique :** les bornes de la recherche binaire (`left <= right` ou `left < right`,
`mid + 1` ou `mid`). Écris **une seule** version, apprends-la par cœur, ne la réinvente plus.

**Checkpoint :** recherche binaire écrite sans bug de borne, du premier coup, deux fois de suite.

---

## Semaine 4 — Listes chaînées et tas

**Classiques :** Reverse Linked List (206), Merge Two Sorted Lists (21),
Linked List Cycle (141), Remove Nth Node From End (19), Reorder List (143),
LRU Cache (146), Kth Largest Element in a Stream (703), Top K Frequent Elements (347),
K Closest Points to Origin (973), Merge k Sorted Lists (23).

**Exercice local :** 017 (médiane glissante avec deux tas) — dur, mais c'est LE problème qui
impressionne quand il tombe.

**Erreur typique :** perdre le pointeur `next` en inversant une liste. Dessine trois nœuds
sur une feuille avant de coder, systématiquement.

**Checkpoint :** tu connais `heapq` de tête (`heappush`, `heappop`, `nlargest`, et l'astuce
du tas-max en négatif : `heappush(tas, -valeur)`).

---

## Semaine 5 — Arbres

**Pattern :** presque tout est une récursion en 3 lignes — cas de base, appel gauche, appel
droit, combinaison.

**Classiques :** Invert Binary Tree (226), Maximum Depth (104), Same Tree (100),
Subtree of Another Tree (572), Lowest Common Ancestor of a BST (235),
Binary Tree Level Order Traversal (102), Validate BST (98), Kth Smallest in a BST (230).

**Erreur typique :** valider un BST en comparant seulement père et fils. Il faut propager un
**intervalle** (min, max). C'est le piège le plus fréquent de toute la catégorie.

**Checkpoint :** tu écris un parcours en largeur (BFS avec `deque`) et un parcours en
profondeur récursif sans réfléchir à la structure.

---

## Semaine 6 — Graphes

**Pattern :** grille = graphe. « composantes », « chemin », « dépendances », « propagation ».

**Classiques :** Number of Islands (200), Clone Graph (133), Rotting Oranges (994),
Pacific Atlantic Water Flow (417), Course Schedule (207), Word Search (79).

**Erreur typique :** oublier l'ensemble `visites` → boucle infinie. Marque le nœud comme
visité **au moment où tu l'empiles**, pas quand tu le dépiles.

**Checkpoint :** tu écris BFS et DFS sur une grille de mémoire, avec la gestion des bords,
en moins de 12 min.

---

## Semaine 7 — Backtracking et programmation dynamique 1D

**Classiques :** Subsets (78), Combination Sum (39), Permutations (46),
Climbing Stairs (70), House Robber (198), Coin Change (322),
Longest Increasing Subsequence (300), Word Break (139), Maximum Subarray (53).

**Erreur typique :** en backtracking, ajouter la liste courante au résultat sans la copier
(`resultat.append(courant)` au lieu de `resultat.append(courant[:])`) — bug silencieux qui
donne des listes vides à la fin.

**Checkpoint :** tu sais transformer une récursion naïve en mémoïsation avec
`@functools.cache` en une ligne, et expliquer ce que ça change à la complexité.

---

## Semaine 8 — Consolidation et simulation

- **Aucun problème neuf.** Uniquement des reprises : tous ceux marqués « à revoir » dans `SUIVI.md`.
- 3 mocks minimum, dont au moins un avec un humain (voir `docs/ressources.md`).
- Refaire les 3 exercices locaux du repo à froid, chronométrés, sans relire les corrigés.
- Relire `docs/dans-la-tete-du-correcteur.md` la veille de ton premier vrai entretien.

**Checkpoint final :** sur un problème de difficulté moyenne jamais vu, tu produis en 35 min
une solution correcte, testée sur un cas limite, avec la complexité annoncée à voix haute.
C'est exactement le niveau attendu. Pas plus.

---

## Et après ?

Si les entretiens visés touchent aux données (BI, data analyst), ajoute deux semaines :
une sur SQL (jointures, fenêtres analytiques, agrégations) et une sur pandas
(`groupby`, `merge`, `pivot`, resampling temporel). Les plateformes sont dans
`docs/ressources.md`. Les réflexes de cadrage et de cas limites, eux, se transposent
tels quels — c'est le même exercice avec une syntaxe différente.
