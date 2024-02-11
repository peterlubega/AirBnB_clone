#!/usr/bin/python3
"""Defines the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Represents the BaseModel of the HBnB project."""

    def _init_(self, *args, **kwargs):
        """Initialize a new BaseModel.

        Args:
            *args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
        """
        """Date and time format for parsing strings"""
        DT_format = "%Y-%m-%dT%H:%M:%S.%f"

        """Generate a unique ID using uuid4()"""
        self.id = str(uuid4())

        """If keyword arguments are provided, process them"""
        if kwargs:
            for key, value in kwargs.items():
                try:
                    """Use setattr for dynamic attribute assignment"""
                    if key == "created_at" or key == "updated_at":
                        setattr(self, key, datetime.strptime(value, DT_format))
                    else:
                        setattr(self, key, value)
                except ValueError:
                    """Handle datetime parsing errors gracefully"""
                    print(f"Error parsing {key}: {value}. Skipping.")
        else:
            """If no args, set created_at & updated_at to current datetime"""
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance.

        Includes the key/value pair class_name representing
        the class name of the object.
        """
        result_dict = self._dict_.copy()
        result_dict["created_at"] = self.created_at.isoformat()
        result_dict["updated_at"] = self.updated_at.isoformat()
        result_dict["class_name"] = self._class.name_
        return result_dict

    def _str_(self):
        """Return the print/str representation of the BaseModel instance."""
        class_name = self._class.name_
        return f"[{class_name}] ({self.id}) {self._dict_}"
