"""
This module contains the routes for managing cities in the API.

Routes:
- POST /cities: Create a new city.
- GET /cities: Get all cities.
- GET /cities/<city_id>: Get a specific city by ID.
- PUT /cities/<city_id>: Update a specific city by ID.
- DELETE /cities/<city_id>: Delete a specific city by ID.
"""
from flask import Blueprint, request, jsonify
from Model.City import City
from Persistence.DataManager import DataManager

cities_bp = Blueprint('cities', __name__)


@cities_bp.route('/cities', methods=['POST'])
def create_city():
    """
    Create a new city.

    Request Body:
    - name: Name of the city (required).
    - country_code: Country code of the city (required).

    Returns:
    - JSON object representing the created city.
    """
    data = request.get_json()
    if 'name' not in data or 'country_code' not in data:
        return jsonify({'error': 'Missing fields'}), 400

    city = City(name=data['name'], country_code=data['country_code'])
    DataManager.save(city)
    return jsonify(city.to_dict()), 201


@cities_bp.route('/cities', methods=['GET'])
def get_cities():
    """
    Get all cities.

    Returns:
    - JSON array representing all cities.
    """
    cities = DataManager.get(City)
    return jsonify([city.to_dict() for city in cities]), 200


@cities_bp.route('/cities/<city_id>', methods=['GET'])
def get_city(city_id):
    """
    Get a specific city by ID.

    Parameters:
    - city_id: ID of the city.

    Returns:
    - JSON object representing the city.
    """
    city = DataManager.get(City, city_id)
    if not city:
        return jsonify({'error': 'City not found'}), 404
    return jsonify(city.to_dict()), 200


@cities_bp.route('/cities/<city_id>', methods=['PUT'])
def update_city(city_id):
    """
    Update a specific city by ID.

    Parameters:
    - city_id: ID of the city.

    Request Body:
    - name: Updated name of the city (optional).

    Returns:
    - JSON object representing the updated city.
    """
    data = request.get_json()
    city = DataManager.update(City, city_id)
    if not city:
        return jsonify({'error': 'City not found'}), 404

    city.name = data.get('name', city.name)
    return jsonify(city.to_dict()), 200


@cities_bp.route('/cities/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    """
    Delete a specific city by ID.

    Parameters:
    - city_id: ID of the city.

    Returns:
    - Empty response with status code 204.
    """
    city = DataManager.get(City, city_id)
    if not city:
        return jsonify({'error': 'City not found'}), 404

    DataManager.delete(city)
    return '', 204
