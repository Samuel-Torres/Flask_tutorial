"""
POSTS Model
"""

from flask import Blueprint, jsonify

posts = Blueprint("posts", __name__)


@posts.route("/posts")
def get_posts():
    "Grabs all posts"
    return jsonify(message="Hello from posts!"), 200


# Get Any post by the authors user_id in the route endpoint.
@posts.route("/posts/<int:user_id>")
def get_post_by_userid(user_id: int):
    "Fetch post by user_id"
    return jsonify(message=f"Found user by ID: {user_id}"), 200


# Example of how to throw status codes
@posts.route("/posts/error")
def error():
    "erroring example"
    return jsonify(message="404 Not Found"), 404
