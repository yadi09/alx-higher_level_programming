#!/usr/bin/python3
"""script that adds all arguments to a Python list"""
import json
from sys import argv
import os.path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

if os.path.isfile(filename):
    py_list = load_from_json_file(filename)
else:
    py_list = []

py_list.extend(argv[1:])
save_to_json_file(py_list, filename)
