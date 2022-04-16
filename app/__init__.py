import os

from dotenv import load_dotenv
from flask import Flask

from app.models.goal import Goal
from app.routes.goal import goal_bp
from app.simple_psyco.database import Database

load_dotenv()
config = {
    "dbname": os.environ.get("APP_DBNAME"),
    "user": os.environ.get("APP_USER")
}

# TODO(auberon): Investigate config.from_pyfile
def create_app(config=config):
    db = Database(config["dbname"], config["user"])
    Goal.db = db

    app = Flask(__name__)
    app.register_blueprint(goal_bp)

    return app