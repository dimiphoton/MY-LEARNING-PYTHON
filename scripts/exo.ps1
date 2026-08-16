param(
    [Parameter(Mandatory = $true)]
    [string]$Exo
)
python -m pytest "exercices/$Exo" -v @args
