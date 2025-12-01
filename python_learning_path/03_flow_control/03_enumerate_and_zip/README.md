# enumerate a zip

Tato lekce představuje téma enumerate a zip a nabízí krátké ukázky, které lze hned spustit. Obsah je stručný, aby bylo možné rychle pochopit hlavní principy a vyzkoušet si je v praxi.

## Teorie
- Iterace s indexem a přes více kolekcí
- Přehlednost oproti ručnímu počítání
- Rozbalování hodnot z zip

## Příklady
```python
letters = ['a', 'b', 'c']
for index, letter in enumerate(letters, start=1):
    print(index, letter)
```

```python
names = ['Eva', 'Petr']
ages = [30, 28]
for name, age in zip(names, ages):
    print(name, 'má', age, 'let')
```

## Úkoly
- Vypracujte příklad související s tématem: Iterace s indexem a přes více kolekcí.
- Napište vlastní variantu, která rozšíří příklady v souboru examples.py.
- Vyzkoušejte vstup od uživatele a ukažte, jak se mění chování programu.
