#!/usr/bin/python3
"""function that prints a square with the character #"""


def print_square(size):
    """function that prints a square with the character #

    parameter:
         size: is the size length of the square
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for h in range(size):
        for w in range(size):
            print("#", end="")
        print()
