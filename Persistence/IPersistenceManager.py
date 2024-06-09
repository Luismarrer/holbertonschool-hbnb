#!/bin/python3
"""
"""
from abc import ABC, abstractmethod

class IPersistenceManager(ABC):
	"""_summary_

	Args:
		ABC (_type_): _description_
	"""

    @abstractmethod
    def save(self, entity):
		"""_summary_

		Args:
			entity (_type_): _description_
		"""
        pass

    @abstractmethod
    def get(self, entity_id, entity_type):
		"""_summary_

		Args:
			entity_id (_type_): _description_
			entity_type (_type_): _description_
		"""
        pass

    @abstractmethod
    def update(self, entity):
		"""_summary_

		Args:
			entity (_type_): _description_
		"""
        pass

    @abstractmethod
def delete(self, entity_id, entity_type):
	"""Deletes an entity from the persistence manager.

	Args:
		entity_id (int): The ID of the entity to be deleted.
		entity_type (str): The type of the entity to be deleted.
	"""
        pass