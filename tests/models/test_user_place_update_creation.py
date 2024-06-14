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
test6 = User("john.doe5@example.com", "John", "Doe")


def test_valid_user_creation():
    """
    Test case for valid user creation.
    """
    assert test6.first_name == "John"
    assert test6.last_name == "Doe"
    assert test6.email == "john.doe5@example.com"
    
def test_valid_user_update():
    """
    Test case for valid user update.
    """
    test6.update("john.doe5@example.com", "Jane", "Smith")
    assert test6.first_name == "Jane"

def test_invalid_user_creation():
    """
    Test case for invalid user creation.
    """
    with pytest.raises(ValueError):
        User("invalid-email", "John", "Doe") 


def test_valid_place_creation():
    """
    Test case for valid place creation.
    """
    place = test6.add_place("San Juan Apartment",
                            San_Juan,
                            "A lovely apartment near Central Park.",
                            100, 2)
    assert place.name == "San Juan Apartment"
    assert place.city == San_Juan.name
    assert place.host == test6.id


def test_invalid_place_creation():
    """
    Test case for invalid place creation.
    """
    with pytest.raises(ValueError):
        test6.add_place("", San_Juan,
                        "A lovely apartment near Central Park.",
                        100, 2)
