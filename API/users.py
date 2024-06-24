"""
This module contains the API endpoints for managing users.

The users module provides the following endpoints:
- POST /users: Create a new user.
- GET /users: Get all users.
- GET /users/<user_id>: Get a specific user.
- PUT /users/<user_id>: Update a specific user.
- DELETE /users/<user_id>: Delete a specific user.
"""

from flask import request, jsonify
from Model.User import User
from .blueprints import users_bp
from Persistence.DataManager import DataManager


@users_bp.route('/', methods=['POST'])
def create_user():
    """
    Create a new user.

    Returns:
        A JSON response containing the created user's information.
    """
    data = request.get_json()
    if 'email' not in data or 'first_name' not in data or 'last_name' not in data:
        return jsonify({'error': 'Missing fields'}), 400

    try:
        user = User(email=data['email'], first_name=data['first_name'], last_name=data['last_name'])
        return jsonify(user.__dict__), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 409
    

@users_bp.route('/', methods=['GET'])
def get_users():
    """
    Get all users.

    Returns:
        A JSON response containing a list of all users' information.
    """

    data_manager = DataManager()
    users = data_manager.get(entity_type=User)
    return jsonify([user.__dict__ for user in users]), 200


@users_bp.route('/<user_id>', methods=['GET'])
def get_user(user_id):
    """
    Get a specific user.

    Args:
        user_id: The ID of the user to retrieve.

    Returns:
        A JSON response containing the user's information if found,
        or an error message if not found.
    """
    data_manager = DataManager()
    user = data_manager.get(user_id, User)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user.__dict__), 200


@users_bp.route('/<user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Update a specific user.

    Args:
        user_id: The ID of the user to update.

    Returns:
        A JSON response containing the updated user's information if found,
        or an error message if not found.
    """
    
    data_manager = DataManager()
    data = request.get_json()
    user = data_manager.get(user_id, User)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    try:
        user.update_info(new_first_name=data.get('first_name'),
                         new_last_name=data.get('last_name'),
                         new_email=data.get('email'))
        data_manager.update(user)
        return jsonify(user.__dict__), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 409


@users_bp.route('/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Delete a specific user.

    Args:
        user_id: The ID of the user to delete.

    Returns:
        An empty response with status code 204 if the user is deleted,
        or an error message if not found.
    """
    data_manager = DataManager()
    user = data_manager.get(user_id, User)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    data_manager.delete(user_id, User)
    return '', 204
