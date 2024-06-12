"""
This module contains the API endpoints for managing places.

Endpoints:
- POST /places: Create a new place.
- GET /places: Get all places.
- GET /places/<place_id>: Get a specific place by ID.
- PUT /places/<place_id>: Update a specific place by ID.
- DELETE /places/<place_id>: Delete a specific place by ID.
"""

from flask import request, jsonify
from Model.Place import Place
from Persistence.DataManager import DataManager
from .blueprints import places_bp

@places_bp.route('/', methods=['POST'])
def create_place():
    """
    Create a new place.

    Request Body:
    - name (str): The name of the place.
    - description (str): The description of the place.
    - address (str): The address of the place.
    - city_id (int): The ID of the city where the place is located.
    - latitude (float): The latitude coordinate of the place.
    - longitude (float): The longitude coordinate of the place.
    - host_id (int): The ID of the host who owns the place.
    - number_of_rooms (int): The number of rooms in the place.
    - number_of_bathrooms (int): The number of bathrooms in the place.
    - price_per_night (float): The price per night for the place.
    - max_guests (int): The maximum number of guests allowed in the place.

    Returns:
    - If successful, returns the created place as JSON with status code 201.
    - If missing fields in the request body, returns an
        error message as JSON with status code 400.
    """
    data = request.get_json()
    required_fields = ['name', 'description', 'address', 'city_id', 'latitude',
                       'longitude', 'host_id', 'number_of_rooms',
                       'number_of_bathrooms', 'price_per_night', 'max_guests']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing fields'}), 400

    place = Place(**data)
    DataManager.save(place)
    return jsonify(place.to_dict()), 201


@places_bp.route('/', methods=['GET'])
def get_places():
    """
    Get all places.

    Returns:
    - Returns a list of all places as JSON with status code 200.
    """
    places = DataManager.get(Place)
    return jsonify([place.to_dict() for place in places]), 200


@places_bp.route('/<place_id>', methods=['GET'])
def get_place(place_id):
    """
    Get a specific place by ID.

    Parameters:
    - place_id (str): The ID of the place.

    Returns:
    - If the place is found, returns the place as JSON with status code 200.
    - If the place is not found, returns an error
        message as JSON with status code 404.
    """
    place = DataManager.get(Place, place_id)
    if not place:
        return jsonify({'error': 'Place not found'}), 404
    return jsonify(place.to_dict()), 200


@places_bp.route('/<place_id>', methods=['PUT'])
def update_place(place_id):
    """
    Update a specific place by ID.

    Parameters:
    - place_id (str): The ID of the place.

    Request Body:
    - name (str): The updated name of the place.
    - description (str): The updated description of the place.
    - address (str): The updated address of the place.
    - city_id (int): The updated ID of the city where the place is located.
    - latitude (float): The updated latitude coordinate of the place.
    - longitude (float): The updated longitude coordinate of the place.
    - host_id (int): The updated ID of the host who owns the place.
    - number_of_rooms (int): The updated number of rooms in the place.
    - number_of_bathrooms (int): The updated number of bathrooms in the place.
    - price_per_night (float): The updated price per night for the place.
    - max_guests (int): The updated maximum number
        of guests allowed in the place.

    Returns:
    - If the place is found and updated successfully,
        returns the updated place as JSON with status code 200.
    - If the place is not found,
        returns an error message as JSON with status code 404.
    """
    data = request.get_json()
    place = DataManager.update(Place, place_id)
    if not place:
        return jsonify({'error': 'Place not found'}), 404

    for key, value in data.items():
        setattr(place, key, value)
    DataManager.save(place)
    return jsonify(place.to_dict()), 200


@places_bp.route('/<place_id>', methods=['DELETE'])
def delete_place(place_id):
    """
    Delete a specific place by ID.

    Parameters:
    - place_id (str): The ID of the place.

    Returns:
    - If the place is found and deleted successfully,
        returns an empty response with status code 204.
    - If the place is not found,
        returns an error message as JSON with status code 404.
    """
    place = DataManager.get(Place, place_id)
    if not place:
        return jsonify({'error': 'Place not found'}), 404

    DataManager.delete(place)
    return '', 204
