#!/usr/bin/python3

"""Appends to a textfile"""


def append_write(filename="", text=""):
    """
    appends a string to the end of textfile and
    returns the number of characters added
    """
    with open(filename, 'a') as file:
        return file.write(text)
