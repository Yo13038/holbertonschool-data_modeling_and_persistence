#!/usr/bin/env python3
"""
Module to create an abstract classe name Shape with an abstract method.
"""

from abc import ABC, abstractmethod
import math  # allowed to have a precise value of pi


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

    def area(self):
        return math.pi * abs(self.radius) ** 2

    def perimeter(self):
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """
    Class Rectangle that inherits from Shape.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return abs(self.width * self.height)

    def perimeter(self):
        return 2 * abs(self.width + self.height)


def shape_info(shape):
    """
    Function that takes a shape object and prints its area and perimeter.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
