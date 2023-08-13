#!/usr/bin/python3
"""
This is a unittest for base_model.py
test for instantiation, save & to_dict
"""
from models.base_model import BaseModel
import unittest
from datetime import datetime
import models
from time import sleep


class TestBaseModel(unittest.TestCase):
    """ unittest for BaseModel """

    def test_no_args(self):
        """ test no args"""
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_args_unused(self):
        """ test args """
        bm = BaseModel(None)
        self.assertNotIn(None, bm.__dict__.values())

    def test_kwargs_unused(self):
        """ test kwargs """
        dt = datetime.fromisoformat(datetime.now().isoformat())
        bm_7 = BaseModel(id = "1234", created_at = str(dt), updated_at = str(dt))
        self.assertEqual(bm_7.id , "1234")
        self.assertEqual(bm_7.created_at, dt)
        self.assertEqual(bm_7.updated_at, dt)

    def test_def_value(self):
        """ test values"""
        self.assertEqual(str, type(BaseModel().id))
        self.assertEqual(datetime, type(BaseModel().created_at))
        self.assertEqual(datetime, type(BaseModel().updated_at))
        self.assertIn(BaseModel(), models.storage.all().values())

    def test_init(self):
        """ test init"""
        bm = BaseModel()
        self.assertIsNotNone(bm.id)
        self.assertIsNotNone(bm.created_at)
        self.assertIsNotNone(bm.updated_at)

    def test_different_values(self):
        """ test different values for different objects"""
        bm_1 = BaseModel()
        sleep(0.02)
        bm_2 = BaseModel()
        self.assertNotEqual(bm_1.id, bm_2.id)
        self.assertNotEqual(bm_1.created_at, bm_2.created_at)
        self.assertNotEqual(bm_1.updated_at, bm_2.updated_at)

    def test_str(self):
        """ test str method """
        bm_3 = BaseModel()
        str_rep = "[BaseModel] ({}) {}".format(bm_3.id, bm_3.__dict__)
        self.assertEqual(str(bm_3), str_rep)

    def test_save(self):
        """ test save"""
        bm_4 = BaseModel()
        bm_4.save()
        self.assertIsNotNone(bm_4.updated_at)

    def test_to_dict(self):
        """ test to_dict """
        bm_5 = BaseModel()
        bm_5_dict = bm_5.to_dict()
        self.assertIsInstance(bm_5_dict, dict)
        self.assertIn("__class__", bm_5_dict)
        self.assertIn("created_at", bm_5_dict)
        self.assertIn("updated_at", bm_5_dict)


if __name__ == '__main__':
    unittest.main()
