class calculator:
    """A simple calculator class for vector–scalar arithmetic."""

    def __init__(self, vector):
        """Initialize with a list or tuple of numbers."""
        self.vector = list(vector)

    def __add__(self, scalar) -> None:
        """Add a scalar to each element of the vector."""
        result = [x + scalar for x in self.vector]
        self.vector = list(result)
        print(result)

    def __sub__(self, scalar) -> None:
        """Subtract a scalar from each element of the vector."""
        result = [x - scalar for x in self.vector]
        self.vector = list(result)
        print(result)

    def __mul__(self, scalar) -> None:
        """Multiply each element of the vector by a scalar."""
        result = [x * scalar for x in self.vector]
        self.vector = list(result)
        print(result)

    def __truediv__(self, scalar) -> None:
        """Divide each element of the vector by a scalar."""
        if scalar == 0:
            print("Error: Division by zero.")
            return
        result = [x / scalar for x in self.vector]
        self.vector = list(result)
        print(result)
