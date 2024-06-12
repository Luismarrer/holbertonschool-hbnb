"""
This module contains the API endpoints for managing reviews.

This module defines the following routes:
- POST /places/<place_id>/reviews: Create a new review for a place.
- GET /users/<user_id>/reviews: Get all reviews by a user.
- GET /places/<place_id>/reviews: Get all reviews for a place.
- GET /reviews/<review_id>: Get a specific review by its ID.
- PUT /reviews/<review_id>: Update a specific review by its ID.
- DELETE /reviews/<review_id>: Delete a specific review by its ID.
"""

from flask import Blueprint, request, jsonify
from Model.Review import Review
from Persistence.DataManager import DataManager

reviews_bp = Blueprint('reviews', __name__)


@reviews_bp.route('/places/<place_id>/reviews', methods=['POST'])
def create_review(place_id):
    """Create a new review for a place.

    Args:
        place_id (str): The ID of the place.

    Returns:
        dict: The created review as a dictionary.

    Raises:
        HTTPException: If the request is missing required fields.
    """
    data = request.get_json()
    if 'user_id' not in data or 'rating' not in data or 'comment' not in data:
        return jsonify({'error': 'Missing fields'}), 400

    review = Review(place_id=place_id, **data)
    DataManager.save(review)
    return jsonify(review.to_dict()), 201


@reviews_bp.route('/users/<user_id>/reviews', methods=['GET'])
def get_reviews_by_user(user_id):
    """Get all reviews by a user.

    Args:
        user_id (str): The ID of the user.

    Returns:
        list: A list of reviews by the user as dictionaries.
    """
    reviews = DataManager.get(Review, 'user_id', user_id)
    return jsonify([review.to_dict() for review in reviews]), 200


@reviews_bp.route('/places/<place_id>/reviews', methods=['GET'])
def get_reviews_by_place(place_id):
    """Get all reviews for a place.

    Args:
        place_id (str): The ID of the place.

    Returns:
        list: A list of reviews for the place as dictionaries.
    """
    reviews = DataManager.get(Review, 'place_id', place_id)
    return jsonify([review.to_dict() for review in reviews]), 200


@reviews_bp.route('/reviews/<review_id>', methods=['GET'])
def get_review(review_id):
    """Get a specific review by its ID.

    Args:
        review_id (str): The ID of the review.

    Returns:
        dict: The review as a dictionary.

    Raises:
        HTTPException: If the review is not found.
    """
    review = DataManager.get(Review, review_id)
    if not review:
        return jsonify({'error': 'Review not found'}), 404
    return jsonify(review.to_dict()), 200


@reviews_bp.route('/reviews/<review_id>', methods=['PUT'])
def update_review(review_id):
    """Update a specific review by its ID.

    Args:
        review_id (str): The ID of the review.

    Returns:
        dict: The updated review as a dictionary.

    Raises:
        HTTPException: If the review is not found.
    """
    data = request.get_json()
    review = DataManager.update(Review, review_id)
    if not review:
        return jsonify({'error': 'Review not found'}), 404

    review.rating = data.get('rating', review.rating)
    review.comment = data.get('comment', review.comment)
    return jsonify(review.to_dict()), 200


@reviews_bp.route('/reviews/<review_id>', methods=['DELETE'])
def delete_review(review_id):
    """Delete a specific review by its ID.

    Args:
        review_id (str): The ID of the review.

    Returns:
        str: An empty response with status code 204.

    Raises:
        HTTPException: If the review is not found.
    """
    review = DataManager.get(Review, review_id)
    if not review:
        return jsonify({'error': 'Review not found'}), 404

    DataManager.delete(review)
    return '', 204
