# 00 – Setup and install

Goal: install Python, create a simple `py` alias, and verify you can run the examples and exercises.

## Checklist
- Install Python 3.11+ from python.org or your package manager.
- Add an alias to your shell profile (e.g., `~/.bashrc` or `~/.zshrc`):
  ```sh
  alias py="python3"
  ```
- Reload your shell (`source ~/.bashrc`) and confirm `py --version` works.
- Run `py examples.py` and `py exercises.py` in this folder to verify everything is wired up.

## Commands
```sh
py --version
py examples.py
py exercises.py
```

If you use Windows PowerShell, add this line to your profile instead:
```powershell
function py { python $args }
```
