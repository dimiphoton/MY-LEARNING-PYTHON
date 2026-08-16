"""Rend le paquet `harness` importable depuis n'importe quel fichier de test."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
