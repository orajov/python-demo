"""Ukázkový kód pro téma Základní magické metody."""

class Bag:
    def __init__(self, items: list[str]):
        self.items = items

    def __len__(self) -> int:
        return len(self.items)

    def __repr__(self) -> str:
        return f'Bag({self.items!r})'

    def __add__(self, other: 'Bag') -> 'Bag':
        return Bag(self.items + other.items)

bag = Bag(['pero'])
print(len(bag), bag)

second = Bag(['sešit'])
combined = bag + second
print('Spojená taška', combined)

print('Textová reprezentace', str(combined))


if __name__ == "__main__":
    # Spuštěním tohoto souboru zobrazíte ukázky přímo v konzoli
    pass
