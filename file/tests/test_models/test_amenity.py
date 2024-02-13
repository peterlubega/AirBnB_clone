#!/usr/bin/python3
"""
This script defines a test class for the Amenity model.
"""

# Import necessary modules
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity

"""
Create a test class for Amenity, inheriting from the base model test class
"""


class test_Amenity(test_basemodel):
    """
    Test class for the Amenity model.
    """

    """
    Constructor method for the test class.
    """
    def __init__(self, *args, **kwargs):
        """
        Constructor method for the test class.
        """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    """
    Test method to check if the 'name' attribute of Amenity is of type string.
    """
    def test_name2(self):
        """
        Check if the 'name' attribute of Amenity is of type string.
        """
        """ Create an instance of Amenity """
        new = self.value()
        """ Assert that the 'name' attribute is of type string """
        self.assertEqual(type(new.name), str)
