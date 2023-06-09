#!/usr/bin/env python3
"""" A user model for a users  database table using declarative mapping"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, VARCHAR


Base = declarative_base()


class User(Base):
    """table of users with attributes specified"""
    # creating a class User taht inherits from Base

    __tablename__ = 'users'  # name of table

    id = Column(Integer, primary_key=True)
    email = Column(VARCHAR(250), nullable=False)  # This means no row can be left null
    hashed_password = Column(VARCHAR(250), nullable=False)
    session_id = Column(VARCHAR(250), nullable=True)  # This means rows can be left null
    reset_token = Column(VARCHAR(250), nullable=True)
