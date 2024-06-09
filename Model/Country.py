#!/bin/python3
"""
This module contains the Country class.
"""


class Country:
	"""
	The Country class represents a country.
	"""
	def __init__(self, name):
		"""
		Initializes a new instance of the Country class.

		Args:
			name (str): The name of the country.
		"""
		self.name = name
		self.cities = [] # List of cities in the country.
	
	def add_city(self, city):
		"""
		Adds a city to the country.

		Args:
			city (City): The city to add.
		"""
		self.cities.append(city)

	def __str__(self):
		"""
		Returns a string representation of the Country object.

		Returns:
			str: A string representation of the Country object.
		"""
		return f"Country: {self.name}"
