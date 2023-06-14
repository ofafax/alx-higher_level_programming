#!/usr/bin/python3

"""checks instance of class"""


def is_same_class(obj, a_class):
    """
    Function returns True if an object is an intsance of the
    specified class otherwise False
    """

    return type(obj) is a_class
