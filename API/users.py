"""
This module contains the API endpoints for managing users.

The users module provides the following endpoints:
- POST /users: Create a new user.
- GET /users: Get all users.
- GET /users/<user_id>: Get a specific user.
- PUT /users/<user_id>: Update a specific user.
- DELETE /users/<user_id>: Delete a specific user.
"""

from flask import Blueprint, request, jsonify
from Model.User import User
from Persistence.DataManager import DataManager

users_bp = Blueprint('users', __name__)


@users_bp.route('/users', methods=['POST'])
def create_user():
    """
    Create a new user.

    Returns:
        A JSON response containing the created user's information.
    """
    data = request.get_json()
    if 'email' not in data or 'first_name' not in data\
       or 'last_name' not in data:
        return jsonify({'error': 'Missing fields'}), 400

    user = User(email=data['email'], first_name=data['first_name'],
                last_name=data['last_name'])
    DataManager.save(user)
    return jsonify(user.to_dict()), 201


@users_bp.route('/users', methods=['GET'])
def get_users():
    """
    Get all users.

    Returns:
        A JSON response containing a list of all users' information.
    """
    users = DataManager.get(User)
    return jsonify([user.to_dict() for user in users]), 200


@users_bp.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """
    Get a specific user.

    Args:
        user_id: The ID of the user to retrieve.

    Returns:
        A JSON response containing the user's information if found,
        or an error message if not found.
    """
    user = DataManager.get(User, user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user.to_dict()), 200


@users_bp.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    """
    Update a specific user.

    Args:
        user_id: The ID of the user to update.

    Returns:
        A JSON response containing the updated user's information if found,
        or an error message if not found.
    """
    data = request.get_json()
    user = DataManager.update(User, user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    user.first_name = data.get('first_name', user.first_name)
    user.last_name = data.get('last_name', user.last_name)
    return jsonify(user.to_dict()), 200


@users_bp.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Delete a specific user.

    Args:
        user_id: The ID of the user to delete.

    Returns:
        An empty response with status code 204 if the user is deleted,
        or an error message if not found.
    """
    user = DataManager.get(User, user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    DataManager.delete(user)
    return '', 204
