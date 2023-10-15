#!/usr/bin/env python3

# Remote library imports
from flask import Flask, request, make_response
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

# Local imports
from config import app, db, api

# Add your model imports

class User(Resource):
    pass

class Taco(Resource):
    pass

class Review(Resource):
    pass

class UserTacoAssociation(Resource):
    pass

# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)

