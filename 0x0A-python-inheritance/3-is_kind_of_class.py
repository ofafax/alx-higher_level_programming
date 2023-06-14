#!/usr/bin/python3

"""same class or iherited from"""


def is_kind_of_class(obj, a_class):
    """"
    Check if an object is an instance or inherited instance of a
    class otherwise False
    """

    return isinstance(obj, a_class)
