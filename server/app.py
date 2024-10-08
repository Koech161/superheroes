from flask import Flask
from flask_migrate import Migrate
from utilities import db
from models.heroes import Hero
from models.powers import Power
from models.hero_power import HeroPower
from flask_restful import Api
from resources import Heroes, HeroesById,Powers,PowerById, HeroPowers 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
migrate = Migrate(app, db)
db.init_app(app)
api = Api(app)

api.add_resource(Heroes, '/heroes')
api.add_resource(HeroesById, '/heroes/<int:id>')
api.add_resource(Powers, '/powers')
api.add_resource(PowerById, '/powers/<int:id>')
api.add_resource(HeroPowers, '/hero_powers')



if __name__ == '__main__':
    app.run(port=5555,debug=True)
