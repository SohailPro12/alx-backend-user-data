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
        if path is None or excluded_paths is None or excluded_paths == []:
            return True
        normalpath = path.rstrip('/')
        ispre = any(normalpath == item.rstrip('/') for item in excluded_paths)
        return not ispre

    def authorization_header(self, request=None) -> str:
        """
        gets the auth header field from the request
        """
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        gets the current user
        """
        return None
