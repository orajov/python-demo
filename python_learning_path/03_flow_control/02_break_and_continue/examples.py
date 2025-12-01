"""Ukázkový kód pro téma break a continue."""

numbers = [1, 5, 8, 2]
for num in numbers:
    if num > 7:
        print('Nalezeno číslo > 7:', num)
        break

for num in numbers:
    if num % 2 == 0:
        continue
    print('Liché číslo', num)

text = 'python'
for char in text:
    if char == 'h':
        print('Zastavuji u h')
        break


if __name__ == "__main__":
    # Spuštěním tohoto souboru zobrazíte ukázky přímo v konzoli
    pass
