import pytest

import importlib.resources as pkg_resources

from app import create_app, schemas
from tests import static_sql

# TODO(auberon): Should this live in simple_psyco?
def clear_db(db):
    clear_db = pkg_resources.read_text(static_sql, 'clear_db.sql')
    db.query(clear_db)

def init_db(db):
    # TODO(auberon): Get everything from the schemas folder
    # TODO(auberon): Move this type of logic to simple_psyco?
    create_goal_table = pkg_resources.read_text(schemas, 'goal.sql')
    db.query(create_goal_table)

@pytest.fixture
def app_config():
    # TODO(auberon): Should this be loaded from a .env?
    return {
        "dbname": "vanilla_test",
        "user": "postgres"
    }

@pytest.fixture
def app(app_config):
    app = create_app(app_config)
    # TODO(auberon): Handle this in app_config?
    app.config.update({
        "TESTING": True,
    })

    clear_db(app.db)
    init_db(app.db)
    yield app
    clear_db(app.db)

@pytest.fixture
def client(app):
    return app.test_client()