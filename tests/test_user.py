#!/usr/bin/python3


"""
Module for User unittest
"""


import uuid
import json
from models.base_model import BaseModel
from models.user import User
import unittest
from datetime import datetime
from models import storage
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    Test the mail class attr
    """
    def test_user_email(self):
        user = User()
        self.assertEqual(user.email, "")

    def test_user_email_1(self):
        user = User()
        user.email = "test@example.fr"
        self.assertEqual(user.email, "test@example.fr")

    def test_user_password(self):
        user = User()
        self.assertEqual(user.password, "")

    def test_user_password_1(self):
        user = User()
        user.password = "1234"
        self.assertEqual(user.password, "1234")

    def test_user_first_name(self):
        user = User()
        self.assertEqual(user.first_name, "")

    def test_user_first_name_1(self):
        user = User()
        user.first_name = "Pascal"
        self.assertEqual(user.first_name, "Pascal")

    def test_user_last_name(self):
        user = User()
        self.assertEqual(user.last_name, "")

    def test_user_last_name_1(self):
        user = User()
        user.last_name = "Titi"
        self.assertEqual(user.last_name, "Titi")


if __name__ == "__main__":
    unittest.main()
