#!/usr/bin/python3
""" Define the parent directory as a package for the python interpreter
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
