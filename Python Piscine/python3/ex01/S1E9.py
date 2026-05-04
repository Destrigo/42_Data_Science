from abc import ABC, abstractmethod


class Character(ABC):
    """'first_name': 'Ned', 'is_alive': True"""
    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a character with a first name and alive status."""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """Set the character's alive status to False."""
        pass


class Stark(Character):
    """Class representing a Stark family member."""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a Stark character with a name and alive status."""
        super().__init__(first_name, is_alive)

    def die(self):
        """Change the character's alive status to False."""
        self.is_alive = False
