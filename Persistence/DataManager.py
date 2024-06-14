#!/bin/python3
"""
This module contains the DataManager class.
"""
import os
import json
from Persistence.IPersistenceManager import IPersistenceManager
storage_path='./Persistence/data'

class DataManager(IPersistenceManager):
    """
    This class represents a data manager
    that handles the persistence of entities.

    Args:
        IPersistenceManager (type):
            The base persistence manager class.
    """
    
            
    def save(self, entity):
        if not os.path.exists(storage_path):
            os.makedirs(storage_path)
        # Load existing data
        if os.path.exists(f"{storage_path}/{type(entity).__name__}.json"):
            with open(f"{storage_path}/{type(entity).__name__}.json", 'r') as f:
                data = json.load(f)
        else:
            data = []
    
        # Update data with new entity
        data.append(entity.__dict__)
    
        # Save updated data to storage
        with open(f"{storage_path}/{type(entity).__name__}.json", 'w') as f:
            json.dump(data, f, indent=4)

        
    def get(self, entity_id="", entity_type=""):
        """
        Retrieve an entity based on ID and type.

        Args:
            entity_id (type): The ID of the entity.
            entity_type (type): The type of the entity.

        Returns:
            The retrieved entity.
        """
        # Logic to retrieve an entity based on ID and type
        with open(f"{storage_path}/{entity_type.__name__}.json", 'r') as f:
            data = json.load(f)
            for entity_data in data:
                if entity_data['id'] == entity_id:
                     return entity_data
            return data

    def update(self, entity):
        """
        Update the given entity in storage.

        Args:
            entity (type): The entity to be updated.
        """
        # Logic to update an entity in storage
        update_entity = self.get(entity.id, type(entity))
        if update_entity is not None:
        # Apply updates to the entity
            for key, value in entity.__dict__.items():
                if key in entity:
                    entity[key] = value
        
            # Save the updated entity
            self.save(entity)
        else:
            print("Entity not found")
        

    def delete(self, entity_id, entity_type):
        """
        Delete an entity from storage based on ID and type.

        Args:
            entity_id (type): The ID of the entity.
            entity_type (type): The type of the entity.
        """
        # Logic to delete an entity from storage
        os.remove(f"{storage_path}/{entity_id}_{entity_type.__name__}.json")
