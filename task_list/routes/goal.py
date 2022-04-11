from datetime import datetime

from flask import Blueprint
from markupsafe import escape

from task_list.models.goal import Goal

goal_bp = Blueprint('goals', __name__)

@goal_bp.route("/insert")
def insert():
    goal = Goal.create_and_insert("Make a vanilla app", datetime.now())
    return f"New Goal: {escape(str(goal))}"

@goal_bp.route("/")
def fetch_all():
    goals = Goal.fetch_all()
    return f"Goals: {escape(str(goals))}"