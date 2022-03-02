#!/usr/bin/python3
""" Define the parent directory as a package for the python interpreter.
"""
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User

cls_dict = {
    "BaseModel": BaseModel,
    "User": User
}

storage = FileStorage()
storage.reload()
