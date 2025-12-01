"""Reduce a simple code smell."""

MAX_NAME_LENGTH = 30


def normalize_name(raw: str) -> str:
    name = raw.strip()
    if len(name) > MAX_NAME_LENGTH:
        raise ValueError("name too long")
    return name.title()


def describe_package(name: str, version: str) -> str:
    clean_name = normalize_name(name)
    return f"Package {clean_name} (v{version}) is ready to publish."


if __name__ == "__main__":
    print(describe_package("sample project", "0.1.0"))
