from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config: object):
    """Application factory.

    Make configuration changes easier during testing.
    """
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)

    from workshop.views import api
    app.register_blueprint(api)

    return app
