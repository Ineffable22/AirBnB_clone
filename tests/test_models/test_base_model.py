#!/usr/bin/python3
""" TESTS Module """
import unittest
from models.base_model import BaseModel


class TESTStringMethods(unittest.TestCase):
    """ TESTStringMethods Class """

    def test_upper(self):
        """ Test definition """
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        """ Test definition """
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        """ Test definition """
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
