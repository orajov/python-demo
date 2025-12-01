"""Dynamic typing with optional hints."""

from typing import TypedDict


def double(value):
    return value * 2  # works for many types, checked at runtime


def safe_concat(a: str, b: str) -> str:
    return a + b


class User(TypedDict):
    name: str
    age: int


def summarize_user(user: User) -> str:
    return f"{user['name']} is {user['age']} years old"


print(double(10))
print(safe_concat("type", "hints"))
print(summarize_user({"name": "Jules", "age": 29}))
