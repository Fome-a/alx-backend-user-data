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
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        for excluded_path in excluded_paths:
            if path.endswith('/') and excluded_path == path[:-1]:
                return False
            elif excluded_path.endswith('/') and path == excluded_path[:-1]:
                return False
            if path in excluded_paths:
                return False
            else:
                return True
            
        
    def authorization_header(self, request=None) -> str:
        """authorization header"""
        if request is None or 'Authorization' not in request.headers:
            return None
        else:
            return request.headers.get('Authorization')


    def current_user(self, request=None) -> TypeVar('User'):
        """current user"""
        return None
