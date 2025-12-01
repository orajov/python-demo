"""Ukázkový kód pro téma Generické kolekce a unie."""

from typing import Union
prices: dict[str, float] = {'kniha': 249.0}
values: list[Union[int, float]] = [1, 2.5]
print(prices, values)

Number = int | float
def average(values: list[Number]) -> float:
    return sum(values) / len(values)

print(average([1, 2.5, 3]))

from typing import Sequence
def first_item(items: Sequence[str]) -> str:
    return items[0]

print(first_item(['a', 'b', 'c']))


if __name__ == "__main__":
    # Spuštěním tohoto souboru zobrazíte ukázky přímo v konzoli
    pass
