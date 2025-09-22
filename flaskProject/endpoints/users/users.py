"""
Users Model
"""

from flask import Blueprint, jsonify, request

users = Blueprint("users", __name__)


@users.route("/users")
def get_users():
    "Project Initialization"
    return jsonify(message="Hello from users!"), 200


# Query Paramaters Example:
@users.route("/userById")
def get_users_by_id():
    "Get user by userId"
    # Request.args.get, gets your query param by name
    return jsonify(message=f"Found User by ID: {int(request.args.get('userId'))}"), 200


# Get Any user by their user ID in the route endpoint.
@users.route("/users/<int:user_id>")
def get_user_by_userid(user_id: int):
    "Fetch user by userId"
    return jsonify(message=f"Found user by ID: {user_id}"), 200


# Example of how to throw status codes
@users.route("/error")
def error():
    "erroring example"
    return jsonify(message="404 Not Found"), 404
