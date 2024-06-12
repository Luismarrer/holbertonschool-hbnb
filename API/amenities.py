"""
This module defines the routes for managing amenities in the API.

Routes:
- POST /amenities: Create a new amenity.
- GET /amenities: Get a list of all amenities.
- GET /amenities/<amenity_id>: Get details of a specific amenity.
- PUT /amenities/<amenity_id>: Update details of a specific amenity.
- DELETE /amenities/<amenity_id>: Delete a specific amenity.
"""
from flask import Blueprint, request, jsonify
from Model.Amenity import Amenity
from Persistence.DataManager import DataManager

amenities_bp = Blueprint('amenities', __name__)


@amenities_bp.route('/amenities', methods=['POST'])
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

    amenity = Amenity(name=data['name'])
    DataManager.save(amenity)
    return jsonify(amenity.to_dict()), 201


@amenities_bp.route('/amenities', methods=['GET'])
def get_amenities():
    """
    Get a list of all amenities.

    Returns:
    - JSON array representing the list of amenities.
    """
    amenities = DataManager.get(Amenity)
    return jsonify([amenity.to_dict() for amenity in amenities]), 200


@amenities_bp.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    """
    Get details of a specific amenity.

    Parameters:
    - amenity_id: The ID of the amenity.

    Returns:
    - JSON object representing the details of the amenity.
    """
    amenity = DataManager.get(Amenity, amenity_id)
    if not amenity:
        return jsonify({'error': 'Amenity not found'}), 404
    return jsonify(amenity.to_dict()), 200


@amenities_bp.route('/amenities/<amenity_id>', methods=['PUT'])
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
    data = request.get_json()
    amenity = DataManager.update(Amenity, amenity_id)
    if not amenity:
        return jsonify({'error': 'Amenity not found'}), 404

    amenity.name = data.get('name', amenity.name)
    return jsonify(amenity.to_dict()), 200


@amenities_bp.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    """
    Delete a specific amenity.

    Parameters:
    - amenity_id: The ID of the amenity.

    Returns:
    - Empty response with status code 204.
    """
    amenity = DataManager.get(Amenity, amenity_id)
    if not amenity:
        return jsonify({'error': 'Amenity not found'}), 404

    DataManager.delete(amenity)
    return '', 204
