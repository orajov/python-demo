# Základy funkcí

Tato lekce představuje téma základy funkcí a nabízí krátké ukázky, které lze hned spustit. Obsah je stručný, aby bylo možné rychle pochopit hlavní principy a vyzkoušet si je v praxi.

## Teorie
- def, návratová hodnota, scope, docstring
- Vstupní argumenty a pořadí
- Pojmenování funkcí podle účelu

## Příklady
```python
def greet(name: str) -> str:
    """Vrátí pozdrav pro zadané jméno."""
    return f'Ahoj {name}'

print(greet('Marie'))
```

```python
def add(a: int, b: int) -> int:
    return a + b

print('Součet', add(2, 3))
```

## Úkoly
- Vypracujte příklad související s tématem: def, návratová hodnota, scope, docstring.
- Napište vlastní variantu, která rozšíří příklady v souboru examples.py.
- Vyzkoušejte vstup od uživatele a ukažte, jak se mění chování programu.
