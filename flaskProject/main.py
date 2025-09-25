"""
Home

Install SQL Alchemy:
pip install flask sqlalchemy flask-sqlalchemy
"""

# import sqlite3
from flask import Flask
from endpoints.users.users import users

# from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.orm import declarative_base

# modular way to import models:
from sqlalchemy import create_engine
from models import Base

# this auto-imports models via models/__init__.py
import models  # pylint: disable=unused-import

app = Flask(__name__)

# SQLite initialization:
# connection = sqlite3.connect("database")
# cursor = connection.cursor()
# cursor.execute(
#     """
#     CREATE TABLE IF NOT EXISTS Users (user_id INT, user_name TEXT, password TEXT)
# """
# )
# connection.commit()
# connection.close()

# _______________________________________________

# Alchemy ORM initialization:

# From main.py approach
# engine = create_engine("sqlite:///database")
# Base = declarative_base()

# modular models directory approach:
engine = create_engine("sqlite:///database")

# class Users(Base):
#     "Users Schema"

#     __tablename__ = "Users"
#     user_id = Column(Integer, primary_key=True)
#     user_name = Column(String)
#     password = Column(String)


# creates table if it doesn't exist
Base.metadata.create_all(engine)


# Route Registrations:
app.register_blueprint(users)


@app.route("/")
def hello_world():
    "Project Initialization"
    return "<h1>Hello World!</h1>", 200


if __name__ == "__main__":
    app.run(debug=True)

# print("RUNNING: ", hello_world())
