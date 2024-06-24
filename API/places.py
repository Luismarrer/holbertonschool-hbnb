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
from Model.City import City
from Model.Amenity import Amenity

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
    data_manager = DataManager()
    data = request.get_json()
    required_fields = ['name', 'description', 'address', 'city_id', 'latitude',
                       'longitude', 'host_id', 'number_of_rooms',
                       'number_of_bathrooms', 'price_per_night', 'max_guests', 'amenity_ids']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing fields'}), 400
    
    city = data_manager.get(data['city_id'], City)
    if not city:
        return jsonify({'error': 'City ID does not exist'}), 400

    amenity_ids = data.get('amenity_ids', [])
    print(amenity_ids)
    for amenity_id in amenity_ids:
        print(amenity_id)
        if not data_manager.get(amenity_id, Amenity):
            return jsonify({'error': 'Amenity ID does not exist'}), 400

    place = Place(name=data['name'], description=data['description'],
                  address=data['address'], city_id=data['city_id'],
                  latitude=data['latitude'], longitude=data['longitude'],
                  host_id=data['host_id'], number_of_rooms=data['number_of_rooms'],
                  number_of_bathrooms=data['number_of_bathrooms'],
                  price_per_night=data['price_per_night'],
                  max_guests=data['max_guests'], amenity_ids=amenity_ids)
    return jsonify(place.__dict__), 201


@places_bp.route('/', methods=['GET'])
def get_places():
    """
    Get all places.

    Returns:
    - Returns a list of all places as JSON with status code 200.
    """
    data_manager = DataManager()
    places = data_manager.get(entity_type=Place)
    return jsonify([place.__dict__ for place in places]), 200


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
    data_manager = DataManager()
    place = data_manager.get(place_id, Place)
    if not place:
        return jsonify({'error': 'Place not found'}), 404
    return jsonify(place.__dict__), 200


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
    data_manager = DataManager()
    place = data_manager.get(place_id, Place)
    if not place:
        return jsonify({'error': 'Place not found'}), 404

    data_manager.delete(place_id, Place)
    return '', 204
