"""Ukázkový kód pro téma Instalace a virtuální prostředí."""

import sys
print('Použitá verze Pythonu:', sys.version)

import venv, pathlib
venv_dir = pathlib.Path('moje_venv')
print('Adresář pro venv:', venv_dir)

print('pip install requests  # ukázkový příkaz')


if __name__ == "__main__":
    # Spuštěním tohoto souboru zobrazíte ukázky přímo v konzoli
    pass
