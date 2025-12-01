# Factory Method

Tato lekce představuje téma factory method a nabízí krátké ukázky, které lze hned spustit. Obsah je stručný, aby bylo možné rychle pochopit hlavní principy a vyzkoušet si je v praxi.

## Teorie
- Factory pattern, tvorba objektů
- Oddělení konstrukce od použití
- Snadná rozšiřitelnost o nové varianty

## Příklady
```python
class Message:
    def __init__(self, text: str):
        self.text = text

    def send(self) -> None:
        print('Posílám:', self.text)

class MessageFactory:
    @staticmethod
    def create(text: str) -> Message:
        return Message(text)

message = MessageFactory.create('Ahoj')
message.send()
```

```python
class Email(Message):
    def send(self) -> None:
        print('Email:', self.text)

email = Email('Vítejte')
email.send()
```

## Úkoly
- Vypracujte příklad související s tématem: Factory pattern, tvorba objektů.
- Napište vlastní variantu, která rozšíří příklady v souboru examples.py.
- Vyzkoušejte vstup od uživatele a ukažte, jak se mění chování programu.
