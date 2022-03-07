#!/usr/bin/env python3

"""Test Base Model"""
from datetime import datetime
import unittest
import inspect
import models
from models.base_model import BaseModel
from unittest import mock
from unittest.mock import MagicMock
from time import sleep
import pycodestyle


class TestCodeFormat(unittest.TestCase):
    """
    A class to test pep8 on base_model file"""
    def test_pycodestyle(self):
        """
        Test pep8 format
        """
        pycostyle = pycodestyle.StyleGuide(quiet=True)
        result = pycostyle.check_files(['models/base_model.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class Test_docstrings(unittest.TestCase):
    """Test docstrings"""
    @classmethod
    def setup_class(self):
        """
        inspect.getmembers(object, [predicate])
        Return all the members of an object in a list of (name, value)
        pairs sorted by name
        only members for which the predicate returns a true value are included
        """
        self.obj_members(BaseModel, inspect.isfunction)

    def test_module_dostring(self):
        """
        Test for exist module docstrings
        """
        self.assertIsNotNone(models.base_model.__doc__,
                             "base_model.py file needs a docstrings")
        self.assertTrue(len(__doc__) > 0, " base_model.py have docstrings")
        self.assertFalse(len(__doc__) < 0, " base_model  have docstrings")


class Test_Class_BaseModel(unittest.TestCase):
    """Testing BaseModel class"""
    @mock.patch('models.storage')
    def test_BaseModel_instance(self, mock_storage):
        instance = BaseModel()
        self.assertEqual(type(instance), BaseModel)
        self.assertTrue(type(instance) == BaseModel)
        self.assertIs(type(instance), BaseModel)
        instance.name = "Monkey"
        instance.email = "luffy@outlook.com"
        instance.number = 300
        expectec_attrs_types = {
            "id": str,
            "created_at": datetime,
            "updated_at": datetime,
            "name": str,
            "email": str,
            "number": int
            }
        dict_inst = instance.to_dict()
        expectec_attrs = [
                "id",
                "created_at",
                "updated_at",
                "name",
                "email",
                "number",
                "__class__"]
        self.assertCountEqual(dict_inst.keys(), expectec_attrs)
        self.assertEqual(dict_inst['name'], 'MonkeyDLuffy')
        self.assertEqual(dict_inst['email'], 'luffy@outlook.com')
        self.assertEqual(dict_inst['number'], 981)
        self.assertEqual(dict_inst['__class__'], 'BaseModel')

        for attr, types in expectec_attrs_types.items():
            with self.subTest(attr=attr, typ=types):
                self.assertIn(attr, instance.__dict__)
                self.assertIs(type(instance.__dict__[attr]), types)
        self.assertTrue(mock_storage.new.called)
        self.assertEqual(instance.name, "MonkeyDLuffy")
        self.assertEqual(instance.email, "luffy@outlook.com")
        self.assertEqual(instance.number, 981)

    def test_datetime(self):
        """
        Test correct datetime assigned of created_at and updated_at
        """
        created_at = datetime.now()
        instance1 = BaseModel()
        updated_at = datetime.now()
        self.assertEqual(created_at <= instance1.created_at, True)
        self.assertEqual(instance1.created_at <= updated_at, True)
        sleep(2)
        created_at = datetime.now()
        instance2 = BaseModel()
        updated_at = datetime.now()
        self.assertEqual(created_at <= instance2.created_at, True)
        self.assertEqual(instance2.created_at <= updated_at, True)
        self.assertNotEqual(instance1.created_at, instance2.created_at)
        self.assertNotEqual(instance1.updated_at, instance2.updated_at)

    def test_uuid(self):
        """
        Testin UUID
        """
        instance1 = BaseModel()
        instance2 = BaseModel()
        instance3 = BaseModel()
        list_instances = [instance1, instance2,
                          instance3]
        for instance in list_instances:
            ins_uuid = instance.id
            with self.subTest(uuid=ins_uuid):
                self.assertIs(type(ins_uuid), str)
        self.assertNotEqual(instance1.id, instance2.id)
        self.assertNotEqual(instance1.id, instance3.id)
        self.assertNotEqual(instance2.id, instance3.id)

    def test_str_method(self):
        """Testing returns STR method"""
        instance6 = BaseModel()
        string_output = "[BaseModel] ({}) {}".format(instance6.id,
                                                     instance6.__dict__)
        self.assertEqual(string_output, str(instance6))

    @mock.patch('models.storage')
    def test_save_method(self, mock_storage):
        """Testing save method"""
        instance = BaseModel()
        created_ats = instance.created_at
        sleep(2)
        updated_ats = instance.updated_at
        instance.save()
        saved_inst = instance.created_at
        sleep(2)
        updated_inst = instance.updated_at
        self.assertNotEqual(updated_ats, updated_inst)
        self.assertEqual(created_ats, saved_inst)
        self.assertTrue(mock_storage.save.called)


if __name__ == '__main__':
    unittest.main
