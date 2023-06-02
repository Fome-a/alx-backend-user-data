#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort, blueprint
from api.v1.views import app_views

index_bp = blueprint('index', __name__)

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GET /api/v1/status
    Return:
      - the status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """ GET /api/v1/stats
    Return:
      - the number of each objects
    """
    from models.user import User
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)

@index_bp.route("/unauthorised")
def unauthorised_endpoint():
    abort(401)