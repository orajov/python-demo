# Čisté funkce a čitelnost

Tato lekce představuje téma čisté funkce a čitelnost a nabízí krátké ukázky, které lze hned spustit. Obsah je stručný, aby bylo možné rychle pochopit hlavní principy a vyzkoušet si je v praxi.

## Teorie
- Pojmenování, čisté funkce, side-effects
- Testovatelnost a předvídatelnost
- Kdy logiku rozdělit do menších funkcí

## Příklady
```python
def square(number: int) -> int:
    return number * number

print(square(5))
```

```python
history: list[str] = []
def add_with_log(a: int, b: int) -> int:
    result = a + b
    history.append(result)
    return result

print(add_with_log(2, 3), history)
```

## Úkoly
- Vypracujte příklad související s tématem: Pojmenování, čisté funkce, side-effects.
- Napište vlastní variantu, která rozšíří příklady v souboru examples.py.
- Vyzkoušejte vstup od uživatele a ukažte, jak se mění chování programu.
