from flask import Flask
from .routes.hello import hello_world_bp

app = Flask(__name__)
app.register_blueprint(hello_world_bp)