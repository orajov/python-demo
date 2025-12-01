"""Ukázkový kód pro téma Příkazová řádka a soubory."""

import os
print('Aktuální adresář:', os.getcwd())

from pathlib import Path
path = Path('data/example.txt')
print('Relativní cesta:', path)
print('Absolutní cesta:', path.resolve())

from pathlib import Path
folder = Path('ukazka')
folder.mkdir(exist_ok=True)
print('Vytvořená složka', folder)


if __name__ == "__main__":
    # Spuštěním tohoto souboru zobrazíte ukázky přímo v konzoli
    pass
