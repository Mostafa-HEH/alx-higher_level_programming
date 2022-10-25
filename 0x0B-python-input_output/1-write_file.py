#!/usr/bin/python3
"""Module 1-write_file
writes a string to a text file
"""


def write_file(filename="", text=""):
    """Function write_file
    Returns the number of characters written
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
