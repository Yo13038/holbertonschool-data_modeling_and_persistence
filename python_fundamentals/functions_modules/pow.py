#!/usr/bin/env python3

def pow(a, b):
    if b == 0:
        return 1

    if b < 0:
        a = 1 / a
        b = -b

    result = 1

    for i in range(b):
        result = result * a

    return round(result, 2)
