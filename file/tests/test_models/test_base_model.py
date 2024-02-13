#!/usr/bin/python3
""" 
This is a Python script that contains unit tests for the BaseModel class.
"""

from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os

class test_basemodel(unittest.TestCase):
    """ 
    This is a TestCase class for testing the functionality of the BaseModel class.
    """
    
    def __init__(self, *args, **kwargs):
        """ 
        Constructor for the test_basemodel class.
        """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ 
        Set up method to initialize any necessary resources before each test.
        """
        pass

    def tearDown(self):
        """
        Tear down method to clean up any resources after each test.
        """
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """ 
        Test case for creating a BaseModel instance with default values.
        """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ 
        Test case for creating a BaseModel instance with provided keyword arguments.
        """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ 
        Test case for creating a BaseModel instance with invalid keyword arguments.
        """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ 
        Test case for saving a BaseModel instance and checking the correctness of the saved data.
        """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ 
        Test case for the string representation of a BaseModel instance.
        """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id, i.__dict__))

    def test_todict(self):
        """ 
        Test case for converting a BaseModel instance to a dictionary.
        """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ 
        Test case for creating a BaseModel instance with None as a keyword argument.
        """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)
 
    def test_kwargs_one(self):
        """ 
        Test case for creating a BaseModel instance with a missing required keyword argument.
        """
        n = {'Name': 'test'}
        with self.assertRaises(KeyError):
            new = self.value(**n)

    def test_id(self):
        """ 
        Test case for verifying the type of the 'id' attribute in a BaseModel instance.
        """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ 
        Test case for verifying the type of the 'created_at' attribute in a BaseModel instance.
        """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)
    
    def test_updated_at(self):
        """ 
        Test case for verifying the type of the 'updated_at' attribute in a BaseModel instance 
        and checking that it is different from 'created_at' after creating an instance from a dictionary.
        """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
