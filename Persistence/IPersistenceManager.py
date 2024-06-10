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
        Save an entity.

        Args:
            entity: The entity to save.
        """
        pass

    @abstractmethod
    def get(self, entity_id, entity_type):
        """
        Retrieve an entity.

        Args:
            entity_id: The ID of the entity to retrieve.
            entity_type: The type of the entity to retrieve.
        """
        pass

    @abstractmethod
    def update(self, entity):
        """
        Update an entity.

        Args:
            entity: The entity to update.
        """
        pass

    @abstractmethod
    def delete(self, entity_id, entity_type):
        """
        Delete an entity.

        Args:
            entity_id: The ID of the entity to delete.
            entity_type: The type of the entity to delete.
        """
        pass
