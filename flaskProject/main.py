"""
Home
"""

from flask import Flask
from endpoints.users.users import users
import sqlite3

app = Flask(__name__)

# SQLite initialization:
connection = sqlite3.connect("database")
cursor = connection.cursor()
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS Users (user_id INT, user_name TEXT, password TEXT)
"""
)
connection.commit()
connection.close()


# Route Registrations:
app.register_blueprint(users)


@app.route("/")
def hello_world():
    "Project Initialization"
    return "<h1>Hello World!</h1>", 200


if __name__ == "__main__":
    app.run(debug=True)

# print("RUNNING: ", hello_world())
