#!/bin/python3
"""
This module defines the Amenity class, which represents
an amenity in a hotel booking system.
"""


from Model.BaseModel import BaseModel


class Amenity(BaseModel):
    """
    The Amenity class represents an amenity in a hotel booking system.

    Attributes:
        name (str): The name of the amenity.
        description (str): The description of the amenity.
        places (list): A list of all places associated with this amenity.
    """


    def __init__(self, name, description):
        """
        Initializes a new instance of the Amenity class.

        Args:
            name (str): The name of the amenity.
            description (str): The description of the amenity.

        """
        self.name = name
        self.description = description
        self.places = []
        super().__init__()

    def update_name(self, new_name):
        """
        Updates the name of the amenity.

        Args:
            new_name (str): The new name of the amenity.
        """
        self.name = new_name
        self.update()

    def update_description(self, new_description):
        """
        Updates the description of the amenity.

        Args:
            new_description (str): The new description of the amenity.
        """
        self.description = new_description
        self.update()

    def update_info(self, new_name=None, new_description=None):
        """
        Updates the amenity's information.
        
        Args:
            new_name (str): The new name of the amenity.
            new_description (str): The new description of the amenity.
        """
        if new_name:
            self.name = new_name
        if new_description:
            self.description = new_description
        self.update()

    def delete(self):
        """
        Deletes the amenity instance.
        """
        for place in self.places:
            if self in place.amenities:
                place.amenities.remove(self)