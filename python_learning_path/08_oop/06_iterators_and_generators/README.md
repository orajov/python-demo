# Iterátory a generátory

Tato lekce představuje téma iterátory a generátory a nabízí krátké ukázky, které lze hned spustit. Obsah je stručný, aby bylo možné rychle pochopit hlavní principy a vyzkoušet si je v praxi.

## Teorie
- Implementace __iter__, __next__
- Generátory pomocí yield
- Líné vyhodnocování

## Příklady
```python
class Countdown:
    def __init__(self, start: int):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

print(list(Countdown(3)))
```

```python
def even_numbers(limit: int):
    for number in range(0, limit, 2):
        yield number

print(list(even_numbers(6)))
```

## Úkoly
- Vypracujte příklad související s tématem: Implementace __iter__, __next__.
- Napište vlastní variantu, která rozšíří příklady v souboru examples.py.
- Vyzkoušejte vstup od uživatele a ukažte, jak se mění chování programu.
