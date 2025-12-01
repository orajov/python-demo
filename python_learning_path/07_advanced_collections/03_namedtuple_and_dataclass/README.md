# namedtuple a dataclass

Tato lekce představuje téma namedtuple a dataclass a nabízí krátké ukázky, které lze hned spustit. Obsah je stručný, aby bylo možné rychle pochopit hlavní principy a vyzkoušet si je v praxi.

## Teorie
- Lehká datová schémata
- Porovnání s klasickou třídou
- Práce s atributy a výchozími hodnotami

## Příklady
```python
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)
```

```python
from dataclasses import dataclass
@dataclass
class Note:
    title: str
    done: bool = False

note = Note('Nakoupit')
print(note)
```

## Úkoly
- Vypracujte příklad související s tématem: Lehká datová schémata.
- Napište vlastní variantu, která rozšíří příklady v souboru examples.py.
- Vyzkoušejte vstup od uživatele a ukažte, jak se mění chování programu.
