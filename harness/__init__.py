"""Chargeur de modules d'exercice.

Les tests importent le code via `charger("nom_du_module")`.
Par defaut le module charge est celui de l'exercice (ton code).
Avec la variable d'environnement CORRIGE=1, c'est le corrige qui est teste :
cela permet de verifier que les tests eux-memes sont corrects (utilise par la CI).
"""

from __future__ import annotations

import importlib.util
import inspect
import os
import sys
from pathlib import Path
from types import ModuleType

RACINE = Path(__file__).resolve().parents[1]


def charger(nom_module: str) -> ModuleType:
    """Charge `<nom_module>.py` situe a cote du fichier de test appelant."""
    dossier_test = Path(inspect.stack()[1].filename).resolve().parent

    if os.environ.get("CORRIGE") == "1":
        chemin = RACINE / "corriges" / dossier_test.name / f"{nom_module}.py"
    else:
        chemin = dossier_test / f"{nom_module}.py"

    if not chemin.exists():
        raise FileNotFoundError(f"Module introuvable : {chemin}")

    nom_unique = f"{dossier_test.name}__{nom_module}"
    spec = importlib.util.spec_from_file_location(nom_unique, chemin)
    module = importlib.util.module_from_spec(spec)
    sys.modules[nom_unique] = module
    spec.loader.exec_module(module)
    return module
