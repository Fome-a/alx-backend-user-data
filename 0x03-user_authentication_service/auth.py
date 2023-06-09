#!/usr/bin/env python3
"""User password authentication model"""

import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    bytes = password.encode('utf-8')
    hashed_password = bcrypt.hashpw(bytes, bcrypt.gensalt())
    return hashed_password


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()  # creating an instance of the
        # DB class is important because thats how
        # I am able to relate to the database
        # and also use the database functions

    def register_user(self, email: str, password: str) -> str:
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            """exception handles if the email is searched for and
            it cannot be found then add it to the database"""
            pwd = _hash_password(password)  # hash the password
            user = self._db.add_user  # using add_user function from db.py file
        else:
            """else if its found then throw an error"""
            raise ValueError(f"User{email} already exists")
