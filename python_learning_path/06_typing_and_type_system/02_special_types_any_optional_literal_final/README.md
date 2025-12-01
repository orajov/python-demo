# Speciální typy Any, Optional, Literal, Final

Tato lekce představuje téma speciální typy any, optional, literal, final a nabízí krátké ukázky, které lze hned spustit. Obsah je stručný, aby bylo možné rychle pochopit hlavní principy a vyzkoušet si je v praxi.

## Teorie
- Any, Optional, Literal, Final
- Kdy se hodí širší vs užší typ
- Práce s None v anotacích

## Příklady
```python
from typing import Any, Optional, Literal, Final
value: Any = 'text'
maybe_number: Optional[int] = None
mode: Literal['r', 'w'] = 'r'
VERSION: Final = '1.0'
print(value, maybe_number, mode, VERSION)
```

```python
def safe_length(text: Optional[str]) -> int:
    return len(text) if text is not None else 0

print(safe_length('abc'))
```

## Úkoly
- Vypracujte příklad související s tématem: Any, Optional, Literal, Final.
- Napište vlastní variantu, která rozšíří příklady v souboru examples.py.
- Vyzkoušejte vstup od uživatele a ukažte, jak se mění chování programu.
