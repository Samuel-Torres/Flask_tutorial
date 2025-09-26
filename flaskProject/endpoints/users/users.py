"""
Users Model
"""

from flask import Blueprint, jsonify, request
from sqlalchemy.exc import SQLAlchemyError
from flaskProject.models.users_model import Users
from flaskProject.db_setup import Session

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
    session = Session()
    try:
        new_user = Users(user_name=data["user_name"], password=data["password"])
        session.add(new_user)
        session.commit()
        session.refresh(new_user)

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


@users.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    "Update an existing user"
    data = request.get_json()
    session = Session()
    try:
        # Fetch the user by ID
        user = session.get(Users, user_id)
        if not user:
            return jsonify(message=f"User with ID {user_id} not found."), 404

        # Update fields if provided
        if "user_name" in data:
            user.user_name = data["user_name"]
        if "password" in data:
            user.password = data["password"]

        session.commit()
        session.refresh(user)  # reloads from DB

        # Verify persisted values
        mismatches = []
        if "user_name" in data and user.user_name != data["user_name"]:
            mismatches.append("user_name")
        if "password" in data and user.password != data["password"]:
            mismatches.append("password")

        if mismatches:
            session.rollback()
            return (
                jsonify(message=f"Update failed for fields: {', '.join(mismatches)}"),
                500,
            )

        return (
            jsonify(
                message=f"User {user.user_name} with ID {user.user_id} updated successfully."
            ),
            200,
        )

    except SQLAlchemyError as e:
        session.rollback()
        return jsonify(message=f"Database error: {str(e)}"), 500

    finally:
        session.close()


@users.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    "Delete an existing user"
    session = Session()
    try:
        # Fetch the user by ID
        user = session.get(Users, user_id)
        if not user:
            return jsonify(message=f"User with ID {user_id} not found."), 404

        session.delete(user)
        session.commit()

        # Verify deletion
        deleted_user = session.get(Users, user_id)
        if deleted_user:
            session.rollback()
            return jsonify(message=f"Failed to delete user with ID {user_id}."), 500

        return jsonify(message=f"User with ID {user_id} deleted successfully."), 200

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
