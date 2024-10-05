from utilities import db
from sqlalchemy_serializer import SerializerMixin

class Power(db.Model, SerializerMixin):
    __tablename__ = 'powers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    description = db.Column(db.String, nullable=False)

    heroes = db.relationship('HeroPower', back_populates='power')

    def __repr__(self):
        return f'<Power {self.id}, {self.name}, {self.description}>'