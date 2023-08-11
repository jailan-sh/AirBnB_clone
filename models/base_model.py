#!/usr/bin/python3
""" parent class basemodel"""

from datetime import datetime
from models import storage
from uuid import uuid4


class BaseModel:
    """
    parent class which defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        constructor of instance attributes
        """
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """ method that return string represents instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """pub.inst.method to updates attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """pub.inst.method returns a dictionary containing
        all keys/values of __dict__ of the instance"""
        inst_dicopy = self.__dict__.copy()
        inst_dicopy["__class__"] = self.__class__.__name__
        inst_dicopy["created_at"] = self.created_at.isoformat()
        inst_dicopy["updated_at"] = self.updated_at.isoformat()
        return inst_dicopy
