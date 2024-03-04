#!/usr/bin/python3


import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.model = BaseModel()

    def test_id(self):
        self.assertIsInstance(self.model.id, str)
        
    def test_init_no_kwargs(self):
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)
        self.assertEqual(self.model.created_at, self.model.updated_at)

    def test_init_with_kwargs(self):
        kwargs = {
            'id': '1234',
            'created_at': '2022-01-01T00:00:00.000000',
            'updated_at': '2022-01-01T00:00:00.000000'
        }
        model = BaseModel(**kwargs)
        self.assertEqual(model.id, '1234')
        self.assertEqual(model.created_at,
                         datetime.strptime(kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f"))
        self.assertEqual(model.updated_at,
                         datetime.strptime(kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f"))
        
    def test_created_at(self):
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at(self):
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str(self):
        expected_str = "[BaseModel] ({}) {}".format(self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), expected_str)

    def test_save(self):
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)

    def test_to_dict(self):
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(model_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], self.model.updated_at.isoformat())

if __name__ == '__main__':
    unittest.main()
