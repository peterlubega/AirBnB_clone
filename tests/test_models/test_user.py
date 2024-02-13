#!/usr/bin/python3
""" 
Script that contains unit tests for the User class, which inherits from test_basemodel.
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
        Test case for verifying the type of the 'first_name' attribute in a User instance.
        """
        new = self.value()
        self.assertEqual(type(new.first_name), str)
    
    def test_last_name(self):
        """ 
        Test case for verifying the type of the 'last_name' attribute in a User instance.
        """
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """ 
        Test case for verifying the type of the 'email' attribute in a User instance.
        """
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """ 
        Test case for verifying the type of the 'password' attribute in a User instance.
        """
        new = self.value()
        self.assertEqual(type(new.password), str)
