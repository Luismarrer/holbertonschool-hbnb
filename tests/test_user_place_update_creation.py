#!/bin/python3
import pytest
from Model.User import User
from Model.Country import Country
"""
This module contains unit tests for user and place creation.
"""

Puerto_Rico = Country("Puerto Rico")

def test_valid_user_creation():
	"""
	Test case for valid user creation.
	"""
	user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
	assert user.first_name == "John"
	assert user.last_name == "Doe"
	assert user.email == "john.doe@example.com"

def test_invalid_user_creation():
	"""
	Test case for invalid user creation.
	"""
	with pytest.raises(ValueError):
		User(first_name="John", last_name="Doe", email="invalid-email")

def test_valid_place_creation():
    """
    Test case for valid place creation.
    """
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
    place = user.create_place(name="Central Park Apartment", city="New York", description="A lovely apartment near Central Park.")
    assert place.name == "Central Park Apartment"
    assert place.city == "New York"
    assert place.host == user

def test_invalid_place_creation():
    """
    Test case for invalid place creation.
    """
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
    with pytest.raises(ValueError):
        user.create_place(name="", city="New York", description="A lovely apartment near Central Park.")
