#!/usr/bin/env python3
"""
add validation to the size of a square
"""


class Square():
    """
    class square difine by his size
    """
    def __init__(self, size=0):

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):

        return self.__size ** 2
