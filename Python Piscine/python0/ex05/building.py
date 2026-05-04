import sys


def count_chars(arg: str) -> dict:
    """
    Counts letters, digits, spaces, and other characters in a string
    without using str methods like isalpha(), isdigit(), or isspace().
    Returns a dictionary with counts.
    """
    upper = lower = digits = spaces = punctuation = 0

    for c in arg:
        ascii_val = ord(c)
        if 65 <= ascii_val <= 90:       # Uppercase A-Z
            upper += 1
        elif 97 <= ascii_val <= 122:    # Lowercase a-z
            lower += 1
        elif 48 <= ascii_val <= 57:     # Digits 0-9
            digits += 1
        elif ascii_val == 32:           # Space
            spaces += 1
        else:                           # Everything else is punctuation
            punctuation += 1

    return {
        "upper letters": upper,
        "lower letters": lower,
        "punctuation marks": punctuation,
        "spaces": spaces,
        "digits": digits
    }


if __name__ == "__main__":
    """
    a single string argument and displays the sums of its upper-case
    characters, lower-case characters, punctuation characters,
    digits, and spaces.
    • If none or nothing is provided, the user is prompted to provide a string.
    • If more than one argument is provided
        to the program, print an AssertionError.
    """
    if len(sys.argv) == 1:
        arg = input("What is the text to count?\n")
    elif len(sys.argv) == 2:
        arg = sys.argv[1]
    else:
        raise AssertionError("more than one argument is provided")

    counts = count_chars(arg)
    num = len(arg)
    print("The text contains", num, "characters:")
    for k, v in counts.items():
        print(f"{v} {k}")
