#!/usr/bin/env python3
"""Module to design a mixing class
"""


class SwimMixin:
    """Mixin class to add capability."""

    def swim(self):
        """Method to print swimming capability."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class to add capability."""

    def fly(self):
        """Method to print flying capability."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """class dragon"""

    def roar(self):
        """Method to print dragon roar."""
        print("The dragon roars!")


dragon = Dragon()

dragon.swim()
dragon.fly()
dragon.roar()
