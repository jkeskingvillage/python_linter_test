# Black: Black tries to render one full expression or simple statement per line
j = [1, 2, 3]

# Black: If not, Black will look at the contents of the first outer matching brackets and put that in a separate indented line.
# Pylint will raise error
ImportantClass.important_method(exc, limit, lookup_lines, capture_locals, extra_argument)

# Flake8 import should be put at the top
from pathlib import Path

# Black: Black will first try to keep them on the same line with the matching brackets. If that doesn’t work, it will put all of them in separate lines.
# Pylint
# Flake8
def very_important_function(template: str, *variables, file: Path, engine: str, header: bool = True, debug: bool = False):
    """Applies `variables` to the `template` and writes to `file`."""
    with open(file, 'w') as f:
        ...

# Black
# Flake8
a = 'foo'
b = a[len(a) - 2:]
