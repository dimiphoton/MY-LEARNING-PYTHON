import random

import pytest

from harness import charger

exo = charger("moyenne_glissante")
moyennes_glissantes = exo.moyennes_glissantes
maxima_glissants = exo.maxima_glissants


@pytest.mark.parametrize(
    "mesures, k, attendu",
    [
        ([1, 2, 3, 4], 2, [1.5, 2.5, 3.5]),
        ([1, 2, 3], 1, [1, 2, 3]),
        ([1, 2, 3], 3, [2]),
        ([1, 2, 3], 4, []),
        ([], 1, []),
        ([-2, -4], 2, [-3]),
        ([5.5, 4.5], 2, [5.0]),
    ],
)
def test_moyennes_glissantes(mesures, k, attendu):
    assert moyennes_glissantes(mesures, k) == pytest.approx(attendu)


@pytest.mark.parametrize(
    "mesures, k, attendu",
    [
        ([1, 3, 2, 5, 4], 3, [3, 5, 5]),
        ([1, 2, 3], 1, [1, 2, 3]),
        ([3, 3, 3], 2, [3, 3]),          # doublons : ne pas perdre le max
        ([5, 4, 3, 2], 2, [5, 4, 3]),    # décroissant : le max sort de la fenêtre
        ([1, 2, 3, 4], 4, [4]),
        ([1, 2], 3, []),
        ([], 2, []),
        ([-5, -1, -9], 2, [-1, -1]),
    ],
)
def test_maxima_glissants(mesures, k, attendu):
    assert maxima_glissants(mesures, k) == pytest.approx(attendu)


@pytest.mark.parametrize("fonction_nom", ["moyennes_glissantes", "maxima_glissants"])
@pytest.mark.parametrize("k", [0, -3])
def test_k_invalide(fonction_nom, k):
    with pytest.raises(ValueError):
        getattr(exo, fonction_nom)([1, 2, 3], k)


@pytest.mark.parametrize("fonction_nom", ["moyennes_glissantes", "maxima_glissants"])
def test_nombre_de_fenetres(fonction_nom):
    mesures = list(range(20))
    for k in range(1, 21):
        assert len(getattr(exo, fonction_nom)(mesures, k)) == len(mesures) - k + 1


def test_maxima_contre_implementation_naive():
    """Test aléatoire contre la version O(n*k) évidemment correcte."""
    random.seed(0)
    for _ in range(50):
        mesures = [random.randint(-50, 50) for _ in range(random.randint(1, 40))]
        k = random.randint(1, len(mesures))
        naif = [max(mesures[i : i + k]) for i in range(len(mesures) - k + 1)]
        assert maxima_glissants(mesures, k) == naif


def test_entree_non_modifiee():
    mesures = [1, 2, 3, 4]
    copie = list(mesures)
    moyennes_glissantes(mesures, 2)
    maxima_glissants(mesures, 2)
    assert mesures == copie
