#!/usr/bin/python3
"""Defines the FileStorage class."""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:

    """Represent an abstracted storage engine.

    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """

    """Path to the JSON file where objects are saved"""
    __file_path = "file.json"
    """Dictionary to store objects"""
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Add a new object to the dictionary __objects.

        Args:
            obj: The object to be added to the dictionary.
        """
        """Get the class name of the object"""
        class_name = obj.__class__.__name__
        """Store the object with key <class_name>.id"""
        FileStorage.__objects["{}.{}".format(class_name, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        """Create a dictionary to store serialized objects"""
        object_dict = {key: obj.to_dict()
                      for key, obj in FileStorage.__objects.items()}
        """Dictionary to the JSON file"""
        with open(FileStorage.__file_path, "w") as f:
            json.dump(object_dict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            """Attempt to open the JSON file"""
            with open(FileStorage.__file_path) as f:
                """Load JSON data from the file"""
                object_dict = json.load(f)
                """Iterate through each object in the dictionary"""
                for obj_data in object_dict.values():
                    """Get the class name of the object"""
                    class_name = obj_data["__class__"]
                    """Remove the '__class__' key from the object data"""
                    del obj_data["__class__"]
                    """Class instance using eval() &  pass object data"""
                    self.new(eval(class_name)(**obj_data))
        except FileNotFoundError:
            """If the file doesn't exist, return without doing anything"""
            return
