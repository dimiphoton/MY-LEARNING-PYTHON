# Méthode : les 25 minutes d'un entretien de codage

Le recruteur n'évalue pas seulement le code final. Il évalue **la façon dont tu y arrives**.
Un candidat qui pond la solution optimale en silence passe souvent après un candidat qui
verbalise, teste et se corrige. Suis toujours les six étapes, dans l'ordre.

## 1. Reformuler et clarifier (2 min)

Ne code pas avant d'avoir posé au moins deux questions. Sur l'exemple des températures :

- Les mesures arrivent-elles **toutes d'un coup** ou **en flux** ? (ça change tout : liste vs O(1))
- Le seuil est-il atteint avec `>` ou `>=` ?
- Que fait-on d'une mesure **manquante** ? Elle rompt la série ou on l'ignore ?
- Quelle taille de données ? 100 points ou 10 milliards ?
- Faut-il **détecter** l'alerte ou la **localiser** ?

Une question bien posée vaut plus qu'une ligne de code : elle montre que tu penses production.

## 2. Écrire les exemples à la main (3 min)

Écris 3 exemples dans le fichier, en commentaire, dont **un cas limite** :

```
[18, 31, 32, 19], seuil=30, k=2  -> True
[31, 19, 31],     seuil=30, k=2  -> False   (isolés)
[],               seuil=30, k=2  -> False   (vide)
```

C'est ton contrat. Fais-le valider : « on est d'accord sur ces trois-là ? »

## 3. Annoncer l'approche AVANT de coder (3 min)

Dis la version naïve, dis sa complexité, dis pourquoi tu ne la prends pas :

> « Naïvement, je regarde chaque fenêtre de k éléments : O(n·k). Mais un simple compteur
> de dépassements consécutifs suffit, ça descend à O(n) temps et O(1) mémoire. Je pars là-dessus. »

Cette phrase à elle seule fait passer un entretien sur deux.

## 4. Coder proprement (10 min)

- Signature typée, docstring d'une ligne.
- Valider les entrées en premier (`if k < 1: raise ValueError`).
- Noms explicites : `consecutifs`, pas `c`. `mesures`, pas `data`.
- Une fonction = une idée. Une petite fonction privée (`_depasse`) vaut mieux qu'un
  commentaire qui explique une condition tordue.
- Pas d'astuce illisible pour gagner deux lignes.

## 5. Dérouler le code à voix haute sur un exemple (4 min)

Prends ton cas limite et exécute mentalement, en annonçant l'état des variables.
**C'est là qu'on trouve ses propres bugs** — et un bug que tu trouves seul est un point gagné,
pas un point perdu. Vérifie systématiquement :
la sortie de boucle, la dernière itération, l'initialisation.

## 6. Proposer la suite (3 min)

Termine toujours par une ouverture, ça montre du recul :

> « Si le flux est infini, je passe sur une classe avec un compteur. Si on veut éviter le
> clignotement autour du seuil, on ajoute une hystérésis. Et je testerais avec hypothesis
> contre une implémentation naïve. »

## Erreurs qui coûtent le poste

| Erreur | Ce que le recruteur en conclut |
|---|---|
| Coder immédiatement sans question | ne saura pas cadrer un besoin flou |
| Rester muet 5 minutes | impossible de travailler en binôme |
| Ne jamais tester son code | livrera des bugs |
| Ignorer la liste vide | ne pense pas aux cas limites |
| Dire « ça marche » sans vérifier | excès de confiance |
| Refuser un indice | mauvais collègue |

## Protocole d'entraînement recommandé

1. `make chrono` (25 min) et tu ouvres `ENONCE.md`.
2. Tu écris **le test qui te manque** avant le code, si tu vois un cas limite non couvert.
3. `make exo EXO=001_alerte_temperature` jusqu'au vert.
4. Tu remplis `NOTES.md` **avant** d'ouvrir le corrigé.
5. Tu compares avec `corriges/`, tu notes une seule chose à retenir.
6. Tu reprends l'exercice **7 jours plus tard**, sans les notes.
