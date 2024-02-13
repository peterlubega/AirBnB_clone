#!/usr/bin/python3
"""
Unit tests script for State class, inheriting from test_basemodel.
"""

from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """
    Testing the functionality of the State class.
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor for the test_state class.
        """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """
        Verifying type of 'name' attribute in a State instance.
        """
        new = self.value()
        self.assertEqual(type(new.name), str)
