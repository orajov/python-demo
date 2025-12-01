"""Ukázkový kód pro téma Speciální typy Any, Optional, Literal, Final."""

from typing import Any, Optional, Literal, Final
value: Any = 'text'
maybe_number: Optional[int] = None
mode: Literal['r', 'w'] = 'r'
VERSION: Final = '1.0'
print(value, maybe_number, mode, VERSION)

def safe_length(text: Optional[str]) -> int:
    return len(text) if text is not None else 0

print(safe_length('abc'))

def use_literal(mode: Literal['light', 'dark']) -> str:
    return f'Režim: {mode}'

print(use_literal('light'))


if __name__ == "__main__":
    # Spuštěním tohoto souboru zobrazíte ukázky přímo v konzoli
    pass
