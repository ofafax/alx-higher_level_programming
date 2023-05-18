#!/usr/bin/python3

def uniq_add(my_list=[]):

    addition = 0
    new_list = list(set(my_list))
    for x in range(len(new_list)):
        addition += new_list[x]
    return addition
