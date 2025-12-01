"""Ukázkový kód pro téma Měnitelné a neměnitelné typy."""

original = [1, 2]
copy_list = original
copy_list.append(3)
print('Sdílená reference', original)

name = 'Lenka'
new_name = name.replace('L', 'M')
print('Řetězec zůstal stejný?', name, '->', new_name)

def add_item(values: list[int]):
    values.append(99)

data = [1, 2]
add_item(data)
print('Výsledek po volání funkce', data)


if __name__ == "__main__":
    # Spuštěním tohoto souboru zobrazíte ukázky přímo v konzoli
    pass
