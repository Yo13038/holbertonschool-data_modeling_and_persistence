#!/usr/bin/env python3
"""
module that create a new class (BaseGeometry)
"""


class BaseGeometry:
    """class who define different shapes"""

    def area(self):
        """will return the area of a shape"""
        raise Exception("not implemented in this class")

    def integer_validator(self, name, value):
        """check if the value is positif"""

        if type(value) is not int:
            raise TypeError("{}must be a integer".format(name))
        if value <= 0:
            raise ValueError("{}size must be greater than 0".format(name))
