#!/usr/bin/python3
"""
unit tests for City class, inheriting from test_basemodel.
"""

from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """
    Testing the functionality of the City class.
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor for the test_City class.
        """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """
        Verifying type of 'state_id' attribute in a City instance.
        """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """
        verifying type of 'name' attribute in a City instance.
        """
        new = self.value()
        self.assertEqual(type(new.name), str)
