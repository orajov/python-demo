# Základní anotace funkcí

Tato lekce představuje téma základní anotace funkcí a nabízí krátké ukázky, které lze hned spustit. Obsah je stručný, aby bylo možné rychle pochopit hlavní principy a vyzkoušet si je v praxi.

## Teorie
- Základní anotace funkcí
- Anotace návratových hodnot
- Komentáře vs skutečné typové kontroly

## Příklady
```python
def repeat(text: str, times: int) -> str:
    return text * times

print(repeat('ha', 3))
```

```python
def midpoint(a: float, b: float) -> float:
    return (a + b) / 2

print(midpoint(2.0, 4.0))
```

## Úkoly
- Vypracujte příklad související s tématem: Základní anotace funkcí.
- Napište vlastní variantu, která rozšíří příklady v souboru examples.py.
- Vyzkoušejte vstup od uživatele a ukažte, jak se mění chování programu.
