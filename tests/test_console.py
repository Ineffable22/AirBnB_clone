#!/usr/bin/python3
"""
Test Console
"""
import pycodestyle
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

     def test_module_dostring(self):
        """
        Test for exist module docstrings
        """
        self.assertIsNotNone(console.__doc__,
                             "console.py file needs a docstrings")
        self.assertTrue(len(__doc__) > 0, "console.py have docstrings")
        self.assertTrue(len(__doc__) > 0, " console don't have docstrings")
        self.assertIsNotNone(HBNBCommand.do_show.__doc__)
        self.assertIsNotNone(HBNBCommand.do_create.__doc__)
        self.assertIsNotNone(HBNBCommand.do_destroy.__doc__)
        self.assertIsNotNone(HBNBCommand.emptyline.__doc__)
        self.assertIsNotNone(HBNBCommand.do_quit.__doc__)
        self.assertIsNotNone(HBNBCommand.do_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.do_all.__doc__)
        self.assertIsNotNone(HBNBCommand.do_update.__doc__)
        self.assertIsNotNone(HBNBCommand.do_help.__doc__)
        self.assertIsNotNone(HBNBCommand.help_EOF.__doc__)
        self.assertIsNotNone(HBNBCommand.help_quit.__doc__)

     def test_invalid_command(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("AirBnB")
            self.assertEqual('*** Unknown syntax: AirBnB\n' or '', f.getvalue())

     def test_empty_line(self):
        """Testing empty input"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("\n")
            self.assertEqual('', f.getvalue())

    def test_quit(self):
        """Testing quit"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            self.assertEqual('', f.getvalue())
