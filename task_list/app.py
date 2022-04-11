import atexit

from flask import Flask

from task_list.models.goal import Goal
from task_list.routes.goal import goal_bp
from task_list.simple_psyco.database import Database

db = Database("vanilla", "postgres")
Goal.db = db

app = Flask(__name__)
app.register_blueprint(goal_bp)

