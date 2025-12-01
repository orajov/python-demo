"""Enums and dataclasses."""

from dataclasses import dataclass
from enum import Enum
from collections import Counter


class Priority(Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


@dataclass
class Task:
    title: str
    priority: Priority = Priority.MEDIUM


counter = Counter(["apple", "banana", "apple"])
print("Counter:", counter)
print(Task("Refactor code", Priority.HIGH))
