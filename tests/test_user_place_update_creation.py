#!/bin/python3
import pytest
from Model.User import User
"""
This module contains unit tests for user and place creation.
"""

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

class TestPlaceCreation(unittest.TestCase):
	def test_valid_place_creation(self):
		"""
		Test case for valid place creation.
		"""
		user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
		place = user.create_place(name="Central Park Apartment", city="New York", description="A lovely apartment near Central Park.")
		self.assertEqual(place.name, "Central Park Apartment")
		self.assertEqual(place.city, "New York")
		self.assertEqual(place.host, user)
		
	def test_invalid_place_creation(self):
		"""
		Test case for invalid place creation.
		"""
		user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
		with self.assertRaises(ValueError):
			user.create_place(name="", city="New York", description="A lovely apartment near Central Park.")
