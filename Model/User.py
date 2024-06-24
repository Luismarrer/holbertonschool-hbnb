#!/bin/python3
"""
This module contains the User class.
"""


from .BaseModel import BaseModel
from .Review import Review
from .Place import Place
from .Amenity import Amenity
from Persistence.DataManager import DataManager
import re

class User(BaseModel):
	"""
	This class represents a user.

	Attributes:
		used_emails (set): A set containing the used email addresses.
	"""

	used_emails = set()

	def __init__(self, email, first_name, last_name):
		"""
		Initializes a new User object.

		Args:
			first_name (str): The first name of the user.
			last_name (str): The last name of the user.
			email (str): The email address of the user.
		"""
		if not self.is_valid_email(email):
			raise ValueError("Invalid email address")
		if email in User.used_emails or self.email_exists_in_db(email):
			raise ValueError("Email already in use")
		User.used_emails.add(email)

		self.email = email
		self.first_name = first_name
		self.last_name = last_name
		self.reviews = []
		self.places = []
		super().__init__()

	@staticmethod
	def is_valid_email(email):
		"""
		Check if an email is valid.

		Args:
			email (str): The email to check.

		Returns:
			bool: True if the email is valid, False otherwise.
		"""
		email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
		return re.match(email_regex, email) is not None

	def email_exists_in_db(self, email):
		"""
		Check if the email exists in the database.

		Args:
			email (str): The email to check.

		Returns:
			bool: True if the email exists, False otherwise.
		"""
		data_manager = DataManager()
		users = data_manager.get(entity_type=User)
		return any(user.email == email for user in users)
	
	def add_place(self, name, description, address, number_of_rooms, number_of_bathrooms, max_guest, price_per_night, latitude, longitude, city):
		"""
		Adds a new place to the user's list of places.

		Args:
			name (str): The name of the place.
			description (str): The description of the place.
			address (str): The address of the place.
			number_of_rooms (int): The number of rooms in the place.
			number_of_bathrooms (int): The number of bathrooms in the place.
			max_guest (int): The maximum number of guests allowed in the place.
			price_per_night (float): The price per night for the place.
			latitude (float): The latitude coordinate of the place.
			longitude (float): The longitude coordinate of the place.
			city (City): The city object associated with the place.

		Returns:
			Place: The newly created place object.
		"""
		place = Place(self.id, name, description, address, number_of_rooms, number_of_bathrooms, max_guest, price_per_night, latitude, longitude, city.id)
		self.places.append(place)
		city.places.append(place)
		return place

	def add_review(self, place, text, rating):
		"""
		Adds a new review to the user's list of reviews.

		Args:
			place (Place): The place object associated with the review.
			text (str): The text of the review.
			rating (int): The rating of the review.

		Returns:
			Review: The newly created review object.
		"""
		review = Review(place_id=place.id, user_id=self.id, rating=rating, comment=text)
		self.reviews.append(review)
		place.reviews.append(review)
		return review

	def update_name(self, new_first_name=None, new_last_name=None):
		"""
		Updates the first and last name of the user.

		Args:
			new_first_name (str): The new first name of the user.
			new_last_name (str): The new last name of the user.
		"""
		if new_first_name:
			self.first_name = new_first_name
		if new_last_name:
			self.last_name = new_last_name
		self.update()

	def update_email(self, new_email):
		"""
		Updates the email of the user.

		Args:
			new_email (str): The new email address of the user.
		"""
		if not self.is_valid_email(new_email):
			raise ValueError("Invalid email address")
		if new_email in User.used_emails or self.email_exists_in_db(new_email):
			raise ValueError("Email already in use")
		if self.email in User.used_emails:
			User.used_emails.remove(self.email)
		User.used_emails.add(new_email)
		self.email = new_email
		self.update()

	def update_info(self, new_first_name=None, new_last_name=None, new_email=None):
		"""
		Updates the user's information.

		Args:
			new_first_name (str): The new first name of the user.
			new_last_name (str): The new last name of the user.
			new_email (str): The new email address of the user.
		"""
		if new_first_name:
			self.first_name = new_first_name
		if new_last_name:
			self.last_name = new_last_name
		if new_email:
			self.update_email(new_email)
		self.update()
