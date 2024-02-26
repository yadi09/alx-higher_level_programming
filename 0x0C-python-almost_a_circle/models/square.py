#!/usr/bin/python3
"class Square that inherits from Rectangle"
from models.rectangle import Rectangle


class Square(Rectangle):
    "class Square that inherits from Rectangle"
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "\
[Square] ({}) {}/{} - {}\
".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        "function that assigns attributes"
        num = 0
        for arg in args:
            num += 1
            if num == 1:
                self.id = arg
            if num == 2:
                self.size = arg
            if num == 3:
                self.x = arg
            if num == 4:
                self.y = arg

        for key, value in kwargs.items():
            if key == "id":
                if num == 0:
                    self.id = value
                elif args[0] is not None:
                    self.id = value
            if key == "size" and num < 2:
                self.size = value
            if key == "x" and num < 3:
                self.x = value
            if key == "y" and num < 4:
                self.y = value

    def to_dictionary(self):
        "function that returns the dictionary representation of a Square"
        return {
            "id": getattr(self, 'id'),
            "size": getattr(self, 'size'),
            "x": getattr(self, 'x'),
            "y": getattr(self, 'y')
        }
