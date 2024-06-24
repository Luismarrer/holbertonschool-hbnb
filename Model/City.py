#!/bin/python3
"""
This module contains the City class, which is a subclass of BaseModel.
"""

from .BaseModel import BaseModel
from .Country import Country
from Persistence.DataManager import DataManager


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
        if not self.country_exists(country_code):
            raise ValueError(f"Country code {country_code} does not exist.")
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
        if not country_code:
            country_code = self.country
        if name:
            if self.city_exists(name, country_code):
                raise ValueError(f"City {name} alredy exist.")
            self.name = name
        if country_code:
            if not self.country_exists(country_code):
                raise ValueError(f"Country code {country_code} does not exist.")
            self.country = country_code
        self.update()

    @staticmethod
    def city_exists(name, country_code):
        """
        Checks if a city with the given name and country code already exists.

        Args:
            name (str): The name of the city.
            country_code (str): The country code where the city is located.

        Returns:
            bool: True if the city exists, False otherwise.
        """
        data_manager = DataManager()
        cities = data_manager.get(entity_type=City)
        for city in cities:
            if city.name == name and city.country == country_code:
                return True
        return False

    @staticmethod
    def country_exists(country_code):
        """
        Checks if a country with the given country code exists.

        Args:
            country_code (str): The country code to check.

        Returns:
            bool: True if the country code exists, False otherwise.
        """
        data_manager = DataManager()
        countries = data_manager.get(entity_type=Country)
        for country in countries:
            if country.code == country_code:
                return True
        return False