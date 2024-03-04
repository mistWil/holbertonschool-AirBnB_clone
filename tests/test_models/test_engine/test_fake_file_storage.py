#!/usr/bin/python3


import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        pass
        # all_objs = self.storage.all()
        # self.assertEqual(all_objs, {})

    def test_new(self):
        pass
        # obj = BaseModel()
        # self.storage.new(obj)
        # all_objs = self.storage.all()
        # self.assertEqual(len(all_objs), 1)

    def test_save_and_reload(self):
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        all_objs = new_storage.all()
        self.assertEqual(len(all_objs), 1)


if __name__ == '__main__':
    unittest.main()
