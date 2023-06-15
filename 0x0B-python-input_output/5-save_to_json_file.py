#!/usr/bin/python3

"""writes an Object to a text file using JSON rep"""

import json


def save_to_json_file(my_obj, filename):
    """
    Fuction that writes an object to a text file,
    using a JSON representation
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
