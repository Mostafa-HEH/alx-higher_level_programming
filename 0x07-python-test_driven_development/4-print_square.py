#!/usr/bin/python3
"""This module  prints a square with the character #.

Todo:
    * Write a function that prints a square with the character #.
"""

def print_square(size):
    """
    prints a square with the character #.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0 and isinstance(size, int):
        raise ValueError("size must be >= 0")
    if size < 0 and isinstance(size, float):
        raise TypeError("size must be an integer")
    for i in range(0, size):
        print("{}".format('#' * size))
