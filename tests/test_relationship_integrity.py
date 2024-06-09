#!/bin/python3
import pytest
from Model.User import User
from Model.Place import Place
from Model.Review import Review
from Model.Country import Country
from Model.City import City

"""
This module contains unit tests for checking the integrity of relationships between models.
"""
Puerto_Rico = Country("Puerto Rico")
San_Juan = City("San Juan", Puerto_Rico)
test4 = User(first_name="John", last_name="Doe", email="john.doe3@example.com", password="password", birthdate="1990-01-01")
USA = Country("United States")
New_York = City("New York", USA)


def test_place_host_relationship():
    """
    Test the relationship between a Place and its host User.
    """
    place = test4.add_place("San Juan Apartment 4", San_Juan, "A lovely apartment near Central Park.", 100, 4)
    assert place.host == test4
    assert place in test4.places
        
def test_review_relationship():
    """
    Test the relationship between a Review and its author User, as well as the relationship between a Review and its associated Place.
    """
    place = test4.add_place("Central Park Apartment", New_York, "A lovely apartment near Central Park.", 100, 4)
    with pytest.raises(ValueError):
        review = test4.add_review(place=place, text="Great place to stay!", rating=5.0)


