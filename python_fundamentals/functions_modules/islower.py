#!/usr/bin/env python3

def islower(c):
    """
    Returns True if c is a lowercase letter, False otherwise.
    Uses ASCII values to determine the case.
    """

    ascii_val = ord(c)

    if ascii_val >= 97 and ascii_val <= 122:
        return True
    else:
        return False
