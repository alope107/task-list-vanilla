from datetime import date

from flask import Blueprint, jsonify
from markupsafe import escape

from app.models.goal import Goal

goal_bp = Blueprint('goals', __name__)

@goal_bp.route("/insert")
def insert():
    goal = Goal.create_and_insert("Make a vanilla app", date.today())
    return jsonify(goal.to_dict())

@goal_bp.route("/")
def fetch_all():
    goals = Goal.fetch_all()
    return jsonify([goal.to_dict() for goal in goals])