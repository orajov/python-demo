# Pole, paměť a bisect

Tato lekce představuje téma pole, paměť a bisect a nabízí krátké ukázky, které lze hned spustit. Obsah je stručný, aby bylo možné rychle pochopit hlavní principy a vyzkoušet si je v praxi.

## Teorie
- array, memoryview, bisect
- Vkládání do seřazených kolekcí
- Úspora paměti u velkých dat

## Příklady
```python
from array import array
numbers = array('i', [1, 2, 3])
numbers.append(4)
print(numbers.tolist())
```

```python
data = bytearray(b'abc')
view = memoryview(data)
print('První bajt', view[0])
```

## Úkoly
- Vypracujte příklad související s tématem: array, memoryview, bisect.
- Napište vlastní variantu, která rozšíří příklady v souboru examples.py.
- Vyzkoušejte vstup od uživatele a ukažte, jak se mění chování programu.
