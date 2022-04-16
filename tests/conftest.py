import pytest

import importlib.resources as pkg_resources

from app import create_app, schemas
from tests import static_sql

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

    clear_db(app.db)
    init_db(app.db)
    yield app
    clear_db(app.db)

@pytest.fixture
def client(app):
    return app.test_client()