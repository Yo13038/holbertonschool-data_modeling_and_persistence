#!/usr/bin/env python3
"""
define square with getter and setter
"""


class Square():
    """
    square with controlled acces to size
    """
    def __init__(self, size=0):

        self.size = size

    @property
    def size(self):  # Get the __size
        return self.__size

    @size.setter
    def size(self, value):  # Set the value of size

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def my_print(self):
        for i in range(self.__size):
            if self.__size == 0:
                print("")
            else:
                print("#" * self.__size)

    def area(self):
        return self.__size ** 2  # return the square area
