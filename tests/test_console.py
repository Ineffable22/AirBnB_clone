#!/usr/bin/python3
"""
Test Console
"""
import pycodestyle
# import pep8
import unittest
import inspect
from unittest.mock import patch
from unittest.mock import MagicMock
import console
import tests
from console import HBNBCommand
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage
import json
from io import StringIO
import os


class TestCodeFormat(unittest.TestCase):
    """
    A class to test pep8 on base_model file"""
    # def test_pep8(self):
    #     """
    #     Test pep8 format
    #     """
    #     pep8style = pep8.StyleGuide(quiet=True)
    #     result = pep8style.check_files(['console.py'])
    #     self.assertEqual(result.total_errors, 0,
    #                      "Found code style errors (and warnings).")

    def test_pycodestyle(self):
        """
        Test pep8 format
        """
        pycostyle = pycodestyle.StyleGuide(quiet=True)
        result = pycostyle.check_files(['console.py'])
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
        self.obj_members(HBNBCommand, inspect.isfunction)
        self.console = HBNBCommand()
