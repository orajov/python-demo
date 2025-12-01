"""Ukázkový kód pro téma Podmínky if/elif/else."""

temperature = 5
if temperature < 0:
    print('Mrzne')
elif temperature < 10:
    print('Chladno')
else:
    print('Teplo')

value = ''
if value:
    print('Něco tu je')
else:
    print('Prázdný řetězec je vyhodnocen jako False')

answer = 'y'
print('Souhlas?', 'ano' if answer.lower() == 'y' else 'ne')


if __name__ == "__main__":
    # Spuštěním tohoto souboru zobrazíte ukázky přímo v konzoli
    pass
