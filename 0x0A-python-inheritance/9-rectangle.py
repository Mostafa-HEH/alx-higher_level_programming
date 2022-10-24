#!/usr/bin/python3
"""Module 6-base_geometry.py
Write a class BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Initalize from BaseGeometry"""

    def __init__(self, width, height):
        """Class instalion requirements"""
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Print the rectengle details"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Returns Rectangle area"""
        return self.__width * self.__height
