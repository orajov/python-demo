# Příkazová řádka a soubory

Tato lekce představuje téma příkazová řádka a soubory a nabízí krátké ukázky, které lze hned spustit. Obsah je stručný, aby bylo možné rychle pochopit hlavní principy a vyzkoušet si je v praxi.

## Teorie
- Terminál, spouštění Python skriptů
- Absolutní/relativní cesty
- Práce se soubory a složkami

## Příklady
```python
import os
print('Aktuální adresář:', os.getcwd())
```

```python
from pathlib import Path
path = Path('data/example.txt')
print('Relativní cesta:', path)
print('Absolutní cesta:', path.resolve())
```

## Úkoly
- Vypracujte příklad související s tématem: Terminál, spouštění Python skriptů.
- Napište vlastní variantu, která rozšíří příklady v souboru examples.py.
- Vyzkoušejte vstup od uživatele a ukažte, jak se mění chování programu.
