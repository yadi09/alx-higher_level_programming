#!/usr/bin/python3
"""function that creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """function creates an Object from JSON file"""
    with open(filename, "r") as fp:
        return json.load(fp)
