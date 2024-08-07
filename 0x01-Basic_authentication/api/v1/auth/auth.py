#!/usr/bin/env python3
""" Class Auth
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """
    Auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        checks if path require auth
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        gets the auth header field from the request
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        gets the current user
        """
        return None
