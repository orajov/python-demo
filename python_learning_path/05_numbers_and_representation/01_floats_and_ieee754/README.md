# Plovoucí čísla a IEEE 754

Tato lekce představuje téma plovoucí čísla a ieee 754 a nabízí krátké ukázky, které lze hned spustit. Obsah je stručný, aby bylo možné rychle pochopit hlavní principy a vyzkoušet si je v praxi.

## Teorie
- IEEE 754, běžné chyby s floaty
- Přesnost a reprezentace
- Ukázka zaokrouhlovacích chyb

## Příklady
```python
result = 0.1 + 0.2
print('0.1 + 0.2 =', result)
```

```python
print('Porovnání s 0.3', result == 0.3)
```

## Úkoly
- Vypracujte příklad související s tématem: IEEE 754, běžné chyby s floaty.
- Napište vlastní variantu, která rozšíří příklady v souboru examples.py.
- Vyzkoušejte vstup od uživatele a ukažte, jak se mění chování programu.
