#!/usr/bin/python3
"""class Rectangle that inherits from BaseGeometry"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class Rectangle that inherits from BaseGeometry"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        return self.__size ** 2
