#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.session import Session

from user import Base, User

from typing import Dict


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
        """
        save the user to the database
        """
        user = User(email=email, hashed_password=hashed_password)
        try:
            self._session.add(user)
            self._session.commit()
        except Exception as e:
            print(f"The new user was not added because: {e}")
            self._session.rollback()
            raise
        return user

    def find_user_by(self, **kwargs: Dict[str, str]) -> User:
        """
        find a  user in the database by different attr

        Raises:
            error: NoResultFound: When no results are found.
            error: InvalidRequestError: When invalid query arguments are passed

        Returns:
            User: First row found in the `users` table.
        """
        session = self._session
        try:
            user = session.query(User).filter_by(**kwargs).one()
            return user
        except NoResultFound:
            raise NoResultFound()
        except InvalidRequestError:
            raise InvalidRequestError()

    def update_user(self, user_id: int, **kwargs) -> None:
        """
        locate the user to update
        the update the user’s attributes as passed in **kwargs
        then commit changes to the database.
        """
        try:
            user = self.find_user_by(id=user_id)
        except NoResultFound:
            raise ValueError("User with id {} is not found".format(user_id))

        for key, value in kwargs.items():
            if not hasattr(user, key):
                raise ValueError("Wrong attribute {}".format(key))
            setattr(user, key, value)

        try:
            self._session.commit()
        except InvalidRequestError:
            raise ValueError("Invalid request")
