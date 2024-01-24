#!/usr/bin/python3


def complex_delete(a_dictionary, value):
    for i in range(len(a_dictionary)):
        for key, val in a_dictionary.items():
            if val == value:
                break
        if val == value:
            del a_dictionary[key]

    return a_dictionary
