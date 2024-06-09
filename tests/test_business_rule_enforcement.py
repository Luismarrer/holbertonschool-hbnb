#!/bin/python3
import pytest
from Model.User import User
from Model.Place import Place

"""
This module contains unit tests for enforcing business rules in the application.
"""


def test_unique_email_constraint():
    """
    Test case to ensure that the email field in the User model has a unique constraint.
    """
    user1 = User(first_name="John", last_name="Doe", email="john.doe@example.com")
    with pytest.raises(Exception):
        user2 = User(first_name="Jane", last_name="Doe", email="john.doe@example.com")
        
def test_host_assignment_rule():
    """
    Test case to ensure that the host field in the Place model is correctly assigned to the user.
    """
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
    place1 = user.create_place(name="Central Park Apartment", city="New York", description="A lovely apartment near Central Park.")
    place2 = user.create_place(name="Times Square Studio", city="New York", description="A cozy studio in Times Square.")
    assert place1.host == user
