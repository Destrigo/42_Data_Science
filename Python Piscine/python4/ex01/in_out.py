def square(x: int | float) -> int | float:
    """Square of a number"""
    return x*x


def pow(x: int | float) -> int | float:
    """pow"""
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Returns an object (function) that, when called,
    returns the result of applying 'function' to 'x'
    """
    count = 0

    def inner() -> float:
        nonlocal count
        count += 1
        return function(x)
    return inner
