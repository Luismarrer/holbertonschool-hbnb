#!/bin/python3
"""
"""
from uuid import uuid4
from datetime import now


class BaseModel:
    """
    """
    def __init__(self):
        """
        """
        self.ID = uuid4()
        self.created_at = now()
        self.update_at = self.created_at

    def update(self):
        """
        """
        self.update_at = now()
