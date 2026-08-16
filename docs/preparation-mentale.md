# Préparation mentale

Deux échecs dominent, et aucun n'est un problème d'algorithmique :

1. **La page blanche** — 10 minutes perdues à fixer l'énoncé, l'angoisse qui monte, plus
   assez de temps pour coder même si l'idée arrive.
2. **Le code bâclé** — l'idée est là, on se jette dessus, on produit du code sale et non
   testé, et on perd les points de codage et de vérification.

Les deux se soignent par des **protocoles**, pas par de la volonté. Sous stress, la volonté
ne répond plus ; les automatismes, si.

---

## Protocole anti-page blanche : les 90 premières secondes

Elles sont scriptées. Tu n'as **rien à décider**, donc rien à rater. Même sans la moindre
idée, tu exécutes ces quatre gestes.

**0-20 s — Reformuler.**
> « Si je comprends bien : on me donne une séquence de mesures et un seuil, et je dois dire
> s'il y a k dépassements consécutifs. C'est ça ? »

Reformuler ne demande aucune intelligence et produit trois effets : ça remplit le silence, ça
te fait relire l'énoncé, ça coche déjà la case communication.

**20-45 s — Poser une question, n'importe laquelle de la liste.**
Flux ou liste complète ? `>` ou `>=` ? Que fait-on des valeurs manquantes ? Quelle volumétrie ?
Ces questions sont valables sur 90 % des problèmes. Tu n'improvises pas, tu piches dans la liste.

**45-70 s — Écrire un exemple à la main.**
Trois lignes en commentaire, dont **une entrée vide**. Écrire un exemple débloque le cerveau
mieux que le fixer : la manipulation concrète réveille la mémoire des patterns.

**70-90 s — Écrire la signature et une force brute en commentaire.**
```python
def resoudre(mesures, seuil, k):
    # Naïf : pour chaque index, regarder les k suivants -> O(n*k)
    ...
```

Au bout de 90 secondes tu as : parlé, cadré, un exemple, une signature, une piste. Tu n'as
plus de page blanche. **Tu n'en auras plus jamais** si tu répètes ce script à chaque
entraînement — c'est précisément pour ça qu'il faut le répéter à l'entraînement.

---

## Toujours avoir une solution moche

> Une solution moche qui existe bat une solution élégante qui n'existe pas.

Écris la force brute **en premier**, même si tu vois l'optimisation. Elle te donne :
un filet de sécurité si le temps manque, une base de comparaison pour tes tests, une preuve
de ta compréhension, et un point de départ pour optimiser à voix haute.

Dis-le explicitement : *« je pars sur la version naïve en O(n²) pour avoir quelque chose de
correct, puis je l'améliore. »* Cette phrase est notée positivement, jamais l'inverse.

---

## L'escalier de déblocage — quand tu es coincé

Cinq marches, dans l'ordre, à voix haute. Ne saute pas de marche.

1. **Un exemple minuscule.** Que vaut la réponse pour 1 élément ? Pour 2 ? La récurrence
   entre les deux est souvent la solution complète.
2. **Enlever une contrainte.** « Si les données étaient triées, je saurais faire. » →
   alors trie, et paie O(n log n). Souvent, c'est la réponse attendue.
3. **La force brute, écrite pour de vrai.** Pas pensée : écrite. On voit presque toujours le
   calcul redondant qu'on peut mémoriser ou éliminer.
4. **La question magique.** *« Quelle structure de données me donnerait l'information dont
   j'ai besoin en O(1) ? »* Un dict ? Un set ? Un tas ? Une pile ? Cette seule question
   résout une large moitié des problèmes.
5. **Passer la liste des patterns.** Ouvre mentalement le tableau de `docs/patterns-algo.md`
   et teste-les un par un, à voix haute. « Fenêtre glissante ? Non, ce n'est pas contigu.
   Deux pointeurs ? Il faudrait que ce soit trié… »

**Après la marche 5, à la minute 12, demande un indice.** Explicitement :

> « J'hésite entre un tri préalable et une table de hachage. Est-ce que je pars dans la
> bonne direction ? »

Demander un indice en montrant ton raisonnement est **noté positivement**. Rester bloqué en
silence est noté négativement. Le choix est vite fait.

---

## Anti-code bâclé : trois règles non négociables

**1. Valider les entrées avant tout.** Première chose écrite dans le corps de la fonction :
```python
if k < 1:
    raise ValueError(f"k doit valoir au moins 1, reçu {k!r}")
```
Deux lignes, écrites quand tu es encore calme, qui cochent la case « cas limites » avant même
que le stress monte.

**2. Aucun nom de variable à une lettre**, sauf `i`, `j` d'index. `consecutifs`, pas `c`.
Sous stress on abrège ; c'est exactement ce qui donne l'impression d'un code jeté.

**3. Ne dis jamais « j'ai fini ».** Dis :
> « Je relis mes cas limites avant de valider. »

Puis déroule vraiment : liste vide, un élément, dernière itération de la boucle. Cette phrase
transforme la fin de l'entretien — le moment dont il se souviendra le plus — en démonstration
de rigueur au lieu d'une remise de copie.

---

## Le découpage des 45 minutes

| Minute | Ce que tu fais | Signal d'alarme |
|---|---|---|
| 0-5 | reformuler, questionner, exemples | tu codes déjà → **stop, remonte** |
| 5-10 | approche + complexité annoncée | rien à minute 12 → **demande un indice** |
| 10-30 | coder, en verbalisant | silence > 45 s → **dis ce que tu écris** |
| 30-40 | dérouler sur un cas limite | tu n'as pas testé → **c'est un axe perdu** |
| 40-45 | complexité finale, améliorations possibles | tu finis sur un bug → **verbalise la piste** |

Garde une montre visible. Regarder l'heure n'est pas impoli : c'est de la gestion de temps,
et ça se voit positivement.

---

## Le corps, avant la tête

Le stress n'est pas un état d'esprit, c'est de la physiologie. On agit dessus mécaniquement.

- **Expiration longue.** Inspire 4 s, expire 6 s, trois fois. L'expiration allongée fait
  redescendre le rythme cardiaque en une trentaine de secondes. Ça se fait pendant que tu lis
  l'énoncé, sans que personne le remarque.
- **Ralentis ton débit de 20 %.** Sous stress on parle vite, on saute des mots, on paraît
  paniqué. Parler lentement te fait paraître plus compétent **et** te laisse le temps de penser.
- **Bois une gorgée d'eau.** C'est cinq secondes de réflexion socialement invisibles. Aie
  toujours un verre à côté de toi.
- **Pieds au sol, dos droit, épaules basses.** La posture recroquevillée entretient l'anxiété.
- **Écris pendant que tu réfléchis.** Les mains occupées calment. Le blanc-page est pire les
  bras croisés.

---

## Rituel J-1 et J-0

**La veille :** aucun problème nouveau. Refais deux problèmes que tu **sais** résoudre —
l'objectif est le sentiment de compétence, pas l'apprentissage. Prépare le matériel :
éditeur, micro, caméra, connexion, une feuille et un stylo. Couche-toi tôt : le sommeil
affecte la résolution de problèmes bien plus que deux heures de révision supplémentaires.

**Le jour même :** 20 minutes avant, échauffe-toi sur un exercice facile déjà connu — comme
un musicien fait ses gammes. Ne jamais arriver « à froid ». Relis les 90 premières secondes
de ce document. Rien d'autre.

---

## Se relever pendant l'entretien

**Tu t'es trompé d'approche à la minute 25.** Ne t'accroche pas par orgueil, ne t'excuse pas
non plus. Dis :
> « Mon approche casse sur le cas où toutes les valeurs sont identiques. Je reprends avec
> une table de hachage, ça règle ce cas. »

Verbaliser une erreur et pivoter proprement est un **signal positif** sur trois axes à la
fois. Beaucoup de candidats retenus se sont trompés en cours de route.

**Tu ne connais pas la notion.** Jamais de bluff — il le verra en une question.
> « Je n'ai pas manipulé de tri topologique. En revanche j'ai un parcours en profondeur avec
> détection de cycle, je peux partir de là. »

**Tu paniques.** Reviens à la marche 1 de l'escalier : un exemple minuscule. Toujours. Il n'y
a pas d'autre porte de sortie, et il y en a toujours une.

---

## Banque de phrases prêtes à l'emploi

À relire jusqu'à ce qu'elles sortent toutes seules. Sous stress, on ne compose pas — on récite.

- « Je reformule pour être sûr d'avoir compris. »
- « Avant de coder, j'ai deux questions. »
- « Je note ce cas limite, j'y reviens après avoir posé la structure. »
- « Naïvement c'est O(n²) ; je pense pouvoir descendre à O(n) avec un dictionnaire. »
- « Je pars sur quelque chose de correct, puis j'optimise. »
- « Je verbalise ce que j'écris : cette boucle parcourt… »
- « Est-ce que je peux avoir un indice sur la structure de données ? »
- « Bonne remarque — effectivement, ça casse si la liste est vide. Je corrige. »
- « Je relis mes cas limites avant de valider. »
- « Avec dix minutes de plus, je testerais avec hypothesis contre la version naïve. »

---

## Après l'entretien

Dix minutes de débrief à chaud, écrites, dans `NOTES.md` : le problème posé, ce que tu as
trouvé seul, où tu as bloqué, ce que tu dirais autrement. Puis tu passes à autre chose.

Ruminer trois jours ne change pas le résultat et abîme l'entretien suivant. Et garde en tête
une chose que le format fait facilement oublier : **un entretien mesure une performance de
45 minutes, pas ta valeur d'ingénieur**. Des gens excellents ratent des entretiens. La
préparation ne sert pas à devenir quelqu'un d'autre — elle sert à ce que ces 45 minutes
montrent ce que tu sais déjà faire.
