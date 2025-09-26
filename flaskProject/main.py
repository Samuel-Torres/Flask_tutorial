"""
Home

Install SQL Alchemy:
pip install flask sqlalchemy flask-sqlalchemy
"""

from flask import Flask
from sqlalchemy import create_engine
from flaskProject.endpoints import register_blueprints
from .models import Base
from . import (  # pylint: disable=unused-import # this auto-imports models via models/__init__.py
    models,
)

app = Flask(__name__)
engine = create_engine("sqlite:///database")
Base.metadata.create_all(engine)


# Auto-register all blueprints
register_blueprints(app)
print("MAP: ", app.url_map)


@app.route("/")
def hello_world():
    "Project Initialization"
    return "<h1>Hello World!</h1>", 200


if __name__ == "__main__":
    app.run(debug=True)
