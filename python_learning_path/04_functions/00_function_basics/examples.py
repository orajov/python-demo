"""Ukázkový kód pro téma Základy funkcí."""

def greet(name: str) -> str:
    """Vrátí pozdrav pro zadané jméno."""
    return f'Ahoj {name}'

print(greet('Marie'))

def add(a: int, b: int) -> int:
    return a + b

print('Součet', add(2, 3))

message = 'global'
def local_example():
    message = 'lokální'
    print('Uvnitř', message)

local_example()
print('Venku', message)


if __name__ == "__main__":
    # Spuštěním tohoto souboru zobrazíte ukázky přímo v konzoli
    pass
