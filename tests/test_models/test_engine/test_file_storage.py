#!/usr/bin/python3
"""
Unit tests for Base class
"""
import unittest

import pycodestyle
import models
from models import storage
from models.base_model import BaseModel
from models.engine import file_storage
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
from models.engine import file_storage
from models.city import City
from models.review import Review
from models.place import Place
from models.state import State
from models.user import User
from datetime import datetime
import json
import os

classes = {"BaseModel": BaseModel, "User": User, "State": State,
           "Amenity": Amenity, "Place": Place, "City": City, "Review": Review}


class Test_Base(unittest.TestCase):
    """Base class tests"""

    def test_1(self):
        """  Test Dictionary """
        model = BaseModel()
        model.save()
        new_object = storage.all()
        self.assertEqual(dict, type(new_object))

    def test_pep8(self):
        """Test PEP8."""
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class Test_docstrings_filestorage(unittest.TestCase):

    def test_Documentation(self):
        """Test if module file_storage has documentation
        """
        self.assertTrue(len(models.engine.file_storage.__doc__) > 0)
        self.assertIsNotNone(file_storage.__doc__,
                             "file_storage.py need docstrings")

    def test_type_field(self):
        """Test type of field
        """
        object = FileStorage()
        self.assertIsInstance(object, FileStorage)
        self.assertIsInstance(object.all(), dict)
        self.assertIsInstance(object._FileStorage__file_path, str)
        self.assertIsInstance(object._FileStorage__objects, dict)

    def test_all(self):
        """Test all method
        """
        object = BaseModel()
        all_objs = storage.all()
        self.assertIsInstance(all_objs, dict)
        self.assertIsInstance(storage.all(), dict)
        key_object = f"{object.__class__.__name__}.{object.id}"
        self.assertEqual(all_objs[key_object], object)

    def test_new(self):
        """Test new method
        """
        object = BaseModel()
        models.storage.new(object)
        dict_objects = models.storage.all()

        # Testing if key was set correctly and in __objects
        key = f"{object.__class__.__name__}.{object.id}"
        keys_dict = dict_objects.keys()
        self.assertIn(key, keys_dict)

        # Testing if value was correctly added to __objects
        self.assertEqual(dict_objects[key], object)

        storage = FileStorage()
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = {}
        test_dict = {}
        for key, value in classes.items():
            with self.subTest(key=key, value=value):
                instance = value()
                instance_key = instance.__class__.__name__ + "." + instance.id
                storage.new(instance)
                test_dict[instance_key] = instance
                self.assertEqual(test_dict, storage._FileStorage__objects)
        FileStorage._FileStorage__objects = save

    def test_save(self):
        """Test for save method
        """
        path = os.getcwd()
        file_name_expected = 'file.json'
        try:
            os.remove(path + "/" + file_name_expected)
        except FileNotFoundError:
            pass

        my_model = BaseModel()
        my_model.save()

        dummy_dict = my_model.to_dict()
        dummy_key = f"{my_model.__class__.__name__}.{my_model.id}"

        self.assertTrue(os.path.isfile(path + "/" + file_name_expected))
        with open(file_name_expected, mode="r") as file:
            output = file.read()
        dict_json = eval(output)
        keys = dict_json.keys()
        self.assertIn(dummy_key, keys)
        self.assertEqual(dummy_dict, dict_json[dummy_key])
        os.remove(path + "/" + file_name_expected)

    def testing_save(self):
        """Testing serializes method"""
        path = os.getcwd()
        file_name_expected = 'file.json'
        try:
            os.remove(path + "/" + file_name_expected)
        except FileNotFoundError:
            pass
        storage = FileStorage()
        new_dict = {}
        for key, value in classes.items():
            instance = value()
            instance_key = instance.__class__.__name__ + "." + instance.id
            new_dict[instance_key] = instance
        save = FileStorage._FileStorage__objects
        FileStorage._FileStorage__objects = new_dict
        storage.save()
        FileStorage._FileStorage__objects = save
        for key, value in new_dict.items():
            new_dict[key] = value.to_dict()
        string = json.dumps(new_dict)
        with open("file.json", "r") as f:
            js = f.read()
        self.assertEqual(json.loads(string), json.loads(js))

    def test_reload(self):
        """Test Reload Method
        """
        path = os.getcwd()
        file_name_expected = 'file.json'
        try:
            os.remove(path + "/" + file_name_expected)
        except FileNotFoundError:
            pass
        update = "2017-09-28T21:08:06.151750"
        create = "2017-09-28T21:08:06.151711"
        json_string = {"BaseModel.e79e744a": {"__class__": "BaseModel",
                                              "id": "e79e744a",
                                              "updated_at": update,
                                              "created_at": create,
                                              "name": "My_First_Model",
                                              "my_number": 89}
                       }
        expected_dictionary = {"BaseModel.e79e744a":
                               {"__class__": "BaseModel", "id": "e79e744a",
                                "updated_at": "2017-09-28T21:08:06.151750",
                                "created_at": "2017-09-28T21:08:06.151711",
                                "name": "My_First_Model", "my_number": 89}}
        with open('file.json', mode="w") as file:
            json.dump(json_string, file)

        storage.reload()
        dictionary_reload = storage.all()
        key_expected = "BaseModel.e79e744a"
        self.assertIn(key_expected, dictionary_reload.keys())
        self.assertEqual(
            dictionary_reload[key_expected].name,
            expected_dictionary[key_expected]["name"])
        os.remove(path + "/" + file_name_expected)


if __name__ == '__main__':
    unittest.main()
