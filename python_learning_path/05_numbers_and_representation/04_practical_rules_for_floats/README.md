# Praktická pravidla pro floaty

Tato lekce představuje téma praktická pravidla pro floaty a nabízí krátké ukázky, které lze hned spustit. Obsah je stručný, aby bylo možné rychle pochopit hlavní principy a vyzkoušet si je v praxi.

## Teorie
- Jak bezpečně pracovat s floaty
- Volba vhodných tolerancí
- Formatování a prezentace výsledků

## Příklady
```python
value = 1/3
print('Formát na tři desetinná místa', f"{value:.3f}")
```

```python
import math
print('Porovnání s tolerancí', math.isclose(0.1 + 0.2, 0.3, rel_tol=1e-9))
```

## Úkoly
- Vypracujte příklad související s tématem: Jak bezpečně pracovat s floaty.
- Napište vlastní variantu, která rozšíří příklady v souboru examples.py.
- Vyzkoušejte vstup od uživatele a ukažte, jak se mění chování programu.
