#!/usr/bin/python3
"""BaseModel class unitests"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):

    def setUp(self):
        self.model1 = BaseModel()
        self.model1.name = "Holberton"
        self.model1.my_number = 89
        self.model2 = BaseModel()
        self.model2.name = "Betty"
        self.model2.my_number = 98
        self.model1.list = []
        self.model1.dict = {'1': 1}
        self.model1.set = {1, 2, 3}
        self.model1.truth = True
        self.model1.none = None
        self.model1.float = 1.1
        self.model1.nan = float('nan')
        self.model1.inf = float('inf')
        self.model1.tuple = (1, 2, 3)

    def test_id(self):
        """id is string
        """
        self.assertEqual(type(self.model1.id), str)
        """model1.id and model2.id are different
        """
        self.assertNotEqual(self.model1.id, self.model2.id)
        """model1.created_at is type datetime
        """
        self.assertEqual(type(self.model1.created_at), datetime)
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
        self.assertGreater(self.model1.updated_at, self.model1.created_at)
        self.assertGreater(self.model2.updated_at, self.model2.created_at)
        """self.model1.created_at < self.model2.created_at
        """
        self.assertGreater(self.model2.created_at, self.model1.created_at)
        self.assertGreater(self.model2.updated_at, self.model1.updated_at)
        """test types of new attrs"""
        self.assertEqual(type(self.model1.id), str)

        """"Test in file.json:
        """
        """model1.created_at : type string
        """
        """model1.updated_at: type string"
        """


        self.assertEqual(type(self.model1.list), list)
        self.assertEqual(type(self.model1.dict), dict)
        self.assertEqual(type(self.model1.set), set)
        self.assertEqual(type(self.model1.truth), bool)
        self.assertEqual(type(self.model1.none), None)
        self.assertEqual(type(self.model1.float), float)
        self.assertEqual(type(self.model1.tuple), tuple)
        
        self.assertEqual(self.model1.nan), nan)
        self.assertEqual(self.model1.inf), inf)