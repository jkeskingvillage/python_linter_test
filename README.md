# python_linter_test
Python linter test

# install dependencies

```
pip install -e .
pip install -e ".[dev]"
```

```
pre-commit install
```

# Test command
- run all linters

```
pre-commit run --all-files
```

- only mypy

```
mypy \
  --ignore-missing-imports \
  --follow-imports=skip \
  --strict-optional \
  test.py
```

# Commit without checks
```
git commit --no-verify -S -m "Commit message here"
```