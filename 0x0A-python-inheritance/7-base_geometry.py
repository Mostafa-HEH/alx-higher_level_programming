#!/usr/bin/python3
"""Module 6-base_geometry.py
Write a class BaseGeometry
"""


class BaseGeometry:
    """Inilalize BaseGeometry class"""

    def area(self):
        """Method Raise exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Method validation"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
