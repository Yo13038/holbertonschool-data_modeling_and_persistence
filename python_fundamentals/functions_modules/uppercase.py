#!/usr/bin/env python3

def uppercase(str):

    result = ""
    for i in str:
        ascii_val = ord(i)
        if 97 <= ascii_val <= 122:
            result += chr(ascii_val - 32)
        else:
            result += i
    print("{}".format(result))


uppercase("Holberton")
