import json


class FileStorage:

    def __init__(self, *args, **kwargs):
        # import pdb; pdb.set_trace()
        self.file_path = kwargs['__file_path']
        self.__objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.objects

    @property
    def file_path(self):
        return self.__file_path

    @file_path.setter
    def file_path(self, value):
        self.__file_path = value
        # try:
        #     with open(value, mode="r", encoding="utf-8"):
        # except FileNotFoundError:
        #     pass

    @property
    def objects(self):
        return self.__objects

    # @objects.setter
    # def objects(self, value):
    #     self.__objects = 

    def new(self, obj):
        """ sets in __objects the obj with key <obj class name>.id"""
        self.objects[
            '{}.{}'.format(obj.__class__, obj.id)
        ] = obj

    def save(self):
        """ serializes __objects to the JSON file (path: __file_path)"""
        try:
            with open(self.file_path, mode="w+", encoding="utf-8") as f:
                json.dump(self.objects, f)
        except FileNotFoundError:
            pass

    def reload(self):
        """ deserializes the JSON file to __objects
         (only if the JSON file (__file_path) exists ; otherwise, do nothing.
         If the file doesn’t exist, no exception should be raised) """
        try:
            with open(self.file_path, mode="r", encoding="utf-8") as f:
                for obj in json.load(f):
                    self.new(obj)
        except FileNotFoundError:
            pass
