"""003 — Corrigé."""

from __future__ import annotations

from collections.abc import Iterable

Intervalle = tuple[float, float]


def fusionner(intervalles: Iterable[Intervalle]) -> list[Intervalle]:
    """Tri par début, puis un seul balayage. O(n log n)."""
    tries = sorted(intervalles)  # sorted, pas .sort() : on ne touche pas à l'entrée
    for debut, fin in tries:
        if fin < debut:
            raise ValueError(f"intervalle invalide : ({debut!r}, {fin!r})")

    fusionnes: list[Intervalle] = []
    for debut, fin in tries:
        if fusionnes and debut <= fusionnes[-1][1]:
            # Chevauchement ou contiguïté : on étend la fin courante.
            debut_courant, fin_courante = fusionnes[-1]
            fusionnes[-1] = (debut_courant, max(fin_courante, fin))
        elif fin > debut:  # un intervalle vide isolé ne couvre rien
            fusionnes.append((debut, fin))

    return fusionnes


def duree_couverte(intervalles: Iterable[Intervalle]) -> float:
    """Somme des longueurs après fusion."""
    return sum(fin - debut for debut, fin in fusionner(intervalles))
