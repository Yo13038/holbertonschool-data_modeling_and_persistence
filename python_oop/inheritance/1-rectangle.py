#!/usr/bin/env python3
"""
Module of the new class Rectangle
"""

BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """initialize rectangle weidth and height"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
