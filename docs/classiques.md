# Les classiques

Les problèmes qui reviennent réellement en entretien, groupés par **pattern** et non par
difficulté — parce que c'est le pattern qu'on cherche à reconnaître, pas le niveau.

Les numéros sont ceux de [LeetCode](https://leetcode.com). Ils sont stables, mais cherche par le titre en cas de doute.

**Légende :** ★ = incontournable, à savoir écrire de mémoire · ☆ = important · (h) = difficile,
à ne faire qu'au second passage.

Coche au fur et à mesure (`- [x]`), et note la date du 3ᵉ passage dans `SUIVI.md`.

---

## 1. Tables de hachage et comptage

Le pattern le plus rentable : il fait tomber la complexité d'un cran presque partout.

- [ ] ★ Contains Duplicate (217) — le « bonjour » du set
- [ ] ★ Valid Anagram (242) — `Counter` en une ligne, mais sache l'écrire à la main
- [ ] ★ Two Sum (1) — le dictionnaire des compléments, à connaître par cœur
- [ ] ★ Group Anagrams (49) — clé = tuple trié ; savoir pourquoi une liste ne peut pas être clé
- [ ] ★ Top K Frequent Elements (347) — `Counter` + tas, ou tri par compartiments en O(n)
- [ ] ☆ Product of Array Except Self (238) — préfixes et suffixes, sans division
- [ ] ☆ Longest Consecutive Sequence (128) — O(n) avec un set : ne démarrer une série que sur
      un début de série
- [ ] ☆ Valid Sudoku (36) — trois familles de sets d'un coup

## 2. Deux pointeurs

Signal : tableau **trié**, ou parcours par les deux extrémités.

- [ ] ★ Valid Palindrome (125) — filtrage des caractères, pointeurs qui convergent
- [ ] ★ Two Sum II (167) — la version triée, sans dictionnaire
- [ ] ★ 3Sum (15) — une boucle + deux pointeurs ; le piège est la gestion des doublons
- [ ] ☆ Container With Most Water (11) — pourquoi déplacer toujours le plus petit côté ?
- [ ] ☆ (h) Trapping Rain Water (42) — le classique des entretiens durs
- [ ] ☆ Remove Duplicates from Sorted Array (26) — écriture en place, pointeur lent/rapide

## 3. Fenêtre glissante

Signal : « sous-tableau contigu », « k éléments de suite », « la plus longue sous-chaîne… ».
**C'est la famille de ton exercice 001.**

- [ ] ★ Best Time to Buy and Sell Stock (121) — minimum courant, une passe
- [ ] ★ Longest Substring Without Repeating Characters (3) — fenêtre + set
- [ ] ★ Longest Repeating Character Replacement (424) — fenêtre variable avec compteur
- [ ] ☆ Permutation in String (567) — comparaison de deux `Counter` glissants
- [ ] ☆ Sliding Window Maximum (239) — deque monotone → **exercice local 002**
- [ ] ☆ (h) Minimum Window Substring (76) — le sommet de la catégorie

## 4. Pile

Signal : « le prochain élément plus grand », appariement, expression à évaluer, annulation.

- [ ] ★ Valid Parentheses (20)
- [ ] ★ Min Stack (155) — deux piles, ou une pile de tuples
- [ ] ★ Daily Temperatures (739) — pile décroissante d'index ; le pattern « prochain plus grand »
- [ ] ☆ Evaluate Reverse Polish Notation (150)
- [ ] ☆ Generate Parentheses (22) — pile mentale + backtracking
- [ ] ☆ Car Fleet (853) — tri + pile, très proche des problèmes d'intervalles

## 5. Recherche binaire

Signal : données triées, **ou** « la plus petite valeur qui satisfait une condition monotone ».

- [ ] ★ Binary Search (704) — apprends **une** version des bornes, définitivement
- [ ] ★ Search in Rotated Sorted Array (33) — identifier la moitié triée
- [ ] ★ Find Minimum in Rotated Sorted Array (153)
- [ ] ☆ Koko Eating Bananas (875) — recherche binaire **sur la réponse**, pas sur le tableau ;
      pattern sous-estimé et très fréquent
- [ ] ☆ Search a 2D Matrix (74) — la matrice vue comme un tableau plat
- [ ] ☆ Time Based Key-Value Store (981) — `bisect` sur des horodatages

## 6. Intervalles

Signal : « chevauchement », « fusion », « planning », « conflits ». **Exercice local 003.**

- [ ] ★ Merge Intervals (56)
- [ ] ★ Insert Interval (57)
- [ ] ☆ Non-overlapping Intervals (435) — glouton : trier par **fin**, pas par début
- [ ] ☆ Meeting Rooms (252) et Meeting Rooms II (253) — le second = balayage d'événements

## 7. Listes chaînées

Signal : manipulation de pointeurs. Toujours dessiner 3 nœuds avant de coder.

- [ ] ★ Reverse Linked List (206) — itératif **et** récursif
- [ ] ★ Merge Two Sorted Lists (21) — le nœud sentinelle, à adopter partout
- [ ] ★ Linked List Cycle (141) — lièvre et tortue
- [ ] ☆ Remove Nth Node From End (19) — deux pointeurs décalés de n
- [ ] ☆ Reorder List (143) — milieu + inversion + fusion : trois patterns en un
- [ ] ☆ LRU Cache (146) — dict + liste doublement chaînée ; très demandé en entreprise

## 8. Tas / file de priorité

Signal : « les k plus grands », « flux continu », « toujours prendre le minimum ».

- [ ] ★ Kth Largest Element in a Stream (703)
- [ ] ★ K Closest Points to Origin (973)
- [ ] ☆ Task Scheduler (621)
- [ ] ☆ (h) Merge k Sorted Lists (23)
- [ ] ☆ (h) Find Median from Data Stream (295) — deux tas → **exercice local 017**

## 9. Arbres

- [ ] ★ Invert Binary Tree (226) — 3 lignes, pose les bases de la récursion
- [ ] ★ Maximum Depth of Binary Tree (104)
- [ ] ★ Same Tree (100) et Subtree of Another Tree (572)
- [ ] ★ Binary Tree Level Order Traversal (102) — BFS avec `deque`
- [ ] ★ Validate Binary Search Tree (98) — propager (min, max) : le piège n°1
- [ ] ☆ Lowest Common Ancestor of a BST (235)
- [ ] ☆ Kth Smallest Element in a BST (230) — parcours infixe = ordre croissant
- [ ] ☆ (h) Binary Tree Maximum Path Sum (124)
- [ ] ☆ (h) Serialize and Deserialize Binary Tree (297)

## 10. Graphes

- [ ] ★ Number of Islands (200) — la grille comme graphe, BFS ou DFS
- [ ] ★ Clone Graph (133) — dict ancien→nouveau
- [ ] ★ Course Schedule (207) — détection de cycle / tri topologique
- [ ] ☆ Rotting Oranges (994) — BFS multi-sources, souvent mal identifié
- [ ] ☆ Pacific Atlantic Water Flow (417) — partir des bords, pas des cellules
- [ ] ☆ Word Search (79) — DFS + backtracking sur grille
- [ ] ☆ (h) Alien Dictionary — tri topologique appliqué

## 11. Backtracking

Toujours le même squelette : choisir → explorer → **défaire**.

- [ ] ★ Subsets (78)
- [ ] ★ Combination Sum (39)
- [ ] ★ Permutations (46)
- [ ] ☆ Letter Combinations of a Phone Number (17)
- [ ] ☆ Palindrome Partitioning (131)
- [ ] ☆ (h) N-Queens (51) — plus pour la culture que pour la fréquence

## 12. Programmation dynamique

En entretien junior, on attend surtout la 1D. La 2D est un bonus.

- [ ] ★ Climbing Stairs (70) — Fibonacci déguisé, la porte d'entrée
- [ ] ★ House Robber (198) et House Robber II (213)
- [ ] ★ Coin Change (322) — DP ascendante, le représentant de la catégorie
- [ ] ★ Maximum Subarray (53) — Kadane, à connaître par cœur
- [ ] ☆ Longest Increasing Subsequence (300)
- [ ] ☆ Word Break (139)
- [ ] ☆ Longest Palindromic Substring (5) — expansion autour du centre
- [ ] ☆ Unique Paths (62) et Longest Common Subsequence (1143) — les deux DP 2D à connaître

## 13. Glouton et divers

- [ ] ☆ Jump Game (55) — savoir dire pourquoi le glouton est correct ici
- [ ] ☆ Gas Station (134)
- [ ] ☆ Number of 1 Bits (191) et Counting Bits (338) — manipulation de bits, culture minimale

---

## Comment cocher intelligemment

Une case cochée signifie : *« je sais réécrire ce problème de mémoire, en moins de 20 minutes,
en annonçant la complexité, et je vois le cas limite »*. Pas : *« j'ai vu la solution une fois »*.

Si tu ne sais pas, en lisant l'intitulé, quelle **famille** de la liste il rejoint, c'est que
le problème n'est pas acquis — quelle que soit la couleur de la case sur LeetCode.
