"""
Home
"""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    "Project Initialization"
    return "<h1>Hello World!</h1>"


# print("RUNNING: ", hello_world())
