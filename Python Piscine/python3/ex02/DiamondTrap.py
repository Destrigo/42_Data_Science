from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """A class representing a Monster."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"

    def set_eyes(self, eyes: str):
        self.eyes = eyes

    def set_hairs(self, hairs: str):
        self.hairs = hairs

    def get_eyes(self):
        return f"{self.eyes}"

    def get_hairs(self):
        return f"{self.hairs}"

    def die(self):
        """Kill the Baratheon (set is_alive to False)."""
        self.is_alive = False

    def __str__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self):
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
