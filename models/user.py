#!/usr/bin/python3
"""
user module
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    class User
    inhereted from BaseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
