from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

# Models go here!

class User(db.Model, SerializerMixin): # Attributes will be user_id, username, id
    pass
     
class Taco(db.Model, SerializerMixin): # Attributes will be taco_id, name, recipe
    __tablename__ = 'taco'
    serialize_rules = (
        "-favorites.taco",
        "-user.tacos",
        "-quantities.taco",
        "-reviews.taco"

    )

    id = db.Column(db.Integer, primary_key=True)
    taco_name = db.Column(db.String)
    image = db.Column(db.String)
    instructions = db.Column(db.Text)
    time_to_cook = db.Column(db.Integer)
    time_to_prepare = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
     # table relationships
    reviews = db.relatinoship("Review", backref="taco", cascade ="all, delete-orphan")
    quantities = db.relationship("Quantity", backref="taco", cascade ="all, delete-orphan")

    # association proxy

    ingredients = association_proxy ("quantities", "ingredient")

    def __repr__ (self):
        return f"Taco {self.taco_name} ID {self.id}"
    
    #add validation rules here once seeded
    

class Review(db.Model, SerializerMixin): # Attributes will be review_id, rating, comment
    pass
 

class Quantity(db.Model, SerializerMixin): # Attributes will b
    pass

class Ingredients(db.Model, SerializerMixin): # Attributes will
    pass

class Favorites (db.Model, SerializerMixin): # Attributes will
    pass
