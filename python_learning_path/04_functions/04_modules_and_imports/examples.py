"""Ukázkový kód pro téma Moduly a importy."""

import math
from math import sqrt
print('Pi:', math.pi, 'Odmocnina 16:', sqrt(16))

print('Aktuální modul:', __name__)

def helper():
    return 'pomocná funkce v modulu'

if __name__ == '__main__':
    print(helper())


if __name__ == "__main__":
    # Spuštěním tohoto souboru zobrazíte ukázky přímo v konzoli
    pass
