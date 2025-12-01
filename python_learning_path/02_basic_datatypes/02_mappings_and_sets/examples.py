"""Ukázkový kód pro téma Slovníky a množiny."""

prices = {'jablko': 25, 'banán': 30}
print('Cena jablka', prices['jablko'])

seen = set()
seen.add('uživatel')
print('Obsah množiny', seen)

for name, price in prices.items():
    print(name, '->', price)


if __name__ == "__main__":
    # Spuštěním tohoto souboru zobrazíte ukázky přímo v konzoli
    pass
