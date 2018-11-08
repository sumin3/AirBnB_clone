#!/usr/bin/
import uuid
import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        """Initer"""
        if len(kwargs):
            for k, v in kwargs.items():
                if k is not "__class__":
                    setattr(self, k, v)

            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())

            if 'created_at' in kwargs:
                self.created_at = datetime.datetime.strptime(
                    kwargs['created_at'],
                    "%Y-%m-%dT%H:%M:%S.%f"
                )
            else:
                self.created_at = datetime.datetime.now()
            self.save()

        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.save()

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
