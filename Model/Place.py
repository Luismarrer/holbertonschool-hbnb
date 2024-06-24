#!/bin/python3
"""
This module contains the definition of the Place class.
"""

from .BaseModel import BaseModel
from .Review import Review
from .Amenity import Amenity


class Place(BaseModel):
    """
    A class representing a place.
    """

    def __init__(self, name, description, address, city_id, latitude, longitude, host_id, number_of_rooms, number_of_bathrooms, price_per_night, max_guests, amenity_ids=None):
        """
        Initialize a new Place object.

        Args:
            name (str): The name of the place.
        """
        if not name or not city_id or not host_id or not description\
                or not price_per_night or not max_guests:
            raise ValueError("Invalid arguments")
        self.host_id = host_id
        self.name = name
        self.city = city_id
        self.description = description
        self.address = address
        self.number_of_rooms = number_of_rooms
        self.number_of_bathrooms = number_of_bathrooms
        self.price_per_night = price_per_night
        self.max_guest = max_guests
        self.latitude = latitude
        self.longitude = longitude
        self.amenities = []
        self.reviews = []
        super().__init__()

    def update_info(self, name=None, description=None, address=None, city_id=None, latitude=None, longitude=None, host_id=None, number_of_rooms=None, number_of_bathrooms=None, price_per_night=None, max_guests=None, amenity_ids=None):
        """
        Updates the place's information.

        Args:
            name (str): The new name of the place.
            description (str): The new description of the place.
            address (str): The new address of the place.
            city_id (str): The new city ID of the place.
            latitude (float): The new latitude of the place.
            longitude (float): The new longitude of the place.
            host_id (str): The new host ID of the place.
            number_of_rooms (int): The new number of rooms in the place.
            number_of_bathrooms (int): The new number of bathrooms in the place.
            price_per_night (float): The new price per night for the place.
            max_guests (int): The new maximum number of guests allowed in the place.
            amenity_ids (list): The new list of amenity IDs associated with the place.
        """
        if name:
            self.name = name
        if description:
            self.description = description
        if address:
            self.address = address
        if city_id:
            self.city = city_id
        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude
        if host_id:
            self.host_id = host_id
        if number_of_rooms is not None:
            self.number_of_rooms = number_of_rooms
        if number_of_bathrooms is not None:
            self.number_of_bathrooms = number_of_bathrooms
        if price_per_night is not None:
            self.price_per_nigth = str(price_per_night)
        if max_guests is not None:
            self.max_guest = max_guests
        if amenity_ids is not None:
            self.amenities = [Amenity(id) for id in amenity_ids]
        self.update() 