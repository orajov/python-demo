# Refaktoringové techniky

Tato lekce představuje téma refaktoringové techniky a nabízí krátké ukázky, které lze hned spustit. Obsah je stručný, aby bylo možné rychle pochopit hlavní principy a vyzkoušet si je v praxi.

## Teorie
- Extract method, rename, move method
- Postupné malé kroky
- Testování po každé změně

## Příklady
```python
def calculate_discount(price: float, discount: float) -> float:
    return price * (1 - discount)

print(calculate_discount(100, 0.1))
```

```python
def print_order(items: list[str]) -> None:
    for item in items:
        print('-', item)

print_order(['banán', 'jablko'])
```

## Úkoly
- Vypracujte příklad související s tématem: Extract method, rename, move method.
- Napište vlastní variantu, která rozšíří příklady v souboru examples.py.
- Vyzkoušejte vstup od uživatele a ukažte, jak se mění chování programu.
