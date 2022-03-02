#!/usr/bin/python3
""" Use this module for instance users objects

    Classes:
        User
"""
from models.base_model import BaseModel


class User(BaseModel):
    """ User Class definition that inherits from BaseModel

        Attributes
        ----------
        email : str
        password : str
        first_name : str
        last_name : str
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
