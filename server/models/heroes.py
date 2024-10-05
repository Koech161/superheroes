from utilities import db
from sqlalchemy_serializer import SerializerMixin

class Hero(db.Model, SerializerMixin):
    __tablename__ = 'heroes'
    id  = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    super_name = db.Column(db.String, nullable=False)
    
    powers = db.relationship('HeroPower', back_populates='hero')

    def __repr__(self):
        return f'<Hero {self.id}, {self.name}, {self.super_name}>'