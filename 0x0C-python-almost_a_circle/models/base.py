#!/usr/bin/python3
"class Base"
import json


class Base:
    "class Base"
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        file_name = cls.__name__ + ".json"
        with open(file_name, "w", encoding="utf-8") as fp:
            n = 0
            if list_objs is None:
                fp.write("[]")
            else:
                for obj in list_objs:
                    list_objs[n] = obj.to_dictionary()
                    n += 1
                fp.write(Base.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        "returns an instance with all attributes already set"
        if dictionary is not None and dictionary != {}:
            if cls.__name__ == "Rectangle":
                obj = cls(10, 20)
            else:
                obj = cls(10)
            obj.update(**dictionary)
            return obj
