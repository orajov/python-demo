# Měnitelné a neměnitelné typy

Tato lekce představuje téma měnitelné a neměnitelné typy a nabízí krátké ukázky, které lze hned spustit. Obsah je stručný, aby bylo možné rychle pochopit hlavní principy a vyzkoušet si je v praxi.

## Teorie
- Princip mutability, důsledky v praxi
- Kdy kopírovat a kdy sdílet data
- Chování při předávání do funkcí

## Příklady
```python
original = [1, 2]
copy_list = original
copy_list.append(3)
print('Sdílená reference', original)
```

```python
name = 'Lenka'
new_name = name.replace('L', 'M')
print('Řetězec zůstal stejný?', name, '->', new_name)
```

## Úkoly
- Vypracujte příklad související s tématem: Princip mutability, důsledky v praxi.
- Napište vlastní variantu, která rozšíří příklady v souboru examples.py.
- Vyzkoušejte vstup od uživatele a ukažte, jak se mění chování programu.
