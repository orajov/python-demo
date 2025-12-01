"""Ukázkový kód pro téma Základní anotace funkcí."""

def repeat(text: str, times: int) -> str:
    return text * times

print(repeat('ha', 3))

def midpoint(a: float, b: float) -> float:
    return (a + b) / 2

print(midpoint(2.0, 4.0))

def shout(message: str) -> None:
    print(message.upper())

shout('pozdrav')


if __name__ == "__main__":
    # Spuštěním tohoto souboru zobrazíte ukázky přímo v konzoli
    pass
