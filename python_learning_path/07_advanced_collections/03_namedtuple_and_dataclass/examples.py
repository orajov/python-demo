"""Ukázkový kód pro téma namedtuple a dataclass."""

from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)

from dataclasses import dataclass
@dataclass
class Note:
    title: str
    done: bool = False

note = Note('Nakoupit')
print(note)

note.done = True
print('Aktualizace dataclass', note)


if __name__ == "__main__":
    # Spuštěním tohoto souboru zobrazíte ukázky přímo v konzoli
    pass
