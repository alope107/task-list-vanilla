import atexit

from flask import Flask

from task_list.models.goal import Goal
from task_list.routes.goal import goal_bp

import psycopg2

# TODO(auberon): Investigate connection pool.
db = psycopg2.connect("dbname='vanilla' user='postgres'")
Goal.db = db
atexit.register(db.close)

app = Flask(__name__)
app.register_blueprint(goal_bp)

