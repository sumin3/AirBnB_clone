#!/usr/bin/python3
"""Place class unitests"""
import unittest
from models.place import Place
from datetime import datetime
from models import storage


class TestPlace(unittest.TestCase):
    """ class Place parent class unit tests
    """

    def setUp(self):
        """ setup tests """
        self.model1 = Place()
        self.model1.city_id = "root"
        self.model1.user_id = "userid"
        self.model1.name = "Holberton"
        self.model1.description = "school"
        self.model1.number_rooms = 4
        self.model1.number_bathrooms = 4
        self.model1.max_guest = 4
        self.model1.price_by_night = 100
        self.model1.latitude = 1.1
        self.model1.longitude = 2.2
        self.model1.amenity_ids = [12]
        self.model1.save()

        self.model2 = Place()
        self.model2.city_id = "root"
        self.model2.user_id = "userid"
        self.model2.name = "Betty"
        self.model2.description = "school"
        self.model2.number_rooms = 2
        self.model2.number_bathrooms = 2
        self.model2.max_guest = 4
        self.model2.price_by_night = 50
        self.model2.latitude = 1.1
        self.model2.longitude = 2.2
        self.model2.amenity_ids = [10]
        self.model2.save()
        self.model2_dict = self.model2.to_dict()
        self.model3 = Place(**self.model2_dict)
        self.model3.save()

    def tearDown(self):
        """ teardown tests """
        all_objs = storage.all()
        all_objs.clear()
        storage.save()

    def test_attr(self):
        """test attr"""
        model = Place()
        self.assertNotIn('city_id', model.__dict__)
        self.assertNotIn('user_id', model.__dict__)
        self.assertNotIn('name', model.__dict__)
        self.assertNotIn('description', model.__dict__)
        self.assertNotIn('number_rooms', model.__dict__)
        self.assertNotIn('number_bathrooms', model.__dict__)
        self.assertNotIn('max_guest', model.__dict__)
        self.assertNotIn('price_by_night', model.__dict__)
        self.assertNotIn('latitude', model.__dict__)
        self.assertNotIn('longitude', model.__dict__)
        self.assertNotIn('amenity_ids', model.__dict__)

    def test_instance_class(self):
        """ test type of the created instance """
        self.assertIsInstance(self.model2, Place)

    def test_attr_existence(self):
        """ test if public attribute exist or not"""
        self.assertTrue(hasattr(self.model2, 'city_id'))
        self.assertTrue(hasattr(self.model2, 'user_id'))
        self.assertTrue(hasattr(self.model2, 'name'))
        self.assertTrue(hasattr(self.model2, 'description'))
        self.assertTrue(hasattr(self.model2, 'number_rooms'))
        self.assertTrue(hasattr(self.model2, 'number_bathrooms'))
        self.assertTrue(hasattr(self.model2, 'max_guest'))
        self.assertTrue(hasattr(self.model2, 'price_by_night'))
        self.assertTrue(hasattr(self.model2, 'latitude'))
        self.assertTrue(hasattr(self.model2, 'longitude'))
        self.assertTrue(hasattr(self.model2, 'amenity_ids'))
        self.assertFalse(hasattr(self.model2, 'invaid_attr'))

    def test_existing_atrr_datatype(self):
        """ test req attr data types """
        self.assertEqual(type(self.model2.city_id), str)
        self.assertEqual(type(self.model2.user_id), str)
        self.assertEqual(type(self.model2.name), str)
        self.assertEqual(type(self.model2.description), str)
        self.assertEqual(type(self.model2.number_rooms), int)
        self.assertEqual(type(self.model2.number_bathrooms), int)
        self.assertEqual(type(self.model2.max_guest), int)
        self.assertEqual(type(self.model2.price_by_night), int)
        self.assertEqual(type(self.model2.latitude), float)
        self.assertEqual(type(self.model2.longitude), float)
        self.assertEqual(type(self.model2.amenity_ids), list)

    def test_existing_atrr_value(self):
        """ test req attr data values """
        self.assertEqual(self.model2.city_id, 'root')
        self.assertEqual(self.model2.user_id, "userid")
        self.assertEqual(self.model2.name, "Betty")
        self.assertEqual(self.model2.description, "school")
        self.assertEqual(self.model2.number_rooms, 2)
        self.assertEqual(self.model2.number_bathrooms, 2)
        self.assertEqual(self.model2.max_guest, 4)
        self.assertEqual(self.model2.price_by_night, 50)
        self.assertEqual(self.model2.latitude, 1.1)
        self.assertEqual(self.model2.longitude, 2.2)
        self.assertEqual(self.model2.amenity_ids, [10])

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

    def test_new_attr_number_rooms(self):
        """model1.number_rooms is int type
        """
        self.assertEqual(type(self.model2.number_rooms), int)
        """model1.number_rooms is 4
        """
        self.assertEqual(self.model1.number_rooms, 4)
        """model2.number_rooms is int
        """
        self.assertEqual(type(self.model2.number_rooms), int)
        """model2.number_rooms is 2
        """
        self.assertEqual(self.model2.number_rooms, 2)

    def test_updated_at(self):
        """test datetime """
        self.assertGreater(self.model2.created_at, self.model1.created_at)
        self.assertGreater(self.model2.updated_at, self.model1.updated_at)

    def test_latitude(self):
        """test types of new attrs"""
        self.assertEqual(type(self.model1.latitude), float)
        self.assertEqual(self.model1.latitude, 1.1)

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
        """ model3 and model2 have the same number_rooms value """
        self.assertEqual(self.model2.number_rooms, self.model3.number_rooms)

    def test_city_id(self):
        """ test Place model city_id """
        self.assertEqual(self.model1.city_id, "root")

    def test_save(self):
        """ test save obj serialization """
        place = Place()
        place.save()
        with open("file.json", "r") as file:
            pre_objs = file.read()
        pre_objs_size = len(pre_objs)

        place = Place()
        place.save()
        place_key = "{}.{}".format(place.__class__.__name__, place.id)
        with open("file.json", "r") as file:
            post_objs = file.read()
        post_objs_size = len(post_objs)

        self.assertGreater(post_objs_size, pre_objs_size)
        self.assertIn(place_key, post_objs)

    def test_reload(self):
        """" ensure storage reload works """
        place = Place()
        place.save()
        place_key = "{}.{}".format(place.__class__.__name__, place.id)
        storage.all().clear()
        self.assertNotIn(place_key, storage.all())
        storage.reload()
        self.assertIn(place_key, storage.all())

    def test_init_kwargs(self):
        """" ensure that kwargs are in new instance"""
        kwarg_dict = {'int': 1, 'float': 2.2, 'str': "3"}
        place = Place(**kwarg_dict)
        self.assertEqual(place.int, 1)
        self.assertEqual(type(place.int), int)
        self.assertEqual(type(place.float), float)
        self.assertEqual(type(place.str), str)


if __name__ == '__main__':
    unittest.main()
