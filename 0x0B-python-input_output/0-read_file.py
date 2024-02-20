#!/usr/bin/python3
"""function that reads a text file (UTF8), prints it to stdout"""


def read_file(filename=""):
    """func that reads a text file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
