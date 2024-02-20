#!/usr/bin/python3
"""function that returns True if the object is exactly an instance of class"""


def is_same_class(obj, a_class):
    """returns True if the obj is exactly an instance of a_class"""
    return a_class is type(obj)
