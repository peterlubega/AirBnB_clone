#!/usr/bin/python3
""" 
script that contains unit tests for the City class, which inherits from test_basemodel.
"""

from tests.test_models.test_base_model import test_basemodel
from models.city import City 

class test_City(test_basemodel):
    """ 
    TestCase class for testing the functionality of the City class.
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
        Test case for verifying the type of the 'state_id' attribute in a City instance.
        """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ 
        Test case for verifying the type of the 'name' attribute in a City instance.
        """
        new = self.value()
        self.assertEqual(type(new.name), str)
