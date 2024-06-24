"""
This module defines the routes for managing amenities in the API.

Routes:
- POST /amenities: Create a new amenity.
- GET /amenities: Get a list of all amenities.
- GET /amenities/<amenity_id>: Get details of a specific amenity.
- PUT /amenities/<amenity_id>: Update details of a specific amenity.
- DELETE /amenities/<amenity_id>: Delete a specific amenity.
"""
from flask import request, jsonify
from Model.Amenity import Amenity
from Persistence.DataManager import DataManager
from .blueprints import amenities_bp

data_manager = DataManager()


@amenities_bp.route('/', methods=['POST'])
def create_amenity():
    """
    Create a new amenity.

    Request Body:
    - name: The name of the amenity.

    Returns:
    - JSON object representing the created amenity.
    """
    data = request.get_json()
    if 'name' not in data:
        return jsonify({'error': 'Missing fields'}), 400
    
    if Amenity.amenity_exists(data['name']):
        return jsonify({'error': 'Amenity already exists'}), 409

    amenity = Amenity(data['name'])
    return jsonify(amenity.__dict__), 201


@amenities_bp.route('/', methods=['GET'])
def get_amenities():
    """
    Get a list of all amenities.

    Returns:
    - JSON array representing the list of amenities.
    """
    data_manager = DataManager()
    amenities = data_manager.get(entity_type=Amenity)
    return jsonify([amenity.__dict__ for amenity in amenities]), 200


@amenities_bp.route('/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    """
    Get details of a specific amenity.

    Parameters:
    - amenity_id: The ID of the amenity.

    Returns:
    - JSON object representing the details of the amenity.
    """
    data_manager = DataManager()
    amenity = data_manager.get(amenity_id, Amenity)
    if not amenity:
        return jsonify({'error': 'Amenity not found'}), 404
    return jsonify(amenity.__dict__), 200


@amenities_bp.route('/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    """
    Update details of a specific amenity.

    Parameters:
    - amenity_id: The ID of the amenity.

    Request Body:
    - name: The updated name of the amenity.

    Returns:
    - JSON object representing the updated amenity.
    """
    data_manager = DataManager()
    data = request.get_json()
    amenity = data_manager.get(amenity_id, Amenity)
    if not amenity:
        return jsonify({'error': 'Amenity not found'}), 404

    try:
        amenity.update_info(new_name=data.get('name'))
        data_manager.update(amenity)
        return jsonify(amenity.__dict__), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 409


@amenities_bp.route('/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    """
    Delete a specific amenity.

    Parameters:
    - amenity_id: The ID of the amenity.

    Returns:
    - Empty response with status code 204.
    """
    data_manager = DataManager()
    amenity = data_manager.get(amenity_id, Amenity)
    if not amenity:
        return jsonify({'error': 'Amenity not found'}), 404

    data_manager.delete(amenity_id, Amenity)
    return '', 204
