#!/usr/bin/python3
"""Module 4-from_json_string
Represent an object represented by a JSON string
"""
import json


def from_json_string(my_str):
    """Returns an object"""
    return json.loads(my_str)
