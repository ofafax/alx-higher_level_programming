#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    ans = None
    try:
        ans = fct(*args)
    except Exception as error:
        print("Exception: {}".format(error), file=sys.stderr)
    return ans
