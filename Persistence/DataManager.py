#!/bin/python3
"""
This module contains the DataManager class.
"""
import os
import json
from Persistence.IPersistenceManager import IPersistenceManager


class DataManager(IPersistenceManager):
    """
    This class represents a data manager
    that handles the persistence of entities.

    Args:
        IPersistenceManager (type):
            The base persistence manager class.
    """
    def __init__(self, storage_path):
        self.storage_path = storage_path
        if not os.path.exists(storage_path):
            os.makedirs(storage_path)

    def save(self, entity):
        """
        Save the given entity to storage.

        Args:
            entity (type): The entity to be saved.
        """
        # Logic to save entity to storage
        with open(f"{self.storage_path}/{type(entity).__name__}.json", 'a') as f:
            json.dump(entity.__dict__, f, indent=4)

    def get(self, entity_id, entity_type):
        """
        Retrieve an entity based on ID and type.

        Args:
            entity_id (type): The ID of the entity.
            entity_type (type): The type of the entity.

        Returns:
            The retrieved entity.
        """
        # Logic to retrieve an entity based on ID and type
        with open(f"{self.storage_path}/{entity_type.__name__}.json", 'r') as f:
            data = json.load(f)
            return data

    def update(self, entity):
        """
        Update the given entity in storage.

        Args:
            entity (type): The entity to be updated.
        """
        # Logic to update an entity in storage
        self.save(entity)

    def delete(self, entity_id, entity_type):
        """
        Delete an entity from storage based on ID and type.

        Args:
            entity_id (type): The ID of the entity.
            entity_type (type): The type of the entity.
        """
        # Logic to delete an entity from storage
        os.remove(f"{self.storage_path}/{entity_id}_{entity_type.__name__}.json")
