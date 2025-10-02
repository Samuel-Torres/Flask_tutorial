"""
Home

Install SQL Alchemy:
pip install flask sqlalchemy flask-sqlalchemy
"""

import os
from flask import Flask
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager
from datetime import timedelta
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flaskProject.db_setup import init_db
from flaskProject.endpoints import register_blueprints
from flaskProject.db_utils import register_cli_commands

load_dotenv()  # take environment variables from .env.

app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "super-secret-key")  
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(weeks=1)
jwt = JWTManager(app)

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

# Register all DB CLI commands
register_cli_commands(app, bcrypt, DATABASE_URL)


@app.route("/")
def hello_world():
    "Project Initialization"
    return "<h1>Hello World!</h1>", 200


if __name__ == "__main__":
    app.run(debug=True)
