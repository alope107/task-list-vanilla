from flask import Flask

from app.models.goal import Goal
from app.routes.goal import goal_bp
from app.simple_psyco.database import Database

def create_app(test_config=None):
    db = Database("vanilla", "postgres")
    Goal.db = db

    app = Flask(__name__)
    app.register_blueprint(goal_bp)

    return app