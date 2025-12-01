# Generika, Callable a TypeVar

Tato lekce představuje téma generika, callable a typevar a nabízí krátké ukázky, které lze hned spustit. Obsah je stručný, aby bylo možné rychle pochopit hlavní principy a vyzkoušet si je v praxi.

## Teorie
- Callable, TypeVar, generika funkcí
- Opakovaně použitelná rozhraní
- Parametrizace typů pro bezpečnost

## Příklady
```python
from typing import Callable, TypeVar
T = TypeVar('T')

def apply_twice(func: Callable[[T], T], value: T) -> T:
    return func(func(value))

def double(x: int) -> int:
    return x * 2

print(apply_twice(double, 3))
```

```python
from typing import TypeVar
U = TypeVar('U')

def identity(value: U) -> U:
    return value

print(identity('text'))
```

## Úkoly
- Vypracujte příklad související s tématem: Callable, TypeVar, generika funkcí.
- Napište vlastní variantu, která rozšíří příklady v souboru examples.py.
- Vyzkoušejte vstup od uživatele a ukažte, jak se mění chování programu.
