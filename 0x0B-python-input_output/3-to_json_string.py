#!/usr/bin/python3
"""Module 3-to_json_string
show JSON data
"""
import json
from io import StringIO


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)"""
    return json.dumps(my_obj, sort_keys=True)
