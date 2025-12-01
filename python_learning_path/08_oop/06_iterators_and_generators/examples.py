"""Ukázkový kód pro téma Iterátory a generátory."""

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

def even_numbers(limit: int):
    for number in range(0, limit, 2):
        yield number

print(list(even_numbers(6)))

generator = (n*n for n in range(3))
print(list(generator))


if __name__ == "__main__":
    # Spuštěním tohoto souboru zobrazíte ukázky přímo v konzoli
    pass
