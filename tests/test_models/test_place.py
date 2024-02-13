#!/usr/bin/python3
"""
Unit tests script  for Place class, inheriting from test_basemodel.
"""

from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """
    Testing functionality of Place class, inheriting test_basemodel.
    """

    def __init__(self, *args, **kwargs):
        """
        Constructor for the test_Place class.
        """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """
        Verifying type of 'city_id' attribute in Place instance.
        """
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """
        Verifying type of 'user_id' attribute in Place instance.
        """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """
        Verifying type of 'name' attribute in a Place instance.
        """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """
        Verifying type of 'description' attribute in a Place instance.
        """
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """
        Verifying type of 'number_rooms' attribute in a Place instance.
        """
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """
        Verifying type of 'number_bathrooms' attribute in Place instance.
        """
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """
        Verifying type of 'max_guest' attribute in Place instance.
        """
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """
        Verifying type of 'price_by_night' attribute in Place instance.
        """
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """
        Verifying type of 'latitude' attribute in a Place instance.
        """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """
        Verifying type of 'longitude' attribute in a Place instance.
        """
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """
        Verifying type of 'amenity_ids' attribute in a Place instance.
        """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
