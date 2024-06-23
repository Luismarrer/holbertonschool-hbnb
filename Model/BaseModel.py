#!/bin/python3
"""
This module contains the BaseModel class.
"""


from uuid import uuid4
from datetime import datetime


class BaseModel():
    """
    This class represents the base model for all other models in the project, except Country.
    """
    def __init__(self):
        """
        Initializes a new instance of the BaseModel class.
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        
    def update(self):
        """
        Updates the `updated_at` attribute to the current datetime.
        """
        self.updated_at = datetime.now()

