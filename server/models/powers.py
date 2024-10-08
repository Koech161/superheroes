from utilities import db
from marshmallow import ValidationError

class Power(db.Model):
    __tablename__ = 'powers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)
    description = db.Column(db.String, nullable=False)

    hero_powers = db.relationship('HeroPower', back_populates='power', cascade='all, delete-orphan')

    def validate(self):
        if len(self.description) < 20:
            raise ValidationError('Description must be at least 20 character long.')

    def __repr__(self):
        return f'<Power {self.id}, {self.name}, {self.description}>'