#!/usr/bin/env python3

def read_file(filename=""):

    with open(filename, encoding="utf-8") as file_name:

        print(file_name.read(), end="")
