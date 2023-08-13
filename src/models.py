from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }
    
class People(db.Model):
    __tablename__ = 'people'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.String(450), unique=True, nullable=False)
    species = db.Column(db.String(120), nullable=False)
    gender = db.column(db.String(120))

    def __repr__(self):
        return '<People %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "species": self.species,
            "gender": self.gender,

            # do not serialize the password, its a security breach
        }
class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    climate = db.Column(db.String(250))
    terrain = db.Column(db.String(250))
    population = db.Column(db.Integer)
    description = db.Column(db.String(450))
    def __repr__(self):
        return '<Planets %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate":self.climate,
            "terrain":self.terrain,
            "population":self.population,
            "description":self.description,
            # do not serialize the password, its a security breach
        }
class Starships(db.Model):
    __tablename__ = 'starships'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), nullable=False)
    model = db.Column(db.String(250), unique=False, nullable=False)
    hyperdrive_rating = db.Column(db.String(250))
    length = db.Column(db.Integer)
    crew = db.Column(db.String(250))
    passengers = db.Column(db.string(250))

    def __repr__(self):
        return '<Starships %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "hyperdrive_rating": self.hyperdrive_rating,
            "length": self.length,
            "crew": self.crew,
            "passengers": self.passengers,
            # do not serialize the password, its a security breach
        }
    
class Favorites(db.Model):
    __tablename__ = "favorites"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    people_name = db.Column(db.String(80), db.ForeignKey("people.name"))
    planets_name = db.Column(db.String(80), db.ForeignKey("planets.name"))
    starships_name = db.Column(db.String(80), db.ForeignKey("starships.name"))

    def __repr__(self):
        return '<Favorites %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "people_name": self.people_name,
            "planets_name": self.planets_name,
            "starships_name": self.starships_name,
        }
