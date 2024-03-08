#!/usr/bin/python3


import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_attributes(self):
        """
        Test if Amenity class attributes are correctly set
        """
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertEqual(amenity.name, "")


if __name__ == '__main__':
    unittest.main()
