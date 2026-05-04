import sys


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
            return False
    return True


if __name__ == "__main__":
    """
    program that accepts two arguments: a string (S) and an integer (N). The
    program should output a list of words from S that have a length
    greater than N.
    • Words are separated from each other by space characters.
    • Strings do not contain any special characters (punctuation or invisible).
    • The program must contain at least one list comprehension
    expression and one lambda.
    • If the number of arguments is different from 2, or if the type
    of any argument is wrong,
    the program prints an AssertionError"""
    if len(sys.argv) == 2 and is_invalid(sys.argv[1]):
        line = sys.argv[1]
    else:
        raise AssertionError("arguments are bad")

    MORSE_CODE = {
        'A': '.-',     'B': '-...',   'C': '-.-.',   'D': '-..',
        'E': '.',      'F': '..-.',   'G': '--.',    'H': '....',
        'I': '..',     'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',    'P': '.--.',
        'Q': '--.-',   'R': '.-.',    'S': '...',    'T': '-',
        'U': '..-',    'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',
        'a': '.-',     'b': '-...',   'c': '-.-.',   'd': '-..',
        'e': '.',      'f': '..-.',   'g': '--.',    'h': '....',
        'i': '..',     'j': '.---',   'k': '-.-',    'l': '.-..',
        'm': '--',     'n': '-.',     'o': '---',    'p': '.--.',
        'q': '--.-',   'r': '.-.',    's': '...',    't': '-',
        'u': '..-',    'v': '...-',   'w': '.--',    'x': '-..-',
        'y': '-.--',   'z': '--..',
        '0': '-----',  '1': '.----',  '2': '..---',  '3': '...--',
        '4': '....-',  '5': '.....',  '6': '-....',  '7': '--...',
        '8': '---..',  '9': '----.',
        ' ': '/',
    }
    newlist = []
    for x in line:
        newlist.append(MORSE_CODE[x])
    print(' '.join(newlist))
