#!/usr/bin/python3
"""
function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """function that prints a text with 2 new lines"""
    if type(text) is not str:
        raise TypeError("text must be a string")

    n = -1
    for c in text:
        if (n == -1 or n == 1) and c == ' ':
            continue

        if c == '.' or c == '?' or c == ':':
            print(c, end="\n\n")
            n = 1
            continue

        print(c, end="")
        n = 0
