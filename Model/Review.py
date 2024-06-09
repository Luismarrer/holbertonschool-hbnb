#!/bin/python3
"""
This module contains the Review class.
"""
from Model.BaseModel import BaseModel


class Review(BaseModel):
	"""
	A class that represents a review.

	Attributes:
		author (str): The author of the review.
		text (str): The text content of the review.
		calification (int): The rating given to the review.
	"""
	def __init__(self, author, place, text, rating):
		"""
		Initializes a new instance of the Review class.

		Args:
			author (str): The author of the review.
			text (str): The text content of the review.
			calification (int): The rating given to the review.
		"""
		super().__init__()
		self.author = author
		self.place = place
		self.text = text
		self.rating = rating
		place.reviews.append(self)
