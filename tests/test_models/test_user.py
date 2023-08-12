#!/usr/bin/python3
"""
This is a unittest for user.py
test for instantiation, save & to_dict
"""
import unittest
from models.user import User

class TestUser(unittest.TestCase):
    """ unittest for user """
    def test_no_args(self):
        """ test no args"""
        self.assertEqual(User, type(User()))
    def test_def_value(self):
        """ test values"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")
        self.assertEqual(user.password, "")
