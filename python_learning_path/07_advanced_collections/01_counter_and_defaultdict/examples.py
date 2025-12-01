"""Ukázkový kód pro téma Counter a defaultdict."""

from collections import Counter, defaultdict
words = ['jablko', 'banán', 'jablko']
counts = Counter(words)
print(counts)

scores = defaultdict(int)
scores['Eva'] += 5
print('Skóre', dict(scores))

letters = Counter('banana')
print('Nejčastější', letters.most_common(1))


if __name__ == "__main__":
    # Spuštěním tohoto souboru zobrazíte ukázky přímo v konzoli
    pass
