# Instalace a virtuální prostředí

Tato lekce představuje téma instalace a virtuální prostředí a nabízí krátké ukázky, které lze hned spustit. Obsah je stručný, aby bylo možné rychle pochopit hlavní principy a vyzkoušet si je v praxi.

## Teorie
- Instalace Pythonu
- Virtuální prostředí (venv)
- Aktivace/deaktivace
- Instalace balíčků přes pip

## Příklady
```python
import sys
print('Použitá verze Pythonu:', sys.version)
```

```python
import venv, pathlib
venv_dir = pathlib.Path('moje_venv')
print('Adresář pro venv:', venv_dir)
```

## Úkoly
- Vypracujte příklad související s tématem: Instalace Pythonu.
- Napište vlastní variantu, která rozšíří příklady v souboru examples.py.
- Vyzkoušejte vstup od uživatele a ukažte, jak se mění chování programu.
