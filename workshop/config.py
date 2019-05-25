import os

IN_MEMORY_DATABASE = 'sqlite:///:memory:'


class DefaultConfig:
    #: Store database in memory by default, for faster access.
    SQLALCHEMY_DATABASE_URI = IN_MEMORY_DATABASE

    #: Deactivate Flask-SQLAlchemy warnings.
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(DefaultConfig):
    """Environment variables can be used to change configuration in PROD."""

    #: Port on which the web server will listen on.
    SERVER_PORT = 5000

    def __init__(self):
        self.SQLALCHEMY_DATABASE_URI = os.environ.get(
            'DB_URI', self.SQLALCHEMY_DATABASE_URI)

        self.SERVER_PORT = os.environ.get(
            'SERVER_PORT', self.SERVER_PORT)



class TestingConfig(DefaultConfig):
    #: Let's raise exceptions during tests,
    #: to know what's happening when an internal server error occurs.
    TESTING = True
