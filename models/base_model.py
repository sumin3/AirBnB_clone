#!/usr/bin/python3
""" Base module """
import uuid
from datetime import datetime
import models


class BaseModel:
    """ class Base parent class
    Attributes:
        id: string - uuid for the model
        created_at: datetime obj - date and time instance was created
        updated_at: datetime obj - date and time instance was updated
    """

    def __init__(self, *args, **kwargs):
        """Initer"""
        if kwargs:
            for k, v in kwargs.items():
                if k in ["created_at", "updated_at"]:
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                if k != '__class__':
                    self.__setattr__(k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """Updates updated_at when saved"""
        self.updated_at = datetime.now()
        models.storage.save()

    def __str__(self):
        """Returns a string descriptor of the rectangle"""
        return ("[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__
        ))

    def to_dict(self):
        """returns a dictionary containing all keys/values of instance"""
        retval = self.__dict__.copy()
        retval["__class__"] = self.__class__.__name__
        retval["created_at"] = self.created_at.isoformat()
        retval["updated_at"] = self.updated_at.isoformat()
        return (retval)
