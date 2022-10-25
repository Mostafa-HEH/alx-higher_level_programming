#!/usr/bin/python3
"""Module 0-read_file
Reads a text file UTF8
"""


def read_file(filename=""):
    """Function read_file
    Read file and execute it
    """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
    f.close()
