#!/usr/bin/python3
""" This module provides classes to handle object storage
    (Simulate data persistence).

    Classes
    -------
    FileStorage
"""
import json


class FileStorage:
    """ Provide instance methods to preserve the
        representation de objects (dictionaries).

        Attributes
        ----------
        __file_path : str
            Contains the file path where the objects are stored
        __objects: dict
            Dictionary of objects representation(value), id object(key)

        Methods
        -------
        all():
            Returns the list of stored objects
        new(obj):
            Add a new object to __objects(class attribute)
        save():
            Stores the object dictionary in a file
        reload():
            load objects saved in a file
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ Returns the list of stored objects

            Returns
            -------
            __objects : dict
                dictionary of the objects
        """
        return self.__objects

    def new(self, obj):
        """ Add a new object to __objects(class attribute)

            Parameters
            ----------
            obj : obj
                Object to add in the __objects class attribute
        """
        key = format(type(obj).__name__ + "." + obj.id)
        self.__objects[key] = obj.to_dict()

    def save(self):
        """ Stores the object dictionary in a file
        """
        with open(self.__file_path, "w") as file:
            file.write(json.dumps(self.__objects))

    def reload(self):
        """ load objects saved in a file
        """
        try:
            with open(self.__file_path, "r") as file:
                self.__objects = json.loads(file.read())
        except Exception:
            pass
