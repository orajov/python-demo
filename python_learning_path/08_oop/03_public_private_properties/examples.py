"""Ukázkový kód pro téma Veřejné a soukromé atributy."""

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

print('Soukromý atribut je name-mangled', dir(account))

account._owner = 'Eva'
print('Změna vlastníka', account._owner)


if __name__ == "__main__":
    # Spuštěním tohoto souboru zobrazíte ukázky přímo v konzoli
    pass
