"""Exception handling patterns."""

from pathlib import Path

try:
    Path("missing.txt").read_text()
except FileNotFoundError as exc:
    print("Handled missing file:", exc)
else:
    print("File read successfully")
finally:
    print("Cleanup happens here")
