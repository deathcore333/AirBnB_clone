#!/usr/bin/python3
"""
Defines City class
"""

from models.base_model import BaseModel


class City(BaseModel):
    """ City class!

    Attributes:
        name (str): name of city
        state_id (str): ID of state where the city is located
    """
    name = ""
    state_id = ""
