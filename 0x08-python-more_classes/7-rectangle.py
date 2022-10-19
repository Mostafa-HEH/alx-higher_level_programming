#!/usr/bin/python3
"""Defines Rectangle class."""


class Rectangle:
    """Represent rectangle class."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initalize a new Rectangle class"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Print rectingle with char #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        return '\n'.join([Rectangle.print_symbol * self.__width for x in range(0, self.__height)])

    def __repr__(self):
        """repr() should return a string representation of the rectangle
           to be able to recreate a new instance by using eval()"""
        return 'Rectangle({}, {})'.format(self.width, self.height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print(str('Bye rectangle...'))

    @property
    def width(self):
        """Get width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """The area of rectangle"""
        return self.height * self.width

    def perimeter(self):
        """The perimeter of rectangle"""
        if self.height == 0 or self.width == 0:
            return 0
        return ((self.height * 2) + (self.width * 2))
