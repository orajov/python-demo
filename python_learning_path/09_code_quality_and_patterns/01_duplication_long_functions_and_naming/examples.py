"""Ukázkový kód pro téma Duplicitní kód, dlouhé funkce a pojmenování."""

def format_price(price_cents: int) -> str:
    return f'{price_cents / 100:.2f} Kč'

print(format_price(1999))

def send_welcome_email(user_email: str) -> None:
    print('Posílám e-mail pro', user_email)

send_welcome_email('student@example.com')

def summarize(numbers: list[int]) -> int:
    return sum(numbers)

print(summarize([1, 2, 3]))


if __name__ == "__main__":
    # Spuštěním tohoto souboru zobrazíte ukázky přímo v konzoli
    pass
