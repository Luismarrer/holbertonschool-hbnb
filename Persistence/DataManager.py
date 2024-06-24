#!/bin/python3
"""
This module contains the DataManager class.
"""
import os
import json
from Persistence.IPersistenceManager import IPersistenceManager
from Model.Country import Country

class DataManager(IPersistenceManager):
    def __init__(self, storage_path="data_storage.json", preload_path="countries_data.json"):
        self.storage_path = storage_path
        self.preload_path = preload_path
        self.data = self._load_storage()
        self._preload_countries()

    def _load_storage(self):
        """
        Load the data from the storage file.
        """
        if os.path.exists(self.storage_path):
            with open(self.storage_path, 'r') as file:
                return json.load(file)
        return {}

    def _save_storage(self):
        """
        Save the data to the storage file.
        """
        with open(self.storage_path, 'w') as file:
            json.dump(self.data, file, indent=4)

    def _preload_countries(self):
        """
        Preload countries from a JSON file.
        """
        if 'Country' not in self.data:
            with open(self.preload_path, 'r') as file:
                countries = json.load(file)
                self.data['Country'] = {country['code']: country for country in countries}
                self._save_storage()

    def save(self, entity):
        """
        Save an entity to the storage.

        Args:
            entity (object): The entity to save.
        """
        entity_type = type(entity).__name__
        if entity_type not in self.data:
            self.data[entity_type] = {}
        self.data[entity_type][entity.id] = entity.__dict__
        self._save_storage()

    def get(self, entity_id=None, entity_type=None):
        """
        Retrieve entities from the storage. If an ID is provided, retrieve a single entity.
        If no ID is provided, retrieve all entities of the given type.

        Args:
            entity_id (str, optional): The ID of the entity to retrieve. Defaults to None.
            entity_type (type, optional): The type of the entity to retrieve. Defaults to None.

        Returns:
            object or list: A single entity object if an ID is provided, otherwise a list of all entities of the given type.
        """
        entity_type_name = entity_type.__name__
        if entity_type_name in self.data:
            if entity_id:
                if entity_id in self.data[entity_type_name]:
                    entity_data = self.data[entity_type_name][entity_id]
                    if entity_type_name == 'Country':
                        return Country(**entity_data)
                    entity = entity_type.__new__(entity_type)
                    entity.__dict__.update(entity_data)
                    return entity
                return None
            else:
                entities = []
                for entity_data in self.data[entity_type_name].values():
                    if entity_type_name == 'Country':
                        entities.append(Country(**entity_data))
                    else:
                        entity = entity_type.__new__(entity_type)
                        entity.__dict__.update(entity_data)
                        entities.append(entity)
                return entities
        return None

    def update(self, entity):
        """
        Update an entity in the storage.

        Args:
            entity (object): The entity to update.
        """
        self.save(entity)

    def delete(self, entity_id, entity_type):
        """
        Delete an entity from the storage based on its ID and type.

        Args:
            entity_id (str): The ID of the entity to delete.
            entity_type (type): The type of the entity to delete.
        """
        entity_type_name = entity_type.__name__
        if entity_type_name in self.data and entity_id in self.data[entity_type_name]:
            del self.data[entity_type_name][entity_id]
            self._save_storage()