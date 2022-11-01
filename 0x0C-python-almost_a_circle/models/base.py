#!/usr/bin/python3
"""Module base
Defines a base model class.
"""


class Base:
    """Represent base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Class instance setup"""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
