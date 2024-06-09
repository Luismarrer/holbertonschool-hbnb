#!/bin/python3
import pytest
from datetime import datetime
from Model.User import User
"""
This module contains unit tests to check the consistency of the User model.
"""


def test_created_at():
    """
    Test if the 'created_at' attribute of a User instance is an instance of datetime.
    """
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
    assert isinstance(user.created_at, datetime)

def test_updated_at():
    """
    Test if the 'updated_at' attribute of a User instance is updated after calling the 'update_name' method.
    """
    user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
    old_updated_at = user.updated_at
    user.update_name("Johnny")
    assert user.updated_at != old_updated_at
