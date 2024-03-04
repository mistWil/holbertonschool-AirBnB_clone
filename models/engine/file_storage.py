#!/usr/bin/python3


"""
Write a class FileStorage that serializes instances to a JSON
file and deserializes JSON file to instances:

models/engine/file_storage.py
Private class attributes:
__file_path: string - path to the JSON file (ex: file.json)
__objects: dictionary - empty but will store all objects by
<class name>.id (ex: to store a BaseModel object with id=12121212,
the key will be BaseModel.12121212)
Public instance methods:
all(self): returns the dictionary __objects
new(self, obj): sets in __objects the obj with key <obj class name>.id
save(self): serializes __objects to the JSON file (path: __file_path)
reload(self): deserializes the JSON file to __objects (only if the
JSON file (__file_path) exists ; otherwise, do nothing. If
the file doesn’t exist, no exception should be raised)
Update models/__init__.py: to create a unique FileStorage
instance for your application

import file_storage.py
create the variable storage, an instance of FileStorage
call reload() method on this variable
Update models/base_model.py: to link your BaseModel to
FileStorage by using the variable storage

import the variable storage
in the method save(self):
call save(self) method of storage
__init__(self, *args, **kwargs):
if it’s a new instance (not from a dictionary representation),
add a call to the method new(self) on storage
"""


import json



class FileStorage:
    """Handles serialization and deserialization of objects
    to/from JSON file."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary of all objects.

        Returns:
            dict: Dictionary containing all objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Sets a new object in the __objects dictionary.

        Args:
            obj: Object to be stored.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects dictionary to JSON file."""
        serialized_objects = {}
        for key, value in self.__objects.items():
            serialized_objects[key] = value.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    from models.base_model import BaseModel
                    self.__objects[key] = BaseModel(**value)
        except FileNotFoundError:
            pass
