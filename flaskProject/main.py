"""
Home
"""

from flask import Flask
from endpoints.users.users import users

app = Flask(__name__)

# Route Registrations:
app.register_blueprint(users)


@app.route("/")
def hello_world():
    "Project Initialization"
    return "<h1>Hello World!</h1>"


if __name__ == "__main__":
    app.run(debug=True)

# print("RUNNING: ", hello_world())
