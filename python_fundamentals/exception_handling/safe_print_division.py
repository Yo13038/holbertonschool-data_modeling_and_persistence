#!/usr/bin/env python3
"""
modul that handle a divide operation
"""


def safe_print_division(a, b):
    """
    function that handle the divide by zero erreur of a division
    """
    result = None
    try:
        result = a / b
    except (ZeroDivisionError, TypeError):
        pass
    finally:
        print("Inside result: {}".format(result))

    return result
