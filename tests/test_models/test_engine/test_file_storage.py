#!/usr/bin/python3
"""FileStorage class unitests"""
import unittest
from models import storage
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from datetime import datetime


class TestFileStorage(unittest.TestCase):
    """ class FileStorage class unit tests
    """

    def setUp(self):
        """set up """
        self.storage = FileStorage()

    def tearDown(self):
        """ teardown tests """
        all_objs = storage.all()
        all_objs.clear()
        storage.save()

    def test_storage_objects_dict_datatype(self):
        """ storage.__objects is a dict """
        self.assertIsInstance(self.storage.all(), dict)

    def test_storage_objects(self):
        """ test size of objects after creates a new instance
        """
        pre_objs_size = len(self.storage.all())
        base = BaseModel()
        base.name = "Holberton"
        post_objs_size = len(self.storage.all())
        self.assertGreater(post_objs_size, pre_objs_size)
        self.assertEqual(post_objs_size, pre_objs_size + 1)

    def test_new(self):
        """ test new method - check create a new instance """
        base = BaseModel()
        base_key = "{}.{}".format(base.__class__.__name__, base.id)
        all_objs = self.storage.all()
        self.assertIn(base_key, all_objs)

        city = City()
        city_key = "{}.{}".format(city.__class__.__name__, city.id)
        all_objs = self.storage.all()
        self.assertIn(city_key, all_objs)

    def test_unsave(self):
        """ test not save obj serialization """
        city_unsave = City()
        unsave_key = "{}.{}".format(
            city_unsave.__class__.__name__, city_unsave.id)
        with open("file.json", "r") as file:
            unsave_objs = file.read()
        self.assertNotIn(unsave_key, unsave_objs)

    def test_save(self):
        """ test save obj serialization """
        city = City()
        storage.save()
        with open("file.json", "r") as file:
            pre_objs = file.read()
        pre_objs_size = len(pre_objs)

        base = BaseModel()
        storage.save()
        base_key = "{}.{}".format(base.__class__.__name__, base.id)
        with open("file.json", "r") as file:
            post_objs = file.read()
        post_objs_size = len(post_objs)

        self.assertGreater(post_objs_size, pre_objs_size)
        self.assertIn(base_key, post_objs)

    def test_reload(self):
        base = BaseModel()
        storage.save()
        base_key = "{}.{}".format(base.__class__.__name__, base.id)
        storage.all().clear()
        self.assertNotIn(base_key, storage.all())
        storage.reload()
        self.assertIn(base_key, storage.all())

if __name__ == '__main__':
    unittest.main()
