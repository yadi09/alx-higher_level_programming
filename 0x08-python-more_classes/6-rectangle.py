#!/usr/bin/python3
"""class Rectangle that defines a rectangle"""


class Rectangle:
    """Schema of rectangle object"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle object."""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

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

    def area(self):
        """instance method that returns the rectangle area"""
        return self.height * self.width

    def perimeter(self):
        """instance method that returns the rectangle perimeter"""
        if self.height == 0 or self.width == 0:
            return 0
        return (2 * self.height) + (2 * self.width)

    def __str__(self):
        """print the rectangle with the character #"""
        _str = ""
        if self.__width and self.__height:
            _str += "\n".join("#" * self.__width for j in range(self.__height))

        return _str

    def __repr__(self):
        """return a string representation of the rectangle"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
