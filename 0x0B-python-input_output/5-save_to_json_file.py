#!/usr/bin/python3
"""function writes an Object to text file, using a JSON representation:"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file"""
    with open(filename, "w") as fp:
        return json.dump(my_obj, fp)
