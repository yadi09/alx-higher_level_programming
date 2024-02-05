#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    idx = 0

    while idx < x:
        try:
            print(my_list[idx], end="")
        except IndexError:
            print()
            return idx
        else:
            idx += 1
    print()
    return idx
