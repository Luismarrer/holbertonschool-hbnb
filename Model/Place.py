#!/bin/python3
"""
This module contains the definition of the Place class.
"""

from .BaseModel import BaseModel


class Place(BaseModel):
    """
    A class representing a place.
    """

    def __init__(self, host_id, name, description, number_of_rooms, number_of_bathrooms, max_guest, price_per_nigth, latitude, longitude, city):
        """
        Initialize a new Place object.

        Args:
            name (str): The name of the place.
        """
        if not name or not city or not host_id or not description\
                or not price_per_nigth or not max_guest:
            raise ValueError("Invalid arguments")
        self.host_id = host_id
        self.name = name
        self.city = city.id
        self.description = description
        self.price_per_nigth = price_per_nigth
        self.max_guest = max_guest
        self.amenities = []
        self.reviews = []
        super().__init__()

    def add_amenity(self, amenity):
        """
        Add an amenity to the place.

        Args:
            amenity (Amenity): The amenity to add.
        """
        self.amenities.append(amenity)

    def add_review(self, review):
        """
        Add a review to the place.

        Args:
            review (Review): The review to add.
        """
        self.reviews.append(review)
