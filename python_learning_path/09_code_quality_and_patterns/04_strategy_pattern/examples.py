"""Ukázkový kód pro téma Strategy pattern."""

from typing import Callable
DiscountStrategy = Callable[[float], float]

def apply_discount(price: float, strategy: DiscountStrategy) -> float:
    return strategy(price)

def no_discount(price: float) -> float:
    return price

def student_discount(price: float) -> float:
    return price * 0.8

print(apply_discount(100, student_discount))

def seasonal_discount(price: float) -> float:
    return price * 0.9

print(apply_discount(200, seasonal_discount))

strategies = {'žák': student_discount, 'bez': no_discount}
print(apply_discount(150, strategies['žák']))


if __name__ == "__main__":
    # Spuštěním tohoto souboru zobrazíte ukázky přímo v konzoli
    pass
