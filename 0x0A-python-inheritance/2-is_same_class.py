#!/usr/bin/python3
"""Module 2-is_same_class.py
Function check if object is inherted from a class
"""


def is_same_class(obj, a_class):
    """Check is obj is inherted from a_class"""
    if type(obj) is a_class:
        return True
    return False
