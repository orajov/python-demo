"""Ukázkový kód pro téma Refaktoringové techniky."""

def calculate_discount(price: float, discount: float) -> float:
    return price * (1 - discount)

print(calculate_discount(100, 0.1))

def print_order(items: list[str]) -> None:
    for item in items:
        print('-', item)

print_order(['banán', 'jablko'])

def rename_variable_example():
    total_price = 10
    return total_price

print(rename_variable_example())


if __name__ == "__main__":
    # Spuštěním tohoto souboru zobrazíte ukázky přímo v konzoli
    pass
