"""Ukázkový kód pro téma Halda a prioritní fronta."""

import heapq
queue: list[tuple[int, str]] = []
heapq.heappush(queue, (2, 'úkol B'))
heapq.heappush(queue, (1, 'úkol A'))
print('Pop', heapq.heappop(queue))

heapq.heappush(queue, (3, 'úkol C'))
heapq.heappush(queue, (0, 'urgentní'))
print('Celá fronta', queue)

print('Další v pořadí', queue[0])


if __name__ == "__main__":
    # Spuštěním tohoto souboru zobrazíte ukázky přímo v konzoli
    pass
