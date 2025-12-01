# Výchozí a pojmenované argumenty

Tato lekce představuje téma výchozí a pojmenované argumenty a nabízí krátké ukázky, které lze hned spustit. Obsah je stručný, aby bylo možné rychle pochopit hlavní principy a vyzkoušet si je v praxi.

## Teorie
- Výchozí argumenty
- Pozor na mutable default
- Klíčové argumenty pro čitelnost

## Příklady
```python
def greet(name: str, greeting: str = 'Ahoj') -> str:
    return f'{greeting} {name}'

print(greet('Eva'))
print(greet('Petr', greeting='Zdravím'))
```

```python
def append_value(value: int, items=None):
    if items is None:
        items = []
    items.append(value)
    return items

print(append_value(1))
print(append_value(2))
```

## Úkoly
- Vypracujte příklad související s tématem: Výchozí argumenty.
- Napište vlastní variantu, která rozšíří příklady v souboru examples.py.
- Vyzkoušejte vstup od uživatele a ukažte, jak se mění chování programu.
