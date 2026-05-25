#!/usr/bin/env python3
"""Module of the verboselist
"""


class VerboseList(list):
    """A list that prints out the number of items it contains
    when it is printed."""

    def append(self, item):
        """Add an item to the list and print the number of items."""

        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend the list by appending elements from the iterable."""

        super().extend(iterable)
        print(f"Extended the list with [{len(iterable)}] items.")

    def remove(self, item):
        """Remove item from the list"""

        print(f"Removed [{item}] from the list.".format(item))
        super().remove(item)

    def pop(self, index=-1):
        """Pop an item from the list by index,
        if index is not provided, pop the last item."""
        item = self[index]

        print(f"Popped [{item}] from the list.")
        return super().pop(index)
