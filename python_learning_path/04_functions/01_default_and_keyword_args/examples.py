"""Ukázkový kód pro téma Výchozí a pojmenované argumenty."""

def greet(name: str, greeting: str = 'Ahoj') -> str:
    return f'{greeting} {name}'

print(greet('Eva'))
print(greet('Petr', greeting='Zdravím'))

def append_value(value: int, items=None):
    if items is None:
        items = []
    items.append(value)
    return items

print(append_value(1))
print(append_value(2))

print(greet(name='Lenka', greeting='Čau'))


if __name__ == "__main__":
    # Spuštěním tohoto souboru zobrazíte ukázky přímo v konzoli
    pass
