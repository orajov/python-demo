# Counter a defaultdict

Tato lekce představuje téma counter a defaultdict a nabízí krátké ukázky, které lze hned spustit. Obsah je stručný, aby bylo možné rychle pochopit hlavní principy a vyzkoušet si je v praxi.

## Teorie
- Počítání výskytů, implicitní hodnoty
- Zjednodušení práce s chybějícími klíči
- Praktické příklady agregace

## Příklady
```python
from collections import Counter, defaultdict
words = ['jablko', 'banán', 'jablko']
counts = Counter(words)
print(counts)
```

```python
scores = defaultdict(int)
scores['Eva'] += 5
print('Skóre', dict(scores))
```

## Úkoly
- Vypracujte příklad související s tématem: Počítání výskytů, implicitní hodnoty.
- Napište vlastní variantu, která rozšíří příklady v souboru examples.py.
- Vyzkoušejte vstup od uživatele a ukažte, jak se mění chování programu.
