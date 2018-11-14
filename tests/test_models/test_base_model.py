#!/usr/bin/python3
"""BaseModel class unitests"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models import storage


class TestBaseModel(unittest.TestCase):
    """ class Base parent class unit tests
    """

    def setUp(self):
        """ setup tests """
        self.model1 = BaseModel()
        self.model1.name = "Holberton"
        self.model1.my_number = 89
        self.model1.float = 1.1

        self.model2 = BaseModel()
        self.model2.name = "Betty"
        self.model2.my_number = 98

        self.model2_dict = self.model2.to_dict()
        self.model3 = BaseModel(**self.model2_dict)

    def tearDown(self):
        """ teardown tests """
        all_objs = storage.all()
        all_objs.clear()
        storage.save()

    def test_init_kwargs(self):
        """" ensure storage reload works """
        d = {'a': 'v1', 'b': 1, 'c': 1.1}
        b = BaseModel(**d)
        self.assertTrue(hasattr(b, 'a'))
        self.assertTrue(hasattr(b, 'b'))
        self.assertTrue(hasattr(b, 'c'))
        self.assertEqual(type(b.a), str)
        self.assertEqual(type(b.b), int)
        self.assertEqual(type(b.c), float)
        self.assertEqual(b.a, 'v1')
        self.assertEqual(b.b, 1)
        self.assertEqual(b.c, 1.1)

    def test_instance_class(self):
        """ test type of the created instance """
        self.assertIsInstance(self.model1, BaseModel)

    def test_attr_existence(self):
        """ test if public attribute exist or not"""
        self.assertTrue(hasattr(self.model1, 'id'))
        self.assertTrue(hasattr(self.model1, 'updated_at'))
        self.assertTrue(hasattr(self.model1, 'created_at'))
        self.assertFalse(hasattr(self.model1, 'invaid_attr'))

    def test_existing_atrr_datatype(self):
        """ test if public attribute data types """
        self.assertEqual(type(self.model1.created_at), datetime)
        self.assertEqual(type(self.model1.updated_at), datetime)
        self.assertEqual(type(self.model1.id), str)

    def test_id(self):
        """model1.id and model2.id are different
        """
        self.assertNotEqual(self.model1.id, self.model2.id)

    def test_new_attr_name(self):
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

    def test_new_attr_my_number(self):
        """model1.my_number is int type
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

    def test_updated_at(self):
        """test datetime """
        self.assertGreater(self.model2.created_at, self.model1.created_at)
        self.assertGreater(self.model2.updated_at, self.model1.updated_at)

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
        self.assertEqual(type(created_at), str)
        created_at = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(type(created_at), datetime)

        updated_at = self.model2_dict['updated_at']
        self.assertEqual(type(updated_at), str)
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

    def test_save(self):
        """ test save obj serialization """
        base = BaseModel()
        base.save()
        with open("file.json", "r") as file:
            pre_objs = file.read()
        pre_objs_size = len(pre_objs)

        base2 = BaseModel()
        base2.save()
        base2_key = "{}.{}".format(base2.__class__.__name__, base2.id)
        with open("file.json", "r") as file:
            post_objs = file.read()
        post_objs_size = len(post_objs)

        self.assertGreater(post_objs_size, pre_objs_size)
        self.assertIn(base2_key, post_objs)

    def test_reload(self):
        """" ensure storage reload works """
        base = BaseModel()
        base.save()
        base_key = "{}.{}".format(base.__class__.__name__, base.id)
        storage.all().clear()
        self.assertNotIn(base_key, storage.all())
        storage.reload()
        self.assertIn(base_key, storage.all())


if __name__ == '__main__':
    unittest.main()
