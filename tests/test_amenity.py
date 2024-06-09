#!/bin/python3
import unittest
from Model.User import User
from Model.Place import Place
from Model.Amenity import Amenity

"""
This module contains unit tests for the Place and Amenity classes.
"""

class TestPlaceDeletion(unittest.TestCase):
	"""
	This class contains unit tests for deleting a place.
	"""

	def test_delete_place(self):
		"""
		Test case for deleting a place.
		"""
		user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
		place = user.create_place(name="Central Park Apartment", city="New York", description="A lovely apartment near Central Park.")
		user.places.remove(place)
		self.assertNotIn(place, user.places)
		
class TestAmenityAddition(unittest.TestCase):
	"""
	This class contains unit tests for adding an amenity to a place.
	"""

	def test_add_amenity(self):
		"""
		Test case for adding an amenity to a place.
		"""
		user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
		place = user.create_place(name="Central Park Apartment", city="New York", description="A lovely apartment near Central Park.")
		amenity = Amenity(name="WiFi", description="Free WiFi", author="Admin")
		place.add_amenity(amenity)
		self.assertIn(amenity, place.amenities)

if __name__ == '__main__':
	unittest.main()
