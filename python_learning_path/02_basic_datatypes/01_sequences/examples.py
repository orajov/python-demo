"""Ukázkový kód pro téma Sekvence a práce s nimi."""

text = 'Python'
print('První písmeno', text[0], 'Řez', text[1:4])

numbers = [1, 2, 3]
numbers.append(4)
print('List je měnitelný:', numbers)

coords = (10, 20)
for value in coords:
    print('Souřadnice', value)


if __name__ == "__main__":
    # Spuštěním tohoto souboru zobrazíte ukázky přímo v konzoli
    pass
