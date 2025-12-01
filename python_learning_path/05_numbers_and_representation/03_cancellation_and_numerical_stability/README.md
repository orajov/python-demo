# Ztráta přesnosti a stabilita

Tato lekce představuje téma ztráta přesnosti a stabilita a nabízí krátké ukázky, které lze hned spustit. Obsah je stručný, aby bylo možné rychle pochopit hlavní principy a vyzkoušet si je v praxi.

## Teorie
- Ztráta přesnosti, přepis vzorců
- Vyhýbání se odčítání blízkých čísel
- Kontrola výsledků pomocí alternativních výpočtů

## Příklady
```python
small = 1e-9
print('Odčítání blízkých čísel', (1 + small) - 1)
```

```python
def stable_mean(values: list[float]) -> float:
    return sum(values) / len(values)

print('Průměr', stable_mean([1e6, 1e6 + 1, 1e6 + 2]))
```

## Úkoly
- Vypracujte příklad související s tématem: Ztráta přesnosti, přepis vzorců.
- Napište vlastní variantu, která rozšíří příklady v souboru examples.py.
- Vyzkoušejte vstup od uživatele a ukažte, jak se mění chování programu.
