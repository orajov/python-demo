# ChainMap a MappingProxyType

Tato lekce představuje téma chainmap a mappingproxytype a nabízí krátké ukázky, které lze hned spustit. Obsah je stručný, aby bylo možné rychle pochopit hlavní principy a vyzkoušet si je v praxi.

## Teorie
- Více vrstev konfigurace
- Read-only pohled
- Bezpečné sdílení map

## Příklady
```python
from collections import ChainMap
defaults = {'lang': 'cs'}
overrides = {'theme': 'dark'}
config = ChainMap(overrides, defaults)
print(config['lang'], config['theme'])
```

```python
from types import MappingProxyType
settings = {'mode': 'view'}
readonly = MappingProxyType(settings)
print(readonly['mode'])
```

## Úkoly
- Vypracujte příklad související s tématem: Více vrstev konfigurace.
- Napište vlastní variantu, která rozšíří příklady v souboru examples.py.
- Vyzkoušejte vstup od uživatele a ukažte, jak se mění chování programu.
