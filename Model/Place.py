#!/bin/python3
"""
This module contains the definition of the Place class.
"""

from Model.BaseModel import BaseModel
from Model.City import City


class Place(BaseModel):
	"""
	A class representing a place.
	"""

	def __init__(self, name, City, User, description, price_per_nigth, max_guest):
		"""
		Initialize a new Place object.

		Args:
			name (str): The name of the place.
		"""
		super().__init__()
		self.host = User
		self.city = City
		self.name = name
		self.description = description
		self.price_per_nigth = price_per_nigth
		self.max_guest = max_guest
		self.amenities = []
		self.reviews = []


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