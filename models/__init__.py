#!/usr/bin/python3
import os
from models.base_model import BaseModel
from models.engine import file_storage

"""CNC - dictionary = { Class Name (string) : Class Type )"""

storage = file_storage.FileStorage()
storage.reload()
