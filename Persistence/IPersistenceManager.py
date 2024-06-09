#!/bin/python3
"""
This module defines the IPersistenceManager interface.
"""


from abc import ABC, abstractmethod


class IPersistenceManager(ABC):
    """
    This is the base interface for
    all persistence managers.

    Args:
        ABC (type): The ABC metaclass for
        defining abstract base classes.
    """

    @abstractmethod
    def save(self, entity):
        """
        Saves an entity to the persistence manager.

        Args:
            entity (object): The entity to be saved.
        """
        pass

    @abstractmethod
    def get(self, entity_id, entity_type):
        """
        Retrieves an entity from the persistence manager.

        Args:
            entity_id (int): The ID of the entity to be retrieved.
            entity_type (str): The type of the entity to be retrieved.
        """
        pass

    @abstractmethod
    def update(self, entity):
        """
        Updates an entity in the persistence manager.

        Args:
            entity (object): The entity to be updated.
        """
        pass

    @abstractmethod
    def delete(self, entity_id, entity_type):
        """
        Deletes an entity from the persistence manager.

        Args:
            entity_id (int): The ID of the entity to be deleted.
            entity_type (str): The type of the entity to be deleted.
        """
        pass
