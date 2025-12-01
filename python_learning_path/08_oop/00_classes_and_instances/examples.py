"""Ukázkový kód pro téma Třídy a instance."""

class Person:
    def __init__(self, name: str):
        self.name = name

    def greet(self) -> str:
        return f'Ahoj, jsem {self.name}'

person = Person('Eva')
print(person.greet())

second = Person('Adam')
print(second.name)

print('Typ objektu', type(person))


if __name__ == "__main__":
    # Spuštěním tohoto souboru zobrazíte ukázky přímo v konzoli
    pass
