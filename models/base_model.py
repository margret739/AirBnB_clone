#!/usr/bin/python3
"""
module for the BaseModel class"""

import uuid
from json import dump
from datetime import datetime


class BaseModel:
    def __init__(self, *args, **kwargs):
        """ instatiates a new model """
        if not kwargs:
            from models import storage
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def save(self):
        """

        """
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """ convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def __str__(self):
        """ """
        class_name = (str(type(self)).split('.')[-1]).split('\'')[0]
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
