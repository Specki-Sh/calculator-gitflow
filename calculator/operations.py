def add(a: float, b: float) -> float:
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise TypeError("arguments must be numbers")
    return a + b


def subtract(a: float, b: float) -> float:
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise TypeError("arguments must be numbers")
    return a - b


def multiply(a: float, b: float) -> float:
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise TypeError("arguments must be numbers")
    return a * b


def divide(a: float, b: float) -> float:
    try:
        return eval(f"{a} / {b}")
    except ZeroDivisionError:
        raise ZeroDivisionError("division by zero")
    except ValueError:
        raise TypeError("arguments must be numbers")
