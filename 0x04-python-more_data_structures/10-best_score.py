#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    biggest = max(a_dictionary, key=a_dictionary.get)
    return = biggest
