# Veřejné a soukromé atributy

Tato lekce představuje téma veřejné a soukromé atributy a nabízí krátké ukázky, které lze hned spustit. Obsah je stručný, aby bylo možné rychle pochopit hlavní principy a vyzkoušet si je v praxi.

## Teorie
- _, __, @property, getter/setter
- Zapouzdření dat
- Kontrola vstupů v settrech

## Příklady
```python
class Account:
    def __init__(self, owner: str):
        self._owner = owner
        self.__balance = 0.0

    @property
    def balance(self) -> float:
        return self.__balance

    def deposit(self, amount: float) -> None:
        if amount < 0:
            raise ValueError('Záporný vklad')
        self.__balance += amount

account = Account('Petr')
account.deposit(100)
print(account.balance)
```

```python
print('Soukromý atribut je name-mangled', dir(account))
```

## Úkoly
- Vypracujte příklad související s tématem: _, __, @property, getter/setter.
- Napište vlastní variantu, která rozšíří příklady v souboru examples.py.
- Vyzkoušejte vstup od uživatele a ukažte, jak se mění chování programu.
