"""Ukázkový kód pro téma enumerate a zip."""

letters = ['a', 'b', 'c']
for index, letter in enumerate(letters, start=1):
    print(index, letter)

names = ['Eva', 'Petr']
ages = [30, 28]
for name, age in zip(names, ages):
    print(name, 'má', age, 'let')

pairs = list(zip(letters, names))
print('Spojené páry', pairs)


if __name__ == "__main__":
    # Spuštěním tohoto souboru zobrazíte ukázky přímo v konzoli
    pass
