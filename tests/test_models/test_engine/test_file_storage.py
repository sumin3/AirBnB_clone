#!/usr/bin/python3
"""FileStorage class unitests"""
import unittest
from models import storage
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestFileStorage(unittest.TestCase):
    """ class Base parent class unit tests
    """

    def setUp(self):
        self.storage = FileStorage()

    def test_storage_objects(self):
        """ storage.__objects is a dict """
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """ test new obj serializtion """
        base = BaseModel()
        base_key = "{}.{}".format(base.__class__.__name__, base.id)
        all_objs = self.storage.all()
        self.assertIn(base_key, all_objs)
        city = City()
        city_key = "{}.{}".format(city.__class__.__name__, city.id)
        all_objs = self.storage.all()
        self.assertIn(city_key, all_objs)

    def test_save(self):
        """ test save obj serializtion """
        pre_objs = self.storage.all()
        base = BaseModel()
        base.name = "Holberton"
        post_objs = self.storage.all()
        self.assertFalse(pre_objs == post_objs)
