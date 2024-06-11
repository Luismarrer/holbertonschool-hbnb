import pytest
from Model.User import User
from Model.Place import Place
from Model.Review import Review
from Model.Amenity import Amenity
from Model.City import City
from Model.Country import Country
Luis4 = User("Luis", "Luis", "Luis@luis101.com", "password", "2000-01-01")
Luis5 = User("Luis", "Luis", "Luis@luis102.com", "password", "2000-01-01")
san_juan = City("San Juan", Country("Puerto Rico"))
vega_baja = City("Vega Baja", Country("Puerto Rico"))


def test_save_and_load_user(data_manager):
    data_manager.save(Luis4)
    loaded_user = data_manager.get(Luis4.id, User)
    assert Luis4.email == loaded_user["email"]
"""
def test_delete_user(data_manager):
    data_manager.delete(Luis4.id, User)
    with pytest.raises(FileNotFoundError):
        loaded_user = data_manager.get(Luis4.id, User)
"""
def test_save_and_load_place(data_manager):
    san_juan = City("San Juan", Country("Puerto Rico"))
    mi_casa = Luis4.add_place("Test Place", san_juan, "123 Main St", 100, 4)
    data_manager.save(mi_casa)
    loaded_place = data_manager.get(mi_casa.id, Place)
    assert mi_casa.name == loaded_place['name']

def test_save_and_load_city(data_manager):
    data_manager.save(san_juan)
    loaded_city = data_manager.get(san_juan.id, City)
    assert san_juan.name == loaded_city['name']

def test_save_and_load_review(data_manager):
    data_manager.save(Luis5)
    data_manager.save(vega_baja)
    place = Luis5.add_place("Test Place", vega_baja, "123 Main St", 100, 4)
    data_manager.save(place)
    review = Luis4.add_review(place, "This is a test review", 5)
    data_manager.save(review)
    loaded_review = data_manager.get(review.id, Review)
    assert review.text == loaded_review['text']
    assert review.rating == loaded_review['rating']

def test_save_and_load_amenity(data_manager):
    amenity = Amenity(name="Test Amenity", description="This is a test amenity")
    data_manager.save(amenity)
    loaded_amenity = data_manager.get(amenity.id, Amenity)
    assert amenity.name == loaded_amenity['name']
    assert amenity.description == loaded_amenity['description']

def test_save_and_load_country(data_manager):
    country = Country(name="Test Country")
    data_manager.save(country)
    loaded_country = data_manager.get(country, Country)
    assert country.name == loaded_country['name']
