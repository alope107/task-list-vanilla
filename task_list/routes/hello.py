from flask import Blueprint

hello_world_bp = Blueprint('hello world', __name__)

@hello_world_bp.route("/")
def hello_world():
    return "<p>Hello, World!!!!</p>"