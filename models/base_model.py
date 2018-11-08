#!/usr/bin/
import uuid
import datetime


class BaseModel:
    def __init__(self):
        """Initer"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.save()

    # @property
    # def id(self):
    #     return self.__id

    # @property
    # def created_at(self):
    #     return self.__created_at

    # @property
    # def updated_at(self):
    #     return self.__updated_at

    def save(self):
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """Returns a string descriptor of the rectangle"""
        return ("[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        ))

    def to_dict(self):
        """returns a dictionary containing all keys/values of instance"""
        retval = self.__dict__
        retval["__class__"] = self.__class__.__name__
        retval["created_at"] = self.created_at.isoformat()
        retval["updated_at"] = self.updated_at.isoformat()
        return (retval)
