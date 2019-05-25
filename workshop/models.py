from workshop import db


class Cat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    country = db.Column(db.String(30), nullable=False)

    @classmethod
    def all(cls):
        return Cat.query.all()
