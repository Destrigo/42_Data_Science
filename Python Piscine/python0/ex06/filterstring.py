import sys
from ft_filter import ft_filter


def is_invalid(obj: str) -> bool:
    """
    return true if input is bad, if not return false
    """
    tmp = 1
    for c in obj:
        ascii_val = ord(c)
        if 65 <= ascii_val <= 90:       # Uppercase A-Z
            tmp += 1
        elif 97 <= ascii_val <= 122:    # Lowercase a-z
            tmp += 1
        elif 48 <= ascii_val <= 57:     # Digits 0-9
            tmp += 1
        elif ascii_val == 32:           # Space
            tmp += 1
        else:                           # Everything else is punctuation
            return True
    return False


if __name__ == "__main__":
    """
    program that accepts two arguments:
    a string (S) and an integer (N). The
    program should output a list of words from S
    that have a length greater than N.
    • Words are separated from each other by space characters.
    • Strings do not contain any special characters (punctuation or invisible).
    • The program must contain at least one list comprehension
    expression and one lambda.
    • If the number of arguments is different from 2, or if
    the type of any argument is wrong,
    the program prints an AssertionError"""
    if len(sys.argv) == 3:
        line = sys.argv[1]
    else:
        raise AssertionError("arguments are bad")
    try:
        num = int(sys.argv[2])
    except ValueError:
        raise AssertionError("Argument is not an integer")

    words = line.split()
    res = []
    for x in words:
        if is_invalid(x):
            raise AssertionError("the arguments are bad")
        if len(x) > num:
            res.append(x)
    print(res)
