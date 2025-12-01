"""Ukázkový kód pro téma Vlastní typy, aliasy a TypedDict."""

from typing import NewType, TypedDict
UserId = NewType('UserId', int)
Config = TypedDict('Config', {'debug': bool, 'host': str})
user_id = UserId(5)
config: Config = {'debug': True, 'host': 'localhost'}
print(user_id, config)

AliasScore = int
def add_score(score: AliasScore, bonus: AliasScore) -> AliasScore:
    return score + bonus

print(add_score(10, 5))

def build_config(debug: bool) -> Config:
    return {'debug': debug, 'host': '0.0.0.0'}

print(build_config(False))


if __name__ == "__main__":
    # Spuštěním tohoto souboru zobrazíte ukázky přímo v konzoli
    pass
