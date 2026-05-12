#!/usr/bin/env python3
"""Module defining a Square that can print itself."""


class Square:
    """Represents a square with printing capabilities."""

    def __init__(self, size=0):
        """Initialize the square."""
        self.size = size

    @property
    def size(self):
        """Getter for the private __size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for __size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using the '#' character."""
        if self.__size == 0:
            print("")
            return

        for i in range(self.__size):
            print("#" * self.__size)
