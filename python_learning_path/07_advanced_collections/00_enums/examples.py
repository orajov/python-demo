"""Ukázkový kód pro téma Výčtové typy."""

from enum import Enum, auto
class Mood(Enum):
    HAPPY = auto()
    SAD = auto()

print(Mood.HAPPY)

from enum import IntEnum
class Priority(IntEnum):
    LOW = 1
    HIGH = 2

print(Priority.HIGH.value)

for mood in Mood:
    print('Stav:', mood.name)


if __name__ == "__main__":
    # Spuštěním tohoto souboru zobrazíte ukázky přímo v konzoli
    pass
