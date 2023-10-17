from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property

from config import db
from config import db, bcrypt

# Models go here!

class User(db.Model, SerializerMixin): # Attributes will be user_id, username, id
    pass
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
    __tablename__ = 'taco'
    serialize_rules = (
        "-favorites.taco",
        '-user.taco',
        '-quantities.taco', 
        '-reviews.taco')

id = db.Column(db.Integer, primary_key=True)
taco_name = db.Column(db.String)
image = db.Column(db.String)
instuctions = db.Column(db.Text)
time_to_cook = db.Column(db.Integer)
time_to_prepare = db.Column(db.Integer)
user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

# table relationships 
reviews = db.relationship('Review', back_populates="taco", cascade='all, delete-orphan')
quantities = db.relationship("Quantity", back_populates='taco', cascade="all, delete-orphan")

# association proxy 

ingredients = association_proxy("quantities", "ingredient")

class Review(db.Model, SerializerMixin): # Attributes will be review_id, rating, comment
    pass
def __repr__(self):
    return f'Taco {self.taco_name} ID {self.id}'

# add validation rules here once seeded 

# class Review(db.Model, SerializerMixin): # Attributes will be review_id, rating, comment
#     __tablename__ = "reviews"
#     # serialize_rules = (
#     #     "-users.review",
#     #     "-tacos.review",
#     # )

#     id = db.Column(db.Integer, primary_key=True)
#     body = db.Column(db.Text)
#     title = db.Column(db.String)
#     taco_id = db.Column(db.Integer)

#     reviews = db.relationship('Review', back_populates="user", cascade="all, delete-orphan")



class UserTacoAssociation(db.Model, SerializerMixin): # Attribute will be association_id, user_id, taco_id
    pass
class Quantity(db.Model, SerializerMixin):
    __tablename__ = "quantities"
    id = db.Column(db.Integer, primary_key = True)
    quantity = db.Column(db.Float)
    measurement = db.Column(db.String)
    taco_id = db.Column(db.Integer, db.ForeignKey("tacos.id"))
    ingredients_id = db.Column(db.Integer, db.ForeignKey("ingredients.id"))

    def __repr__(self):
        return f"Quantity {self.quantity}"

    @validates("measurement")
    def validates_measurement(self, key, measurement):
        quantity_list =  [
            "tsp",
            "tbsp",
            "C",
            "pt",
            "qt",
            "gal",
            "oz",
            "fl oz",
            "lb",
            "L",
            "g",
            "kg",
            "mL",
            "",
        ]
        if measurement not in quantity_list:
            return ValueError("Invalid measurement")
        return measurement

class Ingredients(db.Model, SerializerMixin):
    __tablename__ = "ingredients"
    # serialize_rules = (
    #     "-quantities.ingredient",
    #     "-quantities.taco",
    # )

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __repr__(self):
        return f"Ingredient {self.name}"

    quantities = db.relationship("Quantity", back_populates="ingredient", cascade="all, delete-orphan")
    tacos = association_proxy("quantities", "taco")

class Favorite(db.Model, SerializerMixin):
    __tablename__ = "favorites"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    image = db.Column(db.String)

    def __repr__(self):
        return f"Favorite {self.name}, ID {self.id}"
