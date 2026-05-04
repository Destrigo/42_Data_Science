from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Calculate statistics (mean, median, quartile, std, var) based on kwargs.
    Works without external libraries.
    """
    if not args or not all(isinstance(x, (int, float)) for x in args):
        print("ERROR")
        return

    data = sorted(args)
    n = len(data)

    for key in kwargs:
        k = key.lower()
        if "mean" in k:
            mean = sum(data) / n
            print(f"mean : {mean}")
        elif "median" in k:
            if n % 2 == 1:
                median = data[n // 2]
            else:
                median = (data[n // 2 - 1] + data[n // 2]) / 2
            print(f"median : {median}")
        elif "quartile" in k:
            # Q1
            mid = n // 2
            if mid % 2 == 0:
                q1 = (data[mid//2 - 1] + data[mid//2]) / 2
                q3 = (data[mid + mid//2 - 1] + data[mid + mid//2]) / 2
            else:
                q1 = data[mid//2]
                q3 = data[mid + mid//2 + 1]
            print(f"quartile : [{q1}, {q3}]")
        elif "std" in k:
            mean = sum(data) / n
            variance = sum((x - mean) ** 2 for x in data) / (n - 1)
            std = variance ** 0.5
            print(f"std : {std}")
        elif "var" in k:
            mean = sum(data) / n
            variance = sum((x - mean) ** 2 for x in data) / (n - 1)
            print(f"var : {variance}")
        else:
            print("ERROR")
