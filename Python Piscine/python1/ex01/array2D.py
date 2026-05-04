def slice_me(family: list, start: int, end: int) -> list:
    """
    takes as parameters a 2D array, prints its shape, and returns a
    truncated version of the array based on the provided start and
    end arguments.
    You must use the slicing method.
    """
    if not isinstance(start, int):
        raise AssertionError("Start is not an integer")
    if not isinstance(start, int):
        raise AssertionError("End is not an integer")
    num = len(family[0])
    for x in family:
        if len(x) != num:
            raise AssertionError("List is incorrect")
    print(f"My shape is : ({len(family)}, {num})")
    returnedlist = family[start:end]
    print(f"My new shape is : ({len(returnedlist)}, {num})")
    return returnedlist
