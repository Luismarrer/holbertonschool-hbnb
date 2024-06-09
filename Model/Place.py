#!/bin/python3
"""
This module contains the definition of the Place class.
"""

from . import BaseModel


class Place(BaseModel):
	"""
	A class representing a place.
	"""

	def __init__(self, name, host, city, description, price_per_nigth, max_guest):
		"""
		Initialize a new Place object.

		Args:
			name (str): The name of the place.
		"""
		super().__init__()
		self.host = host
		self.city = city
		self.types = types
		self.name = name
		self.description = description
		self.address = address
		self.latitude = latitude
		self.longitude = longitude
		self.numbers_rooms = numbers_rooms
		self.numbers_bathrooms = numbers_bathrooms
		self.price_per_nigth = price_per_nigth
		self.max_guest = max_guest
		self.amenities = []
		self.reviews = []
		city.add_place(self)

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