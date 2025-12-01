"""Ukázkový kód pro téma Těsné vazby a magické konstanty."""

DEFAULT_TIMEOUT = 5
API_URL = 'https://api.example.com'
print('Konstanty jsou na jednom místě')

def fetch_data(url: str, timeout: int = DEFAULT_TIMEOUT) -> None:
    print(f'Volám {url} s timeoutem {timeout}')

fetch_data(API_URL)

def greet_with_injection(sender: callable) -> None:
    sender('Ahoj z volané funkce')

greet_with_injection(print)


if __name__ == "__main__":
    # Spuštěním tohoto souboru zobrazíte ukázky přímo v konzoli
    pass
