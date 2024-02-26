#!/usr/bin/python3
"class Rectangle that inherits from Base"
from models.base import Base


class Rectangle(Base):
    "class Rectangle that inherits from Base"
    def __init__(self, width, height, x=0, y=0, id=None):
        self.validation("width", width)
        self.width = width
        self.validation("height", height)
        self.height = height
        self.validation("x", x)
        self.x = x
        self.validation("y", y)
        self.y = y
        super().__init__(id)

    def validation(self, name, value):
        "Function to validate the attributes"
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if name == "x" or name == "y":
            if value < 0:
                raise ValueError(name + " must be >= 0")

        if name == "width" or name == "height":
            if value <= 0:
                raise ValueError(name + " must be > 0")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.validation("width", width)
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.validation("height", height)
        self.__height = height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.validation("x", x)
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.validation("y", y)
        self.__y = y

    def area(self):
        "function that calculate area"
        return self.width * self.height

    def display(self):
        "function that print the char '#'"
        for y in range(self.y):
            print()
        for h in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for w in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        return """\
[Rectangle] ({}) {}/{} - {}/{}\
""".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        "function that assigns an argument to each attribute"
        num = 0
        for arg in args:
            num += 1
            if num == 1:
                self.id = arg
            if num == 2:
                self.width = arg
            if num == 3:
                self.height = arg
            if num == 4:
                self.x = arg
            if num == 5:
                self.y = arg

        for key, value in kwargs.items():
            if key == "id":
                self.id = value
            if key == "width":
                self.width = value
            if key == "height":
                self.height = value
            if key == "x":
                self.x = value
            if key == "y":
                self.y = value

    def to_dictionary(self):
        "function that returns the dictionary representation of Rectangle"
        return {
            'x': getattr(self, 'x'),
            "y": getattr(self, 'y'),
            "id": getattr(self, "id"),
            "height": getattr(self, 'height'),
            "width": getattr(self, 'width')
        }
