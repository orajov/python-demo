# Strategy pattern

Tato lekce představuje téma strategy pattern a nabízí krátké ukázky, které lze hned spustit. Obsah je stručný, aby bylo možné rychle pochopit hlavní principy a vyzkoušet si je v praxi.

## Teorie
- Eliminace větvení pomocí strategií
- Výběr chování za běhu
- Jednoduchá kompozice funkcí

## Příklady
```python
from typing import Callable
DiscountStrategy = Callable[[float], float]

def apply_discount(price: float, strategy: DiscountStrategy) -> float:
    return strategy(price)

def no_discount(price: float) -> float:
    return price

def student_discount(price: float) -> float:
    return price * 0.8

print(apply_discount(100, student_discount))
```

```python
def seasonal_discount(price: float) -> float:
    return price * 0.9

print(apply_discount(200, seasonal_discount))
```

## Úkoly
- Vypracujte příklad související s tématem: Eliminace větvení pomocí strategií.
- Napište vlastní variantu, která rozšíří příklady v souboru examples.py.
- Vyzkoušejte vstup od uživatele a ukažte, jak se mění chování programu.
