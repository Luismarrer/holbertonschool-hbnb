#!/bin/python3
"""
This module contains the User class.
"""
from Model.BaseModel import BaseModel
from Model.Review import Review
from Model.Place import Place

class User(BaseModel):
	"""
	This class represents a user.
	"""
	used_emails = set()
	def __init__(self, first_name, last_name, email, password, birthdate):
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
		if email in User.used_emails:
			raise ValueError("Email already in use")
		User.used_emails.add(email)
		self.first_name = first_name
		self.last_name = last_name
		self.email = email
		self.password = password
		self.birthdate = birthdate
		self.age = ''
		self.places = []
		self.reviews = []

	def add_place(self, name, City, description, price_per_nigth, max_guest):
			"""
			Adds a place to the user.

			Args:
				name (str): The name of the place.
				city (str): The city where the place is located.
				description (str): A description of the place.

			Returns:
				Place: The newly created place object.

			"""
			place = Place(name, City, self, description, price_per_nigth, max_guest)
			self.places.append(place)
			City.add_place(place)
			return place
	
	def add_review(self, place, text, rating):
		"""
		Add a review for a place.

		Args:
			place (Place): The place to review.
			text (str): The review text.
			rating (float): The review rating.

		Returns:
			Review: The created review object.

		Raises:
			ValueError: If the user tries to review their own place.
		"""
		if place.host == self:
			raise ValueError("A host cannot review their own place.")
		review = Review(self, place, text, rating)
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

	def __str__(self):
		"""
		Returns a string representation of the User object.

		Returns:
			str: A string representation of the User object.
		"""
		return f"User: {self.first_name} {self.last_name}"
	
	def update_name(self, new_name):
		"""
		Updates the name of the user.
		"""
		self.first_name = new_name
		super().update()