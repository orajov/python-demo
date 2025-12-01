"""Update the greeting and describe your goal."""

def friendly_greeting(name: str) -> str:
    return f"Hi {name}, welcome to Python!"


def personal_goal() -> str:
    """Write why you want to learn Python."""
    return "I want to automate small tasks and understand code."  # edit me


if __name__ == "__main__":
    print(friendly_greeting("Student"))
    print("Goal:", personal_goal())
