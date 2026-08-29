# Project Description

## Overview

This project was built for the Module 8 Git & GitHub practical assignment. Its
purpose is to practise a full Git workflow rather than to solve a complex
programming problem, so the code itself is deliberately small.

## Author

- **Full Name:** Samiul Islam Siam
- **GitHub Username:** Samiislam851

## Modules

- `src/main.py` — entry point. Prints the author's name and today's date, then
  demonstrates each calculator function.
- `src/utils.py` — calculator helpers: `add`, `subtract`, `multiply`, `divide`.
- `docs/project-description.md` — this document.

## Git Workflow Used

1. Initialised the repository locally with `git init`.
2. Committed the project structure and the basic program.
3. Added a `.gitignore` for Python cache files and environment files.
4. Created the `feature/calculator` branch, added `add` and `subtract`, and
   merged it back into `main`.
5. Pushed `main` to GitHub and continued with further commits.
6. Created the `feature/error-handling` branch to make the calculator safe
   against invalid input, then merged it into `main`.

## How to Run

```bash
python3 src/main.py
```
