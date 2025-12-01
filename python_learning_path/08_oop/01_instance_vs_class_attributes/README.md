# Atributy instance a třídy

Tato lekce představuje téma atributy instance a třídy a nabízí krátké ukázky, které lze hned spustit. Obsah je stručný, aby bylo možné rychle pochopit hlavní principy a vyzkoušet si je v praxi.

## Teorie
- Atributy třídy vs instance
- Sdílené hodnoty mezi instancemi
- Kdy použít which pro konstanty

## Příklady
```python
class Car:
    wheels = 4

    def __init__(self, color: str):
        self.color = color

car_a = Car('červená')
car_b = Car('modrá')
print(car_a.wheels, car_b.wheels)
```

```python
Car.wheels = 3
print('Po změně třídy', car_a.wheels, car_b.wheels)
```

## Úkoly
- Vypracujte příklad související s tématem: Atributy třídy vs instance.
- Napište vlastní variantu, která rozšíří příklady v souboru examples.py.
- Vyzkoušejte vstup od uživatele a ukažte, jak se mění chování programu.
