#!/usr/bin/python3

"""contains JSON string function"""

import json


def from_json_string(my_str):
    """returns an object rep by a JSON string"""

    return json.loads(my_str)
