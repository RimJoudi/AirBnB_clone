#!/usr/bin/python3
"""
Init
to create a unique FileStorage instance for our AirBnB
clone app
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()













"""
Update models/__init__.py: to create a unique FileStorage instance for your application

    import file_storage.py
    create the variable storage, an instance of FileStorage
    call reload() method on this variable
"""

