#!/usr/bin/python3


import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    def test_inheritance(self):
        """
        Test if Place class inherits from BaseModel
        """
        place = Place()
        self.assertIsInstance(place, BaseModel)


if __name__ == '__main__':
    unittest.main()
