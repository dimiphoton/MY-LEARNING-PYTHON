#!/usr/bin/env python3
"""Crée le squelette d'un nouvel exercice.

Usage :
    python outils/nouvel_exo.py detection-pics
    make new NOM=detection-pics

Génère :
    exercices/00X_detection_pics/{ENONCE.md, detection_pics.py, test_detection_pics.py, NOTES.md}
    corriges/00X_detection_pics/detection_pics.py
"""

from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

RACINE = Path(__file__).resolve().parents[1]
EXERCICES = RACINE / "exercices"
CORRIGES = RACINE / "corriges"

ENONCE = """# {numero} — {titre}

**Thème :** ...  — **Difficulté :** ...
**Temps cible :** 25 min.

## Contexte

...

## Conventions

- ...
- Paramètre invalide → `ValueError`.

## Niveau 1

```python
resoudre(...) -> ...
```

Exemple : `resoudre(...)` → `...`

## Niveau 2

...

## Ce qui est évalué

| Critère | Attendu |
|---|---|
| Complexité | O(?) temps, O(?) mémoire |
| Cas limites | vide, un élément, paramètre invalide |
| Robustesse | l'entrée n'est pas modifiée |

## Pièges classiques

- ...
"""

STUB = '''"""{numero} — {titre}. Voir ENONCE.md."""

from __future__ import annotations


def resoudre():
    """..."""
    raise NotImplementedError
'''

CORRIGE = '''"""{numero} — Corrigé."""

from __future__ import annotations


def resoudre():
    """..."""
    raise NotImplementedError
'''

TEST = '''import pytest

from harness import charger

exo = charger("{module}")
resoudre = exo.resoudre


@pytest.mark.parametrize(
    "entree, attendu",
    [
        # (..., ...),
    ],
)
def test_resoudre(entree, attendu):
    assert resoudre(entree) == attendu


def test_cas_vide():
    ...


def test_parametre_invalide():
    ...


def test_entree_non_modifiee():
    ...
'''

NOTES = """# Notes de session

À remplir **après** chaque tentative, avant de regarder le corrigé.

| Date | Temps passé | Niveau atteint | Tests au vert du 1er coup ? |
|---|---|---|---|
|  |  |  |  |

## Complexité que j'ai annoncée
Temps : ...  Mémoire : ...

## Cas limites auxquels j'ai pensé seul

-

## Cas limites que les tests m'ont appris

-

## Ce que je dirais à voix haute en entretien (2 phrases)

-

## À revoir dans 7 jours ? oui / non
"""


def normaliser(nom: str) -> str:
    """'Détection de pics !' -> 'detection_de_pics'"""
    sans_accent = unicodedata.normalize("NFKD", nom).encode("ascii", "ignore").decode()
    slug = re.sub(r"[^a-zA-Z0-9]+", "_", sans_accent).strip("_").lower()
    if not slug:
        raise SystemExit("Nom d'exercice vide après normalisation.")
    return slug


def prochain_numero() -> str:
    numeros = [
        int(chemin.name[:3])
        for chemin in EXERCICES.iterdir()
        if chemin.is_dir() and chemin.name[:3].isdigit()
    ]
    return f"{max(numeros, default=0) + 1:03d}"


def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit("Usage : python outils/nouvel_exo.py <nom-de-l-exercice>")

    module = normaliser(" ".join(sys.argv[1:]))
    numero = prochain_numero()
    dossier_nom = f"{numero}_{module}"
    titre = module.replace("_", " ").capitalize()

    dossier = EXERCICES / dossier_nom
    if dossier.exists():
        raise SystemExit(f"{dossier} existe déjà.")
    dossier.mkdir(parents=True)
    (CORRIGES / dossier_nom).mkdir(parents=True, exist_ok=True)

    (dossier / "ENONCE.md").write_text(
        ENONCE.format(numero=numero, titre=titre), encoding="utf-8"
    )
    (dossier / f"{module}.py").write_text(
        STUB.format(numero=numero, titre=titre), encoding="utf-8"
    )
    (dossier / f"test_{module}.py").write_text(TEST.format(module=module), encoding="utf-8")
    (dossier / "NOTES.md").write_text(NOTES, encoding="utf-8")
    (CORRIGES / dossier_nom / f"{module}.py").write_text(
        CORRIGE.format(numero=numero), encoding="utf-8"
    )

    print(f"Créé : exercices/{dossier_nom}/")
    print(f"       corriges/{dossier_nom}/{module}.py")
    print(f"Lancer : make exo EXO={dossier_nom}")


if __name__ == "__main__":
    main()
