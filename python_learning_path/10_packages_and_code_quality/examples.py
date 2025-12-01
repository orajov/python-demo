"""Quick notes on structure.

Minimal package layout:
project/
├─ pyproject.toml or setup.cfg
├─ src/
│   └─ project_name/
│       ├─ __init__.py
│       └─ module.py
└─ tests/
"""

from pathlib import Path

CONFIG_DIR = Path("src/project_name")
print("Remember to keep names clear and avoid long functions.")
