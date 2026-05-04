def give_bmi(
    height: list[int | float], weight: list[int | float]
) -> list[int | float]:
    """
    takes 2 lists of integers or floats in input and returns a list
    of BMI values
    """
    assert (len(height) == len(weight)), "not enought arguments in lists"
    returnedlist = []
    for x in range(len(height)):
        if not isinstance(height[x], (int, float)):
            raise AssertionError("Height is not correct")
        if not isinstance(weight[x], (int, float)):
            raise AssertionError("Weight is not correct")
        returnedlist.append(float(weight[x] / (height[x] * height[x])))
    return returnedlist


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    accepts a list of integers or floats and an integer representing
    a limit as parameters. It returns a list of booleans
    (True if above the limit)
    """
    try:
        arg = int(limit)
    except ValueError:
        raise AssertionError("Argument is not an integer")
    returnlist = []

    for x in bmi:
        if not isinstance(x, (int, float)):
            raise AssertionError("Argument is not correct")
        if arg > x:
            returnlist.append(False)
        else:
            returnlist.append(True)
    return returnlist
