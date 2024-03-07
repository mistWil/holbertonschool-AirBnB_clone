#!/usr/bin/python3


import unittest
from models.city import City


class TestCity(unittest.TestCase):
    def test_inheritance(self):
        """
        Test if City class inherits from BaseModel
        """
        city = City()
        self.assertIsInstance(city, BaseModel)


if __name__ == '__main__':
    unittest.main()
