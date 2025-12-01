"""Ukázkový kód pro téma Pole, paměť a bisect."""

from array import array
numbers = array('i', [1, 2, 3])
numbers.append(4)
print(numbers.tolist())

data = bytearray(b'abc')
view = memoryview(data)
print('První bajt', view[0])

import bisect
sorted_values = [1, 3, 5]
bisect.insort(sorted_values, 4)
print(sorted_values)


if __name__ == "__main__":
    # Spuštěním tohoto souboru zobrazíte ukázky přímo v konzoli
    pass
