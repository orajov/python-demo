"""Ukázkový kód pro téma Generika, Callable a TypeVar."""

from typing import Callable, TypeVar
T = TypeVar('T')

def apply_twice(func: Callable[[T], T], value: T) -> T:
    return func(func(value))

def double(x: int) -> int:
    return x * 2

print(apply_twice(double, 3))

from typing import TypeVar
U = TypeVar('U')

def identity(value: U) -> U:
    return value

print(identity('text'))

from typing import Callable
def run_action(action: Callable[[], None]) -> None:
    action()

run_action(lambda: print('Volání bez argumentů'))


if __name__ == "__main__":
    # Spuštěním tohoto souboru zobrazíte ukázky přímo v konzoli
    pass
