from utilities import db


class Hero(db.Model):
    __tablename__ = 'heroes'
    id  = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    super_name = db.Column(db.String, nullable=False)
    
    hero_powers = db.relationship('HeroPower', back_populates='hero', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Hero {self.id}, {self.name}, {self.super_name}>'