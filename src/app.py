"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, People, Planets, Starships, Favorites
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['GET'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200


@app.route('/people', methods=['GET'])
def get_people():
    people = People.query.all()
    return jsonify([person.serialize() for person in people]), 200

@app.route('/people/<int:people_id>', methods=['GET'])
def get_single_person(people_id):
    person = People.query.get(people_id)
    if person is None:
        raise APIException('Person not found', status_code=404)
    return jsonify(person.serialize()), 200

@app.route('/planets', methods=['GET'])
def get_planets():
    planets = Planets.query.all()
    return jsonify([planet.serialize() for planet in planets]), 200

@app.route('/planets/<int:planet_id>', methods=['GET'])
def get_planet(planet_id):
    planet = Planets.query.get(planet_id)
    if planet is None:
        raise APIException("Planet not found", status_code=404)
    return jsonify(planet.serialize()), 200

@app.route('/Starships', methods=['GET'])
def get_Starships():
    all_Starships = Starships.query.all()
    return jsonify(all_Starships), 200

@app.route('/Starships', methods=['GET'])
def get_Starship():

    starship = starship.query.get(starship_id)
    if starship is None:
        raise APIException("User not found", status_code=404)


    return jsonify(starship), 200

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.serialize() for user in users]), 200

@app.route('/users/favorites', methods=['GET'])
def get_user_favorites():
    # Assume you have a way to identify the current user
    # Replace 'current_user_id' with the actual user ID
    current_user_id = 1
    user = User.query.get(current_user_id)
    if user is None:
        raise APIException('User not found', status_code=404)
    favorites = {
        'planets': [planet.serialize() for planet in user.favorite_planets],
        'people': [person.serialize() for person in user.favorite_people],
        'starships': [starships.serialize() for starships in user.favorite_starships],
    }
    return jsonify(favorites), 200

@app.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def add_favorite_planet(planet_id):
    # Assume you have a way to identify the current user
    # Replace 'current_user_id' with the actual user ID
    current_user_id = 1
    user = User.query.get(current_user_id)
    if user is None:
        raise APIException('User not found', status_code=404)
    planet = Planets.query.get(planet_id)
    if planet is None:
        raise APIException('Planet not found', status_code=404)
    user.favorite_planets.append(planet)
    db.session.commit()
    return jsonify({'message': 'Favorite planet added'}), 201

@app.route('/favorite/people/<int:people_id>', methods=['POST'])
def add_favorite_people(people_id):
    # Assume you have a way to identify the current user
    # Replace 'current_user_id' with the actual user ID
    current_user_id = 1
    user = User.query.get(current_user_id)
    if user is None:
        raise APIException('User not found', status_code=404)
    person = People.query.get(people_id)
    if person is None:
        raise APIException('Person not found', status_code=404)
    user.favorite_people.append(person)
    db.session.commit()
    return jsonify({'message': 'Favorite person added'}), 201

@app.route('/favorite/starships/<int:starships_id>', methods=['POST'])
def add_favorite_starships(starships_id):
    # Assume you have a way to identify the current user
    # Replace 'current_user_id' with the actual user ID
    current_user_id = 1
    user = User.query.get(current_user_id)
    if user is None:
        raise APIException('User not found', status_code=404)
    starships = starships.query.get(starships_id)
    if starships is None:
        raise APIException('Person not found', status_code=404)
    user.favorite_starships.append(starships)
    db.session.commit()
    return jsonify({'message': 'Favorite Starships added'}), 201

@app.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
def delete_favorite_planet(planet_id):
    # Assume you have a way to identify the current user
    # Replace 'current_user_id' with the actual user ID
    current_user_id = 1
    user = User.query.get(current_user_id)
    if user is None:
        raise APIException('User not found', status_code=404)
    planet = Planets.query.get(planet_id)
    if planet is None:
        raise APIException('Planet not found', status_code=404)
    user.favorite_planets.remove(planet)
    db.session.commit()
    return jsonify({'message': 'Favorite planet deleted'}), 200

@app.route('/favorite/people/<int:people_id>', methods=['DELETE'])
def delete_favorite_people(people_id):
    # Assume you have a way to identify the current user
    # Replace 'current_user_id' with the actual user ID
    current_user_id = 1
    user = User.query.get(current_user_id)
    if user is None:
        raise APIException('User not found', status_code=404)
    person = People.query.get(people_id)
    if person is None:
        raise APIException('Person not found', status_code=404)
    user.favorite_people.remove(person)
    db.session.commit()
    return jsonify({'message': 'Favorite person deleted'}), 200

@app.route('/favorite/starships/<int:starships_id>', methods=['DELETE'])
def delete_favorite_starships(starships_id):
    # Assume you have a way to identify the current user
    # Replace 'current_user_id' with the actual user ID
    current_user_id = 1
    user = User.query.get(current_user_id)
    if user is None:
        raise APIException('User not found', status_code=404)
    starships = People.query.get(starships_id)
    if starships is None:
        raise APIException('Person not found', status_code=404)
    user.favorite_starships.remove(starships)
    db.session.commit()
    return jsonify({'message': 'Favorite starships deleted'}), 200



# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
