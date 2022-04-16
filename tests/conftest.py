import importlib.resources as pkg_resources

import pytest

from app import create_app, schemas

def init_db(db):
    create_goal_table = pkg_resources.read_text(schemas, 'schemas.sql')
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

    db = app.db

    db.clear_db()
    init_db(db)
    yield app
    db.clear_db()

@pytest.fixture
def client(app):
    return app.test_client()