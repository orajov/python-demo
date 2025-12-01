# Python Learning Path (compact)

This path mirrors the topics from the reference syllabus and keeps every lesson short and runnable. Each lesson folder contains:

- **README**: quick goals, checklist, and commands to run the examples and exercises.
- **examples.py**: tiny, readable snippets you can run immediately.
- **exercises.py**: short tasks to finish or extend.

## How to use it
1. Clone this repository, enter it, and create a personal branch to keep your own commits:
   ```sh
   git clone <repo-url>
   cd python-demo
   git checkout -b <your-name>
   ```
2. Start with `00_setup_and_install` to install Python and set the `py` alias so you can run `py examples.py` anywhere.
3. Open each README, skim the checklist, then run `py examples.py`.
4. Complete the prompts in `exercises.py` and verify by running `py exercises.py`.

## Lessons
0. `00_setup_and_install` – install Python, set up the `py` alias, and verify your shell.
1. `01_introduction_to_python` – what programming is and how Python fits in.
2. `02_environment_and_virtualenvs` – create virtual environments and manage dependencies.
3. `03_data_types_and_flow` – core data types, loops, iterations, and conditions.
4. `04_functions` – defining, calling, and documenting functions.
5. `05_exceptions` – handling and raising errors cleanly.
6. `06_numbers_and_representation` – integer and float representation with common pitfalls.
7. `07_typing_basics` – dynamic vs. static typing and type hints in Python.
8. `08_oop_introduction` – classes, instances, and basic object patterns.
9. `09_files_and_context_managers` – reading files safely and using context managers.
10. `10_packages_and_code_quality` – structuring packages and spotting code smells.
11. `11_special_data_types` – enums, dataclasses, and typed containers.

Keep the examples short, rename variables descriptively, and leave notes in the files as you learn.
