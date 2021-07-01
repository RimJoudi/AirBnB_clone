#!/usr/bin/python3

import unittest
import models
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.review import Review
from models.place import Place


class stateTest(unittest.TestCase):
    '''
    Test cases for BaseModel class
    '''
    def setUp(self):
        """
        simple set up
        """
        self.new_inst = State()

    def tearDown(self):
        """
        tear down method
        """
        del self.new_inst

    def test_is_basemodel_inst(self):
        """
        tests if new_inst is an instance of BaseModel
        """
        self.assertIsInstance(self.new_inst, BaseModel)

    def test_if_name_exists(self):
        """
        checks if new_inst has attr 'name'
        """
        self.assertTrue(hasattr(self.new_inst, 'name'))

    def test_to_dict_on_State(self):
        """
        checks to_dict method
        """
        new_dict = self.new_inst.to_dict()
        self.assertEqual(new_dict['__class__'], 'State')
        self.assertEqual(str(type(new_dict['created_at'])), "<class 'str'>")
        self.assertEqual(str(type(new_dict['updated_at'])), "<class 'str'>")


if __name__ == "__main__":
    unittest.main()
