"""
This module contains the routes for handling country-related requests.
"""

from flask import jsonify
from Model.Country import Country
from Model.City import City
from Persistence.DataManager import DataManager
from .blueprints import countries_bp


@countries_bp.route('/', methods=['GET'])
def get_countries():
    """
    Get all countries.

    Returns:
        A JSON response containing a list of all countries.
    """
    data_manager = DataManager()
    countries = data_manager.get(entity_type=Country)
    return jsonify([country.__dict__ for country in countries]), 200


@countries_bp.route('/<country_code>', methods=['GET'])
def get_country(country_code):
    """
    Get a specific country by its ISO 3166-1 alpha-2 code.

    Args:
        country_code: The ISO 3166-1 alpha-2 code of the country to retrieve.

    Returns:
        A JSON response containing the country's information if found,
        or an error message if not found.
    """
    data_manager = DataManager()
    country = data_manager.get(country_code, Country)
    if not country:
        return jsonify({'error': 'Country not found'}), 404
    return jsonify(country.__dict__), 200


@countries_bp.route('/<country_code>/cities', methods=['GET'])
def get_cities_by_country(country_code):
    """
    Get all cities belonging to a specific country by its ISO 3166-1 alpha-2 code.

    Args:
        country_code: The ISO 3166-1 alpha-2 code of the country.

    Returns:
        A JSON response containing a list of cities.
    """
    data_manager = DataManager()
    cities = data_manager.get(entity_type=City)
    country_cities = [city.__dict__ for city in cities if city.country == country_code]
    return jsonify(country_cities), 200
