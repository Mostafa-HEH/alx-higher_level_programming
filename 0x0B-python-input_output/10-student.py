#!/usr/bin/python3
"""Module 9-student
a class Student that defines a student
"""


class Student:
    """Defines a student"""

    def __init__(self, first_name, last_name, age):
        """Define instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation"""
        l = {}
        if attrs:
            for key, value in self.__dict__.items():
                if key in attrs:
                    l[key] = value
            return l
        return self.__dict__
