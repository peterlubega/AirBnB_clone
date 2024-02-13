#!/usr/bin/python3
"""
Unit tests script for Review class, inheriting from test_basemodel.
"""

from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """
    TestCase class for testing functionality of Review class.
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
        Verifying type of 'place_id' attribute in Review instance.
        """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """
        Verifying type of 'user_id' attribute in  Review instance.
        """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """
        Verifying the type of the 'text' attribute in a Review instance.
        """
        new = self.value()
        self.assertEqual(type(new.text), str)
