from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()

"""
base_model.py
user.py
state.py
city.py
amenity.py
place.py
review.py
engine/
    __init__.py
    file_storage.py
"""
