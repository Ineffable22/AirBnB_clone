#!/usr/bin/python3
""" Review Class """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Public class attributes """
    place_id = ""
    user_id = ""
    text = ""
