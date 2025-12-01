# Dataclass v OOP

Tato lekce představuje téma dataclass v oop a nabízí krátké ukázky, které lze hned spustit. Obsah je stručný, aby bylo možné rychle pochopit hlavní principy a vyzkoušet si je v praxi.

## Teorie
- @dataclass, asdict, srovnání s klasickou třídou
- Automaticky generované metody
- Jednodušší definice datových objektů

## Příklady
```python
from dataclasses import dataclass, asdict
@dataclass
class Book:
    title: str
    pages: int

book = Book('Python', 300)
print(book)
```

```python
print('Jako slovník', asdict(book))
```

## Úkoly
- Vypracujte příklad související s tématem: @dataclass, asdict, srovnání s klasickou třídou.
- Napište vlastní variantu, která rozšíří příklady v souboru examples.py.
- Vyzkoušejte vstup od uživatele a ukažte, jak se mění chování programu.
