"""Ukázkový kód pro téma Fronty s deque."""

from collections import deque
queue = deque()
queue.append('první')
queue.append('druhý')
print('Odebráno', queue.popleft())

stack = deque()
stack.append('A')
stack.append('B')
print('Zásobník pop', stack.pop())

queue.extend(['třetí', 'čtvrtý'])
print('Obsah fronty', list(queue))


if __name__ == "__main__":
    # Spuštěním tohoto souboru zobrazíte ukázky přímo v konzoli
    pass
