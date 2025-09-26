"""
Home

Install SQL Alchemy:
pip install flask sqlalchemy flask-sqlalchemy
"""

# import sqlite3
from flask import Flask

# modular way to import models:
from sqlalchemy import create_engine

from flaskProject.endpoints.users.users import users
from flaskProject.endpoints.posts.posts import posts

from .models import Base
from . import (  # pylint: disable=unused-import # this auto-imports models via models/__init__.py
    models,
)

app = Flask(__name__)
engine = create_engine("sqlite:///database")
Base.metadata.create_all(engine)


# Route Registrations:
app.register_blueprint(users)
app.register_blueprint(posts)

print("MAP: ", app.url_map)


@app.route("/")
def hello_world():
    "Project Initialization"
    return "<h1>Hello World!</h1>", 200


if __name__ == "__main__":
    app.run(debug=True)
