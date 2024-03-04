#!/usr/bin/python3


import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def test_all(self):
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.assertEqual(len(self.storage.all()), 1)

    def test_save_and_reload(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage = FileStorage()
        self.storage.reload()
        self.assertEqual(len(self.storage.all()), 1)
        loaded_obj = list(self.storage.all().values())[0]
        self.assertIsInstance(loaded_obj, BaseModel)

if __name__ == '__main__':
    unittest.main()
