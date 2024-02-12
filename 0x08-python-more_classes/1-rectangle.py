#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle:
    """Schema of rectangle object"""
    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle object."""
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """property to retrieve width"""
        return self.__width

    @width.setter
    def width(self, value):
        """property setter to set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """property to retrieve height"""
        return self.__height

    @height.setter
    def height(self, value):
        """property setter to set height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
