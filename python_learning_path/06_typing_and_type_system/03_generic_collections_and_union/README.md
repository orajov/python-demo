# Generické kolekce a unie

Tato lekce představuje téma generické kolekce a unie a nabízí krátké ukázky, které lze hned spustit. Obsah je stručný, aby bylo možné rychle pochopit hlavní principy a vyzkoušet si je v praxi.

## Teorie
- Anotace kolekcí (list[int], dict[str, float])
- int | float
- Čitelné popisy očekávaných hodnot

## Příklady
```python
from typing import Union
prices: dict[str, float] = {'kniha': 249.0}
values: list[Union[int, float]] = [1, 2.5]
print(prices, values)
```

```python
Number = int | float
def average(values: list[Number]) -> float:
    return sum(values) / len(values)

print(average([1, 2.5, 3]))
```

## Úkoly
- Vypracujte příklad související s tématem: Anotace kolekcí (list[int], dict[str, float]).
- Napište vlastní variantu, která rozšíří příklady v souboru examples.py.
- Vyzkoušejte vstup od uživatele a ukažte, jak se mění chování programu.
