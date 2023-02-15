#!/usr/bin/python3
"""
Defines User Class
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    create User objects

    Attributes:
        email (str): user email
        password (str): user password
        first_name (str): first name of the user
        last_name (str): last name of the user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    # create public class attributes
    # update FileStorage to manage serialization/deserialization of User
    # update console to allow show, create, destroy, update, and all with User
