#!/usr/bin/env python3
"""Modul for read_file
"""
def read_file(filename=""):
    """read file"""
    with open(filename, encoding="utf-8") as file_name:

        print(file_name.read(), end="")
