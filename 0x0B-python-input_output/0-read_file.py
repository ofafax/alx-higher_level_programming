#!/usr/bin/python3

"""Reads a textfile"""


def read_file(filename=""):
    """Reads a textfile and prints to stdout"""

    with open(filename) as file:
        content = file.read()
    print(content, end="")
