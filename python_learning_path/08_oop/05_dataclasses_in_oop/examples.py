"""Ukázkový kód pro téma Dataclass v OOP."""

from dataclasses import dataclass, asdict
@dataclass
class Book:
    title: str
    pages: int

book = Book('Python', 300)
print(book)

print('Jako slovník', asdict(book))

other = Book('Python', 300)
print('Porovnání', book == other)


if __name__ == "__main__":
    # Spuštěním tohoto souboru zobrazíte ukázky přímo v konzoli
    pass
