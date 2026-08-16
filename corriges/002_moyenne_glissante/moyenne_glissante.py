"""002 — Corrigé."""

from __future__ import annotations

from collections import deque
from collections.abc import Sequence


def _valider(mesures: Sequence[float], k: int) -> bool:
    if k < 1:
        raise ValueError(f"k doit valoir au moins 1, reçu {k!r}")
    return k <= len(mesures)


def moyennes_glissantes(mesures: Sequence[float], k: int) -> list[float]:
    """Somme courante : on ajoute l'entrant, on retire le sortant. O(n)."""
    if not _valider(mesures, k):
        return []

    somme = sum(mesures[:k])
    resultat = [somme / k]
    for i in range(k, len(mesures)):
        somme += mesures[i] - mesures[i - k]
        resultat.append(somme / k)
    return resultat


def maxima_glissants(mesures: Sequence[float], k: int) -> list[float]:
    """Deque d'index, valeurs décroissantes. Chaque index entre et sort une fois : O(n)."""
    if not _valider(mesures, k):
        return []

    candidats: deque[int] = deque()  # index, mesures[candidats] décroissant
    resultat: list[float] = []

    for i, valeur in enumerate(mesures):
        # L'index de tête est-il sorti de la fenêtre ?
        if candidats and candidats[0] <= i - k:
            candidats.popleft()
        # Tout candidat plus petit que l'entrant ne pourra plus jamais être max.
        while candidats and mesures[candidats[-1]] <= valeur:
            candidats.pop()
        candidats.append(i)

        if i >= k - 1:
            resultat.append(mesures[candidats[0]])

    return resultat
