import random

import pytest

from harness import charger

exo = charger("fusion_intervalles")
fusionner = exo.fusionner
duree_couverte = exo.duree_couverte


@pytest.mark.parametrize(
    "intervalles, attendu",
    [
        ([], []),
        ([(0, 5)], [(0, 5)]),
        ([(5, 9), (0, 5), (12, 14), (13, 20)], [(0, 9), (12, 20)]),
        ([(0, 10), (2, 5)], [(0, 10)]),               # inclusion totale
        ([(0, 10), (2, 3), (4, 12)], [(0, 12)]),      # comparer à la fin fusionnée
        ([(0, 5), (5, 9)], [(0, 9)]),                 # contiguïté : semi-ouvert -> fusion
        ([(0, 5), (6, 9)], [(0, 5), (6, 9)]),         # trou de 1 : pas de fusion
        ([(3, 3)], []),                               # intervalle vide isolé
        ([(0, 5), (3, 3)], [(0, 5)]),                 # intervalle vide absorbé
        ([(10, 20), (0, 5)], [(0, 5), (10, 20)]),     # entrée non triée
        ([(0.5, 1.5), (1.0, 2.0)], [(0.5, 2.0)]),     # flottants
    ],
)
def test_fusionner(intervalles, attendu):
    assert fusionner(intervalles) == attendu


def test_intervalle_invalide():
    with pytest.raises(ValueError):
        fusionner([(5, 2)])


def test_entree_non_modifiee():
    intervalles = [(10, 20), (0, 5)]
    copie = list(intervalles)
    fusionner(intervalles)
    assert intervalles == copie


@pytest.mark.parametrize(
    "intervalles, attendu",
    [
        ([], 0),
        ([(0, 10), (2, 5)], 10),
        ([(0, 5), (5, 9)], 9),
        ([(0, 5), (6, 9)], 8),
    ],
)
def test_duree_couverte(intervalles, attendu):
    assert duree_couverte(intervalles) == pytest.approx(attendu)


def test_sortie_triee_et_disjointe():
    random.seed(1)
    for _ in range(50):
        intervalles = []
        for _ in range(random.randint(0, 12)):
            debut = random.randint(0, 30)
            intervalles.append((debut, debut + random.randint(0, 8)))
        resultat = fusionner(intervalles)
        assert resultat == sorted(resultat)
        for (_, fin), (debut_suivant, _) in zip(resultat, resultat[1:], strict=False):
            assert fin < debut_suivant, "les intervalles fusionnés se touchent encore"


def test_duree_contre_implementation_naive():
    """Comparaison avec un comptage brut d'unités de temps occupées."""
    random.seed(2)
    for _ in range(50):
        intervalles = []
        for _ in range(random.randint(0, 10)):
            debut = random.randint(0, 40)
            intervalles.append((debut, debut + random.randint(0, 6)))
        occupe = set()
        for debut, fin in intervalles:
            occupe.update(range(debut, fin))
        assert duree_couverte(intervalles) == len(occupe)
