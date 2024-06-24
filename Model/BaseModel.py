#!/bin/python3
"""
This module contains the BaseModel class.
"""


from uuid import uuid4
from datetime import datetime
from Persistence.DataManager import DataManager


class BaseModel():
    """
    This class represents the base model for all other models in the project, except Country.
    """
    def __init__(self):
        """
        Initializes a new instance of the BaseModel class.
        """
        data_manager = DataManager()
        self.id = str(uuid4())
        self.created_at = str(datetime.now())
        self.updated_at = self.created_at
        data_manager.save(self)
        
    def update(self):
        """
        Updates the `updated_at` attribute to the current datetime.
        """
        data_manager = DataManager()
        self.updated_at = str(datetime.now())
        data_manager.update(self)

    def delete(self):
        """
        Deletes the current instance.
        """
        data_manager = DataManager()
        data_manager.delete(self.id, type(self))
