"""
Home

Install SQL Alchemy:
pip install flask sqlalchemy flask-sqlalchemy
"""

from flask import Flask

# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
from flaskProject.db_setup import init_db
from flaskProject.endpoints import register_blueprints


app = Flask(__name__)

# Initialize DB and session
init_db("sqlite:///flaskProject/database")

# Auto-register all blueprints
register_blueprints(app)
print("MAP: ", app.url_map)


@app.route("/")
def hello_world():
    "Project Initialization"
    return "<h1>Hello World!</h1>", 200


if __name__ == "__main__":
    app.run(debug=True)
