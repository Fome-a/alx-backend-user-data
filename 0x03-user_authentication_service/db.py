#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Addition of users to database and return of an object """
        session = Session()  # Create a session
        user = User(email=email, hashed_password=hashed_password)
        self.__session.add(user)
        self.__session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """
        method takes an abitrary keyword argument from input and queries
        the database returning the first match made
        from the query
        """

        if kwargs is None:
            return InvalidRequestError
        query = self._session.query(User).filter_by(**kwargs)
        user = query.first()
        if user is None:
            return NoResultFound
        return user

    def update_user(self, user_id: int, **kwargs) -> User:
        """method takes user_id and keyword arguments as input
            uses find_user_by to locate the user to be updated
            and makes required changes
        """
        user = self.find_user_by(id=user_id)

        for key, value in kwargs.items:
            if not hasattr(user, key):
                raise ValueError
            setattr(user, key, value)
        self._session.commit()
