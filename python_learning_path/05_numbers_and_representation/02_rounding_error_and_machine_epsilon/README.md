# Zaokrouhlení a strojové epsilon

Tato lekce představuje téma zaokrouhlení a strojové epsilon a nabízí krátké ukázky, které lze hned spustit. Obsah je stručný, aby bylo možné rychle pochopit hlavní principy a vyzkoušet si je v praxi.

## Teorie
- Strojové epsilon, math.isclose
- Porovnávání čísel s tolerancí
- Praktické dopady při výpočtech

## Příklady
```python
import sys, math
print('Epsilon pro float:', sys.float_info.epsilon)
```

```python
a = 0.1 + 0.2
print('Je výsledek blízko 0.3?', math.isclose(a, 0.3))
```

## Úkoly
- Vypracujte příklad související s tématem: Strojové epsilon, math.isclose.
- Napište vlastní variantu, která rozšíří příklady v souboru examples.py.
- Vyzkoušejte vstup od uživatele a ukažte, jak se mění chování programu.
