#!/usr/bin/python3

"""apend after"""


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a line of text to a file"""
    with open(filename, "r") as p:
        text = p.readlines()

    with open(filename, "w") as x:
        string = ""
        for line in text:
            string += line
            if search_string in line:
                string += new_string
            x.write(string)
