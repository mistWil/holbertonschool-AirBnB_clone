#!/usr/bin/python3


"""
Write a class BaseModel that defines all common attributes/methods
for other classes:

models/base_model.py
Public instance attributes:
id: string - assign with an uuid when an instance is created:
you can use uuid.uuid4() to generate unique id but don’t forget
to convert to a string
the goal is to have unique id for each BaseModel
created_at: datetime - assign with the current datetime
when an instance is created
updated_at: datetime - assign with the current datetime when
an instance is created and it will be updated every time you change your object
__str__: should print: [<class name>] (<self.id>) <self.__dict__>
Public instance methods:
save(self): updates the public instance attribute updated_at with
the current datetime
to_dict(self): returns a dictionary containing all keys/values of
__dict__ of the instance:
by using self.__dict__, only instance attributes set will be returned
a key __class__ must be added to this dictionary with the class name
of the object
created_at and updated_at must be converted to string object in ISO format:
format: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
you can use isoformat() of datetime object
This method will be the first piece of the serialization/deserialization
process: create a dictionary representation with “simple object type” of our
BaseModel
"""


import uuid
from datetime import datetime


class BaseModel:
    """
    Cette classe représente un modèle de base pour d'autres classes.
    Elle fournit des attributs et des méthodes communs.
    """

    def __init__(self):
        """
        Initialise une nouvelle instance de BaseModel.

        Attributs:
            id (str): Identifiant unique de l'instance.
            created_at (datetime): Date et heure de création de l'instance.
            updated_at (datetime): Date et heure de dernière mise à
            jour de l'instance.
        """
        self.id = str(uuid.uuid4())  # Attribution d'un id unique à
        # chaque instance
        self.created_at = datetime.now()  # Attribution de la date et
        # l'heure de création
        self.updated_at = datetime.now()  # Attribution de la date et
        # l'heure de mise à jour

    def __str__(self):
        """
        Renvoie une représentation sous forme de chaîne de
        caractères de l'instance.

        Returns:
            str: Représentation de l'instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Met à jour l'attribut 'updated_at' avec la date et l'heure actuelles.
        """
        self.updated_at = datetime.now()  # Mise à jour de la date
        # et l'heure de mise à jour

    def to_dict(self):
        """
        Convertit l'instance en un dictionnaire contenant tous ses attributs.

        Returns:
            dict: Dictionnaire contenant les attributs de l'instance.
        """
        obj_dict = self.__dict__.copy()  # Copie du dictionnaire des attributs
        obj_dict['__class__'] = self.__class__.__name__  # Ajout de la
        # clé '__class__'
        obj_dict['created_at'] = self.created_at.isoformat()  # Conversion de
        # la date de création en ISO format
        obj_dict['updated_at'] = self.updated_at.isoformat()  # Conversion de
        # la date de mise à jour en ISO format
        return obj_dict
