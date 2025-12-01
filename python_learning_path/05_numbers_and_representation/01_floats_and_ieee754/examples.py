"""Ukázkový kód pro téma Plovoucí čísla a IEEE 754."""

result = 0.1 + 0.2
print('0.1 + 0.2 =', result)

print('Porovnání s 0.3', result == 0.3)

from decimal import Decimal
print('Decimal přesnější:', Decimal('0.1') + Decimal('0.2'))


if __name__ == "__main__":
    # Spuštěním tohoto souboru zobrazíte ukázky přímo v konzoli
    pass
