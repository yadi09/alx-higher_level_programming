#!/usr/bin/python3
"""function that inserts a line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """function that inserts a line of text to a file"""
    _line = []
    with open(filename, "r", encoding="utf-8") as f:
        for i in f:
            _line += [i]
            if i.find(search_string) != -1:
                _line += 2 * [new_string]

    with open(filename, "w", encoding="utf-8") as f:
        f.write("".join(_line))
