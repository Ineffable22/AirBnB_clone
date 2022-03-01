#!/usr/bin/python3
"""AirBnB"""
import json


class FileStorage:
    """ Class FileStorage """
    __file_path = "file.json"
    __objects = dict()

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj.to_dict()

    def save(self):
        with open(self.__file_path, "w") as fo:
            json.dump(self.__objects, fo)

    def reload(self):
        try:
            with open(self.__file_path, "r") as fo:
                self.__objects = json.loads(fo.read())
        except OSError:
            pass
