#!/usr/bin/python3
from models.base_model import BaseModel

""" user class module """


class User(BaseModel):
    """ class User that inherits from BaseModel
    Attributes:
        email: string - empty string
        password: string - empty string
        first_name: string - empty string
        last_name: string - empty string
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
