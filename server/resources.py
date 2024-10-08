from flask import request, make_response
from flask_restful import Resource
from utilities import db
from models.heroes import Hero
from models.powers import Power
from models.hero_power import HeroPower
from schemas import HeroPowerSchema,HeroSchema,PowerSchema ,HeroschemaDetails
from marshmallow import ValidationError

hero_schema = HeroSchema()
power_schema = PowerSchema()
hero_power_schema = HeroPowerSchema()
hero_power = HeroschemaDetails()
heroes_schema= HeroSchema(many=True)
powers_schema = PowerSchema(many=True)

class Heroes(Resource):
    def get(self):
        heroes = Hero.query.all()
        print(heroes)
        return make_response(heroes_schema.dump(heroes),200)

class HeroesById(Resource):
    def get(self, id):
        hero = Hero.query.get(id)
        if hero:

            return make_response(hero_power.dump(hero), 200)  
        else: 
            return {"error": "Hero not found"}, 404  
        
class Powers(Resource):
    def get(self):
        powers = Power.query.all()
        if powers:
            return make_response(powers_schema.dump(powers), 200)
        else:
            return {"Error": "Powers not found."}       
class PowerById(Resource):
    def get(self, id):
        power = Power.query.get(id)

        if power:
            return make_response(power_schema.dump(power), 200)
        else:
            return {"error": "Power not found"}, 404   

    def  patch(self, id):
        power = Power.query.get(id)  
        if not power:
            return {"error": "Power not found"}, 404
        new_data = request.json.get('description')
        if new_data:
            power.description = new_data
        try:
            power.validate()
            db.session.commit()
            return make_response(power_schema.dump(power), 201)
        except ValidationError as e:
            return {"errors": e.messages}, 400   
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 500  


class HeroPowers(Resource):
    def post(self):
        data = request.json
        hero_power = HeroPower(
            strength = data['strength'],
            hero_id = data['hero_id'],
            power_id = data['power_id']
        )
        try:
            hero_power.validate_strength()
            db.session.add(hero_power)
            db.session.commit()
            return make_response(hero_power_schema.dump(hero_power), 201)
        except ValidationError as e:
            return {'errors': e.messages}, 400
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 500

