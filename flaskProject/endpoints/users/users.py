"""
Users Model
"""

from flask import Blueprint, jsonify

users = Blueprint("users", __name__)


@users.route("/users")
def get_users():
    "Project Initialization"
    return jsonify(message="Hello from users!"), 200


# Example of how to throw status codes
@users.route("/error")
def error():
    "erroring example"
    return jsonify(message="404 Not Found"), 404
