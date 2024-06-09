#!/bin/python3
from datetime import datetime
from Model.User import User
from Model.Country import Country
import pytest
"""
This module contains unit tests to check
the consistency of the User model.
"""
Puerto_Rico = Country("Puerto Rico")
user = User(first_name="John", last_name="Doe", email="john.doe2@example.com",
            password="password", birthdate="1990-01-01")


def test_created_at():
    """
    Test if the 'created_at' attribute of a
    User instance is an instance of datetime.
    """
    assert isinstance(user.created_at, datetime)


def test_updated_at():
    """
    Test if the 'updated_at' attribute of a User instance
    is updated after calling the 'update_name' method.
    """
    old_updated_at = user.updated_at
    user.update_name("Johnny")
    assert user.updated_at != old_updated_at
