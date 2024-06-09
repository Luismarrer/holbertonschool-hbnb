#!/bin/python3
from Model.User import User
from Model.City import City
from Model.Country import Country
import pytest
"""
This module contains unit tests for user and place creation.
"""

Puerto_Rico = Country("Puerto Rico")
San_Juan = City("San Juan", Puerto_Rico)
test6 = User(first_name="John", last_name="Doe",
             email="john.doe5@example.com", password="password",
             birthdate="1990-01-01")


def test_valid_user_creation():
    """
    Test case for valid user creation.
    """
    assert test6.first_name == "John"
    assert test6.last_name == "Doe"
    assert test6.email == "john.doe5@example.com"
    assert test6.password == "password"


def test_invalid_user_creation():
    """
    Test case for invalid user creation.
    """
    with pytest.raises(ValueError):
        User(first_name="John", last_name="Doe", email="invalid-email",
             password="password", birthdate="1990-01-01")


def test_valid_place_creation():
    """
    Test case for valid place creation.
    """
    place = test6.add_place("San Juan Apartment",
                            San_Juan,
                            "A lovely apartment near Central Park.",
                            100, 2)
    assert place.name == "San Juan Apartment"
    assert place.city == San_Juan
    assert place.host == test6


def test_invalid_place_creation():
    """
    Test case for invalid place creation.
    """
    with pytest.raises(ValueError):
        test6.add_place("", San_Juan,
                        "A lovely apartment near Central Park.",
                        100, 2)
