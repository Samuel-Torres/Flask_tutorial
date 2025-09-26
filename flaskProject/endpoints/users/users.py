"""
Users Model
"""

from flask import Blueprint, jsonify, request
from flaskProject.models.users_model import Users
from flaskProject.db_setup import Session
from sqlalchemy.exc import SQLAlchemyError

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


@users.route("/users", methods=["POST"])
def create_user():
    "Create a new user"
    data = request.get_json()
    session = Session()  # Use your imported Session
    try:
        new_user = Users(user_name=data["user_name"], password=data["password"])
        session.add(new_user)
        session.commit()
        # Refresh to ensure DB-generated fields (like user_id) are loaded
        session.refresh(new_user)

        # Verify that the user was actually created
        if new_user.user_id:
            return (
                jsonify(
                    message=f"User {new_user.user_name} created with ID: {new_user.user_id}"
                ),
                201,
            )
        else:
            session.rollback()
            return jsonify(message="Failed to create user."), 500

    except SQLAlchemyError as e:
        session.rollback()
        return jsonify(message=f"Database error: {str(e)}"), 500

    finally:
        session.close()


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
