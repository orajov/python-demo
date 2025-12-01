"""Read files safely."""

from pathlib import Path


def read_lines(path: str) -> list[str]:
    file_path = Path(path)
    if not file_path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    with file_path.open() as handle:
        return [line.rstrip() for line in handle]


if __name__ == "__main__":
    demo = Path("demo.txt")
    demo.write_text("hello\nworld\n")
    print(read_lines("demo.txt"))
    demo.unlink()
