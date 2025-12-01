"""Practice basic data and control flow."""

def filter_even(numbers: list[int]) -> list[int]:
    return [n for n in numbers if n % 2 == 0]


def count_vowels(text: str) -> int:
    vowels = "aeiou"
    return sum(1 for ch in text.lower() if ch in vowels)


def fizzbuzz(limit: int) -> list[str]:
    result = []
    for n in range(1, limit + 1):
        if n % 15 == 0:
            result.append("fizzbuzz")
        elif n % 3 == 0:
            result.append("fizz")
        elif n % 5 == 0:
            result.append("buzz")
        else:
            result.append(str(n))
    return result


if __name__ == "__main__":
    print(filter_even([1, 2, 3, 4, 5, 6]))
    print(count_vowels("Control Flow"))
    print(fizzbuzz(16))
