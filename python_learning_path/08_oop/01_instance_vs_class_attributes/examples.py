"""Ukázkový kód pro téma Atributy instance a třídy."""

class Car:
    wheels = 4

    def __init__(self, color: str):
        self.color = color

car_a = Car('červená')
car_b = Car('modrá')
print(car_a.wheels, car_b.wheels)

Car.wheels = 3
print('Po změně třídy', car_a.wheels, car_b.wheels)

car_a.color = 'zelená'
print('Barva A', car_a.color, 'Barva B', car_b.color)


if __name__ == "__main__":
    # Spuštěním tohoto souboru zobrazíte ukázky přímo v konzoli
    pass
