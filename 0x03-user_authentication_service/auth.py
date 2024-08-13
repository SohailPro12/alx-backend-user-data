#!/usr/bin/env python3
"""
Auth process module
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    takes in a password string arguments and returns bytes.

    The returned bytes is a salted hash of the input password

    hashed with bcrypt.hashpw
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
