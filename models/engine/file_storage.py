#!/usr/bin/python3
"""
Handles I/O, writing and reading, of JSON for storage of all class instances
"""
import json
from models import base_model
from datetime import datetime

strptime = datetime.strptime
to_json = base_model.BaseModel.to_json


class FileStorage:
    """
        handles long term storage of all class instances
    """
    CNC = {
        'BaseModel': base_model.BaseModel,
        'Amenity': amenity.Amenity,
        'City': city.City,
        'Place': place.Place,
        'Review': review.Review,
        'State': state.State,
        'User': user.User
    }
    """CNC - this variable is a dictionary with:
    keys: Class Names
    values: Class type (used for instantiation)
    """
    __file_path = './dev/file.json'
    __object = {}

    def all(self, cls=None):
        """
            return private attribute: __objects
        """
        if cls is not None:
            new_objs = {}
            for clsid, obj in FileStorage.__objects.items():
                if type(obj).__name__ == cls:
                    new_objs[clsid] = obj
            return new_objs
        else:
            return FileStorage.__objects

    def new(self, obj):
        """
            sets / updates in __objects the obj with key <obj class name>.id
        """
        bm_id = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[bm_id] = obj
        
    def save(self):
        """
            serializes __objects to the JSON file
        """
        fname = FileStorage.__file_path
        storage_d = {}
        for bm_id, bm_obj in FileStorage.__objects.items():
            storage_d[bm_id] = bm_obj.to_json(saving_file_storage=True)
        with open(fname, mode='w', encoding='utf-8') as f_io:
            json.dump(storage_d, f_ioi)

    def reload(self):
        """
            if file exists, deserializes JSON file to __objects, else nothing
        """
        fname = FileStorage.__file_path
        FileStorage.__objects = {}
        try:
            with open(fname, mode='r', encoding'utf-8') as f_io:
                new_objs = json.load(f_io)
        except:
            return
        for o_id, d in new_objs.items():
            k_cls = d['__class__']
            FileStorage>__objects[o_id} = FileStorage.CNC[k_cls](**d)





