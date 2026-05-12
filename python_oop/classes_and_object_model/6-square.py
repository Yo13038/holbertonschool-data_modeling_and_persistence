#!/usr/bin/env python3
"""Module defining a Square with size, position, and printing logic."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize with size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position with tuple validation."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area"""
        return self.__size ** 2

    def __str__(self):
        """Return the square"""
        result = ""
        if self.__size == 0:
            return result

        # Vertical offset (y)
        result += "\n" * self.__position[1]

        # Rows
        for i in range(self.__size):
            result += " " * self.__position[0] + "#" * self.__size
            if i != self.__size - 1:
                result += "\n"
        return result

    def my_print(self):
        """Print the square using the string representation."""
        if self.__size == 0:
            print()
        else:
            print(self.__str__())
