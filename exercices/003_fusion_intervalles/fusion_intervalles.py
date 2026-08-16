"""003 — Fusion d'intervalles de panne. Voir ENONCE.md."""

from __future__ import annotations

from collections.abc import Iterable

Intervalle = tuple[float, float]


def fusionner(intervalles: Iterable[Intervalle]) -> list[Intervalle]:
    """Niveau 1 : intervalles fusionnés, triés, sans chevauchement."""
    raise NotImplementedError


def duree_couverte(intervalles: Iterable[Intervalle]) -> float:
    """Niveau 2 : durée totale couverte, sans double comptage."""
    raise NotImplementedError
