# all, any a predikáty

Tato lekce představuje téma all, any a predikáty a nabízí krátké ukázky, které lze hned spustit. Obsah je stručný, aby bylo možné rychle pochopit hlavní principy a vyzkoušet si je v praxi.

## Teorie
- Funkce all, any, predikáty
- Vyhodnocení pravdivosti kolekcí
- Zkrácené vyhodnocování

## Příklady
```python
values = [True, True, False]
print('Vše pravda?', all(values))
```

```python
temperatures = [18, 21, 19]
print('Je nějaká teplota nad 20?', any(temp > 20 for temp in temperatures))
```

## Úkoly
- Vypracujte příklad související s tématem: Funkce all, any, predikáty.
- Napište vlastní variantu, která rozšíří příklady v souboru examples.py.
- Vyzkoušejte vstup od uživatele a ukažte, jak se mění chování programu.
