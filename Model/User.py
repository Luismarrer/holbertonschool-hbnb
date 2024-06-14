#!/bin/python3
"""
This module contains the User class.
"""
from .BaseModel import BaseModel
from .Review import Review
from .Place import Place
from datetime import datetime
import re


class User(BaseModel):
    """
    This class represents a user.

    Attributes:
        used_emails (set): A set containing the used email addresses.

    Methods:
        __init__(self, first_name, last_name, email, password, birthdate):
            Initializes a new User object.
        is_valid_email(email): Check if an email is valid.
        calculate_age(self):
            Calculate the age of the user based on the birthdate.
        add_place(self, name, City, description, price_per_night, max_guest):
            Adds a place to the user.
        add_review(self, place, text, rating): Add a review for a place.
        add_amenity(self, place, amenity): Adds an amenity to a place.
        __str__(self): Returns a string representation of the User object.
        update_name(self, new_name): Updates the name of the user.
    """

    used_emails = set()

    def __init__(self, email, first_name, last_name):
        """
        Initializes a new User object.

        Args:
            first_name (str): The first name of the user.
            last_name (str): The last name of the user.
            email (str): The email address of the user.
            password (str): The password of the user.
            birthdate (str): The birthdate of the user.
        """
        if not self.is_valid_email(email):
            raise ValueError("Invalid email address")
        if email in User.used_emails:
            raise ValueError("Email already in use")
        User.used_emails.add(email)
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.reviews = []
        self.places = []
        super().__init__()


    @staticmethod
    def is_valid_email(email):
        """
        Check if an email is valid.

        Args:
            email (str): The email to check.

        Returns:
            bool: True if the email is valid, False otherwise.
        """
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return re.match(email_regex, email) is not None
    
    def add_place(self, name, description, number_of_rooms, number_of_bathrooms, max_guest, price_per_night, latitude, longitude, city):
        """
        Adds a place to the user.

        Args:
            name (str): The name of the place.
            city (str): The city where the place is located.
            description (str): A description of the place.
            price_per_night (float): The price per night for the place.
            max_guest (int): The maximum number of guests allowed in the place.

        Returns:
            Place: The newly created place object.
        """
        place = Place(self.id, name, description, number_of_rooms, number_of_bathrooms, max_guest, price_per_night, latitude, longitude, city.id)
        self.places.append(place)
        City.add_place(place)
        return place

    def add_review(self, place, text, rating):
        """
        Add a review for a place.

        Args:
            place (Place): The place to review.
            text (str): The review text.
            rating (float): The review rating.

        Returns:
            Review: The created review object.

        Raises:
            ValueError: If the user tries to review their own place.
        """
        if place.host == self.id:
            raise ValueError("A host cannot review their own place.")
        review = Review(self, place, text, rating)
        self.reviews.append(review)
        place.add_review(review)
        return review

    def add_amenity(self, place, amenity):
        """
        Adds an amenity to a place.

        Args:
            place (Place): The place to add the amenity to.
            amenity (Amenity): The amenity to add.
        """
        place.add_amenity(amenity)

    def __str__(self):
        """
        Returns a string representation of the User object.

        Returns:
            str: A string representation of the User object.
        """
        return f"User: {self.first_name} {self.last_name}"

    def update_name(self, new_name):
        """
        Updates the name of the user.

        Args:
            new_name (str): The new name for the user.
        """
        self.first_name = new_name
        super().update()
