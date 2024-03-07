#!/usr/bin/python3


import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    def test_inheritance(self):
        """
        Test if Review class inherits from BaseModel
        """
        review = Review()
        self.assertIsInstance(review, BaseModel)


if __name__ == '__main__':
    unittest.main()
