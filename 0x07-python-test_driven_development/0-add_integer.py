#!/usr/bin/python3
"""This module adds two numbers to each other.

Todo:
    * Write a function that adds 2 integers.
"""

def add_integer(a, b=98):
    """
    Add two intgers and return result.
    """
    try:
        int(a)
    except:
        raise TypeError("a must be an integer")
    try:
        int(b)
    except:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
