#!/usr/bin/python3
""" FileStorage module """
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ FileStorage class
    Attributes:
        __objects: dictionary - empty but will store all
                   objects by <class name>.id.
        __file_path: string - path to the JSON file.
    """
    __objects = {}
    __file_path = "file.json"

    def all(self):
        """ all method: returns the dictionary __objects
        Return:
            return dictionary __objects
        """
        return self.__objects

    def new(self, obj):
        """ new method: sets in __objects the obj with
        key <obj class name>.id.
        Args:
            obj: the new object that want to create
        """
        self.__objects['{}.{}'.format(
            obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """ sace method: serializes __objects to the JSON
        file (path: __file_path)
        """
        try:
            with open(self.__file_path, mode="w", encoding="utf-8") as f:
                d = {k: v.to_dict() for k, v in self.__objects.items()}
                f.write(json.dumps(d))
        except FileNotFoundError:
            pass

    def reload(self):
        """ reload method: deserializes the JSON file to __objects
         (only if the JSON file (__file_path) exists ; otherwise,
        do nothing. If the file doesn’t exist, no exception should
        be raised)
        """
        cls_dict = {"BaseModel": BaseModel,
                    "User": User,
                    "State": State,
                    "City": City,
                    "Amenity": Amenity,
                    "Place": Place,
                    "Review": Review}
        try:
            with open(self.__file_path, mode="r", encoding="utf-8") as f:
                d = json.load(f)
                for k, v in d.items():
                    k_list = k.split('.')
                    self.__class__.__objects[k] = cls_dict.get(
                        k_list[0])(**v)
        except FileNotFoundError:
            pass
