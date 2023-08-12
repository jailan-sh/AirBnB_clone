#!/usr/bin/python3
"""
This is a unittest for amenity.py
test for instantiation, save & to_dict
"""
import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """ unittest for amenity """
    def test_no_args(self):
        self.assertEqual(Amenity, type(Amenity()))
    def test_def_value(self):
        """ test values"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")
