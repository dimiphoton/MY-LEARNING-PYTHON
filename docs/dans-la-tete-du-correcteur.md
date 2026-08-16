# Dans la tête du correcteur

Tu ne prépares pas un examen. Tu prépares **la fiche d'évaluation qu'une personne va remplir
sur toi**, puis défendre devant ses collègues. Comprendre ce document change complètement la
façon de se comporter pendant 45 minutes.

---

## Sa situation, que tu ignores probablement

La personne en face de toi n'est pas un juge. C'est un ingénieur qui :

- **a du travail par ailleurs** — ton entretien s'intercale entre deux réunions ;
- **doit rendre un compte-rendu écrit**, souvent le jour même, avec une recommandation
  tranchée : on embauche, ou pas ;
- **devra la défendre** face à des collègues qui ne t'ont jamais vu, à partir de ses notes ;
- **a peur de se tromper** dans les deux sens : faire passer quelqu'un qui échoue lui coûtera
  sa crédibilité ; recaler quelqu'un de bon ne se saura jamais. Ce déséquilibre explique la
  sévérité apparente du processus.

**Conséquence pratique, et c'est la clé de tout ce document :** il a besoin de **preuves
citables**. Ton objectif n'est pas d'être bon, c'est d'être **facile à défendre**. Chaque
phrase que tu prononces à voix haute est une ligne qu'il peut recopier dans son compte-rendu.
Ce que tu penses sans le dire n'existe pas.

---

## Les quatre axes de la fiche

La plupart des grilles, quel que soit l'employeur, reviennent à ces quatre-là.

### 1. Résolution de problème
*Est-ce que la personne sait passer d'un énoncé flou à une approche justifiée ?*

Il observe : les questions de cadrage, la capacité à sortir un exemple, l'identification du
pattern, l'annonce d'une complexité, le choix argumenté entre deux approches.
Il se moque de savoir si tu as déjà vu le problème. Il regarde le **chemin**.

### 2. Codage
*Est-ce que je relirais ce code en revue sans soupirer ?*

Il observe : noms de variables, découpage, gestion des cas d'erreur, absence de code mort,
usage naturel du langage. Une syntaxe oubliée ne coûte rien. Une variable nommée `x2` qui
contient un seuil, si.

### 3. Vérification
*Est-ce que la personne teste son propre code, ou attend-elle que je trouve les bugs ?*

C'est l'axe le plus discriminant et le plus négligé. Dérouler son code à la main sur un cas
limite, **spontanément**, avant qu'on te le demande, place immédiatement au-dessus de la
moyenne des candidats.

### 4. Communication
*Est-ce que je peux travailler avec cette personne ?*

Il observe : le fil de la pensée pendant que tu codes, la réaction à une remarque, la capacité
à dire « je ne sais pas », le calme. Un candidat brillant et silencieux se fait souvent
recaler. Un candidat correct et clair passe souvent.

**La règle qui surprend :** un axe très faible suffit à couler la candidature, même avec trois
axes excellents. On ne cherche pas un pic, on cherche l'absence de trou.

---

## Le test implicite qu'aucune grille ne mentionne

> *« Est-ce que j'ai envie de débugger un incident de production à 23 h avec cette personne ? »*

Il y répond en réalité dans les cinq premières minutes, puis passe le reste de l'entretien à
chercher des raisons de confirmer. Ce que ça implique : ton attitude sur les questions de
cadrage compte davantage que ta performance sur les vingt dernières lignes.

---

## Signaux, en clair

| Ce qu'il voit | Ce qu'il écrit |
|---|---|
| Tu poses 2-3 questions avant de coder | « cadre le besoin avant d'agir » |
| Tu annonces la naïve, sa complexité, puis tu l'améliores | « raisonne en coûts, pas en réflexes » |
| Tu écris un exemple à la main | « méthodique » |
| Tu trouves ton propre bug en déroulant le code | **« se relit — signal fort »** |
| Tu dis « je ne connais pas, voilà comment je m'y prendrais » | « honnête et débrouillard » |
| Tu intègres son indice et tu le remercies | « collaboratif » |
| Tu proposes une amélioration à la fin | « a du recul » |

| Ce qu'il voit | Ce qu'il écrit |
|---|---|
| Tu codes dans les 30 secondes | « fonce sans cadrer » |
| Tu es muet plusieurs minutes | « impossible d'évaluer le raisonnement » |
| Tu dis « ça marche » sans vérifier | **« excès de confiance — signal négatif fort »** |
| Tu ignores sa remarque ou tu te braques | « n'entend pas les retours » (souvent rédhibitoire) |
| Tu bricoles le code jusqu'à ce que les tests passent | « n'a pas compris son propre code » |
| Tu récites une solution mémorisée sans pouvoir l'expliquer | « a appris par cœur » |
| Tu oublies la liste vide et tu n'y reviens pas | « ne pense pas aux cas limites » |

---

## Décoder ses interventions

Il parle rarement pour rien. Traduction :

| Il dit | Il pense |
|---|---|
| « Es-tu sûr de cette ligne ? » | **Il y a un bug à cette ligne.** Relis-la vraiment. |
| « Et si le tableau est vide ? » | Tu as oublié un cas limite ; il te tend une perche. |
| « Peux-tu faire mieux ? » | Ta complexité n'est pas celle attendue. |
| « Pourquoi ce choix ? » | Soit c'est douteux, soit il vérifie que ce n'est pas du hasard. |
| « On peut passer à la suite » | Il a assez de matière ici, ou il abandonne cette piste. |
| Un long silence | Il prend des notes, **ou** il te laisse délibérément te débrouiller. |
| « Ne t'inquiète pas pour la syntaxe » | La syntaxe ne compte pas, le raisonnement oui. |

Un indice n'est **jamais** une punition. C'est un investissement : il continue à dépenser du
temps sur toi. Le refuser, c'est gâcher ce qu'il vient de t'offrir.

---

## Ce qu'il pardonne, et ce qu'il ne pardonne pas

**Pardonné sans difficulté :** oublier un nom de méthode, se tromper puis se corriger, avoir
besoin d'un indice, ne pas finir le niveau bonus, être visiblement nerveux au début, écrire
une première version naïve.

**Rarement pardonné :** affirmer une complexité fausse avec assurance, prétendre connaître un
sujet inconnu, ignorer un cas limite signalé, ne pas tester, se braquer sur une critique,
traiter l'exercice comme absurde ou en dessous de soi.

Le fil commun : ce qui est pardonné relève de la **compétence** — ça s'acquiert. Ce qui ne
l'est pas relève du **comportement** — ça ne se corrige pas en trois mois d'onboarding.

---

## Ses biais, à ton avantage

- **Effet de primauté.** Les cinq premières minutes pèsent anormalement lourd. Soigne le
  cadrage : c'est le moment le plus rentable de l'entretien.
- **Effet de récence.** Il se souvient surtout de la fin. Ne termine jamais sur un bug ouvert :
  même sans le résoudre, conclus par « voilà ce que je ferais avec dix minutes de plus ».
- **Fluidité.** Un raisonnement énoncé calmement paraît meilleur qu'un raisonnement équivalent
  débité en panique. Ralentir ton débit améliore mécaniquement ta note.
- **Effort perçu.** Il valorise la personne qui se bat proprement. L'abandon poli
  (« bon, je sèche ») est jugé plus durement que l'échec en luttant à voix haute.

---

## Ta grille d'auto-évaluation

À recopier dans `NOTES.md` après chaque session, note de 1 à 4 (1 = non-embauche nette,
4 = embauche évidente) :

| Axe | Note | Preuve concrète que j'ai donnée |
|---|---|---|
| Résolution de problème | /4 | |
| Codage | /4 | |
| Vérification | /4 | |
| Communication | /4 | |

Puis la seule question qui compte : **quelle phrase exacte le correcteur pourrait-il recopier
dans son compte-rendu pour justifier un « oui » ?** Si tu ne trouves pas cette phrase, c'est
que tu ne l'as pas prononcée — pas que tu ne la méritais pas.
