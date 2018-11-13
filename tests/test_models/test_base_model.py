#!/usr/bin/python3
"""BaseModel class unitests"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ class Base parent class unit tests
    """

    def setUp(self):
        self.model1 = BaseModel()
        self.model1.name = "Holberton"
        self.model1.my_number = 89
        self.model2 = BaseModel()
        self.model2.name = "Betty"
        self.model2.my_number = 98
        self.model1.float = 1.1
        self.model2_dict = self.model2.to_dict()
        self.model3 = BaseModel(**self.model2_dict)

    def test_id(self):
        """id is string
        """
        self.assertEqual(type(self.model1.id), str)
        """model1.id and model2.id are different
        """
        self.assertNotEqual(self.model1.id, self.model2.id)
        """model1.created_at is type datetime
        """
    def test_created_at(self):
        """model1.created_at is datetime
        """
        self.assertEqual(type(self.model1.created_at), datetime)

    def test_name(self):
        """model1.name is string
        """
        self.assertEqual(type(self.model1.name), str)
        """model1.name is "Holberton"
        """
        self.assertEqual(self.model1.name, "Holberton")

        """model2.name is string
        """
        self.assertEqual(type(self.model2.name), str)

        """model2.name is "Betty"
        """
        self.assertEqual(self.model2.name, "Betty")
        """model1.my_number is int
        """
    def test_number(self):
        self.assertEqual(type(self.model2.my_number), int)
        """model1.my_number is 89
        """
        self.assertEqual(self.model1.my_number, 89)
        """model2.my_number is int
        """
        self.assertEqual(type(self.model2.my_number), int)
        """model2.my_number is 98
        """
        self.assertEqual(self.model2.my_number, 98)
        """model1.created_at < model1.updated_at
        """
    def test_updated_at(self):
        self.assertGreater(self.model1.updated_at, self.model1.created_at)
        self.assertGreater(self.model2.updated_at, self.model2.created_at)
        """self.model1.created_at < self.model2.created_at
        """
        self.assertGreater(self.model2.created_at, self.model1.created_at)
        self.assertGreater(self.model2.updated_at, self.model1.updated_at)

        """"Test in file.json:
        """
        """model1.created_at : type string
        """
        """model1.updated_at: type string"
        """
    def test_new_types(self):
        """test types of new attrs"""
        self.assertEqual(type(self.model1.float), float)
        self.assertEqual(self.model1.float, 1.1)

    def test_str(self):
        """test string method"""
        self.assertEqual(str(self.model1), "[{}] ({}) {}".format(
            self.model1.__class__.__name__,
            self.model1.id,
            self.model1.__dict__
        ))

    def test_to_dict(self):
        """ tests to_dict method """
        self.assertEqual(type(self.model2_dict), dict)
        """ tests to_dict for iso timeformat """
        created_at = self.model2_dict['created_at']
        created_at = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(type(created_at), datetime)
        updated_at = self.model2_dict['updated_at']
        updated_at = datetime.strptime(updated_at, "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(type(updated_at), datetime)

    def test_dict_equals(self):
        """ tests to_dict method """
        self.assertTrue(self.model2_dict == self.model2.to_dict())

    def test_new_model_memory(self):
        """ model3 and model3 are two different objects """
        self.assertIsNot(self.model2, self.model3)

    def test_new_model_id(self):
        """ model3 and model2 have the same id """
        self.assertEqual(self.model2.id, self.model3.id)

    def test_new_model_created_at(self):
        """ model3 and model2 have the same created_at value """
        self.assertEqual(self.model2.created_at, self.model3.created_at)

    def test_new_model_name(self):
        """ model3 and model2 have the same name value """
        self.assertEqual(self.model2.name, self.model3.name)

    def test_new_model_number(self):
        """ model3 and model2 have the same my_number value """
        self.assertEqual(self.model2.my_number, self.model3.my_number)
