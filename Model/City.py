#!/bin/python3
"""
This module contains the City class, which is a subclass of BaseModel.
"""

from .BaseModel import BaseModel


class City(BaseModel):
    """
    This class represents a city.
    """

    def __init__(self, name, country_code):
        """
        Initializes a new instance of the City class.

        Args:
            name (str): The name of the city.
            country (str): The country where the city is located.
        """
        self.name = name
        self.country = country_code
        self.places = []  # List of places in the city.
        super().__init__()

    def update_info(self, name=None, country_code=None):
        """
        Updates the city's information.

        Args:
            name (str): The new name of the city.
            country_code (str): The new country code where the city is located.
        """
        if name:
            self.name = name
        if country_code:
            self.country = country_code
        self.update()
