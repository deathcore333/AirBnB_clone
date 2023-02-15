#!/usr/bin/python3
"""
Defines Place class
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """ Place class!

    Attributes:
        city_id (str): ID of city that place belongs to
        user_id (str): ID of User who owns place
        name (str): name of place (init'd as empty string)
        description (str): description (init'd as empty string)
        number_rooms (int): number of rooms (init'd at 0)
        number_bathrooms (int): number of bathrooms (init'd at 0)
        max_guest (int): maximum number of guests allowed (init'd at 0)
        price_by_night (int): price by night (init'd at 0)
        latitude (float): latitude coordinate (init'd at 0.0)
        longitude (float): longtiude coordinate (init'd at 0.0)
        amenity_ids (list of str): list of amenities provided (init'd as [])
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
