"""Ukázkový kód pro téma Ztráta přesnosti a stabilita."""

small = 1e-9
print('Odčítání blízkých čísel', (1 + small) - 1)

def stable_mean(values: list[float]) -> float:
    return sum(values) / len(values)

print('Průměr', stable_mean([1e6, 1e6 + 1, 1e6 + 2]))

import math
print('Použití math.fsum pro lepší přesnost', math.fsum([0.1] * 10))


if __name__ == "__main__":
    # Spuštěním tohoto souboru zobrazíte ukázky přímo v konzoli
    pass
