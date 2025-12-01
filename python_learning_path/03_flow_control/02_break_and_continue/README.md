# break a continue

Tato lekce představuje téma break a continue a nabízí krátké ukázky, které lze hned spustit. Obsah je stručný, aby bylo možné rychle pochopit hlavní principy a vyzkoušet si je v praxi.

## Teorie
- Předčasné ukončení, přeskočení iterace
- Typické scénáře vyhledávání
- Čitelné kombinace s podmínkami

## Příklady
```python
numbers = [1, 5, 8, 2]
for num in numbers:
    if num > 7:
        print('Nalezeno číslo > 7:', num)
        break
```

```python
for num in numbers:
    if num % 2 == 0:
        continue
    print('Liché číslo', num)
```

## Úkoly
- Vypracujte příklad související s tématem: Předčasné ukončení, přeskočení iterace.
- Napište vlastní variantu, která rozšíří příklady v souboru examples.py.
- Vyzkoušejte vstup od uživatele a ukažte, jak se mění chování programu.
