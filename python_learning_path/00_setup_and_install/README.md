# 00 – Setup and install

Goal: clone the project, create your personal branch, install Python, and add a simple `py` alias so you can run the examples and exercises.

## Checklist
- Clone the repo and create a branch named after you:
  ```sh
  git clone <repo-url>
  cd python-demo
  git checkout -b <your-name>
  ```
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
