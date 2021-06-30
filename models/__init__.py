#!/usr/bin/python3
"""
Init
to create a unique FileStorage instance for our AirBnB
clone
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
