from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db

# Models go here!

class User(db.Model, SerializerMixin): # Attributes will be user_id, username, id
    pass
     
class Taco(db.Model, SerializerMixin): # Attributes will be taco_id, name, recipe
    pass

class Review(db.Model, SerializerMixin): # Attributes will be review_id, rating, comment
    pass
 
class UserTacoAssociation(db.Model, SerializerMixin): # Attribute will be association_id, user_id, taco_id
    pass
