from flask import Flask
from flask_restx import Api
from API.blueprints import amenities_bp, cities_bp, countries_bp, places_bp, reviews_bp, users_bp

app = Flask(__name__)
api = Api(app, version='1.0', title='AirBnB API',
		  description='A simple AirBnB API')

app.register_blueprint(amenities_bp)
app.register_blueprint(cities_bp)
app.register_blueprint(countries_bp)
app.register_blueprint(places_bp)
app.register_blueprint(reviews_bp)
app.register_blueprint(users_bp)

if __name__ == "__main__":
    app.run(debug=True)
