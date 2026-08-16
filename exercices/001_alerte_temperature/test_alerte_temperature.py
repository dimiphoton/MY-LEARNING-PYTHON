import pytest

from harness import charger

exo = charger("alerte_temperature")
alerte_detectee = exo.alerte_detectee
plages_alerte = exo.plages_alerte
DetecteurAlerte = exo.DetecteurAlerte


# --------------------------------------------------------------------------
# Niveau 1
# --------------------------------------------------------------------------
@pytest.mark.parametrize(
    "mesures, seuil, k, attendu",
    [
        ([], 30, 2, False),                      # séquence vide
        ([31], 30, 1, True),                     # k = 1
        ([31], 30, 2, False),                    # k > len
        ([31, 32, 33], 30, 4, False),            # jamais assez long
        ([18, 31, 32, 19], 30, 2, True),         # cas nominal
        ([31, 19, 31, 19, 31], 30, 2, False),    # dépassements isolés
        ([30, 30, 30], 30, 2, False),            # égalité au seuil = pas de dépassement
        ([31, None, 31], 30, 2, False),          # None rompt la série
        ([31, 31, None, 31], 30, 2, True),       # alerte avant le trou
        ([-5, -4, -3], -10, 3, True),            # seuil négatif
        ([18, 19, 31, 32], 30, 2, True),         # alerte en fin de séquence
    ],
)
def test_alerte_detectee(mesures, seuil, k, attendu):
    assert alerte_detectee(mesures, seuil, k) is attendu


def test_alerte_detectee_accepte_un_generateur():
    flux = (t for t in [18, 31, 32, 19])
    assert alerte_detectee(flux, 30, 2) is True


def test_alerte_detectee_ne_modifie_pas_l_entree():
    mesures = [31, 32, 19]
    copie = list(mesures)
    alerte_detectee(mesures, 30, 2)
    assert mesures == copie


@pytest.mark.parametrize("k", [0, -1])
def test_k_invalide_leve_valueerror(k):
    with pytest.raises(ValueError):
        alerte_detectee([31, 32], 30, k)
    with pytest.raises(ValueError):
        plages_alerte([31, 32], 30, k)


# --------------------------------------------------------------------------
# Niveau 2
# --------------------------------------------------------------------------
@pytest.mark.parametrize(
    "mesures, seuil, k, attendu",
    [
        ([], 30, 1, []),
        ([31, 32, 33, 10, 40, 41], 30, 2, [(0, 2), (4, 5)]),
        ([31, 32, 33], 30, 2, [(0, 2)]),                  # plage maximale, pas 2 fenêtres
        ([31, 32, 33], 30, 3, [(0, 2)]),
        ([31, 32, 33], 30, 4, []),
        ([10, 31, 10, 31, 10], 30, 1, [(1, 1), (3, 3)]),  # plages d'un élément
        ([31, None, 31, 31], 30, 2, [(2, 3)]),            # le trou coupe la plage
        ([10, 10, 31, 31], 30, 2, [(2, 3)]),              # plage close par la fin
    ],
)
def test_plages_alerte(mesures, seuil, k, attendu):
    assert plages_alerte(mesures, seuil, k) == attendu


def test_plages_coherentes_avec_le_booleen():
    mesures = [10, 31, 32, 10, 33, 34, 35]
    for k in range(1, 5):
        assert bool(plages_alerte(mesures, 30, k)) is alerte_detectee(mesures, 30, k)


# --------------------------------------------------------------------------
# Niveau 3 — flux
# --------------------------------------------------------------------------
def test_detecteur_declenche_une_seule_fois_par_plage():
    d = DetecteurAlerte(seuil=30, k=2)
    assert [d.ajouter(t) for t in [31, 31, 31, 31]] == [False, True, False, False]


def test_detecteur_rearme_apres_retour_sous_le_seuil():
    d = DetecteurAlerte(seuil=30, k=2)
    assert [d.ajouter(t) for t in [31, 31, 10, 31, 31]] == [False, True, False, False, True]


def test_detecteur_rearme_apres_mesure_manquante():
    d = DetecteurAlerte(seuil=30, k=2)
    assert [d.ajouter(t) for t in [31, None, 31, 31]] == [False, False, False, True]


def test_detecteur_k_egal_un():
    d = DetecteurAlerte(seuil=30, k=1)
    assert [d.ajouter(t) for t in [31, 31, 10, 31]] == [True, False, False, True]


def test_detecteur_k_invalide():
    with pytest.raises(ValueError):
        DetecteurAlerte(seuil=30, k=0)


def test_detecteur_coherent_avec_la_version_batch():
    mesures = [10, 31, 32, 33, 10, None, 31, 31, 10, 31]
    for k in (1, 2, 3):
        d = DetecteurAlerte(seuil=30, k=k)
        declenche = any(d.ajouter(t) for t in mesures)
        assert declenche is alerte_detectee(mesures, 30, k)


def test_detecteur_memoire_constante():
    """Le détecteur ne doit pas accumuler l'historique des mesures."""
    d = DetecteurAlerte(seuil=30, k=3)
    for t in range(10_000):
        d.ajouter(float(t))
    for valeur in vars(d).values():
        assert not isinstance(valeur, list | tuple | set | dict), (
            "le détecteur stocke une collection : la mémoire n'est pas O(1)"
        )
