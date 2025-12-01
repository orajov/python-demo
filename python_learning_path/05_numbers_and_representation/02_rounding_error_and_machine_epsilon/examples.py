"""Ukázkový kód pro téma Zaokrouhlení a strojové epsilon."""

import sys, math
print('Epsilon pro float:', sys.float_info.epsilon)

a = 0.1 + 0.2
print('Je výsledek blízko 0.3?', math.isclose(a, 0.3))

print('Zaokrouhlení', round(2.675, 2))


if __name__ == "__main__":
    # Spuštěním tohoto souboru zobrazíte ukázky přímo v konzoli
    pass
