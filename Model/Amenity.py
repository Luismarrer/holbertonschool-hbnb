#!/bin/python3
"""
This module defines the Amenity class, which represents an amenity in a hotel booking system.
"""

from Model.BaseModel import BaseModel


class Amenity(BaseModel):
	"""
	The Amenity class represents an amenity in a hotel booking system.

	Attributes:
		name (str): The name of the amenity.
		description (str): The description of the amenity.
		author (str): The author of the amenity.
		amenities_list (list): A list of all amenities.

	Methods:
		__init__(self, name, description, author): Initializes a new instance of the Amenity class.
		update_name(self, new_name): Updates the name of the amenity.
		update_description(self, new_description): Updates the description of the amenity.
		select(self): Selects the amenity.
		delete(self): Deletes the amenity.
	"""

	amenities_list = []

	def __init__(self, name, description):
		"""
		Initializes a new instance of the Amenity class.

		Args:
			name (str): The name of the amenity.
			description (str): The description of the amenity.
			author (str): The author of the amenity.
		"""
		super().__init__()
		self.name = name
		self.description = description
		self.amenities_list.append(self)

	def update_name(self, new_name):
		"""
		Updates the name of the amenity.

		Args:
			new_name (str): The new name of the amenity.
		"""
		self.name = new_name

	def update_description(self, new_description):
		"""
		Updates the description of the amenity.

		Args:
			new_description (str): The new description of the amenity.
		"""
		self.description = new_description

	def select(self):
		"""
		Selects the amenity.

		Returns:
			Amenity: The selected amenity.
		"""
		return self

	def delete(self):
		"""
		Deletes the amenity.
		"""
		if self in Amenity.amenities_list:
			Amenity.amenities_list.remove(self)
			print("Amenity has been deleted.")
		else:
			print("Amenity not found")
