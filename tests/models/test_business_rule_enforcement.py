#!/bin/python3
import pytest
from Model.User import User
from Model.Country import Country
from Model.City import City

"""
This module contains unit tests for enforcing
business rules in the application.
"""
Puerto_Rico = Country("Puerto Rico")
San_Juan = City("San Juan", Puerto_Rico)


def test_unique_email_constraint():
    """
    Test case to ensure that the email field in
    the User model has a unique constraint.
    """
    John = User(first_name="John", last_name="Doe",
                email="john.doe@example.com")
    with pytest.raises(Exception):
        John2 = User(first_name="Jane", last_name="Doe",
                     email="john.doe@example.com")


def test_host_assignment_rule():
    """
    Test case to ensure that the host field in the
    Place model is correctly assigned to the user.
    """
    Luis = User(first_name="Luis", last_name="Luis",
                email="luis.luis1@example.com")
    place1 = Luis.add_place("San Juan Apartment",
                            San_Juan,
                            "A lovely apartment near Morro.",
                            100, 4)
    place2 = Luis.add_place("San Juan Studio", San_Juan,
                            "A cozy studio in Santurce.",
                            80, 2)
    assert place1.host == Luis.id
