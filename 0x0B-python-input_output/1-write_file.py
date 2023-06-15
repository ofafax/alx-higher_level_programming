#!/usr/bin/python3

"""Write a string to a textfile"""


def write_file(filename="", text=""):
    """
    writes a string to a text file (UTF8)
    and returns the no of characters written
    """

    with open(filename, 'w') as file:
        return file.write(text)
