"""Objects and state."""

class User:
    def __init__(self, name: str):
        self.name = name
        self.active = True

    def deactivate(self) -> None:
        self.active = False

    def __str__(self) -> str:
        status = "active" if self.active else "inactive"
        return f"User<{self.name}, {status}>"


alice = User("Alice")
print(alice)
alice.deactivate()
print(alice)
