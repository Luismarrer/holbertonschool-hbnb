#!/bin/python3
import pytest
from Model.User import User
from Model.Place import Place
from Model.Amenity import Amenity

"""
This module contains unit tests for the Place and Amenity classes.
"""

def test_delete_place():
    """
    Test case for deleting a place.
    """
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
    place = user.create_place(name="Central Park Apartment", city="New York", description="A lovely apartment near Central Park.")
    user.places.remove(place)
    assert place not in user.places
		
def test_add_amenity():
    """
    Test case for adding an amenity to a place.
    """
    # Assuming the implementation of adding an amenity to a place
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
    place = user.create_place(name="Central Park Apartment", city="New York", description="A lovely apartment near Central Park.")
    amenity = Amenity(name="WiFi")
    place.add_amenity(amenity)
    assert amenity in place.amenities