#!/bin/python3
"""
This module contains the Review class.
"""
from .BaseModel import BaseModel


class Review(BaseModel):
    """
    A class that represents a review.

    Attributes:
        author (str): The author of the review.
        text (str): The text content of the review.
        calification (int): The rating given to the review.
    """
    def __init__(self, place_id, user_id, rating, comment):
        """
        Initializes a new instance of the Review class.

        Args:
            author (str): The author of the review.
            text (str): The text content of the review.
            calification (int): The rating given to the review.
        """
        self.place_id = place_id
        self.user_id = user_id
        self.rating = rating
        self.comment = comment
        super().__init__()

    def update_info(self, rating=None, comment=None):
        """
        Updates the review's information.

        Args:
            rating (int): The new rating of the review.
            comment (str): The new text content of the review.
        """
        if rating is not None:
            self.rating = rating
        if comment is not None:
            self.comment = comment
        self.update()
