#!/usr/bin/python3
"""
Unit test script for User class, inheriting from test_basemodel.
"""

from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """
    TestCase class for testing the functionality of the User class.
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor for the test_User class.
        """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """
        Verifying the type 'first_name' attribute in User instance.
        """
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """
        Verifying the type of 'last_name' attribute in a User instance.
        """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """
        Verifying the type of the 'email' attribute in a User instance.
        """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """
        Verifying the type of the 'password' attribute in a User instance.
        """
        new = self.value()
        self.assertEqual(type(new.password), str)
