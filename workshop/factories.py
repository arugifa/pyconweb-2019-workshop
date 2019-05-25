from factory import Factory, Faker
from factory.alchemy import SQLAlchemyModelFactory

from workshop import db
from workshop.models import Cat


class CatFactory(SQLAlchemyModelFactory):
    class Meta:
        model = Cat

        sqlalchemy_session = db.session
        sqlalchemy_session_persistence = 'commit'

    name = Faker('first_name')
    country = Faker('country')
