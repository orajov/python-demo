"""Ukázkový kód pro téma Praktická pravidla pro floaty."""

value = 1/3
print('Formát na tři desetinná místa', f"{value:.3f}")

import math
print('Porovnání s tolerancí', math.isclose(0.1 + 0.2, 0.3, rel_tol=1e-9))

result = round(2.3456, 2)
print('Zaokrouhleno:', result)


if __name__ == "__main__":
    # Spuštěním tohoto souboru zobrazíte ukázky přímo v konzoli
    pass
