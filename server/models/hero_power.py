from utilities import db
from marshmallow import ValidationError

class HeroPower(db.Model):
    __tablename__ = 'hero_powers'
    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String, nullable=False)
    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable=False)

    hero = db.relationship('Hero', back_populates='hero_powers')
    power = db.relationship('Power', back_populates='hero_powers')

    def validate_strength(self):
        if self.strength not in ['Strong', 'Weak', 'Average']:
            raise ValidationError('Stength must be one following: Strong, Weak or Average')


    def __repr__(self):
        return f'<HeroPower hero_id={self.hero_id}, power_id={self.power_id}, strength={self.strength}>'
