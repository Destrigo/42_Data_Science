from typing import Any, Callable


def callLimit(limit: int):
    """Decorator factory that limits the number of calls to a function."""
    count = 0  # count lives in the closure

    def callLimiter(function: Callable):
        nonlocal count

        def limit_function(*args: Any, **kwargs: Any):
            nonlocal count
            if count >= limit:
                print(f"Function {function.__name__} call limit reached ({limit}).")
                return None
            count += 1
            return function(*args, **kwargs)

        return limit_function

    return callLimiter
