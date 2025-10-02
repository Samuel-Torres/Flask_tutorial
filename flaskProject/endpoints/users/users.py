"""
Users Model
"""

from flask_httpauth import HTTPBasicAuth
from flask import Blueprint, jsonify, request
from sqlalchemy.exc import SQLAlchemyError
from flaskProject.models.users_model import Users
from flaskProject.db_setup import Session
from flaskProject.app import bcrypt

users = Blueprint("users", __name__)
auth = HTTPBasicAuth()


# ---------------------------
# Authentication
# ---------------------------
@auth.verify_password
def verify_password(username, password):
    """Verify user credentials from the database"""
    session = Session()
    try:
        user = session.query(Users).filter_by(user_name=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            return user
    finally:
        session.close()
    return None


# @users.route("/users")
# Can Also use the pattern below to specify methods:
@users.route("/users", methods=["GET"])
def get_users():
    "Gets all users from the database"
    session = Session()
    try:
        all_users = session.query(Users).all()

        users_list = [
            {
                "user_id": user.user_id,
                "user_name": user.user_name,
                "password": user.password,
            }
            for user in all_users
        ]

        if not users_list:
            return jsonify(message="User table found, but is empty."), 200

        return jsonify(users=users_list), 200

    except SQLAlchemyError as e:
        session.rollback()
        return jsonify(message=f"Database error: {str(e)}"), 500

    finally:
        session.close()


@users.route("/users", methods=["POST"])
def create_user():
    "Create a new user with password hashing and database verification"
    data = request.get_json()
    session = Session()

    try:
        # Hash the password before storing
        hashed_pw = bcrypt.generate_password_hash(data["password"]).decode("utf-8")

        # Create new user
        new_user = Users(user_name=data["user_name"], password=hashed_pw)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)  # reload from DB

        # Verify persisted values
        mismatches = []

        if new_user.user_name != data["user_name"]:
            mismatches.append("user_name")

        # Verify password matches input using bcrypt
        if not bcrypt.check_password_hash(new_user.password, data["password"]):
            mismatches.append("password")

        # If any mismatch, rollback and return error
        if mismatches:
            session.rollback()
            return (
                jsonify(message=f"Creation failed for fields: {', '.join(mismatches)}"),
                500,
            )

        return (
            jsonify(
                message=f"User {new_user.user_name} created with ID: {new_user.user_id}"
            ),
            201,
        )

    except SQLAlchemyError as e:
        session.rollback()
        return jsonify(message=f"Database error: {str(e)}"), 500

    finally:
        session.close()


@users.route("/users/<int:user_id>", methods=["PUT"])
@auth.login_required
def update_user(user_id):
    "Update an existing user with bcrypt password hashing"
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
            # Hash the new password
            hashed_pw = bcrypt.generate_password_hash(data["password"]).decode("utf-8")
            user.password = hashed_pw

        # Commit changes to DB
        session.commit()
        session.refresh(user)  # reload user from DB

        # Verify updates
        mismatches = []

        # Check username
        if "user_name" in data and user.user_name != data["user_name"]:
            mismatches.append("user_name")

        # Verify password matches input using bcrypt
        if "password" in data and not bcrypt.check_password_hash(
            user.password, data["password"]
        ):
            mismatches.append("password")

        # If any mismatches, rollback and return error
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
