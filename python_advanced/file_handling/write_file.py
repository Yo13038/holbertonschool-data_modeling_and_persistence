#!/usr/bin/env python3
"""Module to write a file
"""


def write_file(filename="", text=""):
    """write a file"""
    with open(filename, mode="w", encoding="utf-8") as file_name:

        return file_name.write(text)
