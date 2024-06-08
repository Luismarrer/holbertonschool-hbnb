#!/bin/python3
"""
"""
from . import BaseModel


class Review(BaseModel):
    """
    """
    def __init__(self, author, text, calification):
        self.author = author
        self.text = text
        self.calification = calification

