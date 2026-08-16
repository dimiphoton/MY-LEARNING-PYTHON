# Ressources : où s'entraîner, et pour quoi faire

Chaque ressource sert à une chose précise. Les empiler sans savoir laquelle sert à quoi est
la façon la plus efficace de travailler beaucoup en progressant peu.

*État vérifié en août 2026 — les offres et les tarifs bougent, revérifie avant de payer.*

---

## Liens rapides

| Site | URL | Usage principal |
|---|---|---|
| **LeetCode** | [leetcode.com](https://leetcode.com) | Banque de problèmes d'entretien |
| **NeetCode** | [neetcode.io](https://neetcode.io) | Roadmap par pattern (Blind 75 / 150) |
| **France-IOI** | [france-ioi.org](https://www.france-ioi.org) | Algo en français, progression guidée |
| **Exercism** | [exercism.org](https://exercism.org) | Python idiomatique + mentorat |
| **Codewars** | [codewars.com](https://www.codewars.com) | Kata courts, échauffement |
| **Advent of Code** | [adventofcode.com](https://adventofcode.com) | Endurance, parsing (décembre) |
| **Exponent Practice** | [tryexponent.com/practice](https://www.tryexponent.com/practice) | Mock interviews entre pairs |
| **interviewing.io** | [interviewing.io](https://interviewing.io) | Mocks avec ingénieurs seniors (payant) |
| **Python Tutor** | [pythontutor.com](https://pythontutor.com) | Visualiser l'exécution pas à pas |
| **StrataScratch** | [stratascratch.com](https://www.stratascratch.com) | Entretiens data (SQL + Python) |
| **DataLemur** | [datalemur.com](https://datalemur.com) | Questions data / analytics |
| **HackerRank** | [hackerrank.com](https://www.hackerrank.com) | Tests filtrants automatisés |
| **CodinGame** | [codingame.com](https://www.codingame.com) | Tests techniques (France/Belgique) |
| **Kaggle** | [kaggle.com](https://www.kaggle.com) | Notebooks, pandas, compétitions |
| **Doc Python `collections`** | [docs.python.org/3/library/collections.html](https://docs.python.org/3/library/collections.html) | `Counter`, `deque`, `defaultdict` |
| **Doc Python `heapq`** | [docs.python.org/3/library/heapq.html](https://docs.python.org/3/library/heapq.html) | Tas, top-k |
| **Doc Python `bisect`** | [docs.python.org/3/library/bisect.html](https://docs.python.org/3/library/bisect.html) | Recherche binaire sur liste triée |
| **Doc Python `itertools`** | [docs.python.org/3/library/itertools.html](https://docs.python.org/3/library/itertools.html) | `pairwise`, `groupby`, combinaisons |

---

## Le socle : résoudre des problèmes

### [LeetCode](https://leetcode.com)
**Pour quoi :** la référence absolue, celle dont les recruteurs tirent leurs questions.
Environ 3 500 problèmes, discussions très fournies, éditorial parfois payant.
**Comment l'utiliser :** jamais en mode aléatoire. Suis une liste (voir [NeetCode](https://neetcode.io) ci-dessous)
et **écris ton code dans ton éditeur, pas dans le leur**. En entretien, tu n'auras ni
autocomplétion ni exécution instantanée : t'entraîner avec des béquilles crée une dépendance
qui se paie le jour J.
**Piège :** le bouton « Run » qui devient un substitut à la réflexion. Interdis-toi de le
cliquer avant d'avoir déroulé ton code à la main sur un exemple.

### [NeetCode](https://neetcode.io)
**Pour quoi :** la roadmap qui met de l'ordre dans LeetCode. La liste **NeetCode 150** est
devenue le standard de fait de la préparation ; elle est organisée par pattern, du plus
simple au plus dur, chaque section commençant par le problème qui enseigne le pattern.
Les solutions vidéo sont gratuites et pédagogiquement excellentes.
**Comment l'utiliser :** c'est le squelette de [`docs/parcours-revision.md`](parcours-revision.md). Commence par la
version courte (**[Blind 75](https://neetcode.io/practice)**) — 150 problèmes en 8 semaines est irréaliste avec un travail à côté.

### [France-IOI](https://www.france-ioi.org)
**Pour quoi :** **en français**, gratuit, progression algorithmique remarquablement construite,
correction automatique. Le parcours part vraiment de zéro et monte très haut.
**Comment l'utiliser :** si les fondamentaux algorithmiques sont fragiles, commence ici plutôt
que sur LeetCode. C'est plus lent, c'est beaucoup plus solide. La philosophie du site — on
apprend à *trouver*, pas à *connaître* — est exactement celle d'un bon entretien.

### [Exercism](https://exercism.org)
**Pour quoi :** le **Python idiomatique**, gratuit et open source, avec un mentorat humain.
**Comment l'utiliser :** en complément, pas en remplacement. Là où LeetCode te fait écrire du
code jetable, Exercism te fait écrire du code qu'un mentor va critiquer. C'est précisément la
compétence évaluée quand on te note sur la « qualité de code ».

### [Codewars](https://www.codewars.com)
**Pour quoi :** des kata courts, ludiques, avec les solutions de la communauté à la fin.
**Comment l'utiliser :** en échauffement de 10 min, ou les jours sans énergie. Attention :
les solutions les mieux notées sont souvent des one-liners illisibles — c'est l'**inverse**
de ce qu'on attend en entretien. À lire pour l'astuce, jamais à imiter pour le style.

### [Advent of Code](https://adventofcode.com)
**Pour quoi :** en décembre, 25 jours de problèmes avec parsing de données réelles.
Excellent pour l'endurance et la manipulation de données ; peu représentatif du format entretien.

---

## Simuler l'entretien (la partie que tout le monde saute)

Résoudre en silence et résoudre en parlant sont **deux compétences différentes**. La seconde
est celle qui est notée. C'est le poste de dépense le plus rentable de toute ta préparation.

### [Exponent Practice](https://www.tryexponent.com/practice) (ex-Pramp)
**Pour quoi :** mock interviews entre pairs, gratuit dans la limite de quelques crédits par
mois. Pramp a été racheté par Exponent, les sessions se font désormais sur leur plateforme.
**Comment l'utiliser :** c'est la meilleure option gratuite. Deux réserves connues : les
absences sont fréquentes, et la qualité dépend entièrement du partenaire tiré au sort.
**Le bénéfice caché :** tu passes aussi du côté de l'examinateur. Une heure à évaluer
quelqu'un d'autre t'apprend plus sur les signaux attendus que dix problèmes résolus seul.

### [interviewing.io](https://interviewing.io)
**Pour quoi :** mocks avec des ingénieurs seniors de grandes entreprises, retour détaillé.
Payant, et pas qu'un peu (plusieurs centaines de dollars la session).
**Comment l'utiliser :** une ou deux sessions maximum, en fin de préparation, pour calibrer.
Pas pour apprendre — pour vérifier. À réserver si l'enjeu financier du poste le justifie.

### Un pair humain, gratuit
Un ami développeur, un ancien de ta promo, quelqu'un rencontré dans une communauté.
Donne-lui [`docs/dans-la-tete-du-correcteur.md`](dans-la-tete-du-correcteur.md) en lui demandant de te noter sur les 4 axes.
Un retour honnête d'une personne qui te connaît vaut souvent la session à 250 $.

### Toi-même, filmé
La version dégradée mais réelle : téléphone en mode caméra, 35 minutes, à voix haute. Se
revoir est désagréable et instructif — c'est là qu'on découvre ses 40 secondes de silence,
ses « euh » et son débit qui s'emballe.

---

## Livres

- **Cracking the Coding Interview**, Gayle Laakmann McDowell — la bible du format. Les
  chapitres sur le déroulement, les questions comportementales et la négociation valent
  autant que les problèmes. Code en Java, la logique se transpose.
- **Elements of Programming Interviews in Python**, Aziz / Lee / Prakash — plus difficile,
  plus rigoureux, directement en Python. À prendre en second.
- **Grokking Algorithms**, Aditya Bhargava — illustré, court, parfait si les structures de
  données restent abstraites. Se lit en un week-end.
- **Fluent Python**, Luciano Ramalho — pas un livre d'entretien, mais **le** livre qui fait
  passer d'un code correct à un code qui donne envie de recruter son auteur.

---

## Références Python à garder ouvertes

- La doc de [`collections`](https://docs.python.org/3/library/collections.html) (`Counter`, `defaultdict`, `deque`),
  [`heapq`](https://docs.python.org/3/library/heapq.html), [`bisect`](https://docs.python.org/3/library/bisect.html),
  [`itertools`](https://docs.python.org/3/library/itertools.html).
  Ces quatre modules couvrent 90 % des besoins en entretien.
- **[Python Tutor](https://pythontutor.com)** — visualise l'exécution pas à pas. Imbattable pour
  comprendre où une récursion part en vrille.
- [`timeit`](https://docs.python.org/3/library/timeit.html) et [`cProfile`](https://docs.python.org/3/library/profile.html)
  pour vérifier une intuition de complexité plutôt que la supposer.

---

## Si les entretiens visés touchent aux données

- **[StrataScratch](https://www.stratascratch.com)** et **[DataLemur](https://datalemur.com)** — questions SQL et Python posées en entretien data.
- **[HackerRank](https://www.hackerrank.com)** — moins agréable, mais beaucoup d'entreprises l'utilisent pour les tests
  filtrants automatisés. Se familiariser avec l'interface évite une mauvaise surprise.
- **[CodinGame](https://www.codingame.com)** — très utilisé côté France/Belgique, y compris par des recruteurs pour des
  tests techniques. Format ludique, bonne porte d'entrée.
- **[Kaggle](https://www.kaggle.com)** — pour les notebooks et la manipulation pandas, pas pour l'algorithmique.

---

## Ce qu'il faut éviter

**Le tutoriel infini.** Regarder des solutions est confortable et donne l'illusion de
progresser. La règle : jamais de solution avant 45 min de lutte réelle, et toujours réécrire
de mémoire après.

**La collection de listes.** Blind 75, NeetCode 150, Grind 169, top 100 par entreprise…
Choisis-en **une** et finis-la. Changer de liste au milieu, c'est recommencer à zéro en
croyant avancer.

**Le farming de problèmes faciles.** 200 problèmes « easy » cochés ne prouvent qu'une chose :
que tu sais faire des problèmes faciles. La zone qui fait progresser est celle où tu
transpires — les « medium » que tu rates une fois sur deux.

**L'entraînement muet.** C'est la plus coûteuse de toutes. Tu peux résoudre 300 problèmes en
silence et échouer à en expliquer un seul à voix haute sous pression.
