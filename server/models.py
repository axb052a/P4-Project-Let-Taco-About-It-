from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property

from config import db, bcrypt

# Models go here!

user_taco_favorites = db.Table(
    "user_taco_favorites",
    db.Column("user_id", db.Integer, db.ForeignKey("users.id")),
    db.Column("taco_id", db.Integer, db.ForeignKey("tacos.id")),
    

)
class User(db.Model, SerializerMixin):
    __tablename__ = "users"
   
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    _password_hash = db.Column(db.String, nullable=False)

    favorite_tacos = db.relationship(
        "Taco",
        secondary=user_taco_favorites,
        back_populates="favorited_by",
    )

    serialize_rules = (
        '-tacos.user', 
        '-favorites.user',
    )

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
    tacos = db.relationship("Taco", back_populates="user", cascade="all, delete-orphan")
    favorites = association_proxy("tacos", "favorites")
     
class Taco(db.Model, SerializerMixin): 
    __tablename__ = 'tacos'
    
   
    id = db.Column(db.Integer, primary_key=True)
    taco_name = db.Column(db.String)
    taco_type = db.Column(db.String)
    image = db.Column(db.String)
    instructions = db.Column(db.Text) 
    time_to_cook = db.Column(db.Integer)
    time_to_prepare = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', back_populates="tacos", cascade="all, delete-orphan", single_parent=True)

    favorited_by = db.relationship(
        "User",
        secondary=user_taco_favorites,
        back_populates="favorite_tacos",
    )

    # table relationships 
    quantities = db.relationship("Quantity", back_populates='taco', cascade="all, delete-orphan")

    # association proxy


    ingredients = association_proxy("quantities", "ingredient")

    serialize_rules = (
        '-user',
        '-quantities',
        '-favorited_by',
        
    )

    def __repr__(self):
        return f'Taco {self.taco_name} ID {self.id}'

# add validation rules here once seeded 
class Ingredient(db.Model, SerializerMixin):
    __tablename__ = "ingredients"
   

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    quantities = db.relationship("Quantity", back_populates="ingredients", cascade="all, delete-orphan")
    tacos = association_proxy("quantities", "taco")

    serialize_rules = (
        "-quantities",
        "-favorited_by",
        "-tacos",
        
    )

    def __repr__(self):
        return f"Ingredient {self.name}"

    

class Quantity(db.Model, SerializerMixin):
    __tablename__ = "quantities"
    id = db.Column(db.Integer, primary_key = True)
    quantity = db.Column(db.Float)
    measurement = db.Column(db.String)
    taco_id = db.Column(db.Integer, db.ForeignKey("tacos.id"))
    ingredient_id = db.Column(db.Integer, db.ForeignKey("ingredients.id"))
    taco = db.relationship("Taco", back_populates="quantities")

    ingredients = db.relationship("Ingredient", back_populates="quantities")
   
    
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



class Favorite(db.Model, SerializerMixin):
    __tablename__ = "favorites"
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    image = db.Column(db.String)

    def __repr__(self):
        return f"Favorite {self.name}, ID {self.id}"
    