"""001 — Alerte température. Voir ENONCE.md.

À compléter. Ne modifie pas les signatures : les tests s'appuient dessus.
"""

from __future__ import annotations

from collections.abc import Iterable


def alerte_detectee(mesures: Iterable[float | None], seuil: float, k: int) -> bool:
    """Niveau 1 : y a-t-il au moins k dépassements stricts consécutifs ?"""
    raise NotImplementedError


def plages_alerte(
    mesures: Iterable[float | None], seuil: float, k: int
) -> list[tuple[int, int]]:
    """Niveau 2 : plages maximales (début, fin) inclusives de longueur >= k."""
    raise NotImplementedError


class DetecteurAlerte:
    """Niveau 3 : détection en flux, mémoire O(1)."""

    def __init__(self, seuil: float, k: int) -> None:
        raise NotImplementedError

    def ajouter(self, mesure: float | None) -> bool:
        """True uniquement à l'instant où le compteur atteint k."""
        raise NotImplementedError
