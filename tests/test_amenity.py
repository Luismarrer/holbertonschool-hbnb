#!/bin/python3
from Model.User import User
from Model.Amenity import Amenity
from Model.City import City
from Model.Country import Country
import pytest

"""
This module contains unit tests for the Place and Amenity classes.
"""

Puerto_Rico = Country("Puerto Rico")
San_Juan = City("San Juan", Puerto_Rico)
Luis = User(first_name="Luis", last_name="Luis", email="luis.luis@example.com", password="password", birthdate="1990-01-01")

def test_delete_place():
    """
    Test case for deleting a place.
    """
    Airbnb1 = Luis.add_place("Airbnb1", San_Juan, "A lovely apartment near Morro", 100, 4)
    Luis.places.remove(Airbnb1)
    assert Airbnb1 not in Luis.places
		
def test_add_amenity():
    """
    Test case for adding an amenity to a place.
    """
    # Assuming the implementation of adding an amenity to a place
    Airbnb1 = Luis.add_place("Airbnb1", San_Juan, "A lovely apartment near Morro", 100, 4)
    amenity = Amenity(name="WiFi", description="High-speed internet access")
    Airbnb1.add_amenity(amenity)
    assert amenity in Airbnb1.amenities