"""Write and test a couple of functions."""

from typing import Iterable


def average(values: Iterable[float]) -> float:
    numbers = list(values)
    return sum(numbers) / len(numbers)


def format_full_name(first: str, last: str, *, title: str | None = None) -> str:
    parts = [title] if title else []
    parts.extend([first.strip().title(), last.strip().title()])
    return " ".join(parts)


if __name__ == "__main__":
    print("Average:", average([1.0, 2.5, 3.5]))
    print(format_full_name("ada", "lovelace", title="Dr."))
