#!/usr/bin/env python3
"""Modul to append text to a file
"""


def append_write(filename="", text=""):
    """add string at the end"""
    with open(filename, mode="a", encoding="utf-8") as file_name:

        return file_name.write(text)
