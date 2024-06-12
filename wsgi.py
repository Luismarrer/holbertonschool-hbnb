from flask import Flask
from API.blueprints import amenities_bp, cities_bp, countries_bp, places_bp, reviews_bp, users_bp

app = Flask(__name__)

app.register_blueprint(amenities_bp)
app.register_blueprint(cities_bp)
app.register_blueprint(countries_bp)
app.register_blueprint(places_bp)
app.register_blueprint(reviews_bp)
app.register_blueprint(users_bp)

@app.route('/')
def test():
    return "Whats up man?"

if __name__ == "__main__":
    app.run(debug=True)
