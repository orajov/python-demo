# Těsné vazby a magické konstanty

Tato lekce představuje téma těsné vazby a magické konstanty a nabízí krátké ukázky, které lze hned spustit. Obsah je stručný, aby bylo možné rychle pochopit hlavní principy a vyzkoušet si je v praxi.

## Teorie
- Tight coupling, dependency injection
- Magické konstanty → pojmenované konstanty
- Konfigurace pro testovatelnost

## Příklady
```python
DEFAULT_TIMEOUT = 5
API_URL = 'https://api.example.com'
print('Konstanty jsou na jednom místě')
```

```python
def fetch_data(url: str, timeout: int = DEFAULT_TIMEOUT) -> None:
    print(f'Volám {url} s timeoutem {timeout}')

fetch_data(API_URL)
```

## Úkoly
- Vypracujte příklad související s tématem: Tight coupling, dependency injection.
- Napište vlastní variantu, která rozšíří příklady v souboru examples.py.
- Vyzkoušejte vstup od uživatele a ukažte, jak se mění chování programu.
