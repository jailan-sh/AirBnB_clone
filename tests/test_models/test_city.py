#!/usr/bin/python3
"""
This is a unittest for city.py
test for instantiation, save & to_dict
"""
import unittest
from models.city import City

class TestCity(unittest.TestCase):
    """ unittest for city """
    def test_no_args(self):
        self.assertEqual(City, type(City()))
    def test_def_value(self):
        """ test values"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")
