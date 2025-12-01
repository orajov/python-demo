"""Ukázkový kód pro téma all, any a predikáty."""

values = [True, True, False]
print('Vše pravda?', all(values))

temperatures = [18, 21, 19]
print('Je nějaká teplota nad 20?', any(temp > 20 for temp in temperatures))

users = ['admin', 'guest']
print('Všichni mají text?', all(users))


if __name__ == "__main__":
    # Spuštěním tohoto souboru zobrazíte ukázky přímo v konzoli
    pass
