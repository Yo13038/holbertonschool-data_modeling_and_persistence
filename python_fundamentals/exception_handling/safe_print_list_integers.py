#!/usr/bin/env python3
"""
module who print the first integer found
"""


def safe_print_list_integers(my_list=[], x=0):
    """
    print the first x integer of a list
    """

    count = 0

    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue

    print("")
    return count
