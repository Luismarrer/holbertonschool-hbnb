"""
This module contains a fixture for the data manager used in tests.

The data manager fixture creates an instance of the
DataManager class and yields it for use in tests.

Example usage:
    def test_data_manager(data_manager):
        # Use the data_manager fixture to access the DataManager instance
        assert data_manager.get_data() == expected_data
"""
import pytest
from Persistence.DataManager import DataManager


@pytest.fixture
def data_manager():
    """
    Fixture that creates an instance of the DataManager class.

    The DataManager instance is created with the path to a test data file.

    Yields:
        DataManager: An instance of the DataManager class.
    """
    manager = DataManager('tests/\
                          test_data_manager.json')
    yield manager
