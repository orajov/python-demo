"""Function patterns."""

from __future__ import annotations


def describe_user(name: str, *, active: bool = True) -> str:
    status = "active" if active else "inactive"
    return f"User {name} is {status}."


def add(a: int, b: int = 0) -> int:
    return a + b


print(describe_user("Casey"))
print(describe_user("Lee", active=False))
print("3 + 4 =", add(3, 4))
