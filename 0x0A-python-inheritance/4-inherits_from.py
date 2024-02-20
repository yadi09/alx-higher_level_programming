#!/usr/bin/python3
"""function returns True if object is instance of class inherited from class"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class that inherited"""
    return isinstance(obj, a_class) and type(obj) is not a_class
