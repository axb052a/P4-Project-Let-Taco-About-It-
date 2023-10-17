from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property

from config import db, bcrypt

# Models go here!

class User(db.Model, SerializerMixin): # Attributes will be user_id, username, id
    __tablename__ = "users"
    serialize_rules = (
        '-reviews.user',
        '-tacos.user', 
        '-favortites.user'
    )
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    _password_hash = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"User {self.username}, ID {self.id}"

    @hybrid_property
    def password_hash(self):
        raise AttributeError("Passwords cannot be viewed")

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(password.encode("utf-8"))
        self._password_hash = password_hash.decode("utf-8")

    def authenticate(self, password):
        return bcrypt.check_password_hash(self._password_hash, password.encode("utf-8"))

    @validates(username, email)
    def validate_signup(self, key, value):
        if not len(value) > 0:
            raise ValueError("Must provide at least one character to sign up")
        return value

# table relationships 
    reviews = db.relationship("Review", back_populates="user", cascade="all ,delete-orphan")
    tacos = db.relationship("Taco", back_populates="user", cascade="all, delete-orphan")
    favorites = association_proxy("tacos", "favorites")
     
class Taco(db.Model, SerializerMixin): # Attributes will be taco_id, name, recipe
    pass

class Review(db.Model, SerializerMixin): # Attributes will be review_id, rating, comment
    pass
 
class UserTacoAssociation(db.Model, SerializerMixin): # Attribute will be association_id, user_id, taco_id
    pass
