#!/bin/python3
"""
"""


class User(BaseModel):
    """
    """
    def __init__(first_name, last_name, email, password, birthday):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.birthday = birthday
