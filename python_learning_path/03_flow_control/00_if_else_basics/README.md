# Podmínky if/elif/else

Tato lekce představuje téma podmínky if/elif/else a nabízí krátké ukázky, které lze hned spustit. Obsah je stručný, aby bylo možné rychle pochopit hlavní principy a vyzkoušet si je v praxi.

## Teorie
- if/elif/else
- Pravdivostní výrazy
- Idiomatické psaní

## Příklady
```python
temperature = 5
if temperature < 0:
    print('Mrzne')
elif temperature < 10:
    print('Chladno')
else:
    print('Teplo')
```

```python
value = ''
if value:
    print('Něco tu je')
else:
    print('Prázdný řetězec je vyhodnocen jako False')
```

## Úkoly
- Vypracujte příklad související s tématem: if/elif/else.
- Napište vlastní variantu, která rozšíří příklady v souboru examples.py.
- Vyzkoušejte vstup od uživatele a ukažte, jak se mění chování programu.
