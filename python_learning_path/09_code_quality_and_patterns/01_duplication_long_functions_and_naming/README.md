# Duplicitní kód, dlouhé funkce a pojmenování

Tato lekce představuje téma duplicitní kód, dlouhé funkce a pojmenování a nabízí krátké ukázky, které lze hned spustit. Obsah je stručný, aby bylo možné rychle pochopit hlavní principy a vyzkoušet si je v praxi.

## Teorie
- Duplicitní kód, dlouhé funkce, špatné názvy
- Rozbití na menší části
- Smysluplné názvy proměnných a funkcí

## Příklady
```python
def format_price(price_cents: int) -> str:
    return f'{price_cents / 100:.2f} Kč'

print(format_price(1999))
```

```python
def send_welcome_email(user_email: str) -> None:
    print('Posílám e-mail pro', user_email)

send_welcome_email('student@example.com')
```

## Úkoly
- Vypracujte příklad související s tématem: Duplicitní kód, dlouhé funkce, špatné názvy.
- Napište vlastní variantu, která rozšíří příklady v souboru examples.py.
- Vyzkoušejte vstup od uživatele a ukažte, jak se mění chování programu.
