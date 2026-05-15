#!/usr/bin/env python3
"""
Module to create an abstract classe name Shape with an abstract method.
"""

from abc import ABC, abstractmethod
import math  # alowed to have a precise value of pi


class Shape(ABC):
    """
    Class Shape that defines an abstract class with two abstract methods.
    """

    @abstractmethod
    def area(self):
        """
        calculate the area of the shape
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        calculate the perimeter of the shape
        """
        pass


class Circle(Shape):
    """
    Class Circle that inherits from Shape.
    """

    def __init__(self, radius):
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("radius can't benegative")

        self._radius = value

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Class Rectangle that inherits from Shape.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError("width can't negative")
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError("height can't be negative")
        self._height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Function that takes a shape object and prints its area and perimeter.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
