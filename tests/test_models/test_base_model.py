#!/usr/bin/python3
"""
This is a unittest for base_model.py
test for instantiation, save & to_dict
"""
from models.base_model import BaseModel
import unittest
from datetime import datetime
import models

class TestBaseModel(unittest.TestCase):
    """ unittest for BaseModel """

    def test_no_args(self):
        self.assertEqual(BaseModel, type(BaseModel()))
    def test_def_value(self):
        """ test values"""
        self.assertEqual(str, type(BaseModel().id))
        self.assertEqual(datetime, type(BaseModel().created_at))
        self.assertEqual(datetime, type(BaseModel().updated_at))
        self.assertIn(BaseModel(), models.storage.all().values())
if __name__ == '__main__':
    unittest.main()
