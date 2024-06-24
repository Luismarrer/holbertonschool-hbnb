#!/bin/python3
"""
This module defines the Amenity class, which represents
an amenity in a hotel booking system.
"""


from Model.BaseModel import BaseModel
from Persistence.DataManager import DataManager


class Amenity(BaseModel):
    """
    The Amenity class represents an amenity in a hotel booking system.

    Attributes:
        name (str): The name of the amenity.
        description (str): The description of the amenity.
        places (list): A list of all places associated with this amenity.
    """


    def __init__(self, name):
        """
        Initializes a new instance of the Amenity class.

        Args:
            name (str): The name of the amenity.
            description (str): The description of the amenity.

        """
        self.name = name
        self.places = []
        super().__init__()


    def update_info(self, new_name=None):
        """
        Updates the amenity's information.
        
        Args:
            new_name (str): The new name of the amenity.
            new_description (str): The new description of the amenity.
        """
        if new_name:
            self.name = new_name
        self.update()

    def delete(self):
        """
        Deletes the amenity instance.
        """
        for place in self.places:
            if self in place.amenities:
                place.amenities.remove(self)

    @staticmethod
    def amenity_exists(name):
        """
        Checks if an amenity with the given name already exists.

        Args:
            name (str): The name of the amenity.

        Returns:
            bool: True if the amenity exists, False otherwise.
        """
        data_manager = DataManager()
        amenities = data_manager.get(entity_type=Amenity)
        for amenity in amenities:
            if amenity.name == name:
                return True
        return False