# Backlog d'exercices à créer

Thèmes choisis pour ressembler à ce qui tombe en entretien sur des profils orientés
données/instrumentation : séries de mesures, capteurs, journaux d'événements.

Créer un exercice : `make new NOM=detection-pics`

## Fenêtre glissante et séries

- [ ] 004 — Plus longue plage sans dépassement de seuil
- [ ] 005 — Détection de pic : valeur supérieure à ses deux voisines, avec plateau
- [ ] 006 — Hystérésis : alerte à 80 °C, ne retombe qu'en dessous de 70 °C
- [ ] 007 — Compression d'une série par run-length encoding (`[1,1,2] -> [(1,2),(2,1)]`)
- [ ] 008 — Rééchantillonnage : agréger des mesures horodatées par tranches de 5 min

## Table de hachage et comptage

- [ ] 009 — Capteur le plus bavard : top-k des identifiants d'un journal
- [ ] 010 — Première mesure non répétée d'un flux
- [ ] 011 — Deux séries contiennent-elles les mêmes valeurs à permutation près ?
- [ ] 012 — Déduplication d'événements avec fenêtre temporelle (même id sous 30 s = doublon)

## Tri, intervalles, deux pointeurs

- [ ] 013 — Fusionner deux séries triées par horodatage
- [ ] 014 — Nombre maximal de capteurs simultanément en panne (balayage d'événements)
- [ ] 015 — Paire de mesures dont l'écart est le plus proche d'une cible

## Pile, file, structures

- [ ] 016 — Prochaine mesure supérieure à chaque mesure (pile décroissante)
- [ ] 017 — Médiane glissante avec deux tas
- [ ] 018 — Cache LRU des dernières lectures capteur

## Graphes et dépendances

- [ ] 019 — Ordre de démarrage de modules avec dépendances (tri topologique)
- [ ] 020 — Composantes connexes d'un réseau de capteurs

## Conception / oral

- [ ] 021 — Concevoir une API de règles d'alerte configurables (sans coder : classes, tests, extensibilité)
- [ ] 022 — Comment testerais-tu une fonction dont le résultat dépend de l'heure ?
