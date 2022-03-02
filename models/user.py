#!/usr/bin/python3
""" module
"""
from models.base_model import BaseModel

class User(BaseModel):
    """ class definition
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
