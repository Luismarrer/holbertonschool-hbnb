#!/bin/python3
import unittest
from datetime import datetime
from Model.User import User
"""
This module contains unit tests to check the consistency of the User model.
"""


class TestModelConsistency(unittest.TestCase):
	def test_created_at(self):
		"""
		Test if the 'created_at' attribute of a User instance is an instance of datetime.
		"""
		user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
		self.assertIsInstance(user.created_at, datetime)
		
	def test_updated_at(self):
		"""
		Test if the 'updated_at' attribute of a User instance is updated after calling the 'update_name' method.
		"""
		user = User(first_name="John", last_name="Doe", email="john.doe@example.com")
		old_updated_at = user.updated_at
		user.update_name("Johnny")
		self.assertNotEqual(user.updated_at, old_updated_at)

if __name__ == '__main__':
	unittest.main()
