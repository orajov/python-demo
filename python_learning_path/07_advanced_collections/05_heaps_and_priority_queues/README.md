# Halda a prioritní fronta

Tato lekce představuje téma halda a prioritní fronta a nabízí krátké ukázky, které lze hned spustit. Obsah je stručný, aby bylo možné rychle pochopit hlavní principy a vyzkoušet si je v praxi.

## Teorie
- heapq, prioritní fronty
- Nejmenší prvek na vrcholu
- Použití pro plánování úloh

## Příklady
```python
import heapq
queue: list[tuple[int, str]] = []
heapq.heappush(queue, (2, 'úkol B'))
heapq.heappush(queue, (1, 'úkol A'))
print('Pop', heapq.heappop(queue))
```

```python
heapq.heappush(queue, (3, 'úkol C'))
heapq.heappush(queue, (0, 'urgentní'))
print('Celá fronta', queue)
```

## Úkoly
- Vypracujte příklad související s tématem: heapq, prioritní fronty.
- Napište vlastní variantu, která rozšíří příklady v souboru examples.py.
- Vyzkoušejte vstup od uživatele a ukažte, jak se mění chování programu.
