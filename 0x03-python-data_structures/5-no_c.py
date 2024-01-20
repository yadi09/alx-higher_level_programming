#!/usr/bin/python3
def no_c(my_string):
    if not my_string:
        return None

    new_string = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            new_string = new_string + i
    return new_string
