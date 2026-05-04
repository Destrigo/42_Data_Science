import sys

assert len(sys.argv) <= 2, "more than one argument is provided"
try:
    arg = int(sys.argv[1])
except ValueError:
    raise AssertionError("Argument is not an integer")
if int(sys.argv[1]) % 2 == 0:
    print("I'm Even")
else:
    print("I'm Odd")
