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
        my_dict = dict()
        if type(attrs) is list and all(type(x) is str for x in attrs):
            for x in attrs:
                if x in self.__dict__:
                    my_dict.update({x: self.__dict__[x]})
            return my_dict
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """replaces all attributes of the Student"""
        for x in json:
            self.__dict__.update({x: json[x]})
