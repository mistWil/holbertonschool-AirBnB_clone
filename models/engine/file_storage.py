#!/usr/bin/python3
"""
New class to serialize instances to a JSON
"""
import json


class FileStorage:
    """
    File storage class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionnary __objects
        """
        return self.__objects

    def new(self, obj):
        """
        Sets in __object the obj with a special key
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the Json file
        """
        obj_dict = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserializes Json file to __objects
        """
        try:
            with open(self.__file_path, 'r') as file:
                obj_dict = json.load(file)
                from models.base_model import BaseModel
                from models.user import User
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    if class_name == 'BaseModel':
                        obj = BaseModel(**value)
                    elif class_name == 'User':
                        obj = User(**value)
                    else:
                        continue
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass