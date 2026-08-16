# Verifie que les corriges passent les tests (garde-fou / CI)
$env:CORRIGE = "1"
python -m pytest @args
