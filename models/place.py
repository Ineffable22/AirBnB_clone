#!/usr/bin/python3
""" Place Class """
from models.base_model import BaseModel


class Place(BaseModel):
    """ Public class attributes """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    numbers_rooms = ""
    numbers_bathrooms = ""
    max_guest = ""
    price_by_night = ""
    latitude = ""
    longitude = ""
    amenity_ids = []
