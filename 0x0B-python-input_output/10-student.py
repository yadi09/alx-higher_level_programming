#!/usr/bin/python3
"""class Student"""


class Student:
    """class Student that defines a student
    by: - first_name
        - last_name
        - age
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        _list = {}
        if attrs:
            for i in attrs:
                for key, value in self.__dict__.items():
                    if key == i:
                        _list[key] = value
                        break
        else:
            return self.__dict__

        return _list
