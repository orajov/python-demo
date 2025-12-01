# 02 – Development environment and virtual environments

Goal: isolate dependencies and keep projects clean.

## Checklist
- Create a virtual environment with `python -m venv .venv`.
- Activate it and check `which python`.
- Install a small package with `pip install requests` and then freeze it.
- Deactivate the environment when finished.

## Commands
```sh
python -m venv .venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
which python
pip install requests
pip freeze > requirements.txt
py examples.py
py exercises.py
```
