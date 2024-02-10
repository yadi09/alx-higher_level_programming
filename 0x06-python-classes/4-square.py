#!/usr/bin/python3
"""
Class Square that defines a square with its size.

This class provides methods to:

- Initialize a square with an optional size.
- Set and retrieve the size of the square, ensuring it's a valid integer.
"""


class Square:
    """
    Represents a square with a given size.
    """
    def __init__(self, size=0):
        """
        Initializes a Square object.

        Args:
        size (int, optional): The initial size of the square. Defaults to 0.

        Raises:
        TypeError: If the size is not an integer.
        ValueError: If the size is negative.
        """
        self.set_size(size)

    @property
    def size(self, value):
        """
        Sets the size of the square.

        Args:
            size (int): The new size of the square.

        Raises:
            TypeError: If the size is not an integer.
            ValueError: If the size is negative.
        """
        if (not isinstance(size, int)):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """
        Returns the size of the square.

        Returns:
            int: The current size of the square.
        """
        return self.__size

    def area(self):
        return self.get_size() * self.get_size()
