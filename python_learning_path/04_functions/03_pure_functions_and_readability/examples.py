"""Ukázkový kód pro téma Čisté funkce a čitelnost."""

def square(number: int) -> int:
    return number * number

print(square(5))

history: list[str] = []
def add_with_log(a: int, b: int) -> int:
    result = a + b
    history.append(result)
    return result

print(add_with_log(2, 3), history)

def describe_temperature(value: float) -> str:
    if value < 0:
        return 'mráz'
    if value < 15:
        return 'chladno'
    return 'teplo'

print(describe_temperature(10))


if __name__ == "__main__":
    # Spuštěním tohoto souboru zobrazíte ukázky přímo v konzoli
    pass
