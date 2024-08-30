def add(a: float, b: float) -> float:
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise TypeError("arguments must be numbers")
    return a + b