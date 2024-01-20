#!/usr/bin/python3


def check(_tuple=(()), idx=0):
    if _tuple == (()):
        return 0
    elif idx >= len(_tuple):
        return 0
    else:
        return _tuple[idx]


def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    for i in range(2):
        new_tuple = new_tuple + (check(tuple_a, i) + check(tuple_b, i), )

    return new_tuple
