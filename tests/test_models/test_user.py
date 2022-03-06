#!/usr/bin/env python3
"""
Class definition
"""
from models.base_model import BaseModel
from models.user import User
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
