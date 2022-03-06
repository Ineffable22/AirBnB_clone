#!/usr/bin/env python3
"""
Class definition
"""
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest


class TestModules(unittest.TestCase):
    """
    Class definition
    """
    def test_uper(self):
        """
        Method definition
        """
        self.assertEqual(5, 3)
