#!/usr/bin/env python3
"""
Template for API authentication
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Manage the API authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Require authorisation"""
        return False

    def authorization_header(self, request=None) -> str:
        """authorisation user"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """current user"""
        return None
