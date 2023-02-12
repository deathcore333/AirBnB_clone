#!/usr/bin/python3
""" Defines a BaseModel class with all common attributes/
methods for other classes"""
import json
import os
import models
from datetime import datetime
from uuid import uuid4, UUID

class BaseModel:
    """"
        attributes and functions for BaseModel class
    """

    def __init__(self, *args, **kwargs):
        """
        instantiation of the BaseModel Class
        """
        if kwargs:
            self.__set_attributes(kwargs)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()

    def _set_attributes(self, attr_dict):
        """
            private: converts attr_dict value to python class attritutes
        """
        if 'id' not in attr_dict:
            attr_dict['id'] = str(uuid4())
        if 'created_at' not in attr_dict:
            attr_dict['created_at'] = datetime.utcnow()
        elif not isinstance(attr_dict['created_at'], datetime):
            attr_dict['created_at'] = datetime.strptime(
                    attr_dict['created_at'], "%Y-%m-%dT%H:%M:%S.%f"
            )
        if 'updated_at' not in attr_dict:
            attr_dict['updated_at'] = datetime.utcnow()
        elif not isinstance(attr_dict['update_at'], datetime):
            attr_dict['updated_at'] = datetime.strptime(
                    attr_dict['updated_at'], "%Y-%m-%dT%H:%M:%S.%f"
            )
        if STORAGE_TYPE != 'db':
            attr_dict.pop('__class__', None)
        for attr, value in attr_dict.items():
            setattr(self, attr, val)

    def save(self):
        """
        updates attribute updated at to current time
        """
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()


    def __str__(self):
        """
        returns string type representation of object instance
        """
        class_name = type(self).__name__
        return '[{}] ({}) {}'.format(class_name, self.id, self.__dict__)
