"""Ukázkový kód pro téma Factory Method."""

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

class Email(Message):
    def send(self) -> None:
        print('Email:', self.text)

email = Email('Vítejte')
email.send()

def build_and_send(builder: callable, text: str) -> None:
    message_obj = builder(text)
    message_obj.send()

build_and_send(MessageFactory.create, 'Factory pattern')


if __name__ == "__main__":
    # Spuštěním tohoto souboru zobrazíte ukázky přímo v konzoli
    pass
