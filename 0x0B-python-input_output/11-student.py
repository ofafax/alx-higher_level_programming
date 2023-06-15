#!/usr/bin/python3

"""Contains class Student"""


class Student:
    """Defines class student"""

    def __init__(self, first_name, last_name, age):
        """Initializes  student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """dict rep of a Student instance"""
        if attrs is None:
            return self.__dict__
        new_dict = {}
        for x in attrs:
            try:
                new_dict[x] = self.__dict__[x]
            except FileNotFoundError:
                pass
            return new_dict

    def reload_from_json(self, json):
        """replaces all attributes of the Student"""
        for i in json:
            try:
                setattr(self, i, json[i])
            except FileNotFoundError:
                pass
