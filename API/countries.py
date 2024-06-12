"""
This module contains the routes for handling country-related requests.
"""

from flask import Blueprint, jsonify
from Model.Country import Country
from Model.City import City
from Persistence.DataManager import DataManager

countries_bp = Blueprint('countries', __name__)


@countries_bp.route('/countries', methods=['GET'])
def get_countries():
    """
    Get all countries.

    Returns:
        A JSON response containing a list of all countries.
    """
    countries = DataManager.get(Country)
    return jsonify([country.to_dict() for country in countries]), 200


@countries_bp.route('/countries/<country_code>', methods=['GET'])
def get_country(country_code):
    """
    Get a specific country by country code.

    Args:
        country_code (str): The country code.

    Returns:
        A JSON response containing the country information if found,
        or an error message if not found.
    """
    country = DataManager.get(Country, country_code)
    if not country:
        return jsonify({'error': 'Country not found'}), 404
    return jsonify(country.to_dict()), 200


@countries_bp.route('/countries/<country_code>/cities', methods=['GET'])
def get_cities_by_country(country_code):
    """
    Get all cities in a specific country.

    Args:
        country_code (str): The country code.

    Returns:
        A JSON response containing a list of all cities in the specified
        country if found, or an error message if not found.
    """
    country = DataManager.get(Country, country_code)
    if not country:
        return jsonify({'error': 'Country not found'}), 404
    cities = DataManager.get(City, 'country_code', country_code)
    return jsonify([city.to_dict() for city in cities]), 200
