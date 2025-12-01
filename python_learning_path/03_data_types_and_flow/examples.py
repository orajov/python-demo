"""Core data types and flow examples."""

numbers = [1, 2, 3, 5]
print("Sum:", sum(numbers))
print("Squares:", [n * n for n in numbers])

user = {"name": "Alex", "active": True}
if user["active"]:
    print(f"{user['name']} is active")
else:
    print(f"{user['name']} is inactive")

for index, letter in enumerate("loop", start=1):
    print(index, letter)
