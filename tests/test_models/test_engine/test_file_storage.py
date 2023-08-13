#!/usr/bin/python3
"""
tests for class Storage
"""
import unittest
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel
from models import storage
import os

class TestFileStorage(unittest.TestCase):
    """ unittest for FileStorage """
    def test_no_args(self):
        """ test no args """
        self.assertEqual(FileStorage, type(FileStorage()))

    def test_def_value(self):
        """ test values"""
        self.assertEqual(FileStorage._FileStorage__file_path, "file.json")
        self.assertEqual(type(FileStorage._FileStorage__objects), dict)
        self.assertEqual(type(FileStorage._FileStorage__file_path), str)

    def test_all(self):
        """ test all"""
        f_obj = FileStorage._FileStorage__objects
        self.assertEqual(storage.all(), f_obj)

    def test_new(self):
        """ test new"""
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, storage.all().keys())

    def setUp(self):
        """ set variable"""
        self.storage = FileStorage()

    def tearDown(self):
        """remove file"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_save(self):
        """test save"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        with open("file.json", "r") as f:
            data = f.read()
        self.assertIn(obj.__class__.__name__ + "." + obj.id, data)

    def test_reload(self):
        """ test reload"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, self.storage.all().keys())
