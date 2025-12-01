"""Ukázkový kód pro téma Code smells."""

# Dlouhá funkce jako smell
def long_function():
    parts = []
    for number in range(5):
        parts.append(number)
    return parts

print(long_function())

# Magické číslo
PRICE_WITHOUT_MEANING = 42
print('Magické číslo', PRICE_WITHOUT_MEANING)

# Duplicitní kód naznačuje refaktoring
print('Smelly příklady slouží k diskuzi')


if __name__ == "__main__":
    # Spuštěním tohoto souboru zobrazíte ukázky přímo v konzoli
    pass
