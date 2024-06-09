#!/bin/python3
"""
This module contains the User class.
"""
from . import BaseModel
from . import Place

class User(BaseModel):
	"""
	This class represents a user.
	"""
	def __init__(self, first_name, last_name, email, password, birthday):
		"""
		Initializes a new User object.

		Args:
			first_name (str): The first name of the user.
			last_name (str): The last name of the user.
			email (str): The email address of the user.
			password (str): The password of the user.
			birthday (str): The birthday of the user.
		"""
		super().__init__()
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.password = password
		self.birthday = birthday
		self.age = ''
		self.places = []
		self.reviews = []

	def add_place(self, name, city, description):
		"""
		Adds a place to the user.

		Args:
			name (str): The name of the place.
			city (str): The city where the place is located.
			description (str): A description of the place.
		"""
		place = Place(name, self, description)
		self.places.append(place)
		city.add_place(place)
		return place
	
	def add_review(self, place, text, calification):
		"""
		Adds a review to the user.

		Args:
			place (Place): The place to review.
			text (str): The text content of the review.
			calification (int): The rating given to the review.
		"""
		review = Review(self, text, calification)
		self.reviews.append(review)
		place.add_review(review)
		return review
	
	def add_amenity(self, place, amenity):
		"""
		Adds an amenity to a place.

		Args:
			place (Place): The place to add the amenity to.
			amenity (Amenity): The amenity to add.
		"""
		place.add_amenity(amenity)