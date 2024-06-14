import pytest
from Model.User import User
from Model.Place import Place
from Model.Review import Review
from Model.Amenity import Amenity
from Model.City import City
from Model.Country import Country
from Persistence.DataManager import DataManager
Luis4 = User("Luis@luis101.com", "Luis", "Luis")
Luis5 = User("Luis@luis102.com","Luis", "Luis")
san_juan = City("San Juan", Country("Puerto Rico"))
vega_baja = City("Vega Baja", Country("Puerto Rico"))


def test_save_and_load_user():
    loaded_user = Luis4.get
    print(loaded_user)
    assert Luis4.email == loaded_user['email']


def test_save_and_load_place():
    san_juan = City("San Juan", Country("Puerto Rico"))
    mi_casa = Luis4.add_place("Test Place", san_juan, "123 Main St", 100, 4)
    loaded_place = mi_casa.get
    assert mi_casa.name == loaded_place['name']


def test_save_and_load_city():
    loaded_city = san_juan.get
    assert san_juan.name == loaded_city['name']


def test_save_and_load_review():
    place = Luis5.add_place("Test Place", vega_baja, "123 Main St", 100, 4)
    review = Luis4.add_review(place, "This is a test review", 5)
    loaded_review = review.get(review.id, Review)
    assert review.text == loaded_review['text']
    assert review.rating == loaded_review['rating']


def test_save_and_load_amenity():
    amenity = Amenity(name="Test Amenity",
                      description="This is a test amenity")
    loaded_amenity = amenity.get
    assert amenity.name == loaded_amenity['name']
    assert amenity.description == loaded_amenity['description']


def test_save_and_load_country():
    country = Country(name="Test Country")
    loaded_country = country.get(country, Country)
    assert country.name == loaded_country['name']
