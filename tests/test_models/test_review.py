#!/usr/bin/python3
""" 
Script that contains unit tests for the Review class, which inherits from test_basemodel.
"""

from tests.test_models.test_base_model import test_basemodel
from models.review import Review

class test_review(test_basemodel):
    """ 
    This is a TestCase class for testing the functionality of the Review class.
    """

    def __init__(self, *args, **kwargs):
        """ 
        Constructor for the test_review class.
        """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ 
        Test case for verifying the type of the 'place_id' attribute in a Review instance.
        """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """ 
        Test case for verifying the type of the 'user_id' attribute in a Review instance.
        """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """ 
        Test case for verifying the type of the 'text' attribute in a Review instance.
        """
        new = self.value()
        self.assertEqual(type(new.text), str)
