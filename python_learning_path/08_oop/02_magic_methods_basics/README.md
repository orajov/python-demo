# Základní magické metody

Tato lekce představuje téma základní magické metody a nabízí krátké ukázky, které lze hned spustit. Obsah je stručný, aby bylo možné rychle pochopit hlavní principy a vyzkoušet si je v praxi.

## Teorie
- __str__, __repr__, __len__, __add__, atd.
- Vliv na zabudované funkce
- Zlepšení ladění a čitelnosti

## Příklady
```python
class Bag:
    def __init__(self, items: list[str]):
        self.items = items

    def __len__(self) -> int:
        return len(self.items)

    def __repr__(self) -> str:
        return f'Bag({self.items!r})'

    def __add__(self, other: 'Bag') -> 'Bag':
        return Bag(self.items + other.items)

bag = Bag(['pero'])
print(len(bag), bag)
```

```python
second = Bag(['sešit'])
combined = bag + second
print('Spojená taška', combined)
```

## Úkoly
- Vypracujte příklad související s tématem: __str__, __repr__, __len__, __add__, atd..
- Napište vlastní variantu, která rozšíří příklady v souboru examples.py.
- Vyzkoušejte vstup od uživatele a ukažte, jak se mění chování programu.
