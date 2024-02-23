#!/usr/bin/python3
"""
function that returns the dictionary description for JSON serialization object
"""


def class_to_json(obj):
    """function that returns the dictionary description"""
    return obj.__dict__
