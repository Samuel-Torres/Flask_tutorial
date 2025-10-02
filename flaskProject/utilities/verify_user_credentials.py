"""
validates user credentials middleware:
- checks if username exists in the database
- checks if password matches the hashed password in the database
returns user object if valid, else None
"""
from flaskProject.models.users_model import Users
from flaskProject.db_setup import Session
from flaskProject.app import bcrypt

def verify_user_credentials(username: str, password: str):
    """Middleware function to verify username and password."""
    session = Session()
    try:
        user = session.query(Users).filter_by(user_name=username).first()
        if not user or user.user_name != username:
            return None
        if not bcrypt.check_password_hash(user.password, password):
            # Password incorrect
            return None
        return user
    finally:
        session.close()