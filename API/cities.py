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
from .blueprints import cities_bp


@cities_bp.route('/', methods=['POST'])
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
    
    if City.city_exists(data['name'], data['country_code']):
        return jsonify({'error': 'City already exists'}), 409

    try:
        city = City(name=data['name'], country_code=data['country_code'])
        return jsonify(city.__dict__), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 409


@cities_bp.route('/', methods=['GET'])
def get_cities():
    """
    Get all cities.

    Returns:
    - JSON array representing all cities.
    """
    data_manager = DataManager()
    cities = data_manager.get(entity_type=City)
    return jsonify([city.__dict__ for city in cities]), 200


@cities_bp.route('/<city_id>', methods=['GET'])
def get_city(city_id):
    """
    Get a specific city by ID.

    Parameters:
    - city_id: ID of the city.

    Returns:
    - JSON object representing the city.
    """
    data_manager = DataManager()
    city = data_manager.get(city_id, City)
    if not city:
        return jsonify({'error': 'City not found'}), 404
    return jsonify(city.__dict__), 200


@cities_bp.route('/<city_id>', methods=['PUT'])
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
    data_manager = DataManager()
    data = request.get_json()
    city = data_manager.get(city_id, City)
    if not city:
        return jsonify({'error': 'City not found'}), 404

    try:
        city.update_info(name=data.get('name'), country_code=data.get('country_code'))
        data_manager.update(city)
        return jsonify(city.__dict__), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 409


@cities_bp.route('/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    """
    Delete a specific city by ID.

    Parameters:
    - city_id: ID of the city.

    Returns:
    - Empty response with status code 204.
    """
    data_manager = DataManager()
    city = data_manager.get(city_id, City)
    if not city:
        return jsonify({'error': 'City not found'}), 404

    data_manager.delete(city_id, City)
    return '', 204
