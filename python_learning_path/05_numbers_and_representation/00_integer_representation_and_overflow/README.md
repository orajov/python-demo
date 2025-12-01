# Reprezentace celých čísel

Tato lekce představuje téma reprezentace celých čísel a nabízí krátké ukázky, které lze hned spustit. Obsah je stručný, aby bylo možné rychle pochopit hlavní principy a vyzkoušet si je v praxi.

## Teorie
- Binární soustava, velikost integeru
- Overflow v jiných jazycích vs Python
- Konverze do dvojkové soustavy

## Příklady
```python
value = 42
print('Binárně', bin(value))
```

```python
big = 10 ** 100
print('Velmi velké číslo bez overflow', big)

```

## Úkoly
- Vypracujte příklad související s tématem: Binární soustava, velikost integeru.
- Napište vlastní variantu, která rozšíří příklady v souboru examples.py.
- Vyzkoušejte vstup od uživatele a ukažte, jak se mění chování programu.
