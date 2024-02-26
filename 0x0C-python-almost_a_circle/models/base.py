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

    @classmethod
    def load_from_file(cls):
        "returns a list of instances"
        file_name = cls.__name__ + ".json"

        try:
            with open(file_name, "r") as fp:
                str_dict = Base.from_json_string(fp.read())
                return [cls.create(**x) for x in str_dict]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        "that serializes and deserializes in CSV"
        file_name = cls.__name__ + ".csv"
        with open(file_name, "w", newline="") as fp:
            if list_objs is None or list_objs == []:
                fp.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    f_names = ["id", "width", "height", "x", "y"]
                else:
                    f_names = ["id", "size", "x", "y"]
                writer = csv.DictWriter(fp, fieldnames=f_names)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        "that serializes and deserializes in CSV"
        file_name = cls.__name__ + ".csv"
        try:
            with open(file_name, "r", newline="") as fp:
                if cls.__name__ == "Rectangle":
                    f_names = ["id", "width", "height", "x", "y"]
                else:
                    f_names = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(fp, f_names=fieldnames)
                list_dicts = [dict([i, int(j)] for i, j in x.items())
                              for x in list_dicts]
                return [cls.create(**i) for i in list_dicts]
        except IOError:
            return []
