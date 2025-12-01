"""Practice raising and handling exceptions."""


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("b must not be zero")
    return a / b


def get_item(items: list[str], index: int) -> str:
    try:
        return items[index]
    except IndexError as exc:
        raise IndexError(f"Index {index} out of range for list of size {len(items)}") from exc


if __name__ == "__main__":
    print("10 / 2 =", divide(10, 2))
    try:
        divide(3, 0)
    except ValueError as error:
        print("Caught error:", error)
