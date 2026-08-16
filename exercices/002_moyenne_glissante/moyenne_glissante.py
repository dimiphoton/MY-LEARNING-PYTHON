"""002 — Moyenne et maximum glissants. Voir ENONCE.md."""

from __future__ import annotations

from collections.abc import Sequence


def moyennes_glissantes(mesures: Sequence[float], k: int) -> list[float]:
    """Niveau 1 : moyenne de chaque fenêtre de taille k, en O(n)."""
    raise NotImplementedError


def maxima_glissants(mesures: Sequence[float], k: int) -> list[float]:
    """Niveau 2 : maximum de chaque fenêtre de taille k, en O(n)."""
    raise NotImplementedError
