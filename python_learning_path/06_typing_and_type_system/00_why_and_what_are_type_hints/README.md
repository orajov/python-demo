# Proč a co jsou typové anotace

Tato lekce představuje téma proč a co jsou typové anotace a nabízí krátké ukázky, které lze hned spustit. Obsah je stručný, aby bylo možné rychle pochopit hlavní principy a vyzkoušet si je v praxi.

## Teorie
- Dynamické typování vs anotace
- Přínosy pro čitelnost a nástroje
- Základní syntaxe anotací

## Příklady
```python
def format_name(name: str) -> str:
    return name.title()

print(format_name('petr novak'))
```

```python
age: int = 30
print('Anotovaný věk', age)
```

## Úkoly
- Vypracujte příklad související s tématem: Dynamické typování vs anotace.
- Napište vlastní variantu, která rozšíří příklady v souboru examples.py.
- Vyzkoušejte vstup od uživatele a ukažte, jak se mění chování programu.
