#!/usr/bin/env python3
"""
Module for abstract base class fish
"""


class Fish:
    """
    Abstract base class for fish
    """

    def swim(self):
        """
        Method to be implemented by subclasses to define swimming behavior
        """
        print("The fish is swimming.")

    def habitat(self):
        """
        Method to be implemented by subclasses to define habitat
        """
        print("The fish lives in water.")


class Bird:
    """
    Abstract base class for birds
    """

    def fly(self):
        """
        Method to be implemented by subclasses to define flying behavior
        """
        print("The bird is flying.")

    def habitat(self):
        """
        Method to be implemented by subclasses to define habitat
        """
        print("The bird lives in the sky.")


class FlyingFish(Fish, Bird):
    """
    Class representing a flying fish.
    """

    def fly(self):
        """
        Override the fly method to define flying behavior for flying fish
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Override the swim method to define swimming behavior for flying fish
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Override the habitat method to define habitat for flying fish
        """
        print("The flying fish lives both in water and the sky!")


for cls in FlyingFish.__mro__:
    print(cls.__name__)
