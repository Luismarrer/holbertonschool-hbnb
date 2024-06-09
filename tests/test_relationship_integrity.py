#!/bin/python3
import pytest
from Model.User import User
from Model.Place import Place
from Model.Review import Review

"""
This module contains unit tests for checking the integrity of relationships between models.
"""


def test_place_host_relationship():
    """
    Test the relationship between a Place and its host User.
    """
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
    place = user.create_place(name="Central Park Apartment", city="New York", description="A lovely apartment near Central Park.")
    assert place.host == user
    assert place in user.places
		
def test_review_relationship(self):
	"""
	Test the relationship between a Review and its author User, as well as the relationship between a Review and its associated Place.
	"""
	user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
	place = user.create_place(name="Central Park Apartment", city="New York", description="A lovely apartment near Central Park.")
	review = user.create_review(place=place, text="Great place to stay!", rating=5.0)
	self.assertEqual(review.author, user)
	self.assertEqual(review.place, place)
	self.assertIn(review, user.reviews)
	self.assertIn(review, place.reviews)

