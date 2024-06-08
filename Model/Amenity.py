#!/bin/python3
"""
"""


from . import BaseModel


class Amenity(BaseModel):
    """
    """
    amenities_list = []

    def __init__(self, name, descripion, author):
        """
        """
        self.name = name
        self.description = description
        self.author = author
        self.amenities_list.append(self)

    def update_name(self, new_name):
        """
        """
        self.name = new_name

    def update_description(self, new_description):
        """
        """
        self.description = new_description

    def select(self):
        """
        """
        return self

    def delete(self):
        """
        """
        if self in Amenity.amenities_list:
            Amenity.amenities_list.remove(self)
            print("Amenity has been deleted.")
        else:
            print("Amenity not found")
