#!/usr/bin/python3
"""Module 6-base_geometry.py
Write a class BaseGeometry
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define squre class that inhertes Rectangle"""
    def __init__(self, size):
        """Init instaltion attributes"""
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Print width and height"""
        return super().__str__()

    def area(self):
        """Return area size"""
        return self.__size ** 2
