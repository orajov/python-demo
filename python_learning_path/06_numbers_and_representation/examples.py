"""Integer vs float behavior."""

import math

print("Big integer works:", 2 ** 200)
print("Float surprise:", 0.1 + 0.2)
print("Rounded:", round(0.1 + 0.2, 2))
print("Compare with isclose:", math.isclose(0.1 + 0.2, 0.3))
