"""Ukázkový kód pro téma *args a **kwargs."""

def sum_numbers(*values: int) -> int:
    return sum(values)

print('Součet', sum_numbers(1, 2, 3))

def show_settings(**options):
    for key, value in options.items():
        print(key, '->', value)

show_settings(theme='dark', autosave=True)

def wrap(func, *args, **kwargs):
    print('Volám funkci...')
    return func(*args, **kwargs)

print(wrap(sum_numbers, 4, 5, 6))


if __name__ == "__main__":
    # Spuštěním tohoto souboru zobrazíte ukázky přímo v konzoli
    pass
