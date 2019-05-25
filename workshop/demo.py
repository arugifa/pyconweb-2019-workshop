from workshop import create_app, db
from workshop.factories import CatFactory
from workshop.config import ProdConfig


def adopt_cats(count: int = 10):
    """Create ``count`` of cats in database."""
    return CatFactory.create_batch(count)


def server():
    """Run a demo server."""
    config = ProdConfig()
    app = create_app(config)

    with app.app_context():
        db.create_all()
        adopt_cats()

    app.run('0.0.0.0', config.SERVER_PORT)
