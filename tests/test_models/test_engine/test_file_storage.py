#!/usr/bin/python3
"""
Module for BaseModel unittest
"""
import uuid
import json
from models.base_model import BaseModel
import unittest
from datetime import datetime
from models import storage
from models.engine.file_storage import FileStorage

class TestFileStorage(unittest.TestCase):
    def test_path(self):
        file_storage = FileStorage()
        expected_file_storage = 'file.json'
        self.assertEqual(file_storage._FileStorage__file_path, expected_file_storage)
    
    def test_object(self):
        file_object = FileStorage()
        self.assertIsInstance(file_object._FileStorage__objects, dict)
    
    def test_all(self):
        file_storage = FileStorage()
        all_objects = file_storage.all()
        self.assertIsInstance(all_objects, dict)
        self.assertIs(all_objects, file_storage._FileStorage__objects)

    def test_new(self):
        file_storage = FileStorage()
        base_model = BaseModel()
        file_storage.new(base_model)
        obj_key = "BaseModel." + base_model.id
        self.assertIn(obj_key, file_storage._FileStorage__objects)

    def test_save(self):
        file_storage = FileStorage()
        new_model = BaseModel()
        file_storage.new(new_model)
        file_storage.save()
        with open('file.json', 'r') as file:
            recup_file = json.load(file)
        self.assertIn("BaseModel." + new_model.id, recup_file)
        
            
    def test_reload(self):
        file_storage = FileStorage()
        file_storage1 = FileStorage()
        base_model = BaseModel()
        file_storage1.new(base_model)
        file_storage1.save()

        file_storage2 = FileStorage()
        file_storage2.reload()
        obj_key = "BaseModel." + base_model.id
        self.assertIn(obj_key, file_storage2._FileStorage__objects)
        with self.assertRaises(FileNotFoundError):
            file_storage.reload()

if __name__ == "__main__":
    unittest.main()