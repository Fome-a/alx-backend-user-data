#!/usr/bin/env python3
"""Basic Flask application"""

from flask import Flask, jsonify, request
from auth import Auth
app = Flask(__name__)
AUTH = Auth()  # this instatiates the Auth class and creates the object AUTH


@app.route('/', methods=['GET'], strict_slashes=False)
def home():
    respond = jsonify({"message": "Bienvenue"})
    return respond


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.debug = True 
    app.run(host="0.0.0.0", port="5000")



