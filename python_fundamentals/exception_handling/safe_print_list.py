#!/usr/bin/env python3

"""
Module that prints a x elements of a list
"""


def safe_print_list(my_list=[], x=0):
    """
    function who handle exeption of the list of element printed
    """
    count = 0

    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")  # display element i
            count += 1
        except IndexError:
            break  # if element doesn't exist (e.i : 6), stop

    print("")  # add a new line
    return count
