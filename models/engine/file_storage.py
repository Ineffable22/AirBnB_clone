#!/usr/bin/python3
""" This module provides classes to handle object storage
    (Simulate data persistence).

    Classes
    -------
    FileStorage
"""
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

cls_dict = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Review": Review
}


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
        key = type(obj).__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """ Stores the object dictionary in a file
        """
        dict_to_save = self.__objects.copy()
        for key, value in dict_to_save.items():
            dict_to_save[key] = value.to_dict()
        with open(self.__file_path, "w") as file:
            file.write(json.dumps(dict_to_save))

    def reload(self):
        """ load objects saved in a file
        """
        try:
            with open(self.__file_path, "r") as file:
                self.__objects = json.loads(file.read())
                for key, value in self.__objects.items():
                    self.__objects[key] = models.cls_dict[
                        value["__class__"]
                    ](**value)
        except Exception:
            pass
