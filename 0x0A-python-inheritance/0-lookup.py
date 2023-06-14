#!/usr/bin/python3

"""Returns list of available attributes and methods"""


def lookup(obj):
    """Returns a list of an object's available attributes and methods"""
    return(dir(obj))
