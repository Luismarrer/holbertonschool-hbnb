#!/bin/python3
"""
This module contains the BaseModel class.
"""
from uuid import uuid4
from datetime import datetime
from Persistence.DataManager import DataManager


class BaseModel(DataManager):
    """
    This class represents the base model for all other models in the project.
    """
    def __init__(self):
        """
        Initializes a new instance of the BaseModel class.
        """
        self.id = str(uuid4())
        self.created_at = str(datetime.now())
        self.updated_at = self.created_at
        super().save(self)
        
    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)
                self.updated_at = datetime.now()
        super().update(self)
