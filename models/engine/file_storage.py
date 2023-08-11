#!/usr/bin/python3
""" creates database storage of instances as json file and reloads it """

import json


class FileStorage:
    """serializes instances to a JSON file and
    deserializes JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """serializes __objects to the JSONfile"""
        jdict = {}
        for key, value in self.__objects.items():
            jdict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='UTF-8') as jfile:
            json.dump(jdict, jfile)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, encoding="utf-8") as rfile:
                from models.base_model import BaseModel
                from models.amenity import Amenity
                from models.city import City
                from models.place import Place
                from models.review import Review
                from models.state import State
                from models.user import User
                reload_dic = json.load(rfile)
                for key, value in reload_dic.items():
                    cls_name = value["__class__"]
                    obj = eval(cls_name + "(**value)")
                    self.__objects[key] = obj
        except IOError:
            pass
