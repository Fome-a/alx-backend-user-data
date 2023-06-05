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
        if path is None:
            return True

        if excluded_paths is None or len(excluded_paths )== 0:
            return True

        for excluded_path in excluded_paths:
            if path.endswith('/') and excluded_path == path[:-1]:
                return False

        if path == excluded_paths:
            return False

    def authorization_header(self, request=None) -> str:
        """authorisation user"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """current user"""
        return None
