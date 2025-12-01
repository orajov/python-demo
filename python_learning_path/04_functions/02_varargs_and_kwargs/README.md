# *args a **kwargs

Tato lekce představuje téma *args a **kwargs a nabízí krátké ukázky, které lze hned spustit. Obsah je stručný, aby bylo možné rychle pochopit hlavní principy a vyzkoušet si je v praxi.

## Teorie
- *args, **kwargs
- Sbírání proměnlivého počtu argumentů
- Předávání dál do jiných funkcí

## Příklady
```python
def sum_numbers(*values: int) -> int:
    return sum(values)

print('Součet', sum_numbers(1, 2, 3))
```

```python
def show_settings(**options):
    for key, value in options.items():
        print(key, '->', value)

show_settings(theme='dark', autosave=True)
```

## Úkoly
- Vypracujte příklad související s tématem: *args, **kwargs.
- Napište vlastní variantu, která rozšíří příklady v souboru examples.py.
- Vyzkoušejte vstup od uživatele a ukažte, jak se mění chování programu.
