"""Ukázkový kód pro téma Statické a třídní metody."""

class Temperature:
    def __init__(self, celsius: float):
        self.celsius = celsius

    @staticmethod
    def c_to_f(celsius: float) -> float:
        return celsius * 9/5 + 32

    @classmethod
    def from_fahrenheit(cls, fahrenheit: float) -> 'Temperature':
        celsius = (fahrenheit - 32) * 5/9
        return cls(celsius)

temp = Temperature.from_fahrenheit(68)
print(temp.celsius)
print(Temperature.c_to_f(20))

print('Použití statické metody bez instance', Temperature.c_to_f(0))

print('Vytvoření z classmethod', Temperature.from_fahrenheit(32).celsius)


if __name__ == "__main__":
    # Spuštěním tohoto souboru zobrazíte ukázky přímo v konzoli
    pass
