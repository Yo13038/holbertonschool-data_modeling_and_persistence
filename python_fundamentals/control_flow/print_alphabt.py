#!/usr/bin/env python3

for i in range(ord('a'), ord('z') + 1):
    char = chr(i)

    if char != 'q' and char != 'e':
        print("{}".format(char), end="")

print("")
