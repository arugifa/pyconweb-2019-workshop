import pytest
import webtest

from workshop import create_app, db as _db
from workshop.config import TestingConfig


@pytest.fixture(scope='session')
def app():
    """Return the web API's WSGI application.

    Used by Pytest-Flask.
    """
    return create_app(TestingConfig)


@pytest.fixture(scope='session')
def client(app):
    """Return a WSGI client to perform requests on the web API."""
    return webtest.TestApp(app)


@pytest.fixture
def db(app):
    """Clean database between test executions."""
    with app.app_context():
        _db.create_all()
        yield _db
        _db.drop_all()
