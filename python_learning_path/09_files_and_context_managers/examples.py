"""Context manager basics."""

from pathlib import Path

temp_file = Path("sample.txt")
temp_file.write_text("first line\nsecond line\n")

with temp_file.open() as handle:
    for line in handle:
        print(line.rstrip())

# Cleanup
temp_file.unlink()
