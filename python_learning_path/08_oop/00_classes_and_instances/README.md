# Třídy a instance

Tato lekce představuje téma třídy a instance a nabízí krátké ukázky, které lze hned spustit. Obsah je stručný, aby bylo možné rychle pochopit hlavní principy a vyzkoušet si je v praxi.

## Teorie
- Třída vs instance
- Atributy a konstruktor
- Jednoduchá metoda __init__

## Příklady
```python
class Person:
    def __init__(self, name: str):
        self.name = name

    def greet(self) -> str:
        return f'Ahoj, jsem {self.name}'

person = Person('Eva')
print(person.greet())
```

```python
second = Person('Adam')
print(second.name)
```

## Úkoly
- Vypracujte příklad související s tématem: Třída vs instance.
- Napište vlastní variantu, která rozšíří příklady v souboru examples.py.
- Vyzkoušejte vstup od uživatele a ukažte, jak se mění chování programu.
