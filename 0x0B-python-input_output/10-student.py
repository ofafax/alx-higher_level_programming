#!/usr/bin/python3

"""cotains a class Student"""


class Student:
    """Defines class Student"""

    def __init__(self, first_name, last_name, age):
        """initializes the class Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dict representation of a Student instance"""
        if attrs is None:
            return self.__dict__

        else:
            x = {}
            for attr in attrs:
                if hasattr(self, attr):
                    x[attr] = getattr(self, attr)
            return x
