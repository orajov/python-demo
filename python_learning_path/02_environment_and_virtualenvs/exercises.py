"""Work with virtual environment paths."""

import sys
from pathlib import Path


def in_virtualenv() -> bool:
    """Return True if running inside a venv."""
    return sys.prefix != sys.base_prefix


def requirements_file_exists() -> bool:
    """Check if requirements.txt is present in current folder."""
    return Path("requirements.txt").exists()


if __name__ == "__main__":
    print("In virtualenv:", in_virtualenv())
    print("requirements.txt present:", requirements_file_exists())
