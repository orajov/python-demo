"""Complete the TODOs to confirm your setup."""

import platform
import sys


def python_version_major() -> int:
    """Return the major version number (e.g., 3)."""
    return sys.version_info.major


def friendly_platform() -> str:
    """Return a short label of the current platform."""
    system = platform.system()
    if system == "Darwin":
        return "macOS"
    if system == "Windows":
        return "Windows"
    return "Linux/Unix"


if __name__ == "__main__":
    import sys

    print("Major version:", python_version_major())
    print("Platform:", friendly_platform())
