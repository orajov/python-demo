# Fronty s deque

Tato lekce představuje téma fronty s deque a nabízí krátké ukázky, které lze hned spustit. Obsah je stručný, aby bylo možné rychle pochopit hlavní principy a vyzkoušet si je v praxi.

## Teorie
- deque jako fronta a zásobník
- Rychlé přidávání na obou koncích
- Praktické scénáře front

## Příklady
```python
from collections import deque
queue = deque()
queue.append('první')
queue.append('druhý')
print('Odebráno', queue.popleft())
```

```python
stack = deque()
stack.append('A')
stack.append('B')
print('Zásobník pop', stack.pop())
```

## Úkoly
- Vypracujte příklad související s tématem: deque jako fronta a zásobník.
- Napište vlastní variantu, která rozšíří příklady v souboru examples.py.
- Vyzkoušejte vstup od uživatele a ukažte, jak se mění chování programu.
