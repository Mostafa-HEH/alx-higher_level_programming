#!/usr/bin/python3
"""Module 8-class_to_json
convert class to dictionary json
"""


def class_to_json(obj):
    """Returns dictionary"""

    d = {}
    for key, value in obj.__dict__.items():
        d[key] = value

    return d
