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

class TestFileStorage(unittest.TestCase):
    """ unittest for FileStorage """
    def test_no_args(self):
        """ test no args """
        self.assertEqual(FileStorage, type(FileStorage()))

    def test_def_value(self):
        """ test values"""
        self.assertEqual(FileStorage._FileStorage__file_path, "file.json")
        self.assertEqual(type(FileStorage._FileStorage__objects), dict)

    def test_all(self):
        """ test all"""
        f_obj = FileStorage._FileStorage__objects
        self.assertEqual(storage.all(), f_obj)
