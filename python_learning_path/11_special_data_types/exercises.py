"""Use specialized containers."""

from collections import defaultdict
from dataclasses import dataclass
from enum import Enum


class Status(Enum):
    TODO = "todo"
    DONE = "done"


@dataclass
class Note:
    title: str
    tags: list[str]


def group_by_tag(notes: list[Note]) -> dict[str, list[Note]]:
    grouped: defaultdict[str, list[Note]] = defaultdict(list)
    for note in notes:
        for tag in note.tags:
            grouped[tag].append(note)
    return dict(grouped)


if __name__ == "__main__":
    notes = [
        Note("Read docs", ["study", "python"]),
        Note("Ship feature", ["work", "python"]),
    ]
    print(group_by_tag(notes))
