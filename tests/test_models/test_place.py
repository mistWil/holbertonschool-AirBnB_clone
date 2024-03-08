#!/usr/bin/python3


import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    def test_inheritance(self):
        """
        Test if Place class inherits from BaseModel
        """
        place = Place()
        self.assertIsInstance(place, BaseModel)


if __name__ == '__main__':
    unittest.main()
