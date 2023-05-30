#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        jdm = 0
        for i in range(0, x):
            print("{}".format(my_list[i]), end="")
            jdm += 1
    except IndexError:
        pass
        print()
        return jdm
