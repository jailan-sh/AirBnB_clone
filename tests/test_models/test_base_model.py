#!/usr/bin/python3
"""
This is a unittest for base_model.py
test for instantiation, save & to_dict
"""
from models.base_model import BaseModel
import unittest

class TestBaseModel(unittest.TestCase):
    """ unittest for BaseModel """

    def test_no_args(self):
        self.assertEqual(BaseModel, type(BaseModel()))
if __name__ == '__main__':
    unittest.main()
