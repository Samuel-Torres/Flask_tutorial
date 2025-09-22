"""
Users Model
"""

from flask import Blueprint

users = Blueprint("users", __name__)


@users.route("/users")
def get_users():
    "Project Initialization"
    return {"message": "Hello from users!"}
