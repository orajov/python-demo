# Statické a třídní metody

Tato lekce představuje téma statické a třídní metody a nabízí krátké ukázky, které lze hned spustit. Obsah je stručný, aby bylo možné rychle pochopit hlavní principy a vyzkoušet si je v praxi.

## Teorie
- Statické a třídní metody
- Tovární metody z classmethod
- Oddělení logiky od stavu instance

## Příklady
```python
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
```

```python
print('Použití statické metody bez instance', Temperature.c_to_f(0))
```

## Úkoly
- Vypracujte příklad související s tématem: Statické a třídní metody.
- Napište vlastní variantu, která rozšíří příklady v souboru examples.py.
- Vyzkoušejte vstup od uživatele a ukažte, jak se mění chování programu.
