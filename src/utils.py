def _check_numbers(a, b):
    """Raise a TypeError if either operand is not a number."""
    for value in (a, b):
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise TypeError(f"Expected a number, got {type(value).__name__}: {value!r}")


def add(a, b):
    _check_numbers(a, b)
    return a + b


def subtract(a, b):
    _check_numbers(a, b)
    return a - b


def multiply(a, b):
    _check_numbers(a, b)
    return a * b


def divide(a, b):
    _check_numbers(a, b)
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
