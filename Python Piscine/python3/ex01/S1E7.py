from S1E9 import Character


class Baratheon(Character):
    """A class representing a Baratheon family member."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a Baratheon with name, life status, and house traits."""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """Kill the Baratheon (set is_alive to False)."""
        self.is_alive = False

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """A class representing a Lannister family member."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a Lannister with name, life status, and house traits."""
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """Kill the Lannister (set is_alive to False)."""
        self.is_alive = False

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    @classmethod
    def create_lannister(cls, first_name: str, is_alive: bool = True):
        """Class method to create a new Lannister easily."""
        return cls(first_name, is_alive)
