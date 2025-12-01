# Code smells

Tato lekce představuje téma code smells a nabízí krátké ukázky, které lze hned spustit. Obsah je stručný, aby bylo možné rychle pochopit hlavní principy a vyzkoušet si je v praxi.

## Teorie
- Co je code smell
- Proč to není bug, ale problém designu
- Jak je rozpoznat v kódu

## Příklady
```python
# Dlouhá funkce jako smell
def long_function():
    parts = []
    for number in range(5):
        parts.append(number)
    return parts

print(long_function())
```

```python
# Magické číslo
PRICE_WITHOUT_MEANING = 42
print('Magické číslo', PRICE_WITHOUT_MEANING)
```

## Úkoly
- Vypracujte příklad související s tématem: Co je code smell.
- Napište vlastní variantu, která rozšíří příklady v souboru examples.py.
- Vyzkoušejte vstup od uživatele a ukažte, jak se mění chování programu.
