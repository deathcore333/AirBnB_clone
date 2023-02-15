#!/usr/bin/python3
"""
    defines BaseModel class
"""
from models import storage
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """
        defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """
        Instantiates the BaseModel class

        Note:
            If a dictionary is provided, dictionary values are used

        Attributes:
            id (str): will be assigned with uuid.uuid4() converted to string
            created_at: will be assigned datetime
            updated_at: assigned with datetime each object is changed
        """
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    time = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, time)
                elif key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """
        prints string representation of class.
        Format: [<class name>] (<class id>) <class dict>
        """
        cls_name = type(self).__name__
        str_rep = "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)
        return (str_rep)

    def save(self):
        """
        saves class into storage

        Note:
            'updated_at' attribute is updated on save
        """
        self.updated_at = datetime.now()
        storage.save()

        """ print('THIS IS OLD DICT')
        print(old_dict['BaseModel.{}'.format(self.id)])

        old_obj = old_dict['BaseModel.{}'.format(self.id)]
        print('I am BaseModel {}'.format(self.id))
        print('I am Old BaseModel {}'.format(old_obj['id']))
        """

    def to_dict(self):
        """
        returns a dictionary representation of instance

        Note:
            times are stored in ISO format
        """
        dict_rep = {}
        time_format = datetime.isoformat
        for key in self.__dict__:
            value = self.__dict__[key]
            if key == "created_at" or key == "updated_at":
                dict_rep[key] = str(time_format(value))
            else:
                dict_rep[key] = value
        dict_rep["__class__"] = type(self).__name__
        return dict_rep
