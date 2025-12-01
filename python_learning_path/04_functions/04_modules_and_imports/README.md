# Moduly a importy

Tato lekce představuje téma moduly a importy a nabízí krátké ukázky, které lze hned spustit. Obsah je stručný, aby bylo možné rychle pochopit hlavní principy a vyzkoušet si je v praxi.

## Teorie
- Struktura modulů, import, from ... import ...
- Vyhledávací cesta a __name__
- Organizace kódu do balíčků

## Příklady
```python
import math
from math import sqrt
print('Pi:', math.pi, 'Odmocnina 16:', sqrt(16))
```

```python
print('Aktuální modul:', __name__)
```

## Úkoly
- Vypracujte příklad související s tématem: Struktura modulů, import, from ... import ....
- Napište vlastní variantu, která rozšíří příklady v souboru examples.py.
- Vyzkoušejte vstup od uživatele a ukažte, jak se mění chování programu.
