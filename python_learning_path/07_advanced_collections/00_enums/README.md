# Výčtové typy

Tato lekce představuje téma výčtové typy a nabízí krátké ukázky, které lze hned spustit. Obsah je stručný, aby bylo možné rychle pochopit hlavní principy a vyzkoušet si je v praxi.

## Teorie
- Enum, IntEnum, StrEnum, auto()
- Kdy se hodí enumerace
- Přiřazení vlastních hodnot

## Příklady
```python
from enum import Enum, auto
class Mood(Enum):
    HAPPY = auto()
    SAD = auto()

print(Mood.HAPPY)
```

```python
from enum import IntEnum
class Priority(IntEnum):
    LOW = 1
    HIGH = 2

print(Priority.HIGH.value)
```

## Úkoly
- Vypracujte příklad související s tématem: Enum, IntEnum, StrEnum, auto().
- Napište vlastní variantu, která rozšíří příklady v souboru examples.py.
- Vyzkoušejte vstup od uživatele a ukažte, jak se mění chování programu.
