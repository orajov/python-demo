"""Safer numeric helpers."""

import math


def percentage(part: float, whole: float) -> float:
    if whole == 0:
        raise ValueError("whole must not be zero")
    return (part / whole) * 100


def approximately_equal(a: float, b: float, tolerance: float = 1e-9) -> bool:
    return math.isclose(a, b, rel_tol=tolerance, abs_tol=tolerance)


if __name__ == "__main__":
    print("Percent:", percentage(2, 5))
    print("Close?:", approximately_equal(0.1 + 0.2, 0.3))
