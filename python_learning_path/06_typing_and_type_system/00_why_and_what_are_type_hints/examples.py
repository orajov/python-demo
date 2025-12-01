"""Ukázkový kód pro téma Proč a co jsou typové anotace."""

def format_name(name: str) -> str:
    return name.title()

print(format_name('petr novak'))

age: int = 30
print('Anotovaný věk', age)

def add(a: int, b: int) -> int:
    return a + b

print(add(2, 2))


if __name__ == "__main__":
    # Spuštěním tohoto souboru zobrazíte ukázky přímo v konzoli
    pass
