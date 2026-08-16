.PHONY: test exo corrige lint new chrono

# Lance tous les tests sur TON code
test:
	pytest

# Lance les tests d'un seul exercice : make exo EXO=001_alerte_temperature
exo:
	pytest exercices/$(EXO) -v

# Verifie que les corriges passent les tests (sert de garde-fou / CI)
corrige:
	python outils/pytest_corrige.py

lint:
	ruff check .

# Cree un nouvel exercice : make new NOM=detection-pics
new:
	python outils/nouvel_exo.py $(NOM)

# Chrono de 25 min pour simuler la pression d'entretien
chrono:
	python -c "import time; print('Depart. Ctrl-C pour arreter.'); time.sleep(1500); print('TEMPS ECOULE.')"
