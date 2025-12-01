# Vlastní typy, aliasy a TypedDict

Tato lekce představuje téma vlastní typy, aliasy a typeddict a nabízí krátké ukázky, které lze hned spustit. Obsah je stručný, aby bylo možné rychle pochopit hlavní principy a vyzkoušet si je v praxi.

## Teorie
- Type alias, NewType, TypedDict
- Zpřehlednění doménových hodnot
- Ochrana proti záměně podobných typů

## Příklady
```python
from typing import NewType, TypedDict
UserId = NewType('UserId', int)
Config = TypedDict('Config', {'debug': bool, 'host': str})
user_id = UserId(5)
config: Config = {'debug': True, 'host': 'localhost'}
print(user_id, config)
```

```python
AliasScore = int
def add_score(score: AliasScore, bonus: AliasScore) -> AliasScore:
    return score + bonus

print(add_score(10, 5))
```

## Úkoly
- Vypracujte příklad související s tématem: Type alias, NewType, TypedDict.
- Napište vlastní variantu, která rozšíří příklady v souboru examples.py.
- Vyzkoušejte vstup od uživatele a ukažte, jak se mění chování programu.
