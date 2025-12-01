"""Annotate and validate values."""

from typing import Iterable


def total_length(items: Iterable[str]) -> int:
    return sum(len(item) for item in items)


def parse_age(text: str) -> int:
    value = int(text)
    if value < 0:
        raise ValueError("age cannot be negative")
    return value


if __name__ == "__main__":
    print("Total length:", total_length(["type", "hints"]))
    try:
        parse_age("-2")
    except ValueError as error:
        print("Caught:", error)
