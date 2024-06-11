import pytest
from Persistence.DataManager import DataManager

@pytest.fixture
def data_manager():
    manager = DataManager('tests/test_data_manager.json')
    yield manager

