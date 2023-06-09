#!/usr/bin/env python3
"""User password authentication model"""

import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
from user import User


def _hash_password(password: str) -> str:
    """takes in a password string, coverts it to bytes
    salt hasshes the bytes with bcrypt.hashpw """
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
        """Registers a new user to the database"""
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

    def valid_login(self, email: str, password: str) -> bool:
        """method validates user login"""
        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False

        return bcrypt.checkpw(password=password.encode('utf-8'),
                              hashed_password=user.hashed_password)
