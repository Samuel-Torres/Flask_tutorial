"""
Home

Install SQL Alchemy:
pip install flask sqlalchemy flask-sqlalchemy
"""

import os
from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flaskProject.db_setup import init_db
from flaskProject.endpoints import register_blueprints

load_dotenv()  # take environment variables from .env.

app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)

DATABASE_URL = (
    f"postgresql+psycopg2://{os.getenv('POSTGRES_USER')}:"
    f"{os.getenv('POSTGRES_PASSWORD')}@"
    f"{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/"
    f"{os.getenv('POSTGRES_DB')}"
)

# Initialize DB and session
init_db(DATABASE_URL)

# Auto-register all blueprints
register_blueprints(app)
print("MAP: ", app.url_map)


@app.route("/")
def hello_world():
    "Project Initialization"
    return "<h1>Hello World!</h1>", 200


if __name__ == "__main__":
    app.run(debug=True)
