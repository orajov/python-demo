"""Ukázkový kód pro téma None a bool."""

value = None
print('Je hodnota nastavena?', value is None)

items = []
print('Prázdný list je false?', bool(items))

response = ''
if not response:
    print('Nebyl zadán vstup')


if __name__ == "__main__":
    # Spuštěním tohoto souboru zobrazíte ukázky přímo v konzoli
    pass
