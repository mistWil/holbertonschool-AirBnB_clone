#!/usr/bin/python3


import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    def test_inheritance(self):
        """
        Test if State class inherits from BaseModel
        """
        state = State()
        self.assertIsInstance(state, BaseModel)


if __name__ == '__main__':
    unittest.main()
