from flask import Blueprint

# Define Blueprints
amenities_bp = Blueprint('amenities', __name__, url_prefix='/amenities')
cities_bp = Blueprint('cities', __name__, url_prefix='/cities')
countries_bp = Blueprint('countries', __name__, url_prefix='/countries')
places_bp = Blueprint('places', __name__, url_prefix='/places')
reviews_bp = Blueprint('reviews', __name__)
users_bp = Blueprint('users', __name__, url_prefix='/users')

# Import routes
from . import amenities, cities, countries, places, reviews, users