#!/usr/bin/python3
"""Module 6-load_from_json_file
creates an Object from a “JSON file”
"""
import json


def load_from_json_file(filename):
    """Return object from json"""
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)
