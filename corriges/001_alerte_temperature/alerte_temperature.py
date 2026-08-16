"""001 — Corrigé. Un seul balayage, mémoire O(1).

Idée commune aux trois niveaux : on ne garde qu'un compteur de dépassements
consécutifs. Aucune fenêtre n'est recalculée, donc O(n) et pas O(n·k).
"""

from __future__ import annotations

from collections.abc import Iterable


def _valider_k(k: int) -> None:
    if k < 1:
        raise ValueError(f"k doit valoir au moins 1, reçu {k!r}")


def _depasse(mesure: float | None, seuil: float) -> bool:
    return mesure is not None and mesure > seuil


def alerte_detectee(mesures: Iterable[float | None], seuil: float, k: int) -> bool:
    """True si k dépassements stricts consécutifs au moins apparaissent."""
    _valider_k(k)
    consecutifs = 0
    for mesure in mesures:
        consecutifs = consecutifs + 1 if _depasse(mesure, seuil) else 0
        if consecutifs >= k:
            return True
    return False


def plages_alerte(
    mesures: Iterable[float | None], seuil: float, k: int
) -> list[tuple[int, int]]:
    """Plages maximales (début, fin) inclusives de dépassements, de longueur >= k."""
    _valider_k(k)
    plages: list[tuple[int, int]] = []
    debut: int | None = None
    index = -1

    for index, mesure in enumerate(mesures):
        if _depasse(mesure, seuil):
            if debut is None:
                debut = index
        elif debut is not None:
            if index - debut >= k:
                plages.append((debut, index - 1))
            debut = None

    # Ne pas oublier la plage encore ouverte à la fin du flux.
    if debut is not None and index - debut + 1 >= k:
        plages.append((debut, index))

    return plages


class DetecteurAlerte:
    """Détection en flux : un compteur, un verrou, rien d'autre."""

    def __init__(self, seuil: float, k: int) -> None:
        _valider_k(k)
        self.seuil = seuil
        self.k = k
        self._consecutifs = 0
        self._deja_declenche = False

    def ajouter(self, mesure: float | None) -> bool:
        if not _depasse(mesure, self.seuil):
            self._consecutifs = 0
            self._deja_declenche = False
            return False

        self._consecutifs += 1
        if self._consecutifs >= self.k and not self._deja_declenche:
            self._deja_declenche = True
            return True
        return False
